

from typing import Union
from pathlib import Path


def delete_io_file(file_hash: str, upload_folder: Union[str, Path]):
    (Path(upload_folder) / file_hash[:2] / file_hash).unlink(missing_ok=True)
