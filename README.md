# Attendance System Using Face Recognition

This project is a **Python-based Face Recognition Attendance System** that uses a webcam to detect faces, compare them with stored images, and mark attendance automatically in a CSV file. The project leverages the OpenCV library for image handling and the `face_recognition` library for face detection and comparison.

## Features
- **Face Detection**: Detects faces in real-time using a webcam.
- **Face Encoding**: Encodes faces from images stored in the `ATTENDANCE IMAGES` folder.
- **Face Matching**: Matches detected faces with the pre-encoded faces.
- **Attendance Marking**: Records attendance with the person's name and time in a CSV file.
- **Real-Time Operation**: Works seamlessly with live webcam feeds.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.8 or above
- Required Python libraries:
  - `opencv-python`
  - `face_recognition`
  - `numpy`

## Installation
1. Clone the repository or download the source code.
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python face-recognition numpy
   ```

3. Create a folder named `ATTENDANCE IMAGES` in the project directory.

4. Add images of individuals (with clear faces) to the `ATTENDANCE IMAGES` folder. The file name of each image should be the name of the individual (e.g., `John.jpg`).

![Screenshot (155)](https://github.com/user-attachments/assets/a3345a7c-d5ba-4b76-af18-8229b844c272)


## Usage
1. Run the Python script:
   ```bash
   python ATTENDANCE_PROJECT.py
   ```

2. The program will:
   - Load images from the `ATTENDANCE IMAGES` folder and encode faces.
   - Open a webcam feed.
   - Detect and recognize faces in real-time.
   - Mark attendance in a CSV file named with the current date (e.g., `dd-mm-yyyy.csv`).

3. Press the **ESC** key to exit the program.

## Project Structure
```
.
├── ATTENDANCE IMAGES   # Folder containing images of individuals
├── ATTENDANCE_PROJECT.py  # Main Python script
└── README.md           # Project documentation (this file)
```

## Code Explanation
### Face Encoding
The script reads images from `ATTENDANCE IMAGES`, converts them to RGB, and encodes the faces:
```python
def findencoding(imagess):
    encodelist = []
    for img in imagess:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        for encode in encodings:
            encodelist.append(encode)
    return encodelist
```

### Real-Time Face Matching
The program uses the webcam to capture frames, detect faces, and match them with pre-encoded faces:
```python
for encodefac, facloc in zip(encodecurframe, facescurframe):
    matches = face_recognition.compare_faces(encodeknownlist, encodefac)
    facdis = face_recognition.face_distance(encodeknownlist, encodefac)
    if len(facdis) > 0 and matches[np.argmin(facdis)]:
        name = classname[np.argmin(facdis)].capitalize()
        # Mark attendance


![Screenshot (153)](https://github.com/user-attachments/assets/b6920552-18f9-4eee-b647-6932ba1562ab)





```

### Attendance Recording
Attendance is logged in a CSV file with the person's name and timestamp:
```python
current_time = now.strftime('%H-%M-%S')
writer.writerow([name, current_time])
```

## Known Issues
- Faces with poor lighting or partial visibility may not be detected.
- Images in `ATTENDANCE IMAGES` must have clear facial features for proper encoding.

## Future Enhancements
- Add GUI for user interaction.
- Implement database integration for better data management.
- Enhance accuracy for varying lighting conditions.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [OpenCV](https://opencv.org/)
- [Face Recognition](https://github.com/ageitgey/face_recognition)
- [NumPy](https://numpy.org/)
