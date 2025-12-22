from google import genai
from core.config import settings
from fastapi.concurrency import run_in_threadpool

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def _generate(prompt: str):
    return client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
    )


async def generate_market_report(sector: str, raw_data: str) -> str:
    prompt = f"""
You are a professional Trade Analyst specializing in the Indian Market.
Based on the following raw market data, generate a comprehensive trade opportunity report for the {sector} sector.

Raw Data: {raw_data}

The report must be in Markdown format and include:
1. # Executive Summary for {sector}
2. ## Current Market Trends (India Context)
3. ## Key Trade Opportunities (Specific niche areas)
4. ## Regulatory & Policy Landscape (e.g., PLI schemes, GST updates)
5. ## Risk Assessment
6. ## Strategic Recommendations

Ensure the tone is professional, data-driven, and concise.
"""

    response = await run_in_threadpool(_generate, prompt)
    return response.text
