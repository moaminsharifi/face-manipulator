import numpy as np
import cv2
from face_manipulator import face_manipulator
from face_manipulator.utils.path import is_file_ext_valid, is_path_valid, validate_path

def test_face_manipulator():
    image_path = "tests/assets/front-girl.jpg"
    final_image_path = "tests/assets/front-girl_manipulated.jpg"
    threshold = np.random.randint(-100, 100)
    face_for_manipulation = ['left_eye', 'nose']
    face_manipulator(image_path, threshold,face_for_manipulation)
    assert is_file_ext_valid(final_image_path)
    assert is_path_valid(final_image_path)
