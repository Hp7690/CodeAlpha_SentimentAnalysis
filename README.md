# CodeAlpha_Web Scraping

CodeAlpha Internship Task 1 - Web Scraping & Books Dashboard

## Overview

A complete web scraping project that collects book data from [books.toscrape.com](http://books.toscrape.com) and provides an interactive dashboard for analysis.

## Features

- **Web Scraper** (`web_scraper.py`): Collects book data including title, price, rating, and availability
- **Interactive Dashboard** (`books_dashboard.py`): Streamlit-based visualization and filtering interface
- **Data Analysis**: Average pricing, rating distribution, stock analysis

## Project Structure

```
├── web_scraper.py          # Main scraper script
├── books_dashboard.py      # Streamlit dashboard application
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CodeAlpha_SentimentAnalysis.git
cd CodeAlpha_SentimentAnalysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Scraper
```bash
python web_scraper.py
```
This will scrape the first 10 pages (~200 books) and save to `books_dataset.csv`.

### Launch the Dashboard
```bash
streamlit run books_dashboard.py
```
Open your browser to `http://localhost:8501` to view the interactive dashboard.

## Requirements

- Python 3.8+
- pandas
- requests
- beautifulsoup4
- streamlit
- matplotlib

## Author

Harsh Pandey - CodeAlpha Internship

## License

MIT
