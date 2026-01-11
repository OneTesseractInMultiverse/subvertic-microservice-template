from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.hello.endpoints import hello_router
from app.settings.server.general import (
    ALLOWED_ORIGINS,
    TITLE,
    DESCRIPTION,
    VERSION, API_VERSION
)


def create_app() -> FastAPI:
    application: FastAPI = FastAPI(
        title=TITLE,
        description=DESCRIPTION,
        version=VERSION,
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url=None,
    )
    return application


app: FastAPI = create_app()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  # pragma: no cover

app.include_router(
    hello_router,
    prefix=API_VERSION,
)
