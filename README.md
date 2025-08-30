<!-- @format -->

Project Structure
/frontend
/src
/pages/Task.tsx
/services/Tasks.ts
/backend
/app
/core/database.py
/models/task.py
/schemas/task.py
/crud/task.py
/main.py
.env.example
README.md

Backend Setup

1. Clone the repo
   git clone <repo_url>
   cd Backend

2. Create a virtual environment
   python -m venv venv
   venv\Scripts\activate # On Windows

3. Install dependencies
   pip install -r requirements.txt

4. Set up environment variables
   Copy .env.example to .env and update values if needed.

5. Create PostgreSQL database
   Login to psql:
   psql -U postgres -h localhost

Then inside psql:
CREATE DATABASE todo_db;
\q

6. Run the backend server
   uvicorn app.main:app --reload

The server will be available at:
👉 http://127.0.0.1:8000

What Works:
FastAPI backend set up with PostgreSQL.
Database (todo_db) created and connected.
tasks table automatically created using SQLAlchemy models.
Backend server runs successfully with no errors.

Next Steps
Build API endpoints for CRUD operations on tasks.
Connect frontend (Task.tsx + Tasks.ts) to backend.
Add UI for creating, updating, and listing tasks.

📌 Notes
Setting up a working backend
Ensuring the database is connected and schema created
Preparing the frontend structure for integration
