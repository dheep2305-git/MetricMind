from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

from .prompt import SYSTEM_PROMPT

# Load Ollama Llama 3.2
llm = Ollama(model="llama3.2")

# Prompt Template
template = """
{system_prompt}

Business Metrics:

{metrics}

User Question:

{question}

Instructions:

- Answer ONLY using the provided business metrics.
- Do NOT invent values.
- Explain your reasoning clearly.
- If the question cannot be answered using the available metrics, politely say so.

Answer:
"""

prompt = PromptTemplate(
    input_variables=[
        "system_prompt",
        "metrics",
        "question"
    ],
    template=template,
)

# Create LangChain LLM Chain
chain = LLMChain(
    llm=llm,
    prompt=prompt
)


def ask_agent(metrics, question):

    # This message proves LangChain is being used
    print("\n====================================")
    print("✅ LangChain Agent Executed")
    print("====================================\n")

    answer = chain.run(
        system_prompt=SYSTEM_PROMPT,
        metrics=metrics,
        question=question
    )

    return answer