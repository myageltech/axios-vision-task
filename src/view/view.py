import cv2

# MACROS
GAUSSIAN_BLUR_KERNEL_SIZE = (15, 15)
FONT_SCALE = 1
FONT_COLOR = (255, 255, 255)
FONT_THICKNESS = 2
RECTANGLE_COLOR = (0, 255, 0)
RECTANGLE_THICKNESS = 2
TEXT_POSITION = (10, 30)

#the view component
class View:
    def __init__(self):
        self.window_name = "axios-vision Video Stream Analytics"

    def display_frame(self, frame, detections, current_time, no_blurring):
        #draw
        if detections is not None:
            for contour in detections:
                (x, y, w, h) = cv2.boundingRect(contour)
                #use blurring feature if no_blurring isnt specified
                if not no_blurring:
                    # Gaussian Blur
                    roi = frame[y:y+h, x:x+w]
                    blurred_roi = cv2.GaussianBlur(roi, GAUSSIAN_BLUR_KERNEL_SIZE, 0)
                    frame[y:y+h, x:x+w] = blurred_roi
                cv2.rectangle(frame, (x, y), (x + w, y + h), RECTANGLE_COLOR, RECTANGLE_THICKNESS)

        #step1.3
        cv2.putText(frame, current_time, TEXT_POSITION, cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, FONT_COLOR, FONT_THICKNESS)
        cv2.imshow(self.window_name, frame)

    #step3
    def close(self):
        cv2.destroyAllWindows()