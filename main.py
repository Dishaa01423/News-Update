import requests
from send_email import send_email

topic = "tesla"
api_key = "728662fd3e2148a7b28f31fae674a0c1"
"""Search for the newsapi.org to get the  given info"""
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"from=2023-08-21&" \
      "sortBy=publishedAt&" \
      "apiKey=728662fd3e2148a7b28f31fae674a0c1&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" + body + article["title"] \
               + "\n" + article["description"] \
               + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
