# axios-vision-task

This project is part of axios-vision task and its implements a video stream analytics system consisting of three main components: a streamer, a detector, and a view. The system processes video frames to detect movement and displays the results in real-time.

## Project Structure

```
axios-vision-task
├── src
│   ├── streamer
│   │   └── streamer.py
│   ├── detector
│   │   └── detector.py
│   ├── view
│   │   └── view.py
│   └── utils
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Components

### Streamer
- **File:** `src/streamer/streamer.py`
- **Description:** The Streamer class is responsible for reading frames from the specified video file path. It sends each frame to the detector for analysis.

### Detector
- **File:** `src/detector/detector.py`
- **Description:** The Detector class receives frames from the streamer. It utilizes OpenCV to analyze the frames for movement and sends the processed frames along with detection information to the view component.

### View
- **File:** `src/view/view.py`
- **Description:** The View class receives frames and detection data from the detector. It renders the frames on the screen, draws the detections, and displays the current time in the upper left corner of the frame.

### Utilities
- **File:** `src/utils/__init__.py`
- **Description:** This file can contain utility functions or constants shared across components, such as helper functions for time formatting or drawing detections.

## Requirements

To run this project, you need to install the following dependencies:

- OpenCV

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Usage

1. install requirements
2. run main.py
3. if you want to use different input file and not *src/data/People-6387.mp4* use the flag --input-file and specify the path of your file
4. if you want to run the system without blurring (only step 1 and 3) run with flag --no-blurrings

## tests

This system has been tested on:
- macOS (Version: 15.1.1)
- Python 3.11.1

but it should work on any machine with the right requirements.