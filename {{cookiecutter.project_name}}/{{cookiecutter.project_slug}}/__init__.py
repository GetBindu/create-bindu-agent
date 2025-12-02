# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""{{cookiecutter.project_name}} - An Bindu Agent.
"""

from {{cookiecutter.project_slug}}.__version__ import __version__
from {{cookiecutter.project_slug}}.main import (
    handler,
    initialize_agent,
    initialize_all,
    initialize_mcp_tools,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "initialize_all",
    "initialize_mcp_tools",
    "main",
]
