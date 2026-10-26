"""
Website to Clean Markdown, Vector RAG Chunks & llms.txt — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/ai-ready-website-to-markdown-rag-crawler ($0.50 / 1,000 pages)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~ai-ready-website-to-markdown-rag-crawler/run-sync-get-dataset-items"

def run_ai_ready_website_to_markdown_rag_crawler(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes Website to Clean Markdown, Vector RAG Chunks & llms.txt on Apify Cloud ($0.50/1k pages).
    Convert any website or documentation portal into clean boilerplate-free Markdown, overlapping vector RAG chunks with token estimates, H1-H3 hierarchy outlines, and ready-to-deploy /llms.txt index files.
    """
    default_payload = {
    "startUrls": [
        "https://docs.apify.com",
        "https://modelcontextprotocol.io"
    ],
    "chunkSizeTokens": 500
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
