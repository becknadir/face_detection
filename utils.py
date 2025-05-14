import os
import cv2
import numpy as np

def extract_name_from_filename(filename):
    """
    Extract person name from a filename format like 'person_name_number.jpg'
    
    Args:
        filename (str): Filename to parse
        
    Returns:
        str: Extracted name
    """
    name, _ = os.path.splitext(filename)
    return '_'.join(name.split('_')[:-1])  # Remove the number after the last underscore

def draw_face_info(frame, face_location, name, color=(0, 0, 255)):
    """
    Draw rectangle and name label for a detected face
    
    Args:
        frame (numpy.ndarray): Frame to draw on
        face_location (tuple): (top, right, bottom, left) coordinates
        name (str): Name to display
        color (tuple): BGR color tuple
        
    Returns:
        numpy.ndarray: Frame with annotations
    """
    top, right, bottom, left = face_location
    
    # Draw rectangle around the face
    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    
    # Draw name label above the face
    label_size, _ = cv2.getTextSize(name, cv2.FONT_HERSHEY_DUPLEX, 0.6, 1)
    label_height = label_size[1]
    cv2.rectangle(frame, (left, top - label_height - 10), (right, top), color, cv2.FILLED)
    cv2.putText(frame, name, (left + 6, top - 6), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)
    
    return frame

def resize_frame(frame, width=None, height=None):
    """
    Resize a frame while maintaining aspect ratio
    
    Args:
        frame (numpy.ndarray): Frame to resize
        width (int, optional): Target width
        height (int, optional): Target height
        
    Returns:
        numpy.ndarray: Resized frame
    """
    if width is None and height is None:
        return frame
        
    h, w = frame.shape[:2]
    
    if width is None:
        ratio = height / float(h)
        dim = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dim = (width, int(h * ratio))
        
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA) 