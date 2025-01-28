import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.datetime = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
        print(f"Block created: {self.data}, Previous Hash: {self.previous_hash}")

    def calculate_hash(self):
        hash_string = str(self.datetime) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block with difficulty level: {difficulty}")
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"Block mined: {self.hash}")
        print(f"Block successfully mined with nonce: {self.nonce}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        print("Blockchain initialized with Genesis block.")

    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        print(f"\nAdding a new block with data: {new_block.data}")
        new_block.previous_hash = self.get_last_block().hash
        print(f"Previous Hash: {new_block.previous_hash}")
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        print(f"Block with data: {new_block.data} added to the blockchain.")

    def is_chain_valid(self):
        print("\nValidating the blockchain...")
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {i}: {current_block.hash}")
                return False
            
            if current_block.previous_hash != previous_block.hash:
                print(f"Previous hash mismatch at block {i}. Expected: {previous_block.hash}, Found: {current_block.previous_hash}")
                return False
        
        print("The blockchain is valid.")
        return True


blockchain = Blockchain()

print("\nMining Block 1")
blockchain.add_block(Block("Transaction 1", ""))

print("\nMining Block 2")
blockchain.add_block(Block("Transaction 2", ""))

print("\nMining Block 3")
blockchain.add_block(Block("Transaction 3", "")) 

print("\nMining Block 4")
blockchain.add_block(Block("Transaction 4", ""))  

print("\nIs blockchain valid?")
if blockchain.is_chain_valid():
    print("The blockchain is valid. It's not tampered with yet.")

blockchain.chain[1].data = "Tempered transaction"
print("\nIs blockchain valid after tampering?")
if not blockchain.is_chain_valid():
    print("The blockchain is not valid. Blockchain is tampered.")
