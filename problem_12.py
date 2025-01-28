import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp  
        self.data = data            
        self.previous_hash = previous_hash 
        self.hash = self.calculate_hash()  

    def calculate_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_blockchain(self):
        for index, block in enumerate(self.chain):
            print(f"Block {index}:")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Data: {block.data}")
            print(f"  Timestamp: {block.timestamp}")
            print("-" * 60)



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
