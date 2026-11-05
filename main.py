from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

# Workaround: if IPv6 to Google's API hangs on your network, uncomment
# this to resolve IPv4 only.
import socket

_getaddrinfo = socket.getaddrinfo
socket.getaddrinfo = lambda *a, **k: [
    r for r in _getaddrinfo(*a, **k) if r[0] == socket.AF_INET
]

# custom search tool using tavily - not needed when the team already has lanchain_tavily
# from tavily import TavilyClient

# tavily = TavilyClient()


# @tool
# def search(query: str) -> dict:
#     """
#     Tools that searches over the internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-projects!")
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(content="Search the weather for Tokyo, Lahore and London")
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
