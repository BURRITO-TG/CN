import time

TOTAL_FRAMES = 10
WINDOW_SIZE = 4

base = 0
next_seq_num = 0
expected_frame = 0

def receiver(frame_data):
    """Receiver sends a cumulative ACK for the next expected frame."""
    global expected_frame
    print(f"\t\tRECEIVER: Received Frame {frame_data}. Expecting {expected_frame}.")
    
    if frame_data == expected_frame:
        print(f"\t\tRECEIVER: Frame {frame_data} accepted.")
        expected_frame += 1
        
    print(f"\t\tRECEIVER: Sending cumulative ACK {expected_frame}.")
    return expected_frame

def sender():
    """Sender uses a sliding window in a perfect network."""
    global base, next_seq_num
    
    print(f"SENDER: Starting Go-Back-N (Window Size = {WINDOW_SIZE})\n")

    while base < TOTAL_FRAMES:

        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            print(f"SENDER: Sending Frame {next_seq_num}...")
            ack_received = receiver(next_seq_num)
            print(f"SENDER: Received ACK {ack_received}.")

            base = ack_received
            print(f"SENDER: Window slides. New base is {base}.\n")
            
            next_seq_num += 1
            time.sleep(0.5)

    print("SENDER: All frames sent and acknowledged successfully.")

if __name__ == "__main__":
    sender()