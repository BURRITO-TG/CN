import cv2
import socket
import numpy as np

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((HOST, PORT))
print(f"Listening for video stream on {HOST}:{PORT}...")

frame_buffer = b''

while True:
    try:
        packet, _ = client_socket.recvfrom(65536) 
    except socket.error as e:
        print(f"Socket error: {e}")
        break

    if not packet:
        continue

    marker = packet[0:1]
    data = packet[1:]

    frame_buffer += data

    if marker == b'\x01':
        try:
            np_data = np.frombuffer(frame_buffer, dtype=np.uint8)
            
            frame = cv2.imdecode(np_data, 1)

            if frame is not None:
                cv2.imshow("Receiving Video", frame)
            frame_buffer = b''

        except Exception as e:
            print(f"Error decoding frame: {e}")
            frame_buffer = b'' 
            continue

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()
print("Stopped receiving video.")