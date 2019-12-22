import hashlib
import os
import shutil
from pathlib import Path, PurePosixPath


def make_file(path: str, content: str) -> None:
    os.makedirs(PurePosixPath(path).parent, exist_ok=True)
    with open(path, 'w+') as f:
        f.write(content)


def make_empty_dir(path):
    if str(path).startswith("/"):
        raise Exception("Don't make non-relative empty dirs")
    if str(path).startswith(".."):
        raise Exception("Don't make empty dirs above context")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def get_hash(file_path: Path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def sqlite_config():
    return {"Environment": "dev", "Database": {"Type": "SQLITE", "Schema": ':memory:'}}


def has_oracle():
    return 'ORACLE_HOME' in os.environ


def has_datastage():
    return 'GRIDHOME' in os.environ
