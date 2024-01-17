
#movies = ["Sharks", "Titanic", "League of Fist", "sharks"]

#movie_2, *movie_3, = movies

def fnc(**kwargs):
    for key, value in kwargs.items():
        if key == 'city':
            value = "Nairobi"
        elif key == 'name':
            value = "Dahola"
        print(f'{key}: {value}')



fnc(name = "Hola", age = 37, city = "Melborne")