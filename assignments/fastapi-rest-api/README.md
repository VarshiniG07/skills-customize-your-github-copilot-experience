# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a RESTful API using the FastAPI framework. Students will build CRUD endpoints, use Pydantic models for validation, run the app with `uvicorn`, and test endpoints.

## 📝 Tasks

### 🛠️	Core API Implementation

#### Description
Build a simple REST API (for example, an item catalog) that supports creating, reading, updating, and deleting resources using FastAPI.

#### Requirements
Completed program should:

- Use FastAPI and Pydantic models to validate request/response data.
- Implement endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`.
- Keep data in-memory (a Python dict) for the assignment; persistence is optional.
- Run with `uvicorn` and expose OpenAPI documentation at `/docs`.
- Provide example `curl` or `http` requests demonstrating each endpoint.


### 🛠️	Testing and Documentation

#### Description
Verify the API behavior using automated tests and ensure the interactive docs are functional.

#### Requirements
Completed program should:

- Include at least 3 automated tests (use `pytest` + `httpx` or `requests`) that cover creating an item, retrieving it, and updating or deleting it.
- Verify that the automatic API docs are available at `/docs` and `/redoc`.
- Provide instructions to run the server and the tests.


## Starter Code

Use the included `starter-code.py` as a starting point. To run locally:

```bash
python -m pip install -r requirements.txt
uvicorn starter_code:app --reload --port 8000
```

Example `curl` request to create an item:

```bash
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"name": "notebook", "price": 4.5}'
```

Optional enhancements:

- Add query parameters for filtering or pagination.
- Add simple authentication (API key or OAuth) to protected endpoints.
- Persist data to a file or lightweight database (SQLite).
