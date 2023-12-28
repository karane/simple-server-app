from fastapi import FastAPI
import items_router

app = FastAPI()

app.include_router(items_router.router)

