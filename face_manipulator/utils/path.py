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
    assert is_file_ext_valid(path), "file extension must be a valid file extension and in " + str(VALID_EXT)
    return path
