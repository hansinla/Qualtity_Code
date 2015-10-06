def read_restaurants(file):
    """ (file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    openFile = open(file, 'r')
    not_reachedEOL = True

    while not_reachedEOL:
        restaurant=[]
        line = openFile.readline()
        while line != '\n':
            if line == '':
                not_reachedEOL = False
                break
            else:
                restaurant.append(line.rstrip())
                line = openFile.readline()
        name_to_rating[restaurant[0]]=restaurant[1]
        price_to_names[restaurant[2]]=price_to_names[restaurant[2]]+[restaurant[0]]
        cuisines = restaurant[3].split(',')
        for meal in cuisines:
            if meal in cuisine_to_names:
                cuisine_to_names[meal] = cuisine_to_names[meal]+[restaurant[0]]
            else:
                cuisine_to_names[meal] = [restaurant[0]]
                
    openFile.close()
    
    return name_to_rating, price_to_names, cuisine_to_names

a,b,c = read_restaurants('restaurants_large.txt')
print(a)
print()
print(b)
print()
print(c)


