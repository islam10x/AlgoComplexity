import random


class Team:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


def test(N):
    #Check if N is a power of 2.
    if N==1:
        return False
    while N % 2 == 0:
        N //= 2
    return N == 1


def initialize_teams():
    #Initialize teams with names and random strengths.
    while True:
        N = int(input("Enter the number of teams (must be a power of 2): "))
        if test(N):
            break
        print("Invalid input! Please enter a power of 2.")

    teams = []
    for i in range(1, N + 1):
        team = Team(f"T{i}", random.randint(1, 100))
        teams.append(team)

    return teams


def simulate_match(T1, T2):
    #Simulate a match between two teams based on random chance and strength.
    rand = random.randint(1, 100)
    print("Number generated is :",rand)
    if 40 <= rand <= 60:
        print("Weaker Team Wins!")
        return T2 if T1.strength < T2.strength else T1
    else:
        print("Strong Team Wins!")
        return T1 if T1.strength > T2.strength else T2


def simulate_round(teams):
    #Simulate a round of matches and return the winners.
    winners = []
    N = len(teams)
    print("round of ", N)
    for i in range(N // 2):
        print(teams[i].name,"(",teams[i].strength,")","VS", teams[N-1-i].name,"(",teams[N-1-i].strength,")")
        winner = simulate_match(teams[i], teams[N - 1 - i])
        winners.append(winner)
    return winners
def Displayteams(teams):
    N=len(teams)
    for i in range(N):
        print(teams[i].name,"(",teams[i].strength,")","VS",teams[N-1-i].name,"(",teams[N-1-i].strength,")")

def champions_league():
    #Run the tournament until one team remains.
    teams = initialize_teams()
    while len(teams) > 1:
        Displayteams(teams)
        teams = simulate_round(teams)
    print("The champion is:", teams[0].name)


# Run the tournament
champions_league()
