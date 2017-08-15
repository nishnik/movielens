import os
import pandas as pd
BASE_DIR = '.' # Modify this if needed to the local directory that the MovieLens 1M Dataset has been unzipped into. 
MOVIELENS_DIR = BASE_DIR + '/ml-1m/'
USER_DATA_FILE = 'users.dat'
MOVIE_DATA_FILE = 'movies.dat'
RATING_DATA_FILE = 'ratings.dat'


#### read ratings
file_ = open(os.path.join(MOVIELENS_DIR, RATING_DATA_FILE))
user_to_movie = {}
movie_to_user = {}

# Not considering time-stamp
for line in file_.readlines():
    line = line.strip().split('::')
    ## line-> 0: userid, 1:movieid, 2:rating 3:
    line = [int(item) for item in line]
    if (line[0] not in user_to_movie):
        user_to_movie[line[0]] = {}
    # if (line[1] in user_to_movie[line[0]]): # There is no duplication
    #     print ("there is duplication")
    user_to_movie[line[0]][line[1]] = line[2]
    if (line[1] not in movie_to_user):
        movie_to_user[line[1]] = {}
    # if (line[0] in movie_to_user[line[1]]): # There is no duplication
    #     print ("there is duplication")
    movie_to_user[line[1]][line[0]] = line[2]

file_.close()

file_ = open(os.path.join(MOVIELENS_DIR, USER_DATA_FILE))

user_info = {}

# not loading zipcode
for line in file_.readlines():
    line = line.strip().split('::')
    # line -> ['userid', 'gender', 'age', 'occupation', 'zipcode']
    user_info[int(line[0])] = []
    gender = 1 if line[1] == 'M' else 0
    user_info[int(line[0])].append(gender)
    user_info[int(line[0])].append(int(line[2]))
    user_info[int(line[0])].append(int(line[3]))

file_.close()
## We have user_data for every user


file_ = open(os.path.join(MOVIELENS_DIR, MOVIE_DATA_FILE), encoding='latin1')
movie_info = {}

genre_to_index = {'Drama': 6, 'Documentary': 12, 'Western': 17, 'Film-Noir': 16, 'Action': 7, 'Fantasy': 4, 'Comedy': 2, 'War': 13, 'Adventure': 3, 'Horror': 10, 'Thriller': 9, 'Animation': 0, 'Sci-Fi': 11, 'Mystery': 15, 'Crime': 8, 'Romance': 5, 'Musical': 14, "Children's": 1}

for line in file_.readlines():
    line = line.strip().split('::')
    # line -> ['movieid', 'title', 'genre']
    # list form of movie_info for similarity with user_info array
    movie_info[int(line[0])] = []
    for genre in line[2].strip().split('|'):
        movie_info[int(line[0])].append(genre_to_index[genre])

file_.close()


## Some movies are not rated, lets drop them
# >>> len(movie_to_user)
# 3706
# >>> len(movie_info)
# 3883

for movie in list(movie_info.keys()):
    if not movie in movie_to_user:
        print (movie)
        del movie_info[movie]

