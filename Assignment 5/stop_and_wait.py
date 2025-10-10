def receiver(frame_data):
    """A simple receiver that just accepts and prints the frame it gets."""
    print(f"    RECEIVER: Received Frame {frame_data}")

def sender():
    """A simple sender that sends a sequence of frames."""
    total_frames = 5
    print("SENDER: Starting to send frames...")

    for i in range(total_frames):
        print(f"SENDER: Sending Frame {i}")
        receiver(i)
        print(f"SENDER: Frame {i} acknowledged\n")
    
    print("SENDER: All frames sent and acknowledged.")

if __name__ == "__main__":
    sender()