import requests

goat_response = requests.get('https://placegoat.com/600')
print(goat_response)

genre_response = requests.get('https://binaryjazz.us/wp-json/genrenator/v1/genre')
data = genre_response.json()
print(data)
