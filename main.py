from googletrans import Translator
import json

translator = Translator()

with open('data.json') as dataFile:
    data = json.load(dataFile)


def searchLocally(keyword):
    if keyword in data:
        print("Local Result: " + keyword + " -> " + data[keyword])
    else:
        searchAPI(keyword)


def searchAPI(keyword):
    result = translator.translate(keyword, dest="pt")
    data.update({keyword: result.text})

    with open('data.json', 'w') as fp:
        json.dump(data, fp)

    print("Query Result: " + keyword + " -> " + result.text)


keyword = input("Please enter search keyword: ").lower()
searchLocally(keyword)
