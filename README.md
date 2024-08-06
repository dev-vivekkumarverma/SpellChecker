
# SpellChecker

SpellChecker is a FastAPI-based application designed to efficiently manage and check the spelling of words. It utilizes a Trie data structure for quick word lookup and a JSON file to store words permanently.

## Features

- **Word Suggestions**: Get word suggestions based on a provided prefix.
- **Word Validation**: Check if a word exists in the dictionary.
- **Insert Word**: Add new words to the dictionary.

## Scope

This project can be integrated into applications requiring auto-fill and auto-suggestions functionalities, enhancing user experience by providing real-time word suggestions and validations.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dev-vivekkumarverma/SpellChecker.git
   cd spellchecker
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Suggest Words

- **URL**: `/suggest/{word_prefix}`
- **Method**: `GET`
- **Description**: Get word suggestions based on the provided prefix.
- **Example**:
  ```bash
  curl --location 'localhost:8000/suggest/hel'
  ```
  - **Response**:
    ```json
    {
      "given_pref": "hel",
      "suggestions_count": 545,
      "suggestions": ["hel", "hela", "helain", "helaina", "helaine", ...]
    }
    ```

### Check Word Presence

- **URL**: `/{word}`
- **Method**: `GET`
- **Description**: Check if a word exists in the dictionary.
- **Example**:
  ```bash
  curl --location 'localhost:8000/Methionylthreonylthreonylglutaminylarginyltyrosylglutamylserine'
  ```
  - **Response**:
    ```json
    {
      "searched_word": "methionylthreonylthreonylglutaminylarginyltyrosylglutamylserine",
      "is_found": true
    }
    ```

### Insert New Word

- **URL**: `/insert/{word}`
- **Method**: `POST`
- **Description**: Add a new word to the dictionary.
- **Example**:
  ```bash
  curl --location --request POST 'localhost:8000/insert/pneumonoultramicroscopicsilicovolcanoconiosis'
  ```
  - **Response**:
    ```json
    {
      "word": "pneumonoultramicroscopicsilicovolcanoconiosis",
      "is_inserted": true
    }
    ```

## Data Structure

The application uses a Trie data structure for efficient word storage and retrieval, ensuring fast operations even with a large dataset.

## Persistent Storage

Words are stored in a JSON file, allowing the dictionary to persist between restarts of the application.

## API Documentation

For detailed API documentation, visit [Postman API Documentation](https://documenter.getpostman.com/view/26583578/2sA3rxqtBy).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed and reserved by the author (dev-vivekkumarverma) Vivek Kumar Verma.

