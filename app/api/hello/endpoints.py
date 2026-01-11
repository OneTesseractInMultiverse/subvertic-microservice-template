import datetime

from fastapi import APIRouter

hello_router = APIRouter()

TAGS: list[str] = ["Hello"]


@hello_router.get(
    "/hello",
    tags=TAGS,
)
async def get_hello():
    return {"message": "Hi, this is my first API"}


@hello_router.get(
    "/local_time",
    tags=TAGS,
)
async def get_local_time():
    return {"utc": datetime.datetime.now(datetime.UTC).isoformat()}
