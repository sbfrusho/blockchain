import hashlib
import datetime
import sys  # Import sys for program exit

class BlockNode:
    def __init__(self, data, timestamp=None):
        self.data = data
        self.timestamp = timestamp or datetime.datetime.now()
        self.next = None

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.datetime.now() 
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        hash_string = str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
    
    def create_genesis_block(self):
        return Block("Genesis block", "0")
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def hash_change_check(self, block):
        restored_hash = hashlib.sha256(
            (str(block.data) + str(block.previous_hash) + str(block.nonce)).encode()
        ).hexdigest()
        
        if block.hash != restored_hash:
            print("h1 : " , block.hash , " h2: " , restored_hash)
            print("Hash changed! Attack detected")
            sys.exit() 
        else:
            print("Block data: ", block.data)
            print("Block timestamp: ", block.timestamp.strftime('%Y-%m-%d %H:%M:%S'))
            print("Block hash: ", block.hash)
            print("Previous hash: ", block.previous_hash)
            print(" " * 50)


blockchain = Blockchain()
blockchain.add_block(Block("Block 1", ""))
blockchain.add_block(Block("Block 2", ""))
blockchain.add_block(Block("Block 3", ""))

for block in blockchain.chain:
    blockchain.hash_change_check(block)

blockchain.chain[1].data = "Tampered Data"

print("\nAfter tampering with block 1:\n")
for block in blockchain.chain:
    blockchain.hash_change_check(block)
