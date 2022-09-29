from abc import abstractmethod, ABC
from pathlib import Path

from file_storage.kernel.data import InputFile


class Storage(ABC):
    @abstractmethod
    async def get_file(self, id: str) -> Path:
        pass

    @abstractmethod
    async def save_file(self, file: InputFile) -> InputFile:
        pass
