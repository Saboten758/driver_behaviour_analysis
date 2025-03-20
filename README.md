# Driver Behaviour Monitoring
This application monitors real-time video feed to detect driver drowsiness and yawning, enhancing road safety by alerting the driver during such events.

## Setup and Installation

Follow the steps below to set up and run the application:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Saboten758/driver_behaviour_analysis
   cd driver_behaviour_analysis
   ```

2. **Create a Virtual Environment:**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv temp
   ```

3. **Activate the Virtual Environment:**

   - On **Windows**:

     ```bash
     temp\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source temp/bin/activate
     ```

4. **Install Dependencies:**

   Ensure you have [CMake](https://cmake.org/download/) and [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) installed, as they are required for compiling some Python packages like `dlib`.

   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** Installing `dlib` on Windows can be difficult as it relies on cmake library. For detailed guidance, refer to this [Medium article](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f).

   > **Download Pre-trained model (incase of any issue):**
   The application requires a pre-trained facial landmarks model. Download the `shape_predictor_68_face_landmarks.dat` file from the [dlib model repository](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and extract it into the project directory.

5. **Run the Application:**

   ```bash
   python main.py
   ```

   This will start the video capture and begin monitoring for drowsiness and yawning.

## Troubleshooting

- **dlib Installation Issues on Windows:**

  If you encounter errors while installing `dlib`, ensure that:

  - **CMake** is installed and added to your system PATH.
  - **Visual Studio Build Tools** are installed with the "Desktop development with C++" workload selected.

  For a step-by-step guide, refer to this [Medium article](https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f).

- **Permission Errors:**

  If you face permission issues during installation, try running your command prompt or terminal as an administrator.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

