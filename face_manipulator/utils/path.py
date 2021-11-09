import os

VALID_EXT = (".jpg", ".png")


def is_file_ext_valid(path: str) -> bool:
    """Check Extension of file

    Args:
        path (str): file path

    Returns:
        bool: if file is a valid extension return True otherwise False
    """

    # splitext function last element is the extension of file and for Case Sensitive use lower()
    if os.path.splitext(path)[-1].lower() in VALID_EXT:
        return True
    return False


def is_path_valid(path: str) -> bool:
    """check Path is a valid

    Args:
        path (str): file path

    Returns:
        bool: if file path is valid, return True otherwise False
    """
    if os.path.isfile(path):
        return True
    return False


def validate_path(path: str) -> str:
    """Validate Path for cli argument parser

    Args:
        path (str): file path

    Returns:
        bool: if valid return path otherwise raise error
    """
    assert is_path_valid(path), "Path does not exist"
    assert is_file_ext_valid(
        path
    ), f"file extension must be a valid file extension and in {VALID_EXT}"
    return path


def make_save_file_path(path: str) -> str:
    """Make save file path

    Args:
        path (str): file path

    Returns:
        str: file path with _manipulated added between file name and extension
    """
    base_file_dir = os.path.dirname(path)
    file_name = os.path.splitext(path)
    full_path_for_save = os.path.join(
        base_file_dir, f"{file_name[0]}_manipulated{file_name[1]}"
    )
    return full_path_for_save
