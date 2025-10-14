import time

TOTAL_FRAMES = 10
WINDOW_SIZE = 4
TIMEOUT_DURATION = 3

base = 0
next_seq_num = 0
expected_frame = 0
sender_timer = None

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
    """Sender now manages a single timer for the base of the window."""
    global base, next_seq_num, sender_timer
    
    print(f"SENDER: Starting GBN with Timer (Timeout = {TIMEOUT_DURATION}s)\n")
    
    while base < TOTAL_FRAMES:
        
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            if base == next_seq_num:
                sender_timer = time.time()
                print(f"SENDER: Window was empty. Timer started for Frame {base}.")

            print(f"SENDER: Sending Frame {next_seq_num}...")
            next_seq_num += 1
            time.sleep(0.5)
        
        print("\nSENDER: Window full. Waiting for ACKs...")
        
        if sender_timer and (time.time() - sender_timer) > TIMEOUT_DURATION:
            print(f"SENDER: [TIMEOUT!] (This won't happen in our perfect network yet)")
            break

        ack_received = receiver(base)
        print(f"SENDER: Received ACK {ack_received}.\n")

        base = ack_received
        
        if base == next_seq_num:
            sender_timer = None
            print(f"SENDER: All sent frames acknowledged. Timer stopped.")
        else:
            sender_timer = time.time()
            print(f"SENDER: ACK received. Timer reset for new base Frame {base}.")
        print("-" * 40)


    print("\nSENDER: All frames sent and acknowledged successfully.")

if __name__ == "__main__":
    sender()