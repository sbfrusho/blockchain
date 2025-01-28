def text_to_ascii_bits(text):
    return ''.join(f'{ord(c):08b}' for c in text)

def convert_to_512_bits(text):
    ascii_binary = text_to_ascii_bits(text)
    padded_ascii = ascii_binary
    appended_bits = '1' + ('0' * (512 - len(ascii_binary) - 65))

    text_size_in_bits = len(text) * 8
    size_bits = f'{text_size_in_bits:064b}'

    final_bits = padded_ascii + appended_bits + size_bits

    blocks = [final_bits[i:i+32] for i in range(0, len(final_bits), 32)]
    return blocks

def binary_to_hex(binary):
    # Convert binary string to hexadecimal
    return ''.join(f'{int(binary[i:i+4], 2):X}' for i in range(0, len(binary), 4))

text = "They are deterministic"
blocks = convert_to_512_bits(text)

# Print each block in hexadecimal format
for i, block in enumerate(blocks):
    formatted_block = ' '.join(block[j:j+8] for j in range(0, len(block), 8))
    hex_block = binary_to_hex(block)
    print(f"Block {i + 1} : {formatted_block} (Hex: {hex_block})")
