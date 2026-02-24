import pytest
from pdf_summarizer import summarize_pdf

def test_summarize_pdf():
    pdf_path = "tests/sample.pdf"
    result = summarize_pdf(pdf_path)
    assert isinstance(result, str)
    assert len(result) > 0