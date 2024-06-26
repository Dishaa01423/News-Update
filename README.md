# News Fetcher and Email Sender

This Python script fetches the latest news articles about a specified topic using the News API and sends an email containing the article titles, descriptions, and URLs.

## Features

- Fetches the latest news articles for a specified topic.
- Extracts the title, description, and URL of each article.
- Sends the news articles via email.

## Requirements

- Python 3.x
- `requests` library
- A valid API key from [News API](https://newsapi.org/)
- SMTP server credentials for sending emails

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/Dishaa01423/News-Update.git
    cd News-Update
    ```

2. Install the required packages:

    ```sh
    pip install requests
    ```

3. Replace `api_key` in the script with your News API key.

4. Ensure you have SMTP server credentials set up in `send_email.py`.

## Usage

1. Update the `topic` variable in the script to the desired topic you want to fetch news for.

2. Run the script:

    ```sh
    python script.py
    ```
