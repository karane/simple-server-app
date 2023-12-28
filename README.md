# FastAPI Item Service

This FastAPI application provides CRUD operations for managing items.

## Getting Started

    ```
    docker-compose up --build -d
    ```

## Usage

* Health Check
    ```bash
    curl -s -X GET http://localhost:8000/health | jq "."
    ```

* Create Item
    ```bash
    curl -s -X POST -H "Content-Type: application/json" -d '{"name": "New Item", "description": "A sample item"}' http://localhost:8000/items/ | jq "."
    ```
* Retrieve List of Items

    ```bash
    curl -s -X GET http://localhost:8000/items/ | jq "."
    ```
* Update Item

    ```bash
    curl -s -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Item", "description": "An updated item"}' http://localhost:8000/items/1 | jq "."
    ```
* Delete Item

    ```bash
    curl -X DELETE http://localhost:8000/items/1 | jq "."
    ```
