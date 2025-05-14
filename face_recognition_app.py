import cv2
import face_recognition
import os
import numpy as np
import argparse
import sys
from utils import extract_name_from_filename, draw_face_info, resize_frame

def load_known_faces(directory):
    """
    Load and encode face images from a directory.
    
    The function expects images named as 'name_number.jpg' or 'name_number.png',
    where 'name' is the person's name and 'number' is an identifier.
    
    Args:
        directory (str): Path to directory containing face images
        
    Returns:
        dict: Dictionary mapping names to lists of face encodings
    """
    known_faces = {}
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            name = extract_name_from_filename(filename)
            
            image_path = os.path.join(directory, filename)
            print(f"Processing {image_path}")
            
            try:
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)
                
                if encoding:  # Check if a face was found in the image
                    if name not in known_faces:
                        known_faces[name] = []
                    known_faces[name].append(encoding[0])
                    print(f"Successfully encoded face for {name}")
                else:
                    print(f"Warning: No face found in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    return known_faces

def window_closed(window_name):
    """Check if a window has been closed by the user"""
    try:
        return cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1
    except:
        return True

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Face Recognition System')
    parser.add_argument('--faces_dir', type=str, 
                        help='Directory containing face images (default: ./faces)',
                        default='./faces')
    parser.add_argument('--tolerance', type=float,
                        help='Face recognition tolerance (lower is more strict, default: 0.6)',
                        default=0.6)
    parser.add_argument('--resize_width', type=int,
                        help='Resize frame width for processing (default: None)',
                        default=None)
    args = parser.parse_args()
    
    # Load known faces
    print(f"Loading known faces from {args.faces_dir}")
    known_faces = load_known_faces(args.faces_dir)
    
    if not known_faces:
        print("No valid face images found. Please add images to the faces directory.")
        return
    
    print(f"Loaded {sum(len(encodings) for encodings in known_faces.values())} face(s) of {len(known_faces)} unique person(s)")
    
    # Initialize webcam
    print("Initializing webcam...")
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        print("Error: Could not open webcam. Please check your camera connection.")
        return
    
    window_name = 'Face Recognition'
    cv2.namedWindow(window_name)
    print(f"Face recognition started. Press 'q' to quit or close the {window_name} window.")
    
    try:
        while True:
            # Check if window was closed
            if window_closed(window_name):
                print("Window closed by user. Exiting...")
                break
                
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            
            if not ret:
                print("Error: Failed to capture image from webcam")
                break
            
            # Optionally resize frame for faster processing
            if args.resize_width:
                small_frame = resize_frame(frame, width=args.resize_width)
            else:
                small_frame = frame
            
            # Find face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            
            # Process each face in the frame
            for face_location, face_encoding in zip(face_locations, face_encodings):
                name = "Unknown"
                
                # Compare with known faces
                for known_name, known_encodings in known_faces.items():
                    matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=args.tolerance)
                    if True in matches:
                        name = known_name
                        break
                
                # If we're processing a resized frame, scale face_location back to original size
                if args.resize_width:
                    scale = frame.shape[1] / small_frame.shape[1]
                    top, right, bottom, left = face_location
                    face_location = (
                        int(top * scale),
                        int(right * scale),
                        int(bottom * scale),
                        int(left * scale)
                    )
                
                # Draw face info on the frame
                draw_face_info(frame, face_location, name)
            
            # Display the resulting frame
            cv2.imshow(window_name, frame)
            
            # Exit on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quit key pressed. Exiting...")
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user. Shutting down.")
    finally:
        # Release resources
        video_capture.release()
        cv2.destroyAllWindows()
        print("Face recognition stopped")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        # Release OpenCV resources on error
        cv2.destroyAllWindows()
        sys.exit(1) 