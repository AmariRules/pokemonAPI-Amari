### README.md

```markdown
# PokeAPI SDK

A Python SDK for interacting with the PokeAPI, designed to provide a seamless developer experience when working with Pokémon data.

## How to Run

### 1. Download the Repository as a SDK

You can download the repository from GitHub or clone it using the following command:

```bash
git clone https://github.com/yourusername/pokemonAPI-Amari.git
cd pokemonAPI-Amari
```

### 2. Create a Virtual Environment

To create a virtual environment, run:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment using the following command:

- **On macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

- **On Windows**:

  ```bash
  venv\Scripts\activate
  ```

### 4. Install Requirements

Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run Example Usage

To run the example usage script and see how to use the SDK, execute the following command:

```bash
python example_usage.py
```

This will demonstrate how to fetch Pokémon and generation data using the SDK.

### 6. Test Interactive Test with User Input

To run the interactive test that allows you to input a generation ID and output Pokémon in that generation, execute:

```bash
python tests/interactive_test_poke_api.py
```

When prompted, enter a generation ID (e.g., "1") to see the Pokémon in that generation.

### 7. Run Unit Tests

To ensure that the SDK functions as expected, run the unit tests with the following command:

```bash
python -m unittest discover -s tests
```

### Unit Test Overview

The `tests/test_poke_api.py` file contains unit tests designed to validate the core functionality of the PokeAPI SDK. The following scenarios are covered:

1. **Valid Pokémon Retrieval**: Tests if the SDK can successfully retrieve data for a valid Pokémon (e.g., "pikachu").
2. **Invalid Pokémon Retrieval**: Tests the SDK's ability to handle requests for invalid Pokémon names, expecting an appropriate error response.
3. **Valid Generation Retrieval**: Tests if the SDK can successfully retrieve data for a valid generation (e.g., "1").
4. **Invalid Generation Retrieval**: Tests the SDK's handling of requests for invalid generation IDs, expecting an appropriate error response.

## Summary

This README provides a comprehensive guide to running the PokeAPI SDK, including detailed steps for:

1. Downloading or cloning the repository.
2. Setting up a virtual environment.
3. Installing the required dependencies.
4. Running example usage scripts.
5. Executing interactive tests with user input.
6. Running unit tests to validate functionality.

Enjoy exploring the world of Pokémon through the PokeAPI SDK!
