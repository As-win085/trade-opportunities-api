# India Trade Opportunities API

A FastAPI service that analyzes Indian market sectors using real-time search and Google Gemini AI.

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Environment Variables**: Create a `.env` file and add your `GEMINI_API_KEY`.
4. **Run the server**: `python main.py`

## How to Test
1. Open `http://127.0.0.1:8000/docs` (Swagger UI).
2. Use the `/token` endpoint (Username: `admin`, Password: `password`) to get a JWT.
3. Click **Authorize** and paste the token.
4. Execute `GET /analyze/pharmaceuticals`.