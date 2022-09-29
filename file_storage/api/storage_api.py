import io

from fastapi import APIRouter, UploadFile, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse

from file_storage.kernel.data import InputFile
from file_storage.kernel.storage import Storage

router = APIRouter(
    tags=['file_storage'],
    prefix='/files'
)


class AnyFile(FileResponse):
    media_type = '*/*'


class FileId(BaseModel):
    file_id: str


def create_file_storage_api(storage: Storage):
    @router.post("", response_model=FileId)
    async def post(file: UploadFile):
        file = await storage.save_file(InputFile(file_name=file.filename, data=io.BytesIO(await file.read())))
        return dict(file_id=file.id)

    @router.head("/{id}", response_class=AnyFile)
    @router.get("/{id}", response_class=AnyFile)
    async def get(id: str):
        file_path = await storage.get_file(id)
        if not file_path:
            raise HTTPException(status_code=404, detail="File not found")
        return AnyFile(path=file_path, filename=file_path.name)

    return router
