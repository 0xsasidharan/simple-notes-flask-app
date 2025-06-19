
# 🗒️ Flask Notes App REST API

A simple and extendable RESTful API for creating, reading, updating, and deleting notes — built with **Python Flask**.  
This project follows clean backend architecture with proper routing, validation, optional JWT auth, and OpenAPI documentation.

---


## 📝 Features

- Full CRUD for Notes
- Each note includes:
  - `title` (required)
  - `body` (optional)
  - `tags` (optional list of strings)
  - `created_at` (auto-generated UTC timestamp)
  - `note_id` (UUID)
- Input validation using Marshmallow
- RESTful structure using Blueprints and MethodView
- OpenAPI documentation via Flask-Smorest
- JWT-based authentication (coming soon)
- Docker support


---

## 🚧 Project Progress Checklist

| Day | Feature                                  | Status    |
|-----|------------------------------------------|-----------|
| 1   | Basic Flask App with GET, POST, DELETE   | ✅ Done   |
| 2   | Add PUT for updating notes               | ✅ Done   |
| 3   | Add Search & Filter by tag/query         | ✅ Done   |
| 4   | Refactor with Blueprints                 | ✅ Done   |
| 5   | Use MethodView Class-Based Views         | ✅ Done   |
| 6   | Add Marshmallow Schemas                  | ✅ Done   |
| 7   | Switch to Flask-Smorest (Swagger docs)   | ✅ Done   |
| 8   | Add Docker Containerization              | ✅ Done   |
| 9  | Database Inegration                       | ✅ Done   |
| 10   | Add JWT Authentication                  | ⬜ Pending |

---

## 📘 API Endpoints

### `GET /notes`

**Description:** Retrieve all notes. Optionally filter notes by a specific tag.

**Query Parameters:**
- `tag` (optional): Filter notes by a specific tag.

**Responses:**
- `200 OK`: Returns a list of notes.
- `404 Not Found`: If a tag is provided but no notes match.

---

### `POST /notes`

**Description:** Create a new note.

**Request Body (JSON):**
```json
{
  "title": "Buy Groceries",
  "body": "Milk, Eggs, Bread",
  "tags": ["personal", "shopping"]
}
````

**Responses:**

* `201 Created`: Returns the created note with `note_id` and `created_at`.
* `400 Bad Request`: If required fields are missing.

---

### `GET /notes/<note_id>`

**Description:** Retrieve a single note by its ID.

**URL Parameters:**

* `note_id`: UUID of the note to retrieve.

**Responses:**

* `200 OK`: Returns the note.
* `404 Not Found`: If the note does not exist.

---

### `PUT /notes/<note_id>`

**Description:** Update an existing note.

**URL Parameters:**

* `note_id`: UUID of the note to update.

**Request Body (JSON):**

```json
{
  "title": "Updated Title",
  "body": "Updated body",
  "tags": ["updated", "urgent"]
}
```

**Responses:**

* `200 OK`: Returns the updated note.
* `400 Bad Request`: If invalid fields are provided.
* `404 Not Found`: If the note does not exist.

---

### `DELETE /notes/<note_id>`

**Description:** Delete a note by its ID.

**URL Parameters:**

* `note_id`: UUID of the note to delete.

**Responses:**

* `200 OK`: Confirmation message.
* `404 Not Found`: If the note does not exist.

---

# 🔧 Local Installation

## 📦 Using Python (venv)



### Create virtual environment & activate
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
flask run
```

---

## 🐳 Using Docker


### Build Docker image
```bash
docker build -t simple-notes-flask-app .
```

### Run container
```bash
docker run -p 5000:5000 simple-notes-flask-app
```

### Run multiple containers using docker-compose
```bash
docker-compose up --build

```

---


