from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoint import router
from dotenv import load_dotenv
import os


load_dotenv(override=True)

# Create FastAPI app
app = FastAPI(
    title="WooBot API",
    description="WooBot API server",
    version="0.1.0",
)

# Include the router
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("wc_url")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   