import pytest
import numpy as np
from face_manipulator.utils.image import *

def test_open_image():
    """Testing open_image"""
    image = open_image("tests/assets/front-girl.jpg")
    assert image.shape == (517, 926, 3)
    assert type(image) == np.ndarray


def test_open_image_fail():
    """Testing open_image with invalid image file path"""
    random_file_path = 'random_not_excited/image.png'
    im = open_image(random_file_path)
    assert im is None
   

def test_make_gray():
    """Testing open_image and make it gray"""
    image = open_image("tests/assets/front-girl.jpg")
    gray_image = make_gray(image)
    assert gray_image.shape == (517, 926)
    assert type(image) == np.ndarray


def test_make_gray_fail():
    """Testing make_gray with invalid input"""
    with pytest.raises(Exception) as e_info:
        make_gray('str')


def test_dlib_pybind11_shape_to_np_converter():
    pass