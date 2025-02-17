"""Test template."""

from copier import run_copy
from pathlib import Path
import subprocess


OUTPUT_DIR = Path("./output")
DATA_SAMPLE = {
    "project_name": "test-project",
    "package_name": "test_project",
}


def test_generate_template() -> None:
    """Test template generation."""
    run_copy(
        src_path=".",
        dst_path=OUTPUT_DIR,
        data=DATA_SAMPLE,
        vcs_ref="HEAD",
        unsafe=True,
    )
    assert OUTPUT_DIR.exists()


def test_all_files_are_generated() -> None:
    """Test all files are generated."""
    # Expected files after first generation
    expected_files = [
        f"src/{DATA_SAMPLE['project_name'].replace('-', '_')}/__init__.py",
        ".copier-answers.yml",
        "pyproject.toml",
        "README.md",
    ]

    for file_path in expected_files:
        full_path = OUTPUT_DIR / file_path
        assert full_path.exists()


def test_poetry_install_command() -> None:
    """Test poetry install command works."""
    # Run poetry install
    result = subprocess.run(
        ["poetry", "install"],
        cwd=OUTPUT_DIR,
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
        full_path = OUTPUT_DIR / file_path
        assert full_path.exists()
