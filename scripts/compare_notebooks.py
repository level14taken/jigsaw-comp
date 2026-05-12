#!/usr/bin/env python3
"""Comprehensive comparison of speedtriplet.ipynb vs ensemble.ipynb"""

import json

# Read both notebooks
with open('speedtriplet.ipynb', 'r') as f:
    speedtriplet = json.load(f)

with open('ensemble.ipynb', 'r') as f:
    ensemble = json.load(f)

# Extract code cells from speedtriplet (it's a single cell with all code)
speedtriplet_code = ""
for cell in speedtriplet['cells']:
    if cell.get('cell_type') == 'code':
        speedtriplet_code += ''.join(cell.get('source', []))

# Extract relevant triplet-related cells from ensemble
# We need cells 19-30 (triplet model section)
ensemble_triplet_code = ""
ensemble_imports = ""

for i, cell in enumerate(ensemble['cells']):
    if cell.get('cell_type') == 'code':
        source = ''.join(cell.get('source', []))
        # Cell 1 is imports
        if i == 1:
            ensemble_imports = source
        # Cells 19+ are triplet model
        if i >= 19:
            ensemble_triplet_code += source + "\n"

print("="*70)
print("CRITICAL DIFFERENCES ANALYSIS")
print("="*70)

# Check 1: CUDA_VISIBLE_DEVICES placement
print("\n1. CUDA_VISIBLE_DEVICES:")
print("-" * 40)

cuda_in_speedtriplet = 'os.environ["CUDA_VISIBLE_DEVICES"]' in speedtriplet_code
speedtriplet_lines = speedtriplet_code.split('\n')
cuda_line_speed = None
import_os_line = None
import_torch_line = None

for i, line in enumerate(speedtriplet_lines):
    if 'CUDA_VISIBLE_DEVICES' in line:
        cuda_line_speed = i
        print(f"speedtriplet: Line {i}: {line.strip()}")
    if line.strip() == 'import os':
        import_os_line = i
    if 'import torch' in line or 'from torch' in line:
        import_torch_line = i

print(f"  - import os at line: {import_os_line}")
print(f"  - CUDA set at line: {cuda_line_speed}")
print(f"  - torch import at line: {import_torch_line}")

cuda_in_ensemble_imports = 'CUDA_VISIBLE_DEVICES' in ensemble_imports
cuda_in_ensemble_triplet = 'CUDA_VISIBLE_DEVICES' in ensemble_triplet_code

print(f"\nensemble imports cell: {cuda_in_ensemble_imports}")
print(f"ensemble triplet cells: {cuda_in_ensemble_triplet}")

if cuda_in_ensemble_imports:
    ensemble_import_lines = ensemble_imports.split('\n')
    for i, line in enumerate(ensemble_import_lines):
        if 'CUDA_VISIBLE_DEVICES' in line:
            print(f"  Found at line {i}: {line.strip()}")
        if 'import torch' in line:
            print(f"  torch import at line {i}: {line.strip()}")

# Check 2: Model path differences
print("\n2. Model Loading:")
print("-" * 40)

# Extract model loading sections
speed_model_load = [line for line in speedtriplet_lines if 'model_path' in line.lower() or 'bge' in line.lower()]
print("speedtriplet model path lines:")
for line in speed_model_load[:5]:
    if line.strip():
        print(f"  {line.strip()}")

# Check 3: Training arguments
print("\n3. Training Arguments:")
print("-" * 40)

# Find SentenceTransformerTrainingArguments in both
speed_training_args = []
in_args = False
for line in speedtriplet_lines:
    if 'SentenceTransformerTrainingArguments' in line:
        in_args = True
    if in_args:
        speed_training_args.append(line)
        if ')' in line and 'args' in line:
            break

print("speedtriplet training args:")
for line in speed_training_args:
    print(f"  {line.rstrip()}")

# Check 4: Imports differences
print("\n4. Import Differences:")
print("-" * 40)

speed_imports = [line.strip() for line in speedtriplet_lines if line.strip().startswith(('import ', 'from '))]
ensemble_imports_list = [line.strip() for line in ensemble_imports.split('\n') if line.strip().startswith(('import ', 'from '))]

print("speedtriplet imports:")
for imp in speed_imports[:15]:
    print(f"  {imp}")

print("\nensemble imports:")
for imp in ensemble_imports_list[:15]:
    print(f"  {imp}")

# Check specific imports
print("\n5. Specific Import Check:")
print("-" * 40)
print(f"speedtriplet has 'from tqdm.auto import tqdm': {'from tqdm.auto import tqdm' in speedtriplet_code}")
print(f"speedtriplet has 'from tqdm import tqdm': {'from tqdm import tqdm' in speedtriplet_code}")
print(f"ensemble has 'from tqdm.auto import tqdm': {'from tqdm.auto import tqdm' in ensemble_imports}")
print(f"ensemble has 'from tqdm import tqdm': {'from tqdm import tqdm' in ensemble_imports}")

print(f"\nspeedtriplet has 'import faiss': {'import faiss' in speedtriplet_code}")
print(f"ensemble has 'import faiss': {'import faiss' in ensemble_imports}")

# Check 6: Function signatures
print("\n6. Function Signatures:")
print("-" * 40)

def extract_function_sig(code, func_name):
    lines = code.split('\n')
    for i, line in enumerate(lines):
        if f'def {func_name}' in line:
            sig = line.strip()
            return sig
    return None

funcs_to_check = ['fine_tune_model', 'load_or_create_finetuned_model', 'generate_embeddings']

for func in funcs_to_check:
    speed_sig = extract_function_sig(speedtriplet_code, func)
    ensemble_sig = extract_function_sig(ensemble_triplet_code, func)
    print(f"\n{func}:")
    print(f"  speed:    {speed_sig}")
    print(f"  ensemble: {ensemble_sig}")
    if speed_sig != ensemble_sig:
        print(f"  ⚠️  DIFFERENT!")

print("\n" + "="*70)
print("SUMMARY OF KEY FINDINGS")
print("="*70)
