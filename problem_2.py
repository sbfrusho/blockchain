import datetime

class Block:
    def __init__(self, data, timestamp=None):
        self.data = data
        self.timestamp = timestamp or datetime.datetime.now()
        self.next = None
    
class Blockchain:
    def __init__(self):
        self.head = None
    
    def add_block(self, data):
        print(f"Adding block with data: {data}")
        new_block = Block(data)
        if not self.head:
            self.head = new_block
            print(f"Block with data '{data}' is now the head (first block).")
        else:
            last_block = self.get_last_block()
            last_block.next = new_block
            print(f"Block with data '{data}' added after the last block.")

    def mine_block(self, data):
        print(f"Mining new block with data: {data}")
        new_block = Block(data)
        last_block = self.get_last_block()
        if last_block:
            last_block.next = new_block
        else:
            self.head = new_block
        print(f"Block with data '{data}' has been mined and added at the end.")
    
    def get_last_block(self):
        current = self.head
        while current and current.next:
            current = current.next
        return current
    
    def display(self):
        current = self.head
        if not current:
            print("The blockchain is empty.")
            return
        print("Displaying blockchain:")
        index = 1
        while current:
            print(f"Block {index}:")
            print(f"  Data: {current.data}")
            print(f"  Timestamp: {current.timestamp}")
            print()
            current = current.next
            index += 1

blockchain = Blockchain()

print("Initial Blockchain:")
blockchain.display()

blockchain.add_block("Block 1")
blockchain.add_block("Block 2")
blockchain.add_block("Block 3")

print("Blockchain after adding 3 blocks:")
blockchain.display()

blockchain.mine_block("Block 4")

print("Blockchain after mining a new block:")
blockchain.display()
