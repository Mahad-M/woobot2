from pydantic import BaseModel, Field
from typing import Literal


class ChatMessage(BaseModel):
    """Chat message schema"""

    role: Literal["user", "assistant"] = Field(description="Role of the message")
    content: str = Field(description="Content of the message")


class ChatRequest(BaseModel):
    """Chat request schema"""

    messages: list[ChatMessage] = Field(description="List of messages")
