### README.md

```markdown
# PokeAPI SDK

A Python SDK for interacting with the PokeAPI, designed to provide a seamless developer experience when working with Pokémon data.

## How to Run

### 1. Download the Repository as a SDK

You can download the repository from GitHub or clone it using the following command:

```bash
git clone https://github.com/AmariRules/pokemonAPI-Amari.git
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
3. Activate the virtual environment.
4. Installing the required dependencies.
5. Running example usage scripts.
6. Executing interactive tests with user input.
7. Running unit tests to validate functionality.

Enjoy exploring the world of Pokémon through the PokeAPI SDK!

### Key guidelines:
## Showcasing the Best Developer Experience

This SDK is designed with the developer experience in mind, emphasizing clarity, usability, and reliability. The following features showcase what the best developer experience means to me:

1. **Intuitive Interface**: The SDK provides clear and descriptive method names (e.g., `get_pokemon`, `get_generation`), allowing developers to understand functionality at a glance without needing extensive documentation.

2. **Error Handling**: Custom exceptions are used to provide meaningful error messages. When developers encounter issues, they receive detailed feedback that aids in debugging, enhancing their workflow.

3. **Model Representation**: By encapsulating API responses in well-defined models (like `Pokemon` and `Generation`), developers can work with structured data that is easy to manipulate, improving the coding experience.

4. **Testing and Reliability**: Comprehensive unit and integration tests ensure that the SDK behaves as expected, giving developers confidence in its functionality and reliability.  While interactive test with user input aren't neccessary and slows down testing, providing a sample interactive test for the developer may prove useful.

## Critical Design Decisions

1. **Error Handling**: 
   - Implemented custom exceptions (`APIError`) to enhance error feedback and debugging for users.

2. **Model Structures**: 
   - Used classes (`Pokemon`, `Generation`) to represent API data, providing a structured and object-oriented approach to data management.

3. **Method Naming**: 
   - Chose clear and descriptive names for methods to make the SDK intuitive and easy to use, reducing the learning curve for new developers.

4. **Testing Strategy**: 
   - Created a robust suite of unit and integration tests to validate the SDK's functionality against the live API, ensuring reliability.

5. **Documentation**: 
   - Included a comprehensive README file to guide users through installation, usage, and testing processes, facilitating a smoother onboarding experience.

## Impact on Developer Experience

The design choices made in this SDK significantly enhance the developer experience:

- **Clarity**: The intuitive interface and clear method names reduce confusion and help developers quickly understand how to use the SDK effectively.

- **Confidence**: Comprehensive error handling and thorough testing ensure that developers can trust the SDK to behave reliably, minimizing frustration and unexpected issues.

- **Efficiency**: Structured data models and clear documentation streamline the development process, allowing developers to focus on building features rather than struggling with integration details.

Overall, these design decisions create a more enjoyable and productive experience for developers using the PokeAPI SDK, fostering greater engagement and satisfaction.
 
