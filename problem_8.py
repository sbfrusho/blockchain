import requests
import json

API_KEY = 'E34342B4IR3B8RI3K61XG4YKEUT7SR54MM'

ETHERSCAN_URL = 'https://api.etherscan.io/api'

def get_last_block_number():
    """Fetches the latest block number from the Ethereum blockchain."""
    params = {
        'module': 'proxy',
        'action': 'eth_blockNumber',
        'apikey': API_KEY
    }

    response = requests.get(ETHERSCAN_URL, params=params)
    if response.status_code == 200:
        block_number = int(response.json()['result'], 16)
        print(f"Latest Block Number: {block_number}")
        return block_number
    else:
        print(f"Error fetching block number: {response.status_code}")
        return None

def get_block_by_number(block_number):
    """Fetches block information by block number from the Ethereum blockchain."""
    params = {
        'module': 'proxy',
        'action': 'eth_getBlockByNumber',
        'tag': hex(block_number),
        'boolean': 'true', 
        'apikey': API_KEY
    }

    response = requests.get(ETHERSCAN_URL, params=params)
    if response.status_code == 200:
        block_info = response.json()['result']
        return block_info
    else:
        print(f"Error fetching block information: {response.status_code}")
        return None

def print_block_info(block_info):
    """Prints block information."""
    if block_info:
        print("\nBlock Information:")
        print(f"Block Number: {int(block_info['number'], 16)}")
        print(f"Block Hash: {block_info['hash']}")
        print(f"Parent Block Hash: {block_info['parentHash']}")
        print(f"Timestamp: {int(block_info['timestamp'], 16)}")
        print(f"Miner: {block_info['miner']}")
        print(f"Gas Used: {int(block_info['gasUsed'], 16)}")
        print(f"Gas Limit: {int(block_info['gasLimit'], 16)}")
        print(f"Transactions: {len(block_info['transactions'])}")
    else:
        print("No block information available.")

def main():
    """Fetch and print the latest block information."""
    print("Fetching the latest block information...\n")
    
    last_block_number = get_last_block_number()
    
    if last_block_number is not None:
        block_info = get_block_by_number(last_block_number)
        
        print_block_info(block_info)

if __name__ == '__main__':
    main()
