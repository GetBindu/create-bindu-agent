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
This file is run before the project is created.
It handles skill selection and validation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def categorize_skill(skill_name: str) -> str:
    """Categorize a skill based on its name."""
    if any(x in skill_name for x in ["finance", "financial", "competitor-analysis", "startup-analyst", "explainable-business"]):
        return "business"
    elif any(x in skill_name for x in ["deep-research", "analyze-paper", "hackernews-analysis", "media-trend"]):
        return "research"
    elif any(x in skill_name for x in ["instagram", "meme", "screenplay", "recipe", "youtube", "web-extraction"]):
        return "creative"
    elif any(x in skill_name for x in ["travel", "shopping", "movie", "book"]):
        return "lifestyle"
    elif any(x in skill_name for x in ["breakup", "cbt"]):
        return "health"
    elif any(x in skill_name for x in ["legal", "zk-policy"]):
        return "legal"
    elif any(x in skill_name for x in ["system-architect", "biomni"]):
        return "technical"
    return "other"


def get_available_skills() -> dict[str, list[str]]:
    """Get all available skills organized by category."""
    # Get the template directory (parent of hooks/)
    template_dir = Path(__file__).parent.parent
    skills_dir = template_dir / "skills"
    
    if not skills_dir.exists():
        return {}
    
    # Collect all skill YAML files
    skills_by_category = {
        "business": [],
        "research": [],
        "creative": [],
        "lifestyle": [],
        "health": [],
        "technical": [],
        "legal": [],
    }
    
    for skill_file in sorted(skills_dir.glob("*.yaml")):
        skill_name = skill_file.stem.replace("-skill", "")
        category = categorize_skill(skill_name)
        if category in skills_by_category:
            skills_by_category[category].append(skill_name)
    
    # Remove empty categories
    return {k: v for k, v in skills_by_category.items() if v}


def display_skills_and_prompt() -> str:
    """Display skills and prompt for selection. Returns comma-separated skill names."""
    skills_by_category = get_available_skills()
    
    if not skills_by_category:
        return ""
    
    category_display = {
        "business": "💼 Business & Finance",
        "research": "🔬 Research & Analysis",
        "creative": "🎨 Creative & Content",
        "lifestyle": "🌟 Personal & Lifestyle",
        "health": "💚 Health & Wellness",
        "technical": "⚙️  Technical & Development",
        "legal": "⚖️  Legal & Compliance",
    }
    
    print("\n\033[38;2;156;39;176m\033[1mAvailable Skills\033[0m")
    print("\033[38;2;158;158;158mSelect skills to include in your agent (optional)\033[0m\n")
    
    skill_index_map = {}
    counter = 0
    
    for category in ["business", "research", "creative", "lifestyle", "health", "technical", "legal"]:
        if category not in skills_by_category:
            continue
            
        print(f"\033[38;2;186;104;200m{category_display[category]}\033[0m")
        
        for skill in skills_by_category[category]:
            counter += 1
            skill_index_map[counter] = skill
            print(f"  {counter}) {skill}")
        
        print()
    
    # Prompt for selection
    print("\033[38;2;158;158;158mEnter skill numbers separated by spaces (e.g., '1 3 5'),")
    print("'all' for all skills, or press Enter to skip:\033[0m")
    print("\033[38;2;156;39;176m→\033[0m Selection: ", end="", flush=True)
    
    try:
        selection = input().strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\033[38;2;158;158;158m· No skills selected\033[0m")
        return ""
    
    if not selection:
        print("\033[38;2;158;158;158m· No skills selected\033[0m")
        return ""
    
    if selection.lower() == "all":
        selected_skills = list(skill_index_map.values())
        print(f"\033[38;2;102;187;106m✓\033[0m Selected all {len(selected_skills)} skills")
        return ",".join(selected_skills)
    
    # Parse numbers
    selected_skills = []
    try:
        for num_str in selection.split():
            num = int(num_str)
            if num in skill_index_map:
                selected_skills.append(skill_index_map[num])
            else:
                print(f"\033[38;2;255;167;38m!\033[0m Invalid skill number: {num}")
    except ValueError:
        print("\033[38;2;239;83;80m✗\033[0m Invalid input. Please enter numbers separated by spaces.")
        return ""
    
    if selected_skills:
        print(f"\033[38;2;102;187;106m✓\033[0m Selected {len(selected_skills)} skill(s)")
        return ",".join(selected_skills)
    
    return ""


# Main execution
if __name__ == "__main__":
    # Validate project name
    PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
    project_name = "{{cookiecutter.project_name}}"
    if not re.match(PROJECT_NAME_REGEX, project_name):
        print(
            f"ERROR: The project name {project_name} is not a valid Python module name. Please do not use a _ and use - instead"
        )
        sys.exit(1)

    # Validate project slug
    PROJECT_SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
    project_slug = "{{cookiecutter.project_slug}}"
    if not re.match(PROJECT_SLUG_REGEX, project_slug):
        print(
            f"ERROR: The project slug {project_slug} is not a valid Python module name. Please do not use a - and use _ instead"
        )
        sys.exit(1)
