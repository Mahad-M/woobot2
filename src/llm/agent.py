from .tools import woocommerce_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv(override=True)

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

agent = create_react_agent(
    model=model,
    tools=woocommerce_tools,
)


# if __name__ == "__main__":
#     inputs = {"messages": ["hello how many products do we have in the store?"]}

#     for s in agent.stream(inputs, stream_mode="values"):
#         message = s["messages"][-1]
#         if isinstance(message, tuple):
#             print(message)
#         else:
#             message.pretty_print()
