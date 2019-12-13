import requests
import json

def get_movies():
    char = input("Please enter name of the character you want to search for:\n")
    # char = "Luke Skywalker"
    source = f'https://swapi.co/api/people/?search={char}'
    page = requests.get(source)

    data = page.json()

    if data['count'] < 1: 
        print('Your search returned no results. Please try again.\n')
        get_movies()
    
    elif data['count'] > 1:
        print('Your search returned more than 1 character. Please be more specific.\n')
        get_movies()
    
    else:
        movies = data['results'][0]['films']
        films = []

        for movie in movies:
            m = requests.get(movie)
            data = m.json()
            films.append(data['title'])

        print(f'\n{char} was in these Star Wars movies:')
        
        for film in films:
            print(film)


get_movies()
