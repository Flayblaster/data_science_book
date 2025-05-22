from matplotlib import pyplot as plt

movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
num_oscars = [5, 11, 3, 8, 10]

#Plot bars with coordinates x in [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title('My Favorite Movies')
plt.ylabel('# of Academy Awards')

#Rotule axe X with the name from film in center bar
plt.xticks(range(len(movies)), movies)

plt.show()