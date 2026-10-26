"""
Website to Clean Markdown, Vector RAG Chunks & llms.txt — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/ai-ready-website-to-markdown-rag-crawler ($0.50 / 1,000 pages)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~ai-ready-website-to-markdown-rag-crawler/run-sync-get-dataset-items"

payload = {
    "startUrls": [
        "https://docs.apify.com",
        "https://modelcontextprotocol.io"
    ],
    "chunkSizeTokens": 500
}

if __name__ == "__main__":
    print(f"Running Website to Clean Markdown, Vector RAG Chunks & llms.txt on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
