"""Module 1 example: verify the project is set up correctly."""


def get_python_version() -> str:
    """Return the Python version string."""
    import sys

    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def check_python_version(min_major: int = 3, min_minor: int = 12) -> bool:
    """Check that the Python version meets the minimum requirement."""
    import sys

    return (sys.version_info.major, sys.version_info.minor) >= (min_major, min_minor)


if __name__ == "__main__":
    version = get_python_version()
    print(f"Python version: {version}")
    if check_python_version():
        print("✓ Python version meets requirements (>=3.12)")
    else:
        print("✗ Python version is too old. Please install Python 3.12+")