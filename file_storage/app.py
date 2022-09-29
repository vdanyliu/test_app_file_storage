from pathlib import Path

from fastapi import FastAPI

from file_storage.api.factory import init_api
from file_storage.platform.storage import DiskStorage


def create_app() -> FastAPI:
    app = FastAPI()
    storage = DiskStorage(Path("tmp").resolve())
    init_api(app, storage=storage)
    return app
