"""Test template."""

from copier import run_copy
import pytest
from pathlib import Path


@pytest.fixture
def tmp_dir(tmp_path: Path) -> None:
    """Return tmp path for template generation."""
    return tmp_path / "generated"


def test_template_generation(tmp_dir: Path) -> None:
    """Test template generation."""
    run_copy(
        src_path="template",
        dst_path=tmp_dir,
        data={
            "project_name": "test-project",
        },
        vcs_ref="HEAD",
        unsafe=True,
    )

    expected_files = [
        "README.md",
        "pyproject.toml",
    ]

    for file_path in expected_files:
        full_path = tmp_dir / file_path
        assert full_path.exists()
