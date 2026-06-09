# Building REST APIs with FastAPI — Skill Description

This assignment teaches students how to design and implement RESTful APIs using the FastAPI framework and Pydantic models.

## Teaching Goals

- Introduce FastAPI application structure and routing
- Use Pydantic models for request validation and response schemas
- Implement CRUD endpoints with proper HTTP status codes
- Write automated tests using FastAPI's test client

## Assignment Tasks

1. Implement the API endpoints in `starter_code.py` and ensure they meet the contract described in the assignment README.
2. Validate inputs using Pydantic models and return appropriate status codes (`201`, `200`, `204`, `404`).
3. Write or adapt tests in `tests/test_api.py` so they pass reliably.
4. (Optional) Add small integration examples using `httpx` or run the app using `uvicorn`.

## Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Pydantic docs: https://pydantic-docs.helpmanual.io/

## Assessment Criteria

- Correctness of CRUD behavior
- Appropriate status codes and error handling
- Clear, well-typed Pydantic models
- Passing automated tests
