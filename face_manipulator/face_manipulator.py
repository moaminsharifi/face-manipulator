# import the necessary packages
import os
import cv2
from utils import *


def face_manipulator(image_path: str, threshold:int,face_for_manipulation :list):
    """main program for face manipulation

    Args:
        image_path (str): image path
        threshold (int): threshold for changes
        face_for_manipulation (list): list of part of the face muse be manipulated
    """
    # load image from image path
    image = open_image(image_path)
    image_gray = make_gray(image)
    # detect faces
    rects, predictor = detect_parts(image_gray)
    # find diffrent face parts
    face_parts = part_of_face_detection(image_gray, rects, predictor)
    # manipulate face parts
    final_image = face_part_manipulator(
        image, face_parts, face_for_manipulation, threshold)
    base_file_dir = os.path.dirname(image_path)
    file_name = os.path.splitext(image_path)
    full_path_for_save = os.path.join(
        base_file_dir, file_name[0] + '_manipulated' + file_name[1])
    cv2.imwrite(full_path_for_save, final_image)

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    args = parse_args()
    image_path = args['image']
    threshold = args['threshold']
    face_for_manipulation = ['left_eye', 'nose']
    # run main program
    face_manipulator(image_path, threshold, face_for_manipulation)
    
   
