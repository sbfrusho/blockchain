blockchain = Blockchain() 

print("Adding blocks to the blockchain...")
blockchain.add_block(Block(datetime.datetime.now(), "Block 1: First transaction", ""))
blockchain.add_block(Block(datetime.datetime.now(), "Block 2: Second transaction", ""))
blockchain.add_block(Block(datetime.datetime.now(), "Block 3: Third transaction", ""))

print("\nBlockchain after adding blocks:")
blockchain.print_blockchain()

print("\nIs the blockchain valid?")
print("Yes" if blockchain.is_valid() else "No")

print("\nManipulating the blockchain...")
blockchain.chain[1].data = "Modified Block 1"

print("\nIs the manipulated blockchain valid?")
print("Yes" if blockchain.is_valid() else "No")

print("\nBlockchain after manipulation:")
blockchain.print_blockchain()
