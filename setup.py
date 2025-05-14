from setuptools import setup, find_packages

setup(
    name="face_recognition_app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.10.0",
        "face_recognition>=1.3.0",
        "numpy>=2.1.1",
    ],
    entry_points={
        "console_scripts": [
            "face_recognition_app=face_recognition_app:main",
        ],
    },
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple face recognition application",
    keywords="face, recognition, computer vision",
    url="https://github.com/yourusername/face_detection",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 