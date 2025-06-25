# 🎬 Late Show API (Flask Code Challenge)

A Flask REST API for managing late night TV show guests and episodes. Built with:

- 🐍 Flask + SQLAlchemy (MVC)
- 🗃 PostgreSQL
- 🔐 JWT Authentication
- 📮 Postman for testing

---

## 🚀 Setup Instructions

### 📦 Install Dependencies

```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
🧠 PostgreSQL Database
Ensure PostgreSQL is installed and running.

Create the database:

sql
Copy
Edit
CREATE DATABASE late_show_db;
⚙️ Environment Configuration
In server/config.py, ensure your DB URI is correct:

python
Copy
Edit
SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@localhost:5432/late_show_db"
JWT_SECRET_KEY = "your-secret-key"
🧱 Database Setup
bash
Copy
Edit
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
