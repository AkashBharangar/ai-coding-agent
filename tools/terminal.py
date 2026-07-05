from langchain_core.tools import tool
import subprocess

@tool
def run_terminal(command: str) -> str:
    """
    Execute terminal commands
    """

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr

        return output if output else "Command Executed"
    except Exception as e:
        return str(e)