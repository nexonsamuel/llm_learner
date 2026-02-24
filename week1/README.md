# Week 1: PDF Summarizer

A Python-based PDF summarization tool that uses LLMs (Large Language Models) to generate intelligent summaries of PDF documents. The tool supports multiple models including TinyLlama, GPT-4, and Claude.

## Overview

This project demonstrates a multi-stage summarization pipeline:
1. Extract text from PDF files using PyMuPDF
2. Split text into token-safe chunks to respect model context windows
3. Summarize each chunk individually using an LLM
4. Combine chunk summaries and generate a final coherent summary
5. Save the output to a timestamped file

## Project Structure

```
week1/
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── data/                         # PDF files to summarize (create this folder)
├── output/                       # Generated summaries (auto-created)
├── examples/
│   └── run_summary.py           # Main entry point script
├── pdf_summarizer/
│   ├── __init__.py              # Package initialization
│   ├── pdf_parser.py            # PDF text extraction
│   ├── chunker.py               # Token-based text chunking
│   ├── summarizer.py            # Core summarization logic
│   └── model_constants.py        # Model configurations
└── tests/
    └── test_summarizer.py        # Unit tests
```

## Features

- **Multiple Model Support**: Works with TinyLlama, GPT-4, GPT-3.5, and Claude models
- **Dynamic Token Chunking**: Automatically adjusts chunk size based on model context window
- **Safety Factor**: Configurable safety margin (default 30%) to avoid context window overflow
- **Environment Variables**: Secure API key management using `.env` file
- **Progress Feedback**: Clear console output showing processing steps
- **Output Persistence**: Saves summaries with timestamps for record-keeping
- **Error Handling**: Graceful error handling with informative messages

## Setup

### 1. Create Virtual Environment

```bash
cd week1
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
# For OpenAI models (GPT-4, GPT-3.5)
OPENAI_API_KEY=sk-your-openai-key-here

# For Anthropic models (Claude)
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here

# For local Ollama models (TinyLlama, Llama 2, Mistral)
# No API key needed, just ensure ollama serve is running
```

### 4. Prepare Input Files

Create a `data/` folder and add your PDF files:

```bash
mkdir data
# Add your PDF files to the data/ folder
```

## Usage

### Basic Usage (Default Model: TinyLlama)

```bash
python examples/run_summary.py
```

### Using Different Models

To use a different model, modify `run_summary.py`:

```python
# Change this line:
summary = summarize_pdf(str(pdf_path))

# To:
summary = summarize_pdf(str(pdf_path), model="gpt-4")
```

### Programmatic Usage

```python
from pdf_summarizer import summarize_pdf

# Summarize with default settings (TinyLlama)
summary = summarize_pdf("path/to/document.pdf")

# Summarize with GPT-4 and custom safety factor
summary = summarize_pdf(
    "path/to/document.pdf",
    model="gpt-4",
    safety_factor=0.40  # Use 40% of context window
)

print(summary)
```

## Supported Models

| Model | Provider | Context Window | Use Case |
|-------|----------|---|---|
| `tinyllama` | Ollama (Local) | 2,048 | Fast, free, local processing |
| `llama-2` | Ollama (Local) | 4,096 | Better quality, still local |
| `mistral` | Ollama (Local) | 8,192 | High-quality local processing |
| `gpt-3.5-turbo` | OpenAI | 4,096 | Fast, affordable cloud option |
| `gpt-4` | OpenAI | 8,192 | High-quality summaries |
| `gpt-4-turbo` | OpenAI | 128,000 | Very long documents |
| `claude-3-sonnet` | Anthropic | 200,000 | Excellent quality |
| `claude-3-opus` | Anthropic | 200,000 | Best quality |

## Key Concepts

### Token-Based Chunking

The tool uses `tiktoken` to split PDFs into token-safe chunks. This ensures:
- Each chunk respects the model's context window limit
- Accurate token counting prevents errors
- Efficient processing of large documents

**Max Tokens Calculation:**
```
max_tokens = int(context_window * safety_factor)
```

Example for TinyLlama (2,048 context window):
```
max_tokens = int(2048 * 0.30) = 614 tokens per chunk
```

### Multi-Stage Summarization

1. **Chunk Summarization**: Each chunk is summarized independently
2. **Summary Combination**: All chunk summaries are concatenated
3. **Final Summary**: A final pass creates a coherent overall summary

This approach handles very long documents by breaking them into manageable pieces.

### API Key Security

API keys are stored in `.env` file which:
- Is gitignored (never committed to repository)
- Is loaded at runtime via `python-dotenv`
- Keeps sensitive data secure

## Output

Summaries are saved to the `output/` folder with timestamped filenames:

```
output/
├── Nexon_Samuel_summary_20250223_143022.txt
├── research_paper_summary_20250223_144156.txt
└── article_summary_20250223_150305.txt
```

Each file contains:
```
PDF: document_name.pdf
Generated: 2025-02-23 14:30:22
================================================================================

[Summary text here...]
```

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - `PyMuPDF==1.23.1` - PDF text extraction
  - `openai==1.33.0` - LLM API client
  - `tiktoken==0.4.0` - Token counting
  - `rich==13.6.0` - Beautiful console output
  - `python-dotenv==1.0.0` - Environment variable management

## Local Model Setup (Ollama)

To use local models like TinyLlama without API keys:

1. Install Ollama: https://ollama.ai
2. Start Ollama server:
   ```bash
   ollama serve
   ```
3. Pull a model:
   ```bash
   ollama pull tinyllama
   ```
4. Run the summarizer (it will automatically connect to `http://localhost:11434/v1`)

## Testing

Run unit tests:

```bash
pytest tests/test_summarizer.py
```

## Troubleshooting

### "Cannot connect to TinyLlama server"
- Ensure Ollama is running: `ollama serve`
- Check the server URL is correct: `http://localhost:11434/v1`

### "No PDF files found"
- Create a `data/` folder in the project root
- Add PDF files to the `data/` folder

### API Key errors
- Verify your API key is correct in `.env`
- Ensure you have sufficient API credits
- Check that the model name matches your plan

### Token limit exceeded
- Reduce the `safety_factor` (less safe but allows larger chunks)
- Use a model with a larger context window
- Split PDFs into smaller files manually

## Architecture

### `pdf_parser.py`
Handles PDF text extraction using PyMuPDF (fitz). Iterates through all pages and concatenates the text.

### `chunker.py`
Splits text into chunks based on token count rather than character count. Uses `tiktoken` for accurate token counting.

### `summarizer.py`
Orchestrates the entire pipeline:
- Loads model configuration
- Initializes LLM client
- Processes chunks
- Generates final summary

### `model_constants.py`
Centralized configuration for all supported models:
- Model names and API endpoints
- Context window sizes
- API key references

## Best Practices

1. **Start with local models** (TinyLlama) for testing
2. **Use safety_factor=0.30** as a conservative default
3. **Monitor API usage** when using cloud models (GPT, Claude)
4. **Batch process** multiple PDFs to save on API costs
5. **Test with small PDFs** first to ensure setup is correct

## Future Enhancements

- Support for other document formats (DOCX, PPTX)
- Configurable summary length (brief, medium, detailed)
- Language translation support
- Custom summarization prompts
- Batch processing with progress tracking
- Web interface for easier access

## License

This project is part of a LLM learning experimentation.

## Author

Created for data engineering education and practice.