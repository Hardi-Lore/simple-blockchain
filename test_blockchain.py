import unittest
from simple_blockchain import Block, create_genesis_block, create_new_block, calculate_hash

class TestBlockchain(unittest.TestCase):
    # Test case for creating the genesis block
    def test_create_genesis_block(self):
        # Create the genesis block
        genesis_block = create_genesis_block()
        
        # Verify properties of the genesis block
        self.assertEqual(genesis_block.index, 0)  # The index of the genesis block should be 0.
        self.assertEqual(genesis_block.previous_hash, "0")  # The previous hash of the genesis block should be "0".
        self.assertEqual(genesis_block.data, "Genesis Block")  # The data of the genesis block should be "Genesis Block".
        
        # Verify the hash of the genesis block
        self.assertEqual(
            genesis_block.current_hash,
            calculate_hash(0, "0", genesis_block.timestamp, "Genesis Block")
        )

    # Test case for creating a new block
    def test_create_new_block(self):
        # Create the genesis block
        previous_block = create_genesis_block()
        
        # Define test data for the new block
        new_data = "Test Data"
        
        # Create a new block using the previous block
        new_block = create_new_block(previous_block, new_data)
        
        # Verify properties of the new block
        self.assertEqual(new_block.index, previous_block.index + 1)  # The index of the new block is incremented.
        self.assertEqual(new_block.previous_hash, previous_block.current_hash)  # Previous hash matches the previous block's hash.
        self.assertEqual(new_block.data, new_data)  # Data matches the test data.
        
        # Verify the hash of the new block
        self.assertEqual(
            new_block.current_hash,
            calculate_hash(new_block.index, previous_block.current_hash, new_block.timestamp, new_data)
        )

if __name__ == '__main__':
    # Run the unit tests
    unittest.main()
