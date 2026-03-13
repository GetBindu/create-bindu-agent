#
# |-----------------------------------------------------------------------|
# |                                                                       |
# |                       Give Feedback / Get Help                        |
# |   https://github.com/getbindu/create-bindu-agent/issues/new/choose   |
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
    project_slug = "{{cookiecutter.project_slug}}"
    template_dir = os.path.join(
        PROJECT_DIRECTORY, project_slug, "skills", "__TEMPLATE__"
    )
    skill_dir = os.path.join(PROJECT_DIRECTORY, project_slug, "skills", skill_name)
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
    os.rename(
        os.path.join(PROJECT_DIRECTORY, filepath),
        os.path.join(PROJECT_DIRECTORY, target),
    )


def move_dir(src: str, target: str) -> None:
    shutil.move(
        os.path.join(PROJECT_DIRECTORY, src), os.path.join(PROJECT_DIRECTORY, target)
    )


def categorize_skill_from_yaml(yaml_path) -> str:
    """Categorize a skill by reading its YAML file and checking tags."""
    try:
        import yaml

        with open(yaml_path) as f:
            skill_data = yaml.safe_load(f)

        tags = skill_data.get("tags", [])
        skill_name = skill_data.get("name", "")

        # Categorize based on tags or name
        tags_str = " ".join(tags).lower()
        name_lower = skill_name.lower()

        # Business & Finance
        if any(
            x in tags_str or x in name_lower
            for x in [
                "finance",
                "financial",
                "stock",
                "market",
                "business",
                "competitor",
                "startup",
            ]
        ):
            return "business"
        # Research & Analysis
        elif any(
            x in tags_str or x in name_lower
            for x in [
                "research",
                "analysis",
                "paper",
                "academic",
                "hackernews",
                "media-trend",
            ]
        ):
            return "research"
        # Creative & Content
        elif any(
            x in tags_str or x in name_lower
            for x in [
                "instagram",
                "meme",
                "screenplay",
                "recipe",
                "youtube",
                "content",
                "creative",
                "video",
                "web-extraction",
            ]
        ):
            return "creative"
        # Lifestyle
        elif any(
            x in tags_str or x in name_lower
            for x in [
                "travel",
                "shopping",
                "movie",
                "book",
                "recommendation",
                "lifestyle",
            ]
        ):
            return "lifestyle"
        # Health & Wellness
        elif any(
            x in tags_str or x in name_lower
            for x in ["health", "wellness", "breakup", "cbt", "therapy", "mental"]
        ):
            return "health"
        # Legal & Compliance
        elif any(
            x in tags_str or x in name_lower
            for x in ["legal", "law", "policy", "compliance", "zk-policy"]
        ):
            return "legal"
        # Technical & Development
        elif any(
            x in tags_str or x in name_lower
            for x in [
                "technical",
                "system",
                "architect",
                "development",
                "biomni",
                "engineering",
            ]
        ):
            return "technical"

        return "other"
    except Exception:
        # Fallback to name-based categorization if YAML parsing fails
        return "other"


def build_skill_map():
    """Dynamically build skill number to name mapping from skills/ directory."""
    from pathlib import Path

    template_skills_dir = Path(__file__).parent.parent / "skills"
    if not template_skills_dir.exists():
        return {}

    # Collect all skills organized by category
    skills_by_category = {
        "business": [],
        "research": [],
        "creative": [],
        "lifestyle": [],
        "health": [],
        "technical": [],
        "legal": [],
    }

    for skill_file in sorted(template_skills_dir.glob("*.yaml")):
        skill_name = skill_file.stem.replace("-skill", "")
        category = categorize_skill_from_yaml(skill_file)
        if category in skills_by_category:
            skills_by_category[category].append(skill_name)

    # Build numbered map
    skill_map = {}
    counter = 1
    for category in [
        "business",
        "research",
        "creative",
        "lifestyle",
        "health",
        "technical",
        "legal",
    ]:
        for skill in skills_by_category.get(category, []):
            skill_map[str(counter)] = skill
            counter += 1

    return skill_map


if __name__ == "__main__":
    # Handle dynamic skills creation
    project_slug = "{{cookiecutter.project_slug}}"

    # Check if skills were selected (via environment variable or installer)
    skill_names_str = "{{cookiecutter.skill_names}}"

    # Remove the help text if it's still there
    if "Enter skill names" in skill_names_str or "comma-separated" in skill_names_str:
        skill_names_str = ""

    # Also check temp file from pre_gen_project
    from pathlib import Path

    temp_file = Path(__file__).parent / ".selected_skills"
    if temp_file.exists():
        skill_names_str = temp_file.read_text().strip()
        temp_file.unlink()  # Clean up

    # Build skill map dynamically from skills/ directory
    skill_map = build_skill_map()

    # Convert numbers to skill names if user entered numbers
    if skill_names_str:
        parts = skill_names_str.split(",")
        converted_skills = []
        for part in parts:
            part = part.strip()
            if part.isdigit() and part in skill_map:
                converted_skills.append(skill_map[part])
            elif part:  # It's already a skill name
                converted_skills.append(part)
        skill_names_str = ",".join(converted_skills)

    if skill_names_str:
        skill_names = skill_names_str.split(",")

        # Copy skill YAML files from template skills/ directory
        template_skills_dir = Path(__file__).parent.parent / "skills"
        project_skills_dir = Path(PROJECT_DIRECTORY) / project_slug / "skills"
        project_skills_dir.mkdir(parents=True, exist_ok=True)

        for skill_name in skill_names:
            skill_name = skill_name.strip()
            if skill_name:
                # Look for the skill YAML file in template
                skill_yaml = template_skills_dir / f"{skill_name}-skill.yaml"
                if skill_yaml.exists():
                    import shutil

                    shutil.copy(
                        skill_yaml, project_skills_dir / f"{skill_name}-skill.yaml"
                    )
                    print(f"  · Added skill: {skill_name}")

        # Update agent_config.json with converted skill names
        import json

        agent_config_path = Path(PROJECT_DIRECTORY) / project_slug / "agent_config.json"
        if agent_config_path.exists():
            with open(agent_config_path, "r") as f:
                config = json.load(f)

            # Update skills array with converted names
            config["skills"] = [
                f"skills/{skill.strip()}" for skill in skill_names if skill.strip()
            ]

            with open(agent_config_path, "w") as f:
                json.dump(config, f, indent=2)
            print(f"  · Updated agent_config.json with {len(config['skills'])} skills")

    # Remove the template folder
    template_dir = os.path.join(
        PROJECT_DIRECTORY, project_slug, "skills", "__TEMPLATE__"
    )
    if os.path.exists(template_dir):
        remove_dir(os.path.join(project_slug, "skills", "__TEMPLATE__"))

    # Remove skills folder if no skills created
    skills_dir = os.path.join(PROJECT_DIRECTORY, project_slug, "skills")
    if os.path.exists(skills_dir) and not os.listdir(skills_dir):
        remove_dir(os.path.join(project_slug, "skills"))

    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")

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
