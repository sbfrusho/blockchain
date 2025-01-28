
# def text_to_ascii_bits(text):
#     return ''.join(f'{ord(c):08b}' for c in text)

# def convert_to_512_bits(text):
#     ascii_binary = text_to_ascii_bits(text)
#     # print(ascii_binary)
#     padded_ascii = ascii_binary
#     appended_bits = '1' + ('0' * (512 - len(ascii_binary) - 65))  # Adjust padding dynamically

#     text_size_in_bits = len(text) * 8
#     size_bits = f'{text_size_in_bits:064b}'

#     final_bits = padded_ascii + appended_bits + size_bits

#     blocks = [final_bits[i:i+32] for i in range(0, len(final_bits), 32)]
#     return blocks
# def binary_to_hex(binary):
#     # Convert binary string to hexadecimal
#     return ''.join(f'{int(binary[i:i+4], 2):X}' for i in range(0, len(binary), 4))

# text = "They are deterministic"
# blocks = convert_to_512_bits(text)

# # Print each block neatly
# for i, block in enumerate(blocks):
#     # formatted_block = ' '.join(block[j:j+8] for j in range(0,len(block),8))
#     formatted_block = binary_to_hex(block)
#     print(f"Block {i + 1} : {formatted_block} ")
import math
import struct

# Constants for the MD5 algorithm (K constants)
constants = [int(abs(math.sin(i+1)) * 4294967296) & 0xFFFFFFFF for i in range(64)]

# Rotate values (bit shifts) for each of the 64 operations in MD5
rotate_by = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

# MD5 Initialization Vector
A_INIT = 0x67452301
B_INIT = 0xefcdab89
C_INIT = 0x98badcfe
D_INIT = 0x10325476

# F, G, H, I functions for the four rounds
def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)

# Left rotate function (circular shift)
def left_rotate(x, s):
    return ((x << s) | (x >> (32 - s))) & 0xFFFFFFFF

# Convert text to binary (ascii) representation
def text_to_ascii_bits(text):
    return ''.join(f'{ord(c):08b}' for c in text)

# Convert input text to 512-bit blocks
def convert_to_512_bits(text):
    ascii_binary = text_to_ascii_bits(text)
    padded_ascii = ascii_binary
    appended_bits = '1' + ('0' * (512 - len(ascii_binary) - 65))  # Adjust padding dynamically

    text_size_in_bits = len(text) * 8
    size_bits = f'{text_size_in_bits:064b}'

    final_bits = padded_ascii + appended_bits + size_bits

    blocks = [final_bits[i:i+512] for i in range(0, len(final_bits), 512)]
    return blocks

# Convert binary string to hexadecimal
def binary_to_hex(binary):
    return ''.join(f'{int(binary[i:i+4], 2):X}' for i in range(0, len(binary), 4))

# Main MD5 function
def md5(text):
  blocks = convert_to_512_bits(text)
  A, B, C, D = A_INIT, B_INIT, C_INIT, D_INIT

  # Process each 512-bit block
  for block in blocks:
    # Pre-calculate all M values (M0 to M63)
    M = [int(block[i:i+32], 2) for i in range(0, len(block), 32)]

    # Round 1
    for i in range(16):
        f = F(B, C, D)
        g = i
        temp = (A + f + M[g] + constants[i]) & 0xFFFFFFFF
        A = D
        D = C
        C = B
        B = (B + left_rotate(temp, rotate_by[i])) & 0xFFFFFFFF

    # Round 2
    for i in range(16):
        f = G(B, C, D)
        g = (1 + (5*i)) % 16
        temp = (A + f + M[g] + constants[i+16]) & 0xFFFFFFFF
        A = D
        D = C
        C = B
        B = (B + left_rotate(temp, rotate_by[i+16])) & 0xFFFFFFFF
        
    for i in range(16):
        f = H(B, C, D)
        g = (5 + (3*i)) % 16
        temp = (A + f + M[g] + constants[i+32]) & 0xFFFFFFFF
        A = D
        D = C
        C = B
        B = (B + left_rotate(temp, rotate_by[i+32])) & 0xFFFFFFFF

    for i in range(16):
        f = I(B, C, D)
        g = (7 + (2*i)) % 16
        temp = (A + f + M[g] + constants[i+48]) & 0xFFFFFFFF
        A = D
        D = C
        C = B
        B = (B + left_rotate(temp, rotate_by[i+48])) & 0xFFFFFFFF

    A = (A + A_INIT) & 0xFFFFFFFF
    B = (B + B_INIT) & 0xFFFFFFFF
    C = (C + C_INIT) & 0xFFFFFFFF
    D = (D + D_INIT) & 0xFFFFFFFF

    return f'{A:08x}{B:08x}{C:08x}{D:08x}'

# Test the MD5 function with a text
text = "They are deterministic"
hash_result = md5(text)
print(f"MD5 Hash: {hash_result}")