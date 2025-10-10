import time

def receiver(frame_data):
    """A receiver that accepts and acknowledges the frame it gets."""
    print(f"    RECEIVER: Received Frame {frame_data}")
    ack_number=frame_data
    print(f"    RECEIVER: Sending ACK {ack_number}")
    return ack_number

def sender():
    """A sender that waits for ACK and sends the next frame."""
    total_frames = 5
    next_frame_to_send = 0
    print("SENDER: Starting to send frames...")

    while next_frame_to_send < total_frames:
        print(f"SENDER: Sending Frame {next_frame_to_send}...")
        received_ack = receiver(next_frame_to_send)
        print(f"SENDER: Received ACK {received_ack}")
        if(received_ack == next_frame_to_send):
            print(f"SENDER: ACK {received_ack} is correct. Moving to next frame.")
            next_frame_to_send += 1
        else:
            print(f"SENDER: Incorrect ACK. This shouldn't happen yet.\n")
        time.sleep(1)
    print("SENDER: All frames sent and acknowledged.")

if __name__ == "__main__":
    sender()