

from typing import Union
from pathlib import Path


def find_io_file(file_hash: str, upload_folder: Union[str, Path]):
    return (Path(upload_folder) / file_hash).is_file()
