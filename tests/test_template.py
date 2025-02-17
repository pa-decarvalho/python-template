"""Test template."""

from copier import run_copy
from pathlib import Path


DATA_SAMPLE = {
    "project_name": "test-project",
}


def test_template_generation() -> None:
    """Test template generation."""
    output_dir = Path("./output")

    run_copy(
        src_path="template",
        dst_path=output_dir,
        data=DATA_SAMPLE,
        vcs_ref="HEAD",
        unsafe=True,
    )

    expected_files = [
        "README.md",
        "pyproject.toml",
    ]

    for file_path in expected_files:
        full_path = output_dir / file_path
        assert full_path.exists()
