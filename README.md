# My Zootopia API

## Description

My Zootopia API is a Python project that retrieves animal information from the [API Ninjas Animals API](https://api-ninjas.com/api/animals) and generates an HTML page displaying the results.

Users can enter an animal name and receive information about that animal, including its taxonomy, locations and characteristics.

If an animal cannot be found, the program displays an appropriate message.

## Project Structure

- `animals_web_generator.py` – Generates the HTML page.
- `data_fetcher.py` – Retrieves animal data from the API.
- `animals.html` – Generated HTML output.
- `requirements.txt` – Lists the required Python packages.
- `.env` – Stores the API key locally.

## Requirements

- Python 3
- An API key from [API Ninjas](https://api-ninjas.com/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jessicasara-py/My-Zootopia-API.git
   cd My-Zootopia-API
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project's root directory and add your API key:

```text
API_KEY=your_api_key
```

Replace `your_api_key` with your personal API Ninjas key.

**Important:** Never commit your `.env` file or share your API key publicly.

## Usage

Run the program from the project directory:

```bash
python3 animals_web_generator.py
```

Enter the name of an animal when prompted.

The program retrieves the animal data and generates an `animals.html` file, which you can open in your browser.

## Dependencies

- `requests`
- `python-dotenv`