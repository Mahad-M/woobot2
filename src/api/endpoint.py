from fastapi import APIRouter
from .schemas import ChatRequest
from ..llm.agent import agent


# Create a router instance
router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    """Root endpoint. Returns a test string"""
    return {"message": "Welcome to the WooBot"}


@router.post("/chat")
async def chat(request: ChatRequest):
    """Chat endpoint."""
    request = request.model_dump()
    inputs = {"messages": request["messages"]}
    agent_response = agent.invoke(input=inputs)
    response = request
    response["messages"].append({"role": "assistant", "content": agent_response["messages"][-1].content})
    
    return response
