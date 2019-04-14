#enconding:utf-8
from itertools import combinations
teams = ["Packers", "reset", "Ravens", "Patrions"]

for game in combinations(teams, 2):
    print(game)


teams = ["Packers", "reset", "Ravens", "paration"]
print(", ".join(teams))

teams = ["Packers", "reset", "Ravens", "paration"]
print({key: value for value, key in enumerate(teams)})

teams = ["Packers", "reset", "Ravens", "paration"]
for index, team in enumerate(teams):
    print(index, team)