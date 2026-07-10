from pathlib import Path

WORKSPACE_ROOT = Path("workspace").resolve()


def resolve_workspace_path(file_path: str) -> Path:
    """
    Resolve a path and ensure it stays inside the workspace directory.
    """

    path = Path(file_path)

    if not path.is_absolute():
        path = WORKSPACE_ROOT / path

    path = path.resolve()

    if WORKSPACE_ROOT not in path.parents and path != WORKSPACE_ROOT:
        raise ValueError("Access outside the workspace is not allowed.")

    return pathgit status