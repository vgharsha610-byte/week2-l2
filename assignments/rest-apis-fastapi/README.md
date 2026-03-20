# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn the fundamentals of building REST APIs using the FastAPI framework. You'll create a web service that handles HTTP requests, processes data, and returns JSON responses while implementing best practices for API design.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application with Basic Routes

#### Description
Create a FastAPI application with basic HTTP endpoints to understand routing and request handling.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a root endpoint (`GET /`) that returns a welcome message in JSON format
- Define at least two additional endpoints for retrieving data (e.g., `GET /items`, `GET /students`)
- Run the application using `uvicorn` and verify endpoints work in a browser or using a tool like `curl`
- Example response format:
  ```json
  {"message": "Welcome to the API", "version": "1.0"}
  ```


### 🛠️ Implement POST Requests and Data Validation

#### Description
Add functionality to handle POST requests that accept and validate user input data.

#### Requirements
Completed program should:

- Create a POST endpoint that accepts JSON data (e.g., create a new student record)
- Use Pydantic models to define and validate request data with required fields and types
- Return a success response with the created data
- Include error handling for invalid input
- Example request body:
  ```json
  {"name": "Alice", "age": 16, "grade": "10A"}
  ```


### 🛠️ Build a Complete CRUD-Style API

#### Description
Expand the API to support Create, Read, Update, and Delete operations on a resource.

#### Requirements
Completed program should:

- Implement at least 4 endpoints: GET (list), GET (by ID), POST (create), DELETE (or PUT for update)
- Store data in memory using a Python dictionary or list (no database required)
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Handle edge cases like invalid IDs or duplicate entries
- Include documentation by adding descriptions to endpoints using docstrings