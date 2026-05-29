from dotenv import load_dotenv
load_dotenv()
from importlib.metadata import version

core_version = version("langchain_core")
graph_version = version("langgraph")
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

print(f"langchain_core version: {core_version}")
print(f"langgraph version: {graph_version}")

def main():
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    response = llm.invoke("Say 'set up complete' in one word.")
    print(f"Response from ChatOpenAI: {response}")

    llm_anthropic = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
    response_anthropic = llm_anthropic.invoke("Say 'set up complete' in one word.")
    print(f"Response from ChatAnthropic: {response_anthropic}")


if __name__ == "__main__":
    main()
