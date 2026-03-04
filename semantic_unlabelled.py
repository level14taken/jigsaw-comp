import pandas as pd

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search, dot_score
from tqdm.auto import tqdm

from utils import get_dataframe_to_train, prepare_dataframe
from sampling import sample_unlabelled_data
from constants import DATA_PATH, EMBDEDDING_MODEL_PATH, EMBEDDING_MODEL_QUERY, TOP_K, BATCH_SIZE


def get_unlabelled_scores(unlabelled_dataframe):
    """Generate similarity scores for unlabelled data using training corpus"""
    corpus_dataframe = get_dataframe_to_train(DATA_PATH)
    corpus_dataframe = prepare_dataframe(corpus_dataframe)
    
    embedding_model = SentenceTransformer(
        model_name_or_path=EMBDEDDING_MODEL_PATH,
        device="cuda",
    )

    result = []
    for rule in tqdm(unlabelled_dataframe["rule"].unique(), desc="Generate scores for each rule"):
        unlabelled_rule_data = unlabelled_dataframe.query("rule == @rule").reset_index(drop=True)
        corpus_rule_data = corpus_dataframe.query("rule == @rule").reset_index(drop=True)
        corpus_rule_data = corpus_rule_data.reset_index(names="row_id")
        
        # Prepare prompts for unlabelled data
        unlabelled_rule_data = prepare_dataframe(unlabelled_rule_data)
        
        query_embeddings = embedding_model.encode(
            sentences=unlabelled_rule_data["prompt"].tolist(),
            prompt=EMBEDDING_MODEL_QUERY,
            batch_size=BATCH_SIZE,
            show_progress_bar=True,
            convert_to_tensor=True,
            device="cuda",
            normalize_embeddings=True,
        )
        document_embeddings = embedding_model.encode(
            sentences=corpus_rule_data["prompt"].tolist(),
            batch_size=BATCH_SIZE,
            show_progress_bar=True,
            convert_to_tensor=True,
            device="cuda",
            normalize_embeddings=True,
        )
        
        unlabelled_rule_data["semantic"] = semantic_search(
            query_embeddings,
            document_embeddings,
            top_k=TOP_K,
            score_function=dot_score,
        )
        
        def get_score(semantic):
            semantic = pd.DataFrame(semantic)
            semantic = semantic.merge(
                corpus_rule_data[["row_id", "rule_violation"]],
                how="left",
                left_on="corpus_id",
                right_on="row_id",
            )
            semantic["score"] = semantic["score"] * semantic["rule_violation"]
            return semantic["score"].sum()
            
        tqdm.pandas(desc=f"Add predictions for {rule=}")
        unlabelled_rule_data["prediction"] = unlabelled_rule_data["semantic"].progress_apply(get_score)
        
        # Keep only required columns
        result.append(unlabelled_rule_data[["rule", "body", "prediction"]].copy())
        
    final_results = pd.concat(result, axis=0)
    return final_results


def generate_unlabelled_predictions(unlabelled_csv_path):
    """Main function to generate predictions on unlabelled data"""
    # Get test data size for sampling calculation
    test_df = pd.read_csv(f"{DATA_PATH}/test.csv")
    test_size = len(test_df)
    
    # Sample unlabelled data maintaining proportions
    print("Sampling unlabelled data...")
    sampled_unlabelled = sample_unlabelled_data(unlabelled_csv_path, test_size, multiplier=5)
    print(f"Sampled {len(sampled_unlabelled)} examples from unlabelled data")
    
    # Generate predictions
    print("Generating predictions...")
    predictions = get_unlabelled_scores(sampled_unlabelled)
    
    # Shuffle final results
    predictions = predictions.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Save results
    predictions.to_csv("unlabelled_predictions.csv", index=False)
    print(f"Saved {len(predictions)} predictions to unlabelled_predictions.csv")
    
    return predictions


if __name__ == "__main__":
    unlabelled_csv_path = "reddit_unlabelled.csv"  # Update this path as needed
    generate_unlabelled_predictions(unlabelled_csv_path)