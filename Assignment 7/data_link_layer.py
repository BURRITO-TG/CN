# -----------------------------------------------------------
# Assignment 9 — Data Link Layer : Python Coding Tasks
# -----------------------------------------------------------
# Contains:
#   Part 1: Error Detection (Parity, Checksum, CRC)
#   Part 2: Error Correction (Hamming Code 7,4)
#   Part 3: MAC Address → Binary
#   Part 4: MTU-Based Fragmentation
# -----------------------------------------------------------


# -----------------------------------------------------------
# Part 1A — Parity Bit (Even Parity)
# -----------------------------------------------------------
def even_parity(data):
    """
    Compute even parity bit for a binary string.
    """
    ones = data.count("1")
    parity_bit = "0" if ones % 2 == 0 else "1"
    return data + parity_bit


# Sample I/O
# Input:  1010110
# Output: 10101101
# -----------------------------------------------------------


# -----------------------------------------------------------
# Part 1B — 16-bit Checksum
# -----------------------------------------------------------
def checksum_16bit(data):
    """
    Compute 16-bit checksum using binary addition and one's complement.
    Input must be a binary string.
    """
    # pad to multiples of 16 bits
    while len(data) % 16 != 0:
        data = "0" + data

    sum_val = 0

    for i in range(0, len(data), 16):
        block = data[i:i+16]
        sum_val += int(block, 2)

        # wrap-around carry
        sum_val = (sum_val & 0xFFFF) + (sum_val >> 16)

    # one's complement
    checksum = (~sum_val) & 0xFFFF
    return format(checksum, "016b")


# Sample I/O
# Input:  1011001110001111 0101010101010101
# Output: 0011100010101000 (checksum 16 bits)
# -----------------------------------------------------------


# -----------------------------------------------------------
# Part 1C — CRC Implementation
# -----------------------------------------------------------
def xor(a, b):
    return "".join("0" if i == j else "1" for i, j in zip(a, b))

def crc(data, generator="1101"):
    """
    Compute CRC remainder.
    Default polynomial = x^3 + x^2 + 1  (1101)
    """
    n = len(generator)
    dividend = data + "0"*(n-1)
    temp = dividend[:n]

    for i in range(n, len(dividend)):
        if temp[0] == "1":
            temp = xor(temp, generator) + dividend[i]
        else:
            temp = xor(temp, "0"*n) + dividend[i]

    # last step
    if temp[0] == "1":
        temp = xor(temp, generator)
    else:
        temp = xor(temp, "0"*n)

    return temp[1:]  # remainder


# Sample I/O
# Input: data = 11010011101100, generator = 1101
# Output: 100 (remainder)
# -----------------------------------------------------------



# -----------------------------------------------------------
# Part 2 — Hamming Code (7,4)
# -----------------------------------------------------------
def hamming_7_4(data):
    """
    Encode 4 bits into 7-bit Hamming code.
    Positions: 1 2 3 4 5 6 7
               p1 p2 d1 p3 d2 d3 d4
    """
    d1, d2, d3, d4 = map(int, data)

    # parity bits
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    codeword = f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"
    return codeword


# Sample I/O
# Input:  1011
# Output: 0110011
# -----------------------------------------------------------



# -----------------------------------------------------------
# Part 3 — MAC Address → Binary
# -----------------------------------------------------------
def mac_to_binary(mac):
    """
    Convert MAC address (hex) → 48-bit binary.
    Example input: AA:BB:CC:DD:EE:FF
    """
    parts = mac.split(":")
    return "".join(format(int(p, 16), "08b") for p in parts)


# Sample I/O
# Input:  AA:BB:CC:DD:EE:FF
# Output: 1010101010111011...
# -----------------------------------------------------------



# -----------------------------------------------------------
# Part 4 — Simple MTU-Based Fragmentation
# -----------------------------------------------------------
def fragment_packet(packet, mtu):
    """
    Fragment string/binary packet into frames ≤ MTU.
    """
    frames = []
    for i in range(0, len(packet), mtu):
        frames.append(packet[i:i+mtu])
    return frames


# Sample I/O
# Input:  packet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", MTU=5
# Output: [ABCDE, FGHIJ, KLMNO, PQRST, UVWXY, Z]
# -----------------------------------------------------------



# -----------------------------------------------------------
# MAIN (for demonstration)
# -----------------------------------------------------------
if __name__ == "__main__":

    print("---- PART 1A : EVEN PARITY ----")
    print(even_parity("1010110"))

    print("\n---- PART 1B : 16-bit CHECKSUM ----")
    print(checksum_16bit("10110011100011110101010101010101"))

    print("\n---- PART 1C : CRC ----")
    print(crc("11010011101100", "1101"))

    print("\n---- PART 2 : HAMMING (7,4) ----")
    print(hamming_7_4("1011"))

    print("\n---- PART 3 : MAC → BINARY ----")
    print(mac_to_binary("AA:BB:CC:DD:EE:FF"))

    print("\n---- PART 4 : FRAGMENTATION ----")
    print(fragment_packet("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5))
