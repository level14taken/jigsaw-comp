import numpy as np
import pandas as pd

def prob_to_logit(p):
    """Convert probability to logit"""
    p = np.clip(p, 1e-10, 1-1e-10)
    return np.log(p / (1 - p))

def logit_to_prob(logit):
    """Convert logit to probability"""
    return 1 / (1 + np.exp(-logit))

def untrained_to_trained(prob_untrained):
    """
    Convert 14b_untrained predictions to 14b_trained predictions

    Formula: logit_trained = (logit_untrained - 5.00) / 5.70

    Args:
        prob_untrained: probability from untrained model (scalar or array)

    Returns:
        probability in trained model format
    """
    logit_u = prob_to_logit(np.array(prob_untrained))
    logit_t = (logit_u - 5.00) / 5.70
    return logit_to_prob(logit_t)

def trained_to_untrained(prob_trained):
    """
    Convert 14b_trained predictions to 14b_untrained predictions

    Formula: logit_untrained = logit_trained * 5.70 + 5.00

    Args:
        prob_trained: probability from trained model (scalar or array)

    Returns:
        probability in untrained model format
    """
    logit_t = prob_to_logit(np.array(prob_trained))
    logit_u = logit_t * 5.70 + 5.00
    return logit_to_prob(logit_u)


if __name__ == "__main__":
    print("14B Model Prediction Converter")
    print("=" * 60)

    print("\nExample: Untrained → Trained")
    untrained_vals = [0.001, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999]
    for val in untrained_vals:
        trained_val = untrained_to_trained(val)
        print(f"  {val:8.6f} → {trained_val:8.6f}")

    print("\nExample: Trained → Untrained")
    trained_vals = [0.02, 0.05, 0.1, 0.3, 0.5, 0.7, 0.9]
    for val in trained_vals:
        untrained_val = trained_to_untrained(val)
        print(f"  {val:8.6f} → {untrained_val:8.6f}")

    print("\nYou can use this to convert entire DataFrames:")
    print("  df['pred_yes_trained'] = untrained_to_trained(df['pred_yes_untrained'])")
    print("  df['pred_yes_untrained'] = trained_to_untrained(df['pred_yes_trained'])")
