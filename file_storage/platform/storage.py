import uuid
from io import BytesIO
from os import walk
from pathlib import Path
from typing import Optional

import aiofiles as aiofiles

from file_storage.kernel.data import InputFile
from file_storage.kernel.storage import Storage


class DiskStorage(Storage):
    def __init__(self, storage_dir: Path):
        self.storage_dir = storage_dir
        self._init_storage()

    async def get_file(self, id: str) -> Optional[Path]:
        try:
            return self._get_file_path(id)
        except ValueError:
            return None

    async def save_file(self, file: InputFile) -> InputFile:
        c = 1
        file_dir_path = Path(self.storage_dir, file.id)
        file_dir_path.mkdir(parents=True)
        file_path = Path(file_dir_path, file.file_name)
        async with aiofiles.open(file_path, 'wb') as fd:
            await fd.write(file.data.read())
        return file

    def _init_storage(self):
        Path(self.storage_dir).mkdir(parents=True, exist_ok=True)

    def _get_file_path(self, id: str) -> Path:
        file_dir_path = Path(self.storage_dir, id)
        for (*_, filenames) in walk(file_dir_path):
            if filenames:
                return Path(file_dir_path, filenames[0])
            raise ValueError
