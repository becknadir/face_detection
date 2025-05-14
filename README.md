https://github.com/user-attachments/assets/3ac4dcd5-83c5-4ea3-aed9-8d406b412ae5

# Face Recognition System

A simple face recognition application that uses your webcam to detect and identify faces based on a set of reference images.

## Features

- Real-time face detection using webcam
- Face recognition based on a database of known faces
- Interactive command-line interface
- Visual display of recognized faces with bounding boxes and name labels

## Requirements

- Python 3.6+
- Webcam
- Required libraries (see requirements.txt)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/face_detection.git
   cd face_detection
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   **Note for Windows users:** 
   If you encounter issues installing `dlib` (a dependency of face_recognition), you may need to:
   - Install CMake (download from [cmake.org](https://cmake.org/download/))
   - Install Visual Studio Build Tools with C++ development tools

   **Alternative installation for Windows:**
   You can use conda to install dlib:
   ```
   conda install -c conda-forge dlib
   pip install -r requirements.txt
   ```

## Usage

### Step 1: Prepare face images

1. Create a directory to store face images (e.g., `faces`)
2. Add clear face images of people you want to recognize
3. Name the files using the format: `person_name_1.jpg`, `person_name_2.jpg`, etc.
   - Example: `john_1.jpg`, `john_2.jpg`, `alice_1.jpg`
   - The naming is important as the program uses it to identify people

### Step 2: Run the application

```
python face_recognition_app.py --faces_dir ./faces
```

Replace `./faces` with the path to your directory of face images if different.

### Step 3: Use the application

- The application will open a window showing the webcam feed
- Detected faces will be highlighted with a red rectangle
- Names will be displayed above recognized faces
- Press 'q' to quit the application

## How it works

1. The program loads and encodes faces from the specified directory
2. It captures video from your webcam in real-time
3. For each frame, it:
   - Detects face locations
   - Extracts face encodings (numerical representations of faces)
   - Compares against known face encodings
   - Displays the results with visual indicators

## Customization

- Edit the code to change visual elements (colors, fonts, etc.)
- Modify the face recognition tolerance by editing the comparison threshold
- Add additional features like saving recognized faces or tracking

## Troubleshooting

- **No faces detected**: Ensure your lighting is good and face is clearly visible
- **Installation issues**: See the installation notes for platform-specific guidance
- **Webcam not found**: Check your camera connection and permissions
- **Slow performance**: Reduce video resolution or processing frequency

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
