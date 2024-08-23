from pathlib import Path


def get_project_root_from_readme(readme_file_path: str = "../../README.md") -> Path:
    """Returns project root folder based on the provided relative path to README.md."""
    readme_path = Path(__file__).resolve().parent / readme_file_path
    project_root = readme_path.resolve().parent

    if readme_path.exists():
        return project_root
    else:
        raise FileNotFoundError(f"'{readme_file_path}' does not exist. Unable to determine project root.")


def get_project_root() -> Path:
    """Returns project root folder by looking for README.md file at a known relative path."""
    return get_project_root_from_readme()


# If you prefer working with string paths
def get_project_root_str() -> str:
    return str(get_project_root())
