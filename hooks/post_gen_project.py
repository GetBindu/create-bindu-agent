#
# |-----------------------------------------------------------------------|
# |                                                                       |
# |                       Give Feedback / Get Help                        |
# |   https://github.com/Saptha-me/create-bindu-agent/issues/new/choose   |
# |                                                                       |
# |-----------------------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""
This file is run after the project is created.
"""
from __future__ import annotations

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(full_path):
        os.remove(full_path)


def remove_dir(filepath: str) -> None:
    full_path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(full_path):
        shutil.rmtree(full_path)


def create_skill_from_template(skill_name: str) -> None:
    template_dir = os.path.join(PROJECT_DIRECTORY, "skills", "__TEMPLATE__")
    skill_dir = os.path.join(PROJECT_DIRECTORY, "skills", skill_name)
    if os.path.exists(template_dir):
        # Copy template to new skill folder
        shutil.copytree(template_dir, skill_dir)
        skill_yaml_path = os.path.join(skill_dir, "skill.yaml")
        if os.path.exists(skill_yaml_path):
            with open(skill_yaml_path) as f:
                content = f.read()
            content = content.replace("__SKILL_NAME__", skill_name)
            with open(skill_yaml_path, "w") as f:
                f.write(content)


def move_file(filepath: str, target: str) -> None:
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, target))


def move_dir(src: str, target: str) -> None:
    shutil.move(os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target))


if __name__ == "__main__":
    # Handle dynamic skills creation
    if "{{cookiecutter.include_example_skills}}" == "y":
        skill_names = "{{cookiecutter.skill_names}}".split(",")
        
        for skill_name in skill_names:
            skill_name = skill_name.strip()
            if skill_name:
                create_skill_from_template(skill_name)
    
    # Remove the template folder
    template_dir = os.path.join(PROJECT_DIRECTORY, "skills", "__TEMPLATE__")
    if os.path.exists(template_dir):
        remove_dir(os.path.join("skills", "__TEMPLATE__"))
    
    # Remove skills folder if no skills created
    skills_dir = os.path.join(PROJECT_DIRECTORY, "skills")
    if os.path.exists(skills_dir) and not os.listdir(skills_dir):
        remove_dir("skills")
        
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")
    else:
        if "{{cookiecutter.mkdocs}}" != "y" and "{{cookiecutter.publish_to_pypi}}" == "n":
            remove_file(".github/workflows/on-release-main.yml")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(".github/workflows/validate-codecov-config.yml")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")

    if "{{cookiecutter.open_source_license}}" == "MIT license":
        move_file("LICENSE_MIT", "LICENSE")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "BSD license":
        move_file("LICENSE_BSD", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "ISC license":
        move_file("LICENSE_ISC", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_APACHE")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "Apache Software License 2.0":
        move_file("LICENSE_APACHE", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_GPL")

    if "{{cookiecutter.open_source_license}}" == "GNU General Public License v3":
        move_file("LICENSE_GPL", "LICENSE")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")

    if "{{cookiecutter.open_source_license}}" == "Not open source":
        remove_file("LICENSE_GPL")
        remove_file("LICENSE_MIT")
        remove_file("LICENSE_BSD")
        remove_file("LICENSE_ISC")
        remove_file("LICENSE_APACHE")
