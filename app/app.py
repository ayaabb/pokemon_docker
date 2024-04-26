from fastapi import FastAPI

from routes import pokemon_api_router

app = FastAPI()

app.include_router(pokemon_api_router.router)
