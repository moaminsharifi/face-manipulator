import numpy as np
import cv2

def open_image(image_path: str) -> np.ndarray:
    """import image from path

    Args:
        image_path (str): image file image_path

    Returns:
        np.ndarray: image as numpy array
    """
    return cv2.imread(image_path)


def make_gray(image: np.ndarray, handler: int = cv2.COLOR_BGR2GRAY) -> np.ndarray:
    """convert other color spaces (like RGB, BGR) to  image to grayscale

    Args:
        image (np.ndarray): image   
        handler ([int], optional): handler. Defaults to cv2.COLOR_BGR2GRAY.

    Returns:
        np.ndarray: grayscale image
    """
    return cv2.cvtColor(image, handler)


def dlib_pybind11_shape_to_np_converter(shape, dtype: str = "int") -> np.ndarray:
    """convert dlib_pybind11.full_object_detectio to numpy array

    Args:
        shape (dlib_pybind11.full_object_detectio): detected array
        dtype (str, optional): datatype of numpy array. Defaults to "int".

    Returns:
        np.ndarray: shape of detected face as 
    """
	# initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)

	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
	    coords[i] = (shape.part(i).x, shape.part(i).y)

    return coords


