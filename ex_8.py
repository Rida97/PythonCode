# Functions :

def book(title):
    print(' My favourite book is : ', title)
book('Harry Potter')
book('Charlie and the Chocolate Factory')
book('Angels and Demons')

def make_shirts(size = 'large',msg=' I love PYTHON !'):
    print(' Size of your shirt is: ' + size + ' and msg to be printed is : ' + msg)

make_shirts('medium', ' Hello World !')            # positional arg
# error :   make_shirts('turn on the Music ', 20)        # Order matters in positional arg
make_shirts(size= 'small', msg=' DaddYy CoOl')     # KeyWord arg, key, value pair(Key names: size and msg shd be same as parameter)
make_shirts()
make_shirts('medium')

def shirts(msg,size='small' ):
    print(' Size of your shirt is: ' + size + ' and msg to be printed is : ' + msg)
shirts(size= 'small', msg=' DaddYy CoOl')    #meter)
shirts('small')
shirts('medium')

def city_country_name(city, country):
    City_Country_name = city + ' : ' + country
    return City_Country_name.title()

City_Conutry= city_country_name('Karachi' , 'Pakitan')
print(City_Conutry)


def make_album(artist_name, title_name, no_of_tracks = '' ):                                  # dict : key:value pairs
    Album = {'Artist' : artist_name, 'title' : title_name, 'no_of_tracks' : no_of_tracks }
 #   if no_of_tracks:                                                                         # non empty string returns true
  #      Album[no_of_tracks] = no_of_tracks                                                   # no need of these two lines
    return Album


while True:
    artist = input(' Artist name : ')
    title = input('  Title       : ')
    no_of_tracks = input('No of tracks :')
    Exit = input(' want to quit?  : ')
    albums = make_album(artist, title, no_of_tracks)
    for album in albums.items():
        if no_of_tracks:
            print(" Artist name is: " + artist + " Title of the album is : " + title + " and Track is : " + no_of_tracks)
        else:
            print(" Artist name is: " + artist + " Title of the album is : " + title)
        break

    if Exit == 'yes':
        break


def make_great(magicians):
    while magicians:
        current_magician = magicians.pop()
        current_magician += ' The Great'
        great_magicians.append(current_magician)

    return great_magicians


def show_magicians(magicians):
    Magicianss = make_great(magicians[:])
    for magician in Magicianss:
        print(' ' + magician)
    print('\n\t Unchanged list : ')
    for magician in magicians:
        print(' ' + magician)


magicians = ['blake', 'drain' , 'eric', 'la menza']
great_magicians = []

show_magicians(magicians)

# 8-12 : Subway Sandwiches !

def make_your_sandwich(*ingredients):
    print(' You ordered Sandwich with : ')

    for ingredient in ingredients:
        if ingredient:
            print(ingredient)
        else:
            print(' you did not place the order! ')


make_your_sandwich('jalapeno', 'cucumber', 'pickels', 'bbq Sauce')
make_your_sandwich('cabbage', 'sausage', 'pickels', 'red Sauce')
make_your_sandwich('jalapeno', 'onion', 'Chillies')
make_your_sandwich('')                                                       # else part wint run w/o ''


# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.


def make_car(manufacturer , model, **car_build):
    car_profile = {}
    car_profile['Manufacturer'] = manufacturer
    car_profile['Model'] = model

    for key, value in car_build.items():
        car_profile[key] = value
    return car_profile


Car_profile = make_car('subaru', 'outback', color='blue', tow_package=True)

print(Car_profile)          # dict will be printed in the same way as it is stored
