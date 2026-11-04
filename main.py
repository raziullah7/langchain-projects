import socket

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# from langchain_ollama import ChatOllama

load_dotenv()

# Workaround: IPv6 to Google's API hangs on this network, so resolve IPv4 only.
_getaddrinfo = socket.getaddrinfo
socket.getaddrinfo = lambda *a, **k: [
    r for r in _getaddrinfo(*a, **k) if r[0] == socket.AF_INET
]


def main():
    # print("Hello from langchain-course!")
    # print(os.getenv("GOOGLE_API_KEY"))

    information = "Batman"

    summary_template = """
    give short information about {information}
    1. short summary
    2. two fun facts
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    gemini_llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
    # local_llm = ChatOllama(temperature=0, model="gemma4:e2b")

    chain = summary_prompt_template | gemini_llm

    result = chain.invoke(input={"information": information})
    print(result.content)


if __name__ == "__main__":
    main()
