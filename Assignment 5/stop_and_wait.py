import time
import random

LOSS_PROBABILITY=0.4

def receiver(frame_data):
    """A receiver that accepts and acknowledges the frame it gets."""
    print(f"    RECEIVER: Received Frame {frame_data}")
    ack_number=frame_data
    print(f"    RECEIVER: Sending ACK {ack_number}")
    return ack_number

def network_simulation(frame_data):
    """
    This function simulates the unreliable network.
    It can lose the frame or the ack too.
    """
    if random.random() < LOSS_PROBABILITY:
        print("NETWORK: >> Oh no! The frame was lost! <<")
        return -1
    
    recieved_ack=receiver(frame_data)

    if random.random() < LOSS_PROBABILITY:
        print("NETWORK: >> Oh! no! The ACK was lost! <<")
        return -1
    
    return recieved_ack

def sender():
    """A sender that waits for ACK and sends the next frame."""
    total_frames = 5
    next_frame_to_send = 0
    print("SENDER: Starting to send frames...\n")

    while next_frame_to_send < total_frames:
        print(f"SENDER: Sending Frame {next_frame_to_send}...")
        received_ack = network_simulation(next_frame_to_send)
        print(f"SENDER: Received ACK {received_ack}")
        if(received_ack == next_frame_to_send):
            print(f"SENDER: ACK {received_ack} is correct. Moving to next frame.\n")
            next_frame_to_send += 1
        else:
            print(f"SENDER: Incorrect or no ACK.\n")
        time.sleep(1.5)
    print("SENDER: All frames sent and acknowledged.")

if __name__ == "__main__":
    sender()