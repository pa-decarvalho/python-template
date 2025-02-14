import pytest
from pathlib import Path


OUTPUT_DIR = Path("./output")


def test_template_dir_exists() -> None:
    assert OUTPUT_DIR.exists()

def test_readme_file_exists() -> None:
    readme_path = OUTPUT_DIR / "README.md"
    assert readme_path.exists()
    content = readme_path.read_text()
    assert "# test" in content
