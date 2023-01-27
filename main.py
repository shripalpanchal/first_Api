import requests
from send_email import send_email

topic = "tesla"
api_key = "61528ff8f8ff4b7e8799d3466a21a25b"

url = "https://newsapi.org/v2/everything"\
      f"?q={topic}&from=2022-12-27&sortBy=publishedAt&"\
      "apiKey=61528ff8f8ff4b7e8799d3466a21a25b&"\
      "language=en"



# Make request
requests = requests.get(url)

# Get a dictionary with data
content = requests.json()

body = ""
# Access the article title and description

for article in content["articles"][:20]:
    #print(article["title"])
    #print(article["description"])
    if article["title"] is not None:
        body = "Subject: Tesla News" \
                + "\n" + body + article["title"] \
                + "\n" + article["description"] \
                + article["description"] \
                +"\n" + article["url"] + 2*"\n"


print(body)
# convert body into utf-8 format
body = body.encode("utf-8")
# Send email.
send_email(message= body)