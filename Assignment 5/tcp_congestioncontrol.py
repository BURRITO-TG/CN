import matplotlib.pyplot as plt

TOTAL_ROUNDS = 100
INITIAL_SSTHRESH = 64
INITIAL_CWND = 1

def simulate_tcp_congestion_control():
    """
    Simulates TCP Congestion Control: Slow Start, Congestion Avoidance, and reaction to loss.
    """
    cwnd = INITIAL_CWND
    ssthresh = INITIAL_SSTHRESH
    
    rounds_list = []
    cwnd_list = []
    
    print("Starting TCP Congestion Control Simulation...")
    print(f"Initial State: cwnd = {cwnd}, ssthresh = {ssthresh}\n")

    for round_num in range(1, TOTAL_ROUNDS + 1):
        rounds_list.append(round_num)
        cwnd_list.append(cwnd)
        
        if round_num in [30, 60, 90]:
            print(f"--- Round {round_num}: PACKET LOSS DETECTED! ---")
            ssthresh = cwnd // 2
            cwnd = 1
            print(f"Action: Multiplicative Decrease. New ssthresh = {ssthresh}, cwnd reset to {cwnd}.\n")
            continue

        if cwnd < ssthresh:
            old_cwnd = cwnd
            cwnd *= 2
            print(f"Round {round_num}: In Slow Start. cwnd grows exponentially from {old_cwnd} to {cwnd}.")
        
        else:
            old_cwnd = cwnd
            cwnd += 1
            print(f"Round {round_num}: In Congestion Avoidance. cwnd grows linearly from {old_cwnd} to {cwnd}.")
            
    return rounds_list, cwnd_list

def plot_results(rounds, cwnds):
    """
    Uses Matplotlib to plot the congestion window size over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(rounds, cwnds, marker='o', linestyle='-', label='Congestion Window (cwnd)')
    
    plt.title('TCP Congestion Control Simulation')
    plt.xlabel('Transmission Rounds')
    plt.ylabel('Congestion Window Size (cwnd)')
    plt.grid(True)
    plt.legend()
    
    plt.axvline(x=30, color='r', linestyle='--', label='Packet Loss Event')
    plt.axvline(x=60, color='r', linestyle='--')
    plt.axvline(x=90, color='r', linestyle='--')
    
    plt.savefig('cwnd_plot.png')
    print("\nPlot has been saved to cwnd_plot.png")
    
    plt.show()


if __name__ == "__main__":
    transmission_rounds, congestion_windows = simulate_tcp_congestion_control()
    plot_results(transmission_rounds, congestion_windows)