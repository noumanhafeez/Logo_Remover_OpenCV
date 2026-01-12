import cv2

coords = []

def click_and_crop(event, x, y, flags, param):
    global coords
    if event == cv2.EVENT_LBUTTONDOWN:
        coords = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        coords.append((x, y))
        print("Top-left:", coords[0], "Bottom-right:", coords[1])

# Open video
cap = cv2.VideoCapture("logo.mp4")

# Get frames per second
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)

# Calculate the frame number at 2 seconds
frame_number = int(fps * 13)

# Move to that frame
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Read that frame
ret, frame = cap.read()
if ret:
    cv2.imshow("Frame at 2 seconds", frame)
    cv2.setMouseCallback("Frame at 2 seconds", click_and_crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not read frame at 2 seconds")

cap.release()
