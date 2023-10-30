import cv2


class Camera:
    def __init__(self):
        self.capture = None

    def start_camera(self):
        self.capture = cv2.VideoCapture(0)

    def capture_image(self):
        if self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                return frame
        return None

    def process_image(self, image):
        pass

    @staticmethod
    def display_image(image):
        cv2.imshow('Captured Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def stop_camera(self):
        if self.capture is not None:
            self.capture.release()

