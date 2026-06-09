# Building REST APIs with FastAPI

## Overview

In this assignment you'll build a small RESTful API using the FastAPI framework. You'll design endpoints to create, read, update, and delete simple `Item` resources and write tests to verify the API behavior.

## Learning Objectives

- Understand FastAPI application structure
- Define Pydantic models for request/response validation
- Implement CRUD endpoints
- Write and run HTTP tests with FastAPI's test client

## Tasks

1. Implement the API endpoints in `starter_code.py`:
   - `GET /items` — list all items
   - `GET /items/{item_id}` — retrieve a single item
   - `POST /items` — create a new item
   - `PUT /items/{item_id}` — update an existing item
   - `DELETE /items/{item_id}` — delete an item

2. Ensure request/response models use `pydantic` and return appropriate HTTP status codes.

3. Run the tests in `tests/test_api.py` and make the API pass them.

## Development & Submission

- Install dependencies:

  pip install -r requirements.txt

- Run the app locally:

  uvicorn starter_code:app --reload

- Run tests:

  pytest -q

## Hints

- Use an in-memory dictionary for storage while developing.
- Keep models simple: `id: int`, `name: str`, `description: Optional[str]`.
- Return `404` for missing items and `201` on successful creation.

Good luck — keep endpoints small and well-typed!
