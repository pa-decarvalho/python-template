"""Test template."""

from copier import run_copy
from pathlib import Path
import subprocess


DATA_SAMPLE = {
    "project_name": "test-project",
    "package_name": "test_project",
}


def test_template_generation() -> None:
    """Test template generation."""
    output_dir = Path("./output")

    run_copy(
        src_path=".",
        dst_path=output_dir,
        data=DATA_SAMPLE,
        vcs_ref="HEAD",
        unsafe=True,
    )

    # Expected files after first generation
    expected_files = [
        f"src/{DATA_SAMPLE['project_name'].replace('-', '_')}/__init__.py",
        ".copier-answers.yml",
        "pyproject.toml",
        "README.md",
    ]

    for file_path in expected_files:
        full_path = output_dir / file_path
        assert full_path.exists()

    # Run poetry install
    result = subprocess.run(
        ["poetry", "install"],
        cwd=output_dir,
        capture_output=True,
        text=True,
        check=True,
    )

    # Check if command was successful
    assert result.returncode == 0, f"Poetry install failed with error: {result.stderr}"

    # Expected files after poetry install
    expected_files_after_install = [
        "poetry.lock",
    ]

    for file_path in expected_files_after_install:
        full_path = output_dir / file_path
        assert full_path.exists()
