# MetricMind Architecture

## System Architecture

User
   ↓
Frontend (Next.js)
   ↓
Backend (FastAPI)
   ↓
LLM (LangChain)
   ↓
Semantic Layer (Cube.dev)
   ↓
Snowflake Database
   ↓
Business Dataset

## Workflow

1. User enters a business question.
2. Frontend sends the request to the backend.
3. Backend forwards it to the LLM.
4. The LLM interprets the question.
5. Cube.dev generates the business query.
6. Snowflake retrieves the required data.
7. Results are returned to the frontend.
8. Dashboard displays the insights.