# Authentication application

This repository keeps the Vercel-ready React frontend and AWS-ready FastAPI backend independent.

## Local setup

1. Apply `database/schema.sql` to local PostgreSQL with pgAdmin, or run `docker compose up --build`.
2. Copy `backend/.env.example` to `backend/.env` and fill in database credentials and a strong JWT secret.
3. Copy `frontend/.env.example` to `frontend/.env` and set `VITE_API_URL=http://localhost:8000`.
4. Run the frontend from `frontend/` with `npm install && npm run dev`.
5. Run the backend from `backend/` with `pip install -r requirements.txt && uvicorn app.main:app --reload`.

The frontend contains no database credentials or JWT secrets. Configure `FRONTEND_URL` to the exact Vercel URL in production and use a PostgreSQL-compatible Supabase connection in the backend environment.

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and Oxlint's TypeScript related rules in your project.
