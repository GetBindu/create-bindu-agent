from __future__ import annotations

import os
import shlex
import subprocess

from tests.utils import file_contains_text, is_valid_yaml, run_within_dir


def test_bake_project(cookies):
    """Test basic project creation with custom name."""
    result = cookies.bake(extra_context={"project_name": "test-agent"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "test-agent"
    assert result.project_path.is_dir()


def test_using_pytest(cookies, tmp_path):
    """Test that generated project can run tests."""
    with run_within_dir(tmp_path):
        result = cookies.bake()

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "my-bindu-agent"
        assert result.project_path.is_dir()
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")

        # Install the uv environment and run the tests.
        with run_within_dir(str(result.project_path)):
            assert subprocess.check_call(shlex.split("uv sync")) == 0
            assert subprocess.check_call(shlex.split("uv run pytest tests")) == 0


def test_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are created when devcontainer=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_not_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are not created when devcontainer=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "n"})
        assert result.exit_code == 0
        assert not os.path.isdir(f"{result.project_path}/.devcontainer")


def test_mkdocs(cookies, tmp_path):
    """Test mkdocs is included by default."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "y"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "on-release-main.yml")
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy")
        assert file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert os.path.isdir(f"{result.project_path}/docs")


def test_not_mkdocs(cookies, tmp_path):
    """Test mkdocs can be excluded."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/mkdocs.yml")
        assert not os.path.isdir(f"{result.project_path}/docs")


def test_dockerfile(cookies, tmp_path):
    """Test Dockerfile is included by default."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/Dockerfile")
        assert os.path.isfile(f"{result.project_path}/docker-compose.yml")


def test_not_dockerfile(cookies, tmp_path):
    """Test Dockerfile can be excluded."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/Dockerfile")
        assert not os.path.isfile(f"{result.project_path}/docker-compose.yml")


def test_codecov(cookies, tmp_path):
    """Test codecov is included by default."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"codecov": "y"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert os.path.isfile(f"{result.project_path}/codecov.yaml")
        assert os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")


def test_not_codecov(cookies, tmp_path):
    """Test codecov can be excluded."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"codecov": "n"})
        assert result.exit_code == 0
        assert is_valid_yaml(result.project_path / ".github" / "workflows" / "main.yml")
        assert not os.path.isfile(f"{result.project_path}/codecov.yaml")
        assert not os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")


def test_license_mit(cookies, tmp_path):
    """Test MIT license is created correctly."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "MIT license"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")


def test_license_bsd(cookies, tmp_path):
    """Test BSD license is created correctly."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "BSD license"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")


def test_license_isc(cookies, tmp_path):
    """Test ISC license is created correctly."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "ISC license"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")


def test_license_apache(cookies, tmp_path):
    """Test Apache license is created correctly."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "Apache Software License 2.0"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")


def test_license_gplv3(cookies, tmp_path):
    """Test GPL v3 license is created correctly."""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "GNU General Public License v3"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")


def test_license_no_license(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"open_source_license": "Not open source"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/LICENSE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_MIT")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_BSD")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_ISC")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_APACHE")
        assert not os.path.isfile(f"{result.project_path}/LICENSE_GPL")