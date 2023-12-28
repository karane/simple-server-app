# FastAPI Item Service

This FastAPI application provides CRUD operations for managing items.

## Getting Started

    ```
    docker-compose up --build -d
    ```

## Usage

* Health Check
    ```bash
    curl -X GET http://localhost:8000/health
    ```

* Create Item
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "New Item", "description": "A sample item"}' http://localhost:8000/items/
    ```
* Retrieve List of Items

    ```bash
    curl -X GET http://localhost:8000/items/
    ```
* Update Item

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "An updated item"}' http://localhost:8000/items/1
    ```
* Delete Item

    ```bash
    curl -X DELETE http://localhost:8000/items/1
    ```
