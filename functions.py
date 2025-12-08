## Ashley Ma
## HCDE 310
## P3:FINAL PROJECT

## Terminal codes to activate flask:
# cd /Users/ashley/PycharmProjects/P3-Final-Project_Ashley-Ma
# source venv/bin/activate
# flask --debug run


## Functions for the website

##importing url, json and pprint modules
import urllib.parse, urllib.request, urllib.error, json
import pprint

##Pokemon API

### Finding a certain Pokemon's information/ Finding the Pokemon's type
def pokemon_info(name):
    pokemon_name = name.lower()
    base_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name

    ##exception code in case url fails/ when user puts in wrong Pokemon name
    ## returns none so other functions can run
    try:
        data = urllib.request.urlopen(base_url)
    except urllib.error.HTTPError as e:
        return None
    except urllib.error.URLError as e:
        return None
    data_str = data.read()
    pokemon_info = json.loads(data_str)
    pokemon_type = []
    for info in pokemon_info["types"]:
        type = info["type"]["name"]
        pokemon_type.append(type)

    ## If the Pokemon has multiple types then only take the first type
    return pokemon_type[0]


## get the Pokemon's picture
def pokemon_pic(name):
    pokemon_name = name.lower()
    base_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name

    ## excepetion code in case pokemon doesnt exist
    try:
        data = urllib.request.urlopen(base_url)
    except urllib.error.HTTPError as e:
        return None
    except urllib.error.URLError as e:
        return None
    data_str = data.read()
    pokemon_info = json.loads(data_str)
    ## where the picture is located within the dictionary
    pokemon_pic = pokemon_info["sprites"]["other"]["official-artwork"]["front_default"]

    return pokemon_pic


## function for when it shows the result it will capitalize the Pokemon name
def upper(name):
    lower_name = name.lower()
    user_return = lower_name[0].upper() + lower_name[1:]
    return user_return


## Fetching all the Pokemon types avalible

#List of all the Pokemon types avalible within the API
pokemon_type = []
url = "https://pokeapi.co/api/v2/type/"
data = urllib.request.urlopen(url)
data_str = data.read()
all_types = json.loads(data_str)

for types in all_types["results"]:
    pokemon_type.append(types["name"])

#pprint.pprint(pokemon_type)
#print(len(pokemon_type))


## Fetching all Ghibli Films avalible within the API
G_url = "https://ghibliapi.vercel.app/films/"
data = urllib.request.urlopen(G_url)
data_str = data.read()
Ghibli = json.loads(data_str)

#List of all Ghibli film name
Ghibli_titles = []

for info in Ghibli:
    Ghibli_titles.append(info["title"])

#pprint.pprint(Ghibli_titles)

#print(len(Ghibli_titles))

## Connecting the Pokemon type to Ghibli film, this is just based off where they are in the list.
def connecting_film(name):
    user_choice = pokemon_info(name)
    if user_choice == None:
        return None

    else:
        for i in range(len(pokemon_type)):
            if pokemon_type[i] == user_choice:
                return Ghibli_titles[i]


##Fetches specific ghibli film info
## returns the film description
def film_info(name):
    film_name = connecting_film(name)
    if film_name == None:
        return None
    else:
        id = ""
        for info in Ghibli:
            if info["title"] == film_name:
                id = info["id"]

        all_info_url = "https://ghibliapi.vercel.app/films/" + id
        gib_data = urllib.request.urlopen(all_info_url)
        gib_data_str = gib_data.read()
        all_info = json.loads(gib_data_str)

        return all_info