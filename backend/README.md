# FastAPI backend

Copy `.env.example` to `.env` and provide PostgreSQL and JWT settings. Apply `database/schema.sql` before starting the API.

```powershell
pip install -r requirements.txt
uvicorn app.main:app --reload
```