from dotenv import load_dotenv
from fastapi import Request, HTTPException
import os


load_dotenv(override=True)


ALLOWED_ORIGINS = [
    os.getenv("wc_url"),
    "http://localhost:8000"  # TODO: REMOVE THIS FOR PRODUCTION
]

def verify_origin(request: Request):
    origin = request.headers.get("origin") or request.headers.get("referer")
    if not origin or not any(origin.startswith(allowed) for allowed in ALLOWED_ORIGINS):
        raise HTTPException(status_code=403, detail="Forbidden: Invalid origin")