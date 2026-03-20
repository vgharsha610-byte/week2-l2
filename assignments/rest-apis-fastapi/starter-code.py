"""
FastAPI REST API Starter Code
This template provides a basic structure for building a REST API with FastAPI.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    """Model for an item with required and optional fields"""
    id: int
    name: str
    description: Optional[str] = None
    price: float

# In-memory storage (replace with a database in production)
items_db = []

# Root endpoint
@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to the REST API", "version": "1.0"}

# Example GET endpoint to retrieve all items
@app.get("/items")
def get_items():
    """Retrieve all items from the database"""
    return {"items": items_db}

# Example POST endpoint to create a new item
@app.post("/items")
def create_item(item: Item):
    """Create a new item and store it in the database"""
    items_db.append(item.dict())
    return {"message": "Item created successfully", "item": item}

# TODO: Add more endpoints below
# - GET /items/{item_id} - Retrieve a specific item by ID
# - PUT /items/{item_id} - Update an item
# - DELETE /items/{item_id} - Delete an item

# Run the app with: uvicorn starter-code:app --reload
