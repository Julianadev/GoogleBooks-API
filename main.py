

import requests

endpoint = "https://www.googleapis.com/books/v1/volumes"
query = "python"

params = {"q": query, "maxResults": 10}
response = requests.get(endpoint, params=params).json()
for book in response["items"]:
    volume = book["volumeInfo"]
    title = volume["title"]
    published = volume["publishedDate"]
    description = volume["description"]
    imageLinks = volume["imageLinks"]

    print(f"Título:{title} (Data Publicação: {published})\n Descrição: {description}\n(Imagem:{imageLinks})\t")
