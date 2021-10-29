from fastapi import FastAPI
from . import hello as hello_router


def create_app():
    app = FastAPI(title="fastapi-demo", description="fastapi demo", version="0.0.1")
    app.include_router(
        hello_router.router,
        responses={404: {"description": "Not found"}},
    )
    return app


