import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time() 
        self.data = data 
        self.previous_hash = previous_hash  
        self.nonce = 0  
        self.hash = self.calculate_hash() 

    def calculate_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash() 
        print(f"Block mined: {self.hash} with nonce: {self.nonce}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4 

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty) 
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_blockchain(self):
        for block in self.chain:
            print(f"Block {self.chain.index(block)}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Data: {block.data}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Nonce: {block.nonce}")
            print("-" * 60)

blockchain = Blockchain()

print("Mining Block 1...")
blockchain.add_block(Block("Transaction 1", blockchain.get_last_block().hash))

print("\nMining Block 2...")
blockchain.add_block(Block("Transaction 2", blockchain.get_last_block().hash))

print("\nMining Block 3...")
blockchain.add_block(Block("Transaction 3", blockchain.get_last_block().hash))

print("\nBlockchain:")
blockchain.print_blockchain()

print("\nIs the blockchain valid?")
if blockchain.is_chain_valid():
    print("The blockchain is valid. It's not tempered.")
else:
    print("The blockchain is invalid. It's been tampered.")

print("\nTampering with the blockchain...")
blockchain.chain[1].data = "Tampered Transaction 1"

print("\nIs the blockchain valid after tampering?")
if blockchain.is_chain_valid():
    print("The blockchain is valid. It's not tempered.")
else:
    print("The blockchain is invalid. It's been tampered.")
