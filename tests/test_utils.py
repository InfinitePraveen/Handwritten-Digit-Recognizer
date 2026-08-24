from pathlib import Path
from src.utils import ensure_directory

def test_ensure_directory(tmp_path):
    target = ensure_directory(tmp_path / "new")
    assert Path(target).exists()
