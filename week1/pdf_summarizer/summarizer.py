from openai import OpenAI
from rich.console import Console
from .pdf_parser import pdf_parser_func
from .chunker import chunk_text_by_tokens
from .model_constants import (
    MODEL_CONFIGS,
    DEFAULT_MODEL,
    DEFAULT_SAFETY_FACTOR,
)

console = Console()

def summarize_pdf(path, model=DEFAULT_MODEL, safety_factor=DEFAULT_SAFETY_FACTOR):
    """
    Summarize a PDF using specified model with dynamic token chunking.
    
    Args:
        path: Path to PDF file
        model: Model name (default: "tinyllama")
               Available: "tinyllama", "gpt-4", "gpt-4-turbo", "claude-3-sonnet", etc.
        safety_factor: Fraction of context window to use for chunks (default: 0.30)
    
    Returns:
        str: Final summary of the PDF
    
    Raises:
        ValueError: If model is not supported
    """
    # Validate model
    if model not in MODEL_CONFIGS:
        available = ", ".join(MODEL_CONFIGS.keys())
        console.print(
            f"[red]Error: Model '{model}' not supported.[/red]\n"
            f"[yellow]Available models: {available}[/yellow]"
        )
        raise ValueError(f"Model '{model}' not supported")
    
    config = MODEL_CONFIGS[model]
    
    # Calculate max_tokens dynamically
    max_tokens = int(config["context_window"] * safety_factor)
    
    # Initialize client
    client = OpenAI(
        base_url=config["base_url"],
        api_key=config["api_key"]
    )

    # Parse PDF
    console.print("[cyan]Parsing PDF...[/cyan]")
    pdf_text = pdf_parser_func(path)
    chunks = chunk_text_by_tokens(pdf_text, max_tokens=max_tokens)
    console.print(f"[green]✓[/green] PDF parsed ({len(chunks)} chunks)\n")

    summaries = []

    # Summarize each chunk
    console.print(f"[cyan]Summarizing chunks using {model}...[/cyan]")
    for chunk in chunks:
        messages = [
            {"role": "system", "content": "You are an academically excellent summarizer."},
            {"role": "user", "content": chunk}
        ]

        response = client.chat.completions.create(
            model=config["name"],
            messages=messages
        )
        summaries.append(response.choices[0].message.content)

    console.print(f"[green]✓[/green] All chunks summarized\n")

    # Combine summaries
    combined_summary = "\n".join(summaries)

    # Final summary
    console.print("[cyan]Creating final summary...[/cyan]")
    final_response = client.chat.completions.create(
        model=config["name"],
        messages=[
            {"role": "system", "content": "Provide a concise, coherent final summary."},
            {"role": "user", "content": combined_summary}
        ]
    )

    console.print("[green]✓[/green] Summary complete\n")
    
    return final_response.choices[0].message.content