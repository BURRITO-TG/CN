import time
import random

TOTAL_FRAMES = 10
WINDOW_SIZE = 4
TIMEOUT_DURATION = 3
LOSS_PROBABILITY = 0.25

base = 0
next_seq_num = 0
expected_frame = 0
sender_timer = None

def network_simulation(frame_data):
    """Simulates an unreliable network. Returns None if data is lost."""
    if random.random() < LOSS_PROBABILITY:
        return None
    return frame_data

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
    """Sender implements the full Go-Back-N protocol."""
    global base, next_seq_num, sender_timer
    
    print(f"SENDER: Starting Go-Back-N with unreliable network.\n")
    
    while base < TOTAL_FRAMES:
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < TOTAL_FRAMES:
            if base == next_seq_num:
                sender_timer = time.time()
                print(f"SENDER: Timer started for Frame {base}.")

            print(f"SENDER: Sending Frame {next_seq_num}...")
            
            frame_to_network = network_simulation(next_seq_num)
            if frame_to_network is not None:
                ack_from_receiver = receiver(frame_to_network)
                ack_to_sender = network_simulation(ack_from_receiver)
                
                if ack_to_sender is not None:
                    print(f"SENDER: Received ACK {ack_to_sender}. Sliding window base.")
                    base = ack_to_sender
                    if base == next_seq_num + 1:
                         sender_timer = None
                    else:
                         sender_timer = time.time()

            next_seq_num += 1
            time.sleep(0.5)

        if sender_timer and (time.time() - sender_timer) > TIMEOUT_DURATION:
            print(f"\nSENDER: [TIMEOUT!] for Frame {base}. The alarm clock rang!")
            print("SENDER: --- GOING BACK to Frame {base} --- \n")
            
            next_seq_num = base 
            sender_timer = None
        
        elif base < next_seq_num:
            print("SENDER: Window full. Waiting for ACKs or timeout...")
            time.sleep(1)

    print("\nSENDER: All frames sent and acknowledged successfully.")

if __name__ == "__main__":
    sender()