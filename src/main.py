from dotenv import load_dotenv
from src.api.server import app
import uvicorn
import ngrok
import os

load_dotenv(override=True)

if __name__ == "__main__":
    port=8000
    listener = ngrok.forward(
        addr=f"localhost:{port}",
        authtoken_from_env=True,
        domain=os.getenv("NGROK_DOMAIN"),
    )
    uvicorn.run(app, host="0.0.0.0", port=port)
