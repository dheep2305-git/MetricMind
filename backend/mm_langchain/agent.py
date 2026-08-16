import os

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from .prompt import SYSTEM_PROMPT


# ==========================================
# LOAD GROQ LLM
# ==========================================

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise RuntimeError(
        "GROQ_API_KEY environment variable is not set."
    )


llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0
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
- Do NOT use external data.
- Explain the answer clearly and briefly.
- If the question cannot be answered using the available metrics,
  politely say that the information is not available.
- When comparing values, identify the highest and lowest when appropriate.

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
    print("✅ LangChain Groq Agent Executed")
    print("====================================\n")

    try:

        chain = prompt | llm

        response = chain.invoke({
            "system_prompt": SYSTEM_PROMPT,
            "metrics": metrics,
            "question": question
        })

        return response.content

    except Exception as e:

        print("❌ Groq Agent Error:", e)

        return f"Unable to process your question: {str(e)}"