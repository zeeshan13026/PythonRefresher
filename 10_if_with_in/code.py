movies_watched = {'The Matrix', 'Rambo', 'Green book', 'Her'}
user_movie = input(" Enter your movies : ")

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too")
else:
    print(f"I haven't watched this movie")