from copier import run_copy
import pytest
from pathlib import Path

@pytest.fixture
def tmp_dir(tmp_path):
    return tmp_path / "generated"

def test_template_generation(tmp_dir):
    # Copy template with default values
    run_copy(
        src_path="template",
        dst_path=tmp_dir,
        data={
            "project_name": "test_project",
        },
        vcs_ref="HEAD",
        unsafe=True,
    )

    # Check if README.md exists and contains the right content
    readme_path = tmp_dir / "README.md"
    assert readme_path.exists()

    content = readme_path.read_text()
    assert "# test" in content
