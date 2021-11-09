# import the necessary packages
import os
import cv2
from utils import (
    validate_path,
    open_image,
    make_gray,
    detect_parts,
    part_of_face_detection,
    face_part_manipulator,
    make_save_file_path,
    parse_args,
)


def face_manipulator(image_path: str, threshold: int, face_for_manipulation: list):
    """main program for face manipulation

    Args:
        image_path (str): image path
        threshold (int): threshold for changes
        face_for_manipulation (list): list of part of the face muse be manipulated
    """

    # validate_path image path
    image_path = validate_path(image_path)

    # load image from image path
    image = open_image(image_path)
    image_gray = make_gray(image)

    # detect faces
    rects, predictor = detect_parts(image_gray)

    # find diffrent face parts
    face_parts = part_of_face_detection(image_gray, rects, predictor)

    # manipulate face parts
    final_image = face_part_manipulator(
        image, face_parts, face_for_manipulation, threshold
    )

    # make new full path
    full_path_for_save = make_save_file_path(image_path)
    # save image
    cv2.imwrite(full_path_for_save, final_image)


if __name__ == "__main__":
    # construct the argument parser and parse the arguments
    args = parse_args()
    image_path = args["image"]
    threshold = args["threshold"]
    face_for_manipulation = ["left_eye", "nose"]
    # run main program
    face_manipulator(image_path, threshold, face_for_manipulation)
