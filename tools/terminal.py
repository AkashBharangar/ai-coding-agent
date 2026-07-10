import subprocess

from langchain_core.tools import tool


@tool
def run_terminal(command: str) -> str:
    """
    Execute terminal commands.

    Examples:

    - python app.py

    - pytest

    - pip list

    - npm test

    Always use this tool whenever the user asks to run or execute a command.
    """

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd="workspace",
        )

        return f"""
Exit Code:
{result.returncode}

STDOUT:
{result.stdout}

STDERR:
{result.stderr}
"""

    except Exception as e:

        return str(e)