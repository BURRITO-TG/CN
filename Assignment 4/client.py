# client.py

import cv2
import socket
import numpy as np

# Client settings
HOST = '127.0.0.1' # Listen on all available interfaces
PORT = 9999

# 1. Create a UDP socket and bind it to the listening port [cite: 31]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((HOST, PORT))
print(f"Listening for video stream on {HOST}:{PORT}...")

# Buffer to store frame data
frame_buffer = b''

while True:
    try:
        # 2. Receive packets continuously [cite: 32]
        packet, _ = client_socket.recvfrom(65536) # Buffer size is 65536 bytes
    except socket.error as e:
        print(f"Socket error: {e}")
        break

    if not packet:
        continue

    # The first byte is the marker
    marker = packet[0:1]
    data = packet[1:]

    # 3. Append data until the last packet of the frame is received [cite: 33]
    frame_buffer += data

    # If it's the last packet (marker == 1), process the frame
    if marker == b'\x01':
        try:
            # Convert the byte buffer to a numpy array
            np_data = np.frombuffer(frame_buffer, dtype=np.uint8)
            
            # 4. Decode the frame from JPEG and display it using OpenCV [cite: 34]
            frame = cv2.imdecode(np_data, 1)

            # Ensure frame is not empty before showing
            if frame is not None:
                cv2.imshow("Receiving Video", frame)
            
            # Reset the buffer for the next frame
            frame_buffer = b''

        except Exception as e:
            print(f"Error decoding frame: {e}")
            # Reset buffer in case of corruption
            frame_buffer = b'' 
            continue

    # 5. Stop when the user presses 'q' [cite: 35]
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
client_socket.close()
cv2.destroyAllWindows()
print("Stopped receiving video.")