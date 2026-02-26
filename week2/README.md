# Week 2: Talking Models - Interactive LLM Chat Applications

Building interactive chat interfaces with local LLMs using Gradio and Ollama.

## 📚 Project Overview

This week explores three progressively advanced applications:

1. **My First Gradio App** - Basic single-model chat interfaces
2. **Talking Models** - Two models with different personalities having conversations
3. **Gradio Talking Models** - Interactive Gradio interface for multi-model conversations

## 🚀 Quick Start

### Prerequisites

**System Requirements:**
- Python 3.8+
- Ollama (https://ollama.ai)
- 4GB RAM minimum

**Install Models:**
```bash
ollama pull mistral
ollama pull llama3.2:1b
```

**Install Python Dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Notebooks

**1. Start Ollama Server** (in a separate terminal)
```bash
ollama serve
```

**2. Launch Jupyter**
```bash
jupyter notebook
```

**3. Open and Execute Notebooks**
- Start with: `01_Gradio_App.ipynb`
- Then: `02_Talking_Models.ipynb`
- Finally: `03_Gradio_Talking_Models.ipynb`

Execute cells in order by pressing Shift + Enter

## 📋 File Structure

```
week2/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── 01_Gradio_App.ipynb               # Notebook 1: Single model chat
├── 02_Talking_Models.ipynb           # Notebook 2: Two-model conversation
└── 03_Gradio_Talking_Models.ipynb    # Notebook 3: Interactive Gradio UI
```

## 📓 Notebook Details

### Notebook 1: My First Gradio App
**Topics:**
- OpenAI SDK with Ollama backend
- Single-turn message functions
- Streaming response handlers
- Basic Gradio Interface
- Enhanced interface with examples
- Streaming with Markdown output

**Examples Used:**
- "If gravity were even slightly stronger or weaker..."
- "Should society prohibit euthanasia..."
- "You have to be a fighter..."
- And more thought-provoking prompts

**What You'll Learn:**
- How to initialize and configure local LLMs
- Building interactive chat functions
- Creating Gradio interfaces
- Streaming vs non-streaming responses

### Notebook 2: Talking Models
**Topics:**
- Multiple model initialization
- Personality-based system prompts
- Message history management
- Multi-turn conversation orchestration
- Model interaction patterns

**System Prompts:**
- **Mistral (Argumentative):** "You are a chatbot who is very argumentative; you disagree with anything in the conversation..."
- **Llama (Polite):** "You are a very polite, courteous chatbot. You try to agree with everything the other person says..."

**What You'll Learn:**
- How different system prompts create personalities
- Message perspective management (who is 'user' vs 'assistant')
- How models adapt to each other
- Multi-turn conversation patterns

### Notebook 3: Gradio Talking Models
**Topics:**
- Interactive Gradio interface design
- Model-to-model conversation orchestration
- Configurable conversation turns
- Example-driven interfaces

**Features:**
- Variable number of turns (1-10)
- Pre-configured example conversations
- Real-time model responses
- Markdown output formatting

**Example Topics:**
- "Hello, how are you today?"
- "What do you think about artificial intelligence?"
- "Is climate change real?"
- "What's the best way to learn?"

## 🔧 Technical Details

### Models

| Model | Speed | Quality | Context | Use |
|-------|-------|---------|---------|-----|
| Mistral | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 8K | Main model |
| Llama 3.2 (1B) | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 8K | Fast, lightweight |

### Key Technologies

**OpenAI SDK**
- Compatible with Ollama's local API endpoint
- Supports both streaming and non-streaming
- Standard interface for LLM communication

**Ollama**
- Local LLM server
- No internet required after setup
- Data stays on your machine

**Gradio**
- Python-only UI framework
- No frontend coding required
- Shareable interfaces

## 📖 Execution Flow

### Notebook 1 Flow:
1. Initialize OpenAI + Ollama connection
2. Select models and system message
3. Define message_llama() function
4. Define stream_llama() function
5. Test with simple question
6. Launch basic Gradio interface
7. Launch enhanced interface with examples
8. Launch streaming interface with Markdown

### Notebook 2 Flow:
1. Initialize client and models
2. Define system prompts (argumentative vs polite)
3. Initialize message histories
4. Define response functions (call_llama, call_mistral)
5. Run individual turns
6. Run 5-turn multi-model conversation

### Notebook 3 Flow:
1. Setup and import
2. Define models and personalities
3. Create conversation management function
4. Build Gradio interface with examples
5. Launch interactive application

## ⚠️ Troubleshooting

**"Connection refused" Error**
- Problem: Ollama server not running
- Solution: Run `ollama serve` in another terminal

**"Model not found" Error**
- Problem: Model hasn't been pulled
- Solution: `ollama pull mistral` and `ollama pull llama3.2:1b`

**Slow Responses**
- Problem: Large model or low resources
- Solution: Use faster model (llama3.2:1b) or close other apps

**Port 7860 Already in Use**
- Problem: Gradio can't bind to port
- Solution: Wait 30 seconds or restart Jupyter

## 🎓 Learning Outcomes

After completing all three notebooks, you'll understand:

✅ Local LLM setup and configuration
✅ Building single and multi-turn conversations
✅ System prompt engineering
✅ Streaming vs non-streaming responses
✅ Message perspective management
✅ Creating interactive Gradio interfaces
✅ Multi-model orchestration
✅ Personality-driven AI interactions

## 💡 Customization Ideas

**Change System Prompts:**
Edit mistral_system and llama_system to create new personalities

**Try Different Models:**
Replace 'mistral' with other available Ollama models

**Add More Examples:**
Extend the examples array in Gradio interfaces

**Modify Conversation Flows:**
Change the number of turns or initial messages

## 📚 Resources

- [Ollama Documentation](https://ollama.ai)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Gradio Docs](https://www.gradio.app/)

## ✅ Checklist

Before running:
- [ ] Python 3.8+ installed
- [ ] Ollama installed
- [ ] Models pulled (mistral, llama3.2:1b)
- [ ] Dependencies installed: `pip install -r requirements.txt`

Before each session:
- [ ] Ollama server running: `ollama serve`

## 📝 Notes

- All notebooks are independent - can be run in any order
- First execution may take time as models load
- Subsequent runs are faster (models cached)
- All data stays local - no API calls
- Notebooks preserve outputs after execution

---

**Happy Learning! 🚀**

*Week 2 | Interactive LLM Chat Applications*
