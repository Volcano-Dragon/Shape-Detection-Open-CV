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
   git clone https://github.com/Volcano-Dragon/Shape-Detection-Open-CV.git
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

## **Output**  
1. Pentagon <br> <kbd>![Pentagon](https://github.com/user-attachments/assets/d7c31fc7-37c2-4864-9ea2-8c3538921cb9)</kbd> <br> <br>
2. Rectangle <br> <kbd>![image](https://github.com/user-attachments/assets/891bfc86-960f-4289-b31d-0d0ef8a3475c)</kbd> <br> <br>
3. Triangle <br> <kbd>![image](https://github.com/user-attachments/assets/323cbdfd-5cb6-4b65-af3e-956eb3dcd5c8)</kbd> 

      
   




