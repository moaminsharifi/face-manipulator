import os
from collections import OrderedDict
import numpy as np
import dlib
from .path import is_path_valid
from .image import dlib_pybind11_shape_to_np_converter

FACIAL_LANDMARKS_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 35)),
    ("jaw", (0, 17))
])


def initialize_detector():
    """Initialize detector

    Returns:
        dlib.shape_predictor: detector
    """
    detector = dlib.get_frontal_face_detector()
    return detector


def initialize_predictor(predictor_type: str):
    """Initialize predictor
    Args:
        predictor_type (str): type of predictor

    Returns:
        dlib.shape_predictor: predictor
    """
    predictor_path = os.path.join(os.path.dirname(__file__), predictor_type)
    assert is_path_valid(
        predictor_path), "Predictor not exist in %s" % predictor_path
    predictor = dlib.shape_predictor(predictor_path)
    return predictor


def detect_parts(face_image: np.ndarray,
                 predictor_type="shape_predictor_68_face_landmarks.dat") -> tuple:
    """detect diffrent part of the face

    Args:
        face_image (np.ndarray): face image
        predictor_type (str, optional): name of predictor file. Defaults to "shape_predictor_68_face_landmarks.dat".

    Returns:
        tuple: rects and predictor
    """
    predictor = initialize_predictor(predictor_type)
    detector = initialize_detector()
    rects = detector(face_image, 1)
    return rects, predictor


def part_of_face_detection(image: np.ndarray, rects: np.ndarray, predictor: dlib.shape_predictor) -> dict:
    """Detect Diffrents part of the face

    Args:
        image (np.ndarray): image to detect
        rects (np.ndarray): rects of the face detected
        predictor (dlib.shape_predictor): predictor_type

    Returns:
        dict: face parts
    """
    face_parts = {}
    for (i, rect) in enumerate(rects):
        shape = predictor(image, rect)
        shape_np = dlib_pybind11_shape_to_np_converter(shape)
        for (name, (k, j)) in FACIAL_LANDMARKS_IDXS.items():
            face_parts[name] = shape_np[k:j]

    return face_parts
