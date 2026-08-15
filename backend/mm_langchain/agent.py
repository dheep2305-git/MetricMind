from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

from .prompt import SYSTEM_PROMPT


# ==========================================
# LOAD OLLAMA LLAMA 3.2
# ==========================================

llm = OllamaLLM(
    model="llama3.2"
)


# ==========================================
# PROMPT TEMPLATE
# ==========================================

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


# ==========================================
# CREATE PROMPT
# ==========================================

prompt = PromptTemplate(
    input_variables=[
        "system_prompt",
        "metrics",
        "question"
    ],
    template=template
)


# ==========================================
# ASK AGENT
# ==========================================

def ask_agent(metrics, question):

    print("\n====================================")
    print("✅ LangChain Agent Executed")
    print("====================================\n")

    # Connect prompt to LLM
    chain = prompt | llm

    # Execute the chain
    answer = chain.invoke({
        "system_prompt": SYSTEM_PROMPT,
        "metrics": metrics,
        "question": question
    })

    return answer