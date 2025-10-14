import time
import random

# --- Parameters ---
LOSS_PROBABILITY = 0.5  # Increased loss chance to see more retransmissions
TIMEOUT_DURATION = 2    # Seconds to wait for an ACK
TOTAL_FRAMES = 5

# --- State ---
event_counter = 0 # To track the order of events

def log_event(message):
    """Prints events with a counter for clear sequencing."""
    global event_counter
    event_counter += 1
    print(f"[{event_counter:02d}] {message}")

def receiver(frame_data):
    """Simulates the receiver."""
    log_event(f"    RECEIVER: Received Frame {frame_data} successfully.")
    ack_number = frame_data
    log_event(f"    RECEIVER: Sending ACK {ack_number} <--")
    return ack_number

def network_simulation(frame_data, direction):
    """Simulates the unreliable network for both frames and ACKs."""
    if random.random() < LOSS_PROBABILITY:
        if direction == "FRAME":
            log_event("       NETWORK: [X] Frame lost in transit! [X]")
        else: # Direction is "ACK"
            log_event("       NETWORK: [X] ACK lost in transit! [X]")
        return None

    # If not lost, proceed
    if direction == "FRAME":
        return receiver(frame_data) # Frame reaches receiver
    else: # Direction is "ACK"
        return frame_data # ACK reaches sender

def sender():
    """Sender with enhanced visual output."""
    next_frame_to_send = 0
    log_event("SENDER: Starting Stop-and-Wait ARQ simulation.\n" + "="*50)
    
    while next_frame_to_send < TOTAL_FRAMES:
        log_event(f"SENDER: Preparing to send Frame {next_frame_to_send} -->")
        
        # 1. Send the frame through the network
        ack_from_receiver = network_simulation(next_frame_to_send, "FRAME")
        
        # 2. Simulate the ACK traveling back
        received_ack = None
        if ack_from_receiver is not None:
             received_ack = network_simulation(ack_from_receiver, "ACK")
        
        start_time = time.time()
        
        # 3. Wait for the ACK or for a timeout
        while received_ack is None or received_ack != next_frame_to_send:
            if time.time() - start_time > TIMEOUT_DURATION:
                log_event(f"SENDER: [TIMEOUT!] No ACK for Frame {next_frame_to_send}. Retransmitting...")
                log_event(f"SENDER: Resending Frame {next_frame_to_send} -->")
                
                # RETRANSMIT (send frame and wait for ACK again)
                ack_from_receiver = network_simulation(next_frame_to_send, "FRAME")
                received_ack = None
                if ack_from_receiver is not None:
                    received_ack = network_simulation(ack_from_receiver, "ACK")
                
                start_time = time.time() # Reset timer after retransmitting
            
            time.sleep(0.1)

        # This point is reached only after a successful ACK
        log_event(f"SENDER: <-- ACK {received_ack} confirmed for Frame {next_frame_to_send}.")
        print("="*50)
        next_frame_to_send += 1
        time.sleep(1)
        
    log_event("SENDER: All frames sent and acknowledged successfully.")

# --- Main execution ---
if __name__ == "__main__":
    sender()