from duckduckgo_search import DDGS
import logging

def fetch_market_data(sector: str) -> str:
    """Scrapes current market news and trends for the specified sector in India."""
    try:
        with DDGS() as ddgs:
            query = f"current trade opportunities {sector} sector India market news 2024 2025"
            results = ddgs.text(query, max_results=6)
            
            context_text = "\n".join([f"Source: {r['title']}\nContent: {r['body']}" for r in results])
            return context_text
    except Exception as e:
        logging.error(f"Search error: {e}")
        return ""