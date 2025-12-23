from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from core.config import settings
from core.security import create_access_token, verify_token
from services.search_service import fetch_market_data
from services.ai_service import generate_market_report

app = FastAPI(title="Trade Opportunities API")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Simple guest login: allow any user with password 'password'
    if form_data.password != "password":
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

from fastapi import FastAPI, Depends, HTTPException, Request  # Added Request here
from fastapi.security import OAuth2PasswordRequestForm
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# ... (keep your other imports same)
@app.get("/")
async def root():
    return {"message": "Welcome to the Trade Opportunities API. Go to /docs for API documentation."}

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    sector: str, 
    request: Request,  # <--- Add this argument here
    token: str = Depends(verify_token)
):
    """
    Main endpoint to get a market analysis report.
    """
    # 1. Fetch Data
    market_context = fetch_market_data(sector)
    if not market_context:
        raise HTTPException(status_code=503, detail="Failed to fetch market data")
    
    # 2. Analyze with Gemini
    try:
        report_md = await generate_market_report(sector, market_context)
        return {
            "sector": sector,
            "status": "success",
            "report": report_md
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Analysis failed: {str(e)}")