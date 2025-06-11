# 🗒️ Flask Notes App REST API

A simple and extendable RESTful API for creating, reading, updating, and deleting notes — built with **Python Flask**. This project follows clean backend architecture with routing, input validation, and optional JWT authentication.

---

## 📌 Project Goals


- Add features incrementally:
  - MethodView
  - Blueprints
  - Marshmallow Validation
  - Flask-Smorest (OpenAPI docs)
  - JWT Auth
  - Docker Support (optional)

---

## 🚧 Project Progress Checklist

| Day | Feature                                  | Status    |
|-----|------------------------------------------|-----------|
| 1   | Basic Flask App with GET, POST, DELETE   | ✅ Done   |
| 2   | Add PUT for updating notes               | ✅ Done   |
| 3   | Add Search & Filter by tag/query         | ⬜ Pending |
| 4   | Refactor with Blueprints                 | ✅ Done |
| 5   | Use MethodView Class-Based Views         | ✅ Done |
| 6   | Add Marshmallow Schemas                  | ✅ Done |
| 7   | Switch to Flask-Smorest (Swagger docs)   | ✅ Done |
| 8   | Add JWT Authentication                   | ⬜ Pending |


---

## 📝 Features

- Full CRUD for Notes
- Each note includes:
  - `title` (required)
  - `body` (optional)
  - `tags` (optional list of strings)
  - `created_at` (auto-generated UTC timestamp)
  - `task_id` (auto generated using uuid)
- Input validation
- In-memory data storage (`db.py`)
- Blueprint and MethodView support planned

---

## 🔧 Installation

```bash

pip install -r requirements.txt
flask run
