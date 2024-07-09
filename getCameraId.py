import cv2


def find_camera_ids(max_tests=10):
    available_cameras = []
    for i in range(max_tests):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
        else:
            break  # Stop if we encounter a non-available device ID
    return available_cameras


camera_ids = find_camera_ids()
print("Available camera IDs:", camera_ids)
