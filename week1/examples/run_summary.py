import requests
from pathlib import Path
import sys

# Add parent folder to sys.path for imports
sys.path.append(str(Path(__file__).parent.parent))
from pdf_summarizer import summarize_pdf

# Check if Ollama/TinyLlama server is running
SERVER_URL = "http://localhost:11434/v1"

try:
    r = requests.get(f"{SERVER_URL}/models", timeout=2)
    r.raise_for_status()
except requests.RequestException:
    print(f"⚠️  Cannot connect to TinyLlama server at {SERVER_URL}.")
    print("Make sure you have run: ollama serve")
    sys.exit(1)

# Path to the data folder
data_folder = Path(__file__).parent.parent / "data"

# Find all PDF files in the data folder
pdf_files = list(data_folder.glob("*.pdf"))
if not pdf_files:
    raise FileNotFoundError(f"No PDF files found in {data_folder}")

# Loop over each PDF and summarize
for pdf_path in pdf_files:
    print(f"\n===== Summarizing: {pdf_path.name} =====\n")
    summary = summarize_pdf(str(pdf_path))
    print(summary)
    print("\n" + "="*80 + "\n")