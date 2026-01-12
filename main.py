import cv2
import numpy as np

# Input and output video paths
input_video = "input_video.mp4"
output_video = "output_no_logo.mp4"

# Open the video
cap = cv2.VideoCapture(input_video)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Define the region of the Instagram logo (example: bottom-right corner)
# Adjust these values based on your logo size
x_start, y_start = width - 150, height - 50
x_end, y_end = width, height

# Create a mask for inpainting
mask = np.zeros((height, width), dtype=np.uint8)
mask[y_start:y_end, x_start:x_end] = 255  # White region = logo to remove

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Inpaint the logo area using Telea method
    frame_no_logo = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)

    out.write(frame_no_logo)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processed and saved as", output_video)
