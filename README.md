# Real-Time Face Detection

This project demonstrates a simple real-time face detection system using OpenCV and Python. It captures video from the webcam and detects faces using a pre-trained Haar Cascade Classifier. The system displays whether a face is detected or not in the webcam feed.

## Features

- Real-time face detection using the webcam.
- Displays "Face Detected" when a face is detected and "No Face Detected" when not.
- User-friendly with webcam input for face recognition.

## Requirements

- Python 3.x
- OpenCV
- Pillow
- Numpy
- PyYAML

You can install all the required libraries by running:

```bash
pip install -r requirements.txt
```
Alternatively, if you prefer to install the libraries individually, run:
```bash
pip install opencv-python opencv-contrib-python pillow numpy pyyaml
```
## Setup Instructions
Clone the repository:
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/real-time-face-recognition.git
```
Replace your-username with your actual GitHub username.

Download the Haar Cascade XML File:
The face detection system relies on the Haar Cascade Classifier. You need to download the haarcascade_frontalface_default.xml file and place it in the project root directory (where the Python scripts are).

You can download the file from OpenCV GitHub Repository.

Alternatively, you can download it directly from:

Download haarcascade_frontalface_default.xml

## Set Up Virtual Environment (Optional but Recommended):
It’s recommended to use a virtual environment to manage dependencies. 
Create and activate the virtual environment as follows:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

## Install Dependencies:
Once the virtual environment is activated, install the required dependencies by running:
``` bash
pip install -r requirements.txt
```
## Run the Face Detection Script:
With all dependencies set up, you can now run the face detection script:
```
python src/face_taker.py
```
On macOS, you might need to grant camera access if prompted.

## How It Works

- User Name Input: The script will prompt you to enter a user name before starting the face detection process.
- Face Detection: The script uses the Haar Cascade Classifier to detect faces in the webcam feed.
If a face is detected, it will display "Face Detected." If no face is detected, it will display "No Face Detected."
- End the Process: The video feed will continue until the user presses q to quit the process.

## Troubleshooting
- Camera Access Issue (Mac): If you face issues related to camera access on macOS, ensure that Python has the required permissions in the "Privacy" settings. You might need to grant camera permissions to your terminal or IDE.

- Dependencies Issue: If you get any errors related to missing dependencies or packages, make sure to activate the virtual environment and install the requirements using
```
  pip install -r requirements.txt.
```
