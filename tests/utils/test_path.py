import pytest
from face_manipulator.utils.path import (
    is_file_ext_valid,
    is_path_valid,
    validate_path,
    make_save_file_path,
)


def test_is_file_ext_valid():
    """Check is_file_ext_valid function"""
    file_name = "image.jpg"
    assert is_file_ext_valid(file_name)


def test_is_file_ext_valid_with_capitals():
    """Check is_file_ext_valid function with capitals"""
    file_name = "image.PNG"
    assert is_file_ext_valid(file_name)


def test_is_file_ext_valid_fail():
    """Check is_file_ext_valid function with invalid file extension"""
    file_name = "NOT_IMAGE.EXT"
    assert not is_file_ext_valid(file_name)


def test_is_path_valid(tmpdir):
    """Check is_file_ext_valid function with correct path"""
    tmpdir.mkdir("sub").join("image.png").write("content")
    random_file_path = str(tmpdir / "sub" / "image.png")
    assert is_path_valid(random_file_path)


def test_is_path_valid_fail():
    """Check is_file_ext_valid function with invalid path"""
    random_file_path = "RANDOM_NOT_EXIST_FILE/NOT_IMAGE.EXT"
    assert not is_path_valid(random_file_path)


def test_validate_path(tmpdir):
    """Check is_file_ext_valid function with correct path"""
    tmpdir.mkdir("sub").join("image.png").write("content")
    random_file_path = str(tmpdir / "sub" / "image.png")
    assert validate_path(random_file_path) == random_file_path


def test_validate_path_fail_with_invalid_ext_exception():
    """Check is_file_ext_valid function with invalid path which have invalid extension"""
    random_file_path = "RANDOM_NOT_EXIST_FILE/image.ENT"
    with pytest.raises(Exception) as e_info:
        validate_path(random_file_path)


def test_validate_path_fail_with_invalid_path_exception():
    """Check is_file_ext_valid function with invalid path which have correct extension and invalid file path"""
    random_file_path = "RANDOM_NOT_EXIST_FILE/image.PNG"
    with pytest.raises(Exception) as e_info:
        validate_path(random_file_path)


def test_make_save_file_path(tmpdir):
    tmpdir.mkdir("sub").join("image.png").write("content")
    random_file_path = str(tmpdir / "sub" / "image.png")
    expected_file_path = str(tmpdir / "sub" / "image_manipulated.png")
    assert expected_file_path == make_save_file_path(random_file_path)
