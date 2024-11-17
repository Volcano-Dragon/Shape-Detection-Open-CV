# Shape Detection Using OpenCV  

## 📜 **Project Description**  
This project demonstrates real-time shape detection using Python and OpenCV. By leveraging the webcam feed, the program identifies the largest geometric shape in the frame and classifies it based on its contours. The detected shape is outlined, and its name is displayed on the video feed, making it an interactive and educational computer vision tool.  

---

## 🚀 **Features**  
- Real-time detection and classification of shapes.  
- Classifies common geometric shapes:  
  - **Triangle**  
  - **Rectangle**  
  - **Pentagon**  
  - **Circle**  
  - **Line**  
- Visual feedback with contours and text labels.  
- Simple and intuitive implementation using OpenCV.  

---

## 🛠️ **Technologies Used**  
- **Python**  
- **OpenCV**  

---

## 🔧 **Setup Instructions**  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/your-username/shape-detection-open-cv.git  
   cd shape-detection-opencv  
   ```  

2. **Install dependencies**:  
   Ensure Python 3.x and OpenCV are installed. Install OpenCV via pip:  
   ```bash  
   pip install opencv-python  
   ```  

3. **Run the project**:  
   ```bash  
   python shape_detection.py  
   ```  

4. **Quit the program**:  
   Press the **'q'** key to stop the program.  

---

## 📸 **How It Works**  
1. Captures video feed from the webcam.  
2. Converts each frame to grayscale and applies Gaussian Blur for noise reduction.  
3. Uses the Canny Edge Detection algorithm to identify edges in the frame.  
4. Finds contours of objects and approximates their shapes.  
5. Detects the largest object's shape and displays its name on the video.  

---
