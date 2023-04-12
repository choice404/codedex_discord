import requests
import json
from dotenv import dotenv_values

config = dotenv_values('.env')

def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    jsonData = json.loads(response.text)
    quote = jsonData[0]['q'] + " - " + jsonData[0]['a']
    return quote

def getDadJoke():
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    DAD_JOKES_HEADERS = {
        "X-RapidAPI-Key": str(config['DAD_JOKES_KEY']),
        "X-RapidAPI-Host": str(config['DAD_JOKES_HOST'])
    }
    response = requests.request("GET", url, headers=DAD_JOKES_HEADERS)
    jsonData = json.loads(response.text)
    quote = jsonData["body"][0]["setup"] + "\n\n" + jsonData["body"][0]["punchline"]
    return quote

# def getWeather():
#     key = str(config[WEATHER_KEY])

def getCatPic():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.request("GET", url)
    jsonData = json.loads(response.text)
    pic = jsonData[0]["url"]
    return pic

def getJoke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    response = requests.request("GET", url)
    jsonData = json.loads(response.text)
    joke = jsonData["setup"] + "\n\n" + jsonData["delivery"]
    return joke

def getCocktail(*args):
    url = "https://www.thecocktaildb.com/api/json/v1/1/"
    if len(args) == 0:
        extension = "random.php"
        url += extension
    elif args[0] == "cocktail":
        extension = "search.php?s=" + str(args[1])
        url += extension
    response = requests.request("GET", url)
    jsonData = json.loads(response.text)
    return jsonData

def getGif(*args):
    GIPHY_KEY = str(config['GIPHY_KEY'])
    argsArr = list(args)
    url = ""
    if len(argsArr[0]) == 0:
        url = "https://api.giphy.com/v1/gifs/random?api_key=" + GIPHY_KEY
        response = requests.request("GET", url)
        jsonData = json.loads(response.text)
        gif = jsonData["data"]["embed_url"]
        return gif

    if len(argsArr[0]) > 0:
        prompt = "+".join(args[0])
        url = "https://api.giphy.com/v1/gifs/search?api_key=" + GIPHY_KEY + "&q=" + prompt + "&limit=1&offset=0&rating=r&lang=en"
    response = requests.request("GET", url)
    jsonData = json.loads(response.text)
    gif = jsonData["data"][0]["embed_url"]
    return gif


if __name__ == "__main__":
    array = ["search", "confused"]
    gif = getGif(array)
    print(gif)
