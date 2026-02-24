# data_engg_tutor

A comprehensive, hands-on learning resource for mastering core Data Engineering concepts through practical LLM-based projects.

## Overview

This repository contains a series of data engineering projects that teach fundamental concepts by building real-world applications. Each week focuses on different aspects of data engineering, from pipeline design to multi-provider orchestration.

**Learning Approach:** Learn by doing. Each project is a complete, working system that demonstrates core concepts in practice.

## Project Structure

```
data_engg_tutor/
├── README.md                    # This file (general overview)
├── day1.ipynb                   # Initial exploration and experiments
│
└── week1/                        # Week 1: PDF Summarizer
    ├── README.md               # → Detailed project documentation
    ├── requirements.txt
    ├── check_ollama_enhanced.sh
    ├── data/                   # Input PDF files
    ├── output/                 # Generated summaries
    ├── examples/
    │   └── run_summary.py
    ├── pdf_summarizer/
    │   ├── pdf_parser.py
    │   ├── chunker.py
    │   ├── summarizer.py
    │   └── model_constants.py
    └── tests/
        └── test_summarizer.py
```

## Weeks at a Glance

### [Week 1: PDF Summarizer & Resume Evaluator](./week1/README.md)

Build a document processing pipeline that:
- Extracts text from PDFs
- Intelligently chunks content respecting token limits
- Summarizes using LLMs
- Evaluates resumes with hiring insights

**Key Learning:** Token-based chunking, multi-stage pipelines, configuration management, multi-provider LLM orchestration.

**Technologies:** PyMuPDF, Tiktoken, OpenAI API, Anthropic API, Ollama (local models)

**Recommended Model:** Mistral 7B

→ [Read Week 1 Full Documentation](./week1/README.md)

## Getting Started

Choose your path:

### Quick Start (Local Models - Free)
```bash
cd week1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./check_ollama_enhanced.sh mistral
python examples/run_summary.py
```

### With Cloud Models (OpenAI/Anthropic)
```bash
cd week1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
python examples/run_summary.py
```

## Core Concepts Covered

### Week 1
- **Token Counting & Context Windows** - Why LLMs have limits and how to work within them
- **Text Chunking Strategies** - Splitting large documents intelligently
- **Multi-Stage Pipelines** - Breaking complex tasks into manageable steps
- **Provider Abstraction** - Supporting multiple LLM backends with unified interface
- **Configuration Management** - Centralizing settings for maintainability
- **Prompt Engineering** - Crafting effective instructions for better output

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| PDF Parsing | PyMuPDF | Extract text from documents |
| Token Counting | Tiktoken | Accurate token measurement |
| LLM Access | OpenAI SDK | API client for multiple providers |
| Local Models | Ollama | Run models locally without API keys |
| Config | Python dicts + dotenv | Centralized, secure settings |
| CLI Output | Rich | Beautiful console formatting |
| Testing | Pytest | Unit test framework |

## Model Support

### Local Models (Free, No API Keys)
- Mistral 7B (Recommended)
- Phi 2
- Neural Chat 7B
- Orca 2 7B

### Cloud Models (Paid, High Quality)
- OpenAI: GPT-4, GPT-3.5-turbo
- Anthropic: Claude 3 Opus, Claude 3 Sonnet
- Google: Coming soon

## Real-World Applications

The techniques you'll learn apply to:
- **Automated Resume Screening** - Evaluate candidates at scale
- **Document Analysis** - Extract insights from large documents
- **Content Summarization** - Create executive summaries
- **Data Extraction** - Convert unstructured to structured data
- **Report Generation** - Analyze and summarize business documents
- **Research Analysis** - Process academic papers and research
- **Legal Document Review** - Extract terms from contracts

## Learning Path

1. **Week 1:** Understand token limits, learn chunking strategies, build your first pipeline
2. **Week 2+:** (Coming soon) More advanced topics

## Prerequisites

- Python 3.8+
- Basic understanding of APIs and JSON
- 4GB RAM (for local models)
- Optional: API keys for OpenAI/Anthropic

## Installation & Setup

Full setup instructions are in each week's README:
- [Week 1 Setup](./week1/README.md#quick-start)

## FAQ

**Q: Do I need API keys?**
A: No! You can run everything locally with Ollama and models like Mistral. API keys are optional for cloud models.

**Q: Which model should I start with?**
A: Mistral 7B. It's free, fast, and high-quality. Try it first!

**Q: How much disk space do I need?**
A: ~5-10GB for a few local models. Cloud models use no local space.

**Q: Can I use different models?**
A: Yes! All models are configured in `model_constants.py`. Add new models easily.

**Q: How do I improve output quality?**
A: Tweak the prompts in the code. See Week 1's prompt engineering section.

## Best Practices

1. **Start simple** - Use local models first to understand the concepts
2. **Test small** - Try with small PDFs before processing large batches
3. **Iterate on prompts** - Output quality improves dramatically with better instructions
4. **Monitor costs** - If using cloud APIs, track token usage
5. **Keep secrets safe** - Never commit `.env` files with API keys

## Performance Benchmarks

**Typical performance on 2-page resume:**

| Model | Time | Quality | Cost |
|-------|------|---------|------|
| Mistral (local) | 5-10s | ⭐⭐⭐⭐⭐ | Free |
| GPT-3.5 (cloud) | 2-3s | ⭐⭐⭐⭐⭐ | ~$0.01 |
| GPT-4 (cloud) | 3-5s | ⭐⭐⭐⭐⭐⭐ | ~$0.10 |

## Troubleshooting

See the specific week's README for detailed troubleshooting:
- [Week 1 Troubleshooting](./week1/README.md#troubleshooting)

## Feedback & Contributions

Found an issue? Want to suggest improvements? 
- Check if it's addressed in the specific week's README
- Test with the latest code
- Provide clear reproduction steps

## Resources

### Model Documentation
- [Ollama](https://ollama.ai) - Run LLMs locally
- [OpenAI API](https://platform.openai.com/docs) - GPT models
- [Anthropic Claude](https://docs.anthropic.com) - Claude models

### Learning Resources
- [Tiktoken - Token Counting](https://github.com/openai/tiktoken)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/gpt-best-practices)
- [LLM Context Windows](https://www.promptingguide.ai/)

## Future Roadmap

- **Week 2:** Multi-format document processing (DOCX, PPTX)
- **Week 3:** Building a vector database with embeddings
- **Week 4:** Real-time data pipelines with streaming
- **Week 5:** Production deployment and monitoring

## License

Educational project for learning data engineering concepts.

## Author

Created to teach practical data engineering through hands-on LLM applications.

---

**Ready to learn?** Start with [Week 1: PDF Summarizer](./week1/README.md)