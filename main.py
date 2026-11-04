from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


@tool
def search(query: str) -> str:
    """
    Tools that searches over the internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_retries=1,
    timeout=30,
)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-projects!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="What's the weather in Tokyo?")]}
    )
    print(result)


if __name__ == "__main__":
    main()
