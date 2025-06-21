from fastapi import APIRouter, Depends
from src.api.schemas import ChatMessage
from src.llm.agent import agent
from src.api.utils import verify_origin

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
async def chat(request: ChatMessage, _=Depends(verify_origin)):
    """Chat endpoint."""
    request = request.model_dump()
    inputs = {"messages": request}
    agent_response = agent.invoke(input=inputs, config={"configurable": {"thread_id": request["session_id"]}})
    response = {"messages": []}
    response["messages"].append({"role": "assistant", "content": agent_response["messages"][-1].content})
        
    return response

@router.get("/get_message_history/{session_id}")
async def get_message_history(session_id: str, _=Depends(verify_origin)):
    """Retrieve all messages of a particular session."""
    response = {"messages": []}
    try:
        state = agent.get_state(config={"configurable": {"thread_id": session_id}}).values["messages"]
    except KeyError:
        return response
    
    for message in state:
        mess = {}
        # TODO: not subscriptable error
        if message.type == "human":
            mess["role"] = "user"
        else:
            mess["role"] = "assistant"
        mess["content"] = message.content
        response["messages"].append(mess)
    return response