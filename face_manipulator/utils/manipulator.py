import numpy as np
import cv2
FACE_PARTS = {'mouth', 'right_eyebrow', 'left_eyebrow',
              'right_eye', 'left_eye', 'nose', 'jaw'}


def face_part_manipulator(image: np.ndarray,
                     face_parts:dict,
                     items_for_change:list,
                     threshold:int):
    """manipulate face parts

    Args:
        image (np.ndarray): image of face parts
        face_parts (dict): face parts
        items_for_change (list): list of items for change
        threshold (int): threshold for change

    Returns:
        np.array: final image which manipulated
    """
    for itm_key in items_for_change:
        assert itm_key in FACE_PARTS, 'Wrong item name'

    for itm_key in items_for_change:
        assert itm_key in face_parts, f"face_parts have not {itm_key}"
    
    final_image = image.copy()
	
    for itm_key in items_for_change:
        
        face_part = face_parts[itm_key]
        rect = cv2.boundingRect(face_part)
        
        x, y, w, h = rect
        
        face_part_image = image[y:y+h, x:x+w].copy()
        scale_present = (100 + threshold) / 100
        

        face_part_image_resized = cv2.resize(
            face_part_image,  (0, 0), fx=scale_present,
            		fy=scale_present, interpolation=cv2.INTER_AREA)
       
        # find new center point
        x_org_center, y_org_center = int(x + w / 2), int(y + h / 2)
        h_new, w_new , _= face_part_image_resized.shape
        start_x = int(x_org_center - w_new / 2)
        start_y = int(y_org_center - h_new / 2)
        end_x = start_x + w_new
        end_y = start_y + h_new

        final_image[start_y:end_y, start_x:end_x, :] = face_part_image_resized
        
    
   
       
        
    return final_image
 

