# server.py

import cv2
import socket
import time

# Server settings
HOST = '127.0.0.1' # Listen on all available interfaces
PORT = 9999
CLIENT_ADDR = (HOST, PORT)

# Create a UDP socket [cite: 21]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the video file [cite: 22]
try:
    cap = cv2.VideoCapture('video.mp4')
    if not cap.isOpened():
        raise IOError("Cannot open video.mp4")
except Exception as e:
    print(f"Error opening video file: {e}")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = 1 / fps  # Time to wait between sending frames [cite: 28]
print(f"Streaming video at {fps:.2f} FPS...")

# Define the maximum size for each chunk
# UDP packets have a size limit, so we split frames into smaller chunks.
CHUNK_SIZE = 60000 

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video or failed to read frame.")
        break # Repeat until video ends [cite: 29]

    # (a) Resize and encode the frame into JPEG for compression [cite: 25]
    # Resizing reduces the amount of data to be sent.
    frame = cv2.resize(frame, (640, 480))
    # Encoding to JPEG compresses the image data.
    result, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    if not result:
        continue

    # (b) Split the encoded frame into chunks of a fixed size [cite: 26]
    buffer_bytes = buffer.tobytes()
    buffer_size = len(buffer_bytes)

    # Send chunks
    for i in range(0, buffer_size, CHUNK_SIZE):
        chunk = buffer_bytes[i:i + CHUNK_SIZE]
        
        # (c) Send each chunk with a header [cite: 27]
        # The header is a single byte: 0 for an intermediate chunk, 1 for the last chunk.
        # This marker bit indicates the last packet of the frame [cite: 27]
        marker = b'\x01' if (i + CHUNK_SIZE) >= buffer_size else b'\x00'
        
        try:
            server_socket.sendto(marker + chunk, CLIENT_ADDR)
        except socket.error as e:
            print(f"Socket Error: {e}")
            break

    # Sleep to maintain the original frame rate [cite: 28]
    time.sleep(frame_interval)

# Cleanup
cap.release()
server_socket.close()
print("Streaming finished.")