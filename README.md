# Simple Blockchain Implementation
This is a basic Python implementation of a simple blockchain. It consists of a Python script that defines a `Block` class and functions to create, manage, and add blocks to the blockchain.

## Getting Started

### Prerequisites

- Python 3 (https://www.python.org/downloads/)
- pytest (for running tests, install using `pip install pytest`)

### Running the Blockchain

1. Clone this repository or download the Python script to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the blockchain code with the following command:
    ```
    python simple_blockchain.py
    ```
    You will see the blockchain in action, creating a genesis block and adding additional blocks.

### Running Tests

To run tests for the blockchain code, you can use the `pytest` framework:

1. Ensure you have `pytest` installed. If not, install it using `pip install pytest`.

2. Create a test file, e.g., `test_blockchain.py`, with your unit tests. Example tests are provided in the repository.

3. Run the tests with the following command:

    ```
    pytest test_blockchain.py
    ```

    The tests will be discovered, executed, and the results will be displayed in the terminal.

## Code Structure

- `simple_blockchain.py`: The main blockchain implementation.
- `test_blockchain.py` or `test_blockchain_unittest.py`: Test files for unit testing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This code is a basic example for educational purposes. Real-world blockchain implementations are more complex and feature-rich.

Feel free to modify and extend this code for your own projects and explore more advanced blockchain concepts.
