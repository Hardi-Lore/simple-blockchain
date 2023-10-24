import hashlib
import time

class Block:
    """
    A class representing individual blocks in the blockchain.

    Attributes:
        index (int): The unique identifier of the block.
        previous_hash (str): The hash of the previous block in the chain.
        timestamp (int): The time when the block was created.
        data (str): The data or information stored in the block.
        current_hash (str): The cryptographic hash of the block's contents.

    Methods:
        __init__(self, index, previous_hash, timestamp, data, current_hash): 
            Initializes a new block with the provided attributes.
    """

    def __init__(self, index, previous_hash, timestamp, data, current_hash):
        """
        Initialize a new block with the specified attributes.

        Args:
            index (int): A unique identifier for the block.
            previous_hash (str): The hash of the previous block in the chain.
            timestamp (int): The time when the block is created.
            data (str): Data or information to be stored in the block.
            current_hash (str): The cryptographic hash of the block's contents.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.current_hash = current_hash

def calculate_hash(index, previous_hash, timestamp, data):
    """
    Calculate the cryptographic hash of a block based on its attributes.

    Args:
        index (int): The unique identifier of the block.
        previous_hash (str): The hash of the previous block in the chain.
        timestamp (int): The time when the block was created.
        data (str): The data or information stored in the block.

    Returns:
        str: The computed SHA-256 hash of the block's attributes and data.
    """
    # Concatenate the block's data and attributes and hash it using SHA-256
    value = str(index) + previous_hash + str(timestamp) + data
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    """
    Create the initial (genesis) block for the blockchain.

    Returns:
        Block: The genesis block with predefined attributes.
    """
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    """
    Create a new block in the blockchain based on the previous block.

    Args:
        previous_block (Block): The previous block in the blockchain.
        data (str): Data or information to be stored in the new block.

    Returns:
        Block: The new block with updated attributes.
    """
    index = previous_block.index + 1
    timestamp = int(time.time())
    current_hash = calculate_hash(index, previous_block.current_hash, timestamp, data)
    return Block(index, previous_block.current_hash, timestamp, data, current_hash)

if __name__ == '__main__':
    # Create an empty list to represent the blockchain and add the genesis block
    blockchain = [create_genesis_block()]

    # Store the reference to the previous block
    previous_block = blockchain[0]

    # Define the number of blocks to add to the blockchain
    num_blocks_to_add = 10
    # Loop to create and add blocks to the blockchain
    for i in range(num_blocks_to_add):
        # Generate data for the new block 
        new_data = f"Block #{previous_block.index + 1}"
        
        # Create a new block using the previous block as a reference
        new_block = create_new_block(previous_block, new_data)
        
        # Add the new block to the blockchain
        blockchain.append(new_block)
        
        # Update the reference to the previous block
        previous_block = new_block
        
        # Print information about the newly added block
        print(f"Block #{new_block.index} has been added to the blockchain!")
        print(f"Hash: {new_block.current_hash}\n")

