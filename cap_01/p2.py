from collections import Counter, defaultdict

from fontTools.subset import intersect

users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'},
]

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Search with dict is more efficienty than iterar one by one

#Initilize the dict with a empty list for every user id
friendships = {user['id']: [] for user in users}

#Then, execute a loop for each pair, to fill the friendships
for i, j in friendship_pairs:
    friendships[i].append(j) #Append j as a friend of i
    friendships[j].append(i) #Append i as a friend of j

print(friendships)

#What is the average number of connections
def number_of_friends(user):
    user_id = user['id']
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections/num_users
#print(f'Número médio de conexões por usuário: {avg_connections}')

#What users have the bigger number of connections
#Make a list (user_id, number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)

#Friend of a friend

def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user['id']]
            for foaf_id in friendships[friend_id]]
print(f'Amigos dos amigos do usuário [0]: {foaf_ids_bad(users[0])}')

#Solução do problema de amigos já conhecidos
def friends_of_friends(user):
    user_id = user['id']
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )
print(f'Amigos dos amigos do usuário [3]: {friends_of_friends(users[3])}')

interests = [
    (0, 'Hadoop'), (0, 'Big Data'), (0, 'HBase'), (0, 'Java'),
    (0, 'Spark'), (0, 'Storm'), (0, 'Cassandra'),
    (1, 'Postgres'), (1, 'MongoDB'), (1, 'Cassandra'), (1, 'HBase'),
    (1, 'NoSQL'), (2, 'Python'), (2, 'scikit-learn'), (2, 'scipy'),
    (2, 'numpy'), (2, 'statsmodels'), (2, 'pandas'), (3, 'R'), (3, 'Python'),
    (3, 'statistics'), (3, 'regression'), (3, 'probability'),
    (4, 'machine learning'), (4, 'regression'), (4, 'decision trees'),
    (4, 'libsvm'), (5, 'Python'), (5, 'R'), (5, 'Java'), (5, 'C++'),
    (5, 'Haskell'), (5, 'Programming languages'), (6, 'statistics'),
    (6, 'probability'), (6, 'mathematics'), (6, 'theory'),
    (7, 'machine learning'), (7, 'scikit-learn'), (7, 'Mahout'),
    (7, 'neural networks'), (8, 'neural networks'), (8, 'deep learning'),
    (8, 'Big Data'), (8, 'artificial intelligence'), (9, 'Hadoop'),
    (9, 'Java'), (9, 'MapReduce'), (9, 'Big Data')
]

#Users with the same interests
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

print(f'Cientistas de dados que gostam de Python: {data_scientists_who_like('Python')}')

#The keys are the interests, values is lists of users_ids with the same interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
print(f'Id de usuários por interesse: {user_ids_by_interest}')

#The key are user_ids, the values is a list of user interest
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
print(f'Interesses dos usuários: {interests_by_user_id}')

#The final solution
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user['id']]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user['id']
    )
print(f'Pessoas com os mesmo interesse do usuário [0]: {most_common_interests_with(users[0])}')