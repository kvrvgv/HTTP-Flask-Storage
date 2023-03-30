

from pathlib import Path
from typing import Union, AnyStr


def create_file(file_hash: str, upload_folder: Union[str, Path], content: AnyStr):
    output_file_path = Path(upload_folder) / file_hash[:2] / file_hash
    output_file_path.parent.mkdir(exist_ok=True, parents=True)
    with open(output_file_path, "wb") as file:
        file.write(content)
