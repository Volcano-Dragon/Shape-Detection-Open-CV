import cv2

def detect_shape(approx):
    # Classify shape based on the number of vertices
    vertices = len(approx)
    shape = "Unidentified"
    if vertices == 3:
        shape = "Triangle"
    elif vertices == 4:
        shape = "Rectangle"
    elif vertices == 5:
        shape = "Pentagon"
    elif vertices > 6:
        shape = "Circle"
    elif vertices == 2:
        shape= "Line"
    return shape

# Initialize webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and apply GaussianBlur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Edge detection
    edged = cv2.Canny(blurred, 150, 200)

    # Find contours
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Proceed only if at least one contour was found
    if contours:
        # Find the largest contour by area
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Approximate the contour
        epsilon = 0.04 * cv2.arcLength(largest_contour, True)
        approx = cv2.approxPolyDP(largest_contour, epsilon, True)
        
        # Detect shape
        shape = detect_shape(approx)

        # Draw contour and label the shape
        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
        x, y = approx.ravel()[0], approx.ravel()[1] - 10
        cv2.putText(frame, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)
    
    # Display the output
    cv2.imshow("Largest Object Shape Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
