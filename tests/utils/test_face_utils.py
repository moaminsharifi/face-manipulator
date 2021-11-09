import pytest
import numpy as np
import dlib
from face_manipulator.utils.image import *
from face_manipulator.utils.face_utils import *


def test_detect_parts():
    image = open_image("tests/assets/front-girl.jpg")
    gray_image = make_gray(image)
    rects, predictor = detect_parts(gray_image)


def test_initialize_detector():
    assert type(initialize_detector()) == dlib.fhog_object_detector


def test_initialize_predictor():
    assert (
        type(initialize_predictor("shape_predictor_68_face_landmarks.dat"))
        == dlib.shape_predictor
    )


def test_initialize_predictor_fail():
    with pytest.raises(Exception) as e_info:
        initialize_predictor("SOME_RANDOM_PREDICTOR.dat")


def part_of_face_detection():
    image = open_image("tests/assets/front-girl.jpg")
    image_gray = make_gray(image)
    # detect faces
    rects, predictor = detect_parts(image_gray)
    # find diffrent face parts
    face_parts = part_of_face_detection(image_gray, rects, predictor)
    assert type(face_parts) == dict
