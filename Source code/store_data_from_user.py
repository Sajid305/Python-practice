
                                    # Store data from user
user = {}

name = input('enter your name : ')
age = input('enter your age : ')
fev_movies = input('enter your fev movies separated by comma : ').split(',')
fev_song = input('enter your fev song separated by comma : ').split(',')

user['name'] = name
user['age'] = age
user['fev_movies'] = fev_movies
user['fev_song'] = fev_song

for key,value in user.items():
    print(f'{key} : {value}')