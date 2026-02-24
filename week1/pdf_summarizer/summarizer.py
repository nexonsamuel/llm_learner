from openai import OpenAI
from .pdf_parser import pdf_parser_func
from .chunker import chunk_text_by_tokens

def summarize_pdf(path):
    """
    Summarize a PDF using TinyLlama with token-based chunking.
    """
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )

    pdf_text = pdf_parser_func(path)
    chunks = chunk_text_by_tokens(pdf_text, max_tokens=500)

    summaries = []

    # Summarize each chunk
    for chunk in chunks:
        messages = [
            {"role": "system", "content": "You are an academically excellent summarizer."},
            {"role": "user", "content": chunk}
        ]

        response = client.chat.completions.create(
            model="tinyllama",
            messages=messages
        )
        summaries.append(response.choices[0].message.content)

    # Combine summaries
    combined_summary = "\n".join(summaries)

    # Optional: final summary
    final_response = client.chat.completions.create(
        model="tinyllama",
        messages=[
            {"role": "system", "content": "Provide a concise, coherent final summary."},
            {"role": "user", "content": combined_summary}
        ]
    )

    return final_response.choices[0].message.content