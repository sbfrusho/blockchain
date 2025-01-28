import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash=''):
        self.timestamp = datetime.datetime.now()
        self.data = data 
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = f"{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()
    
    def __str__(self):
        return f"Timestamp: {self.timestamp}\nData: {self.data}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}"

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)
    
    def print_blockchain(self):
        print("Blockchain:")
        for block in self.chain:
            print(f"\nBlock Data:\n{block}")
            print(f"Block Number: {len(self.chain)}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Block Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Data: {block.data}")
            print("-" * 50)

class Transaction:
    def __init__(self, sender, receiver, value, gas, gas_price, nonce, input_data):
        self.block_number = 0 
        self.timestamp = datetime.datetime.now()
        self.hash = hashlib.sha256(f"{sender}{receiver}{value}{gas}{gas_price}{nonce}{input_data}".encode('utf-8')).hexdigest()
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.gas = gas
        self.gas_price = gas_price
        self.nonce = nonce
        self.input_data = input_data
    
    def __str__(self):
        return (f"Transaction Hash: {self.hash}\n"
                f"Block Number: {self.block_number}\n"
                f"Timestamp: {self.timestamp}\n"
                f"From: {self.sender}\n"
                f"To: {self.receiver}\n"
                f"Value: {self.value} ETH\n"
                f"Gas: {self.gas}\n"
                f"Gas Price: {self.gas_price}\n"
                f"Nonce: {self.nonce}\n"
                f"Input: {self.input_data}\n")

blockchain = Blockchain()

transaction1 = Transaction(sender="rusho", receiver="oishe", value=10, gas=21000, gas_price=20, nonce=1, input_data="transaction done")
transaction2 = Transaction(sender="rusho", receiver="shourov", value=5, gas=21000, gas_price=20, nonce=2, input_data="transaction done")

blockchain.add_block(transaction1)
blockchain.add_block(transaction2)

blockchain.chain[1].data.block_number = 1
blockchain.chain[2].data.block_number = 2

blockchain.print_blockchain()

print("\nTransaction Details:")
print(transaction1)
print("-" * 50)
print(transaction2)
