from fastapi import FastAPI

from file_storage.api.storage_api import create_file_storage_api
from file_storage.kernel.storage import Storage


def init_api(app: FastAPI, storage: Storage) -> FastAPI:
    app.include_router(
        create_file_storage_api(storage)
    )
    return app
