import random
import Team
names = ["Chuck Alexander", "Shirley Alexander", "Dolores Bertrand", "Bob Bertrand", "Pam Bianchi", "Selwyn Edwards", "Anita Bittle", "Ray Bittle", "Barbara Calkins", "Ken Calkins", "Shirley Coen", "Mike Coen", "Ann Cornick", "Janet Graham", "Janay Downing", "Gail Reynolds", "Kathryn Elisha", "Norma Shuette", "Mary Fike", "Norma Whitney", "Jean Frazier", "Jan Sangster", "Janie Hawkins", "Jim Hawkins", "Betty Holling", "Doug Holling", "Diane Peck", "Henry Weibler", "Dick Radow", "Phil Steekley", "TBD", "TBD"]
teams = {}
for i in range(0, len(names), 2):
    t = Team.Team(i/2+1, names[i:i+2])
    print (t.number, t.names)
    teams[t.number] = t

print (teams)

unmatchedTeams = teams.copy()
matchedTeams = []
print (unmatchedTeams)
#print ([team.number for team in unmatchedTeams])
for teamNumber in teams.keys():
    if not (teamNumber in unmatchedTeams.keys()): continue
    untriedTeams = unmatchedTeams.copy()
    while True:
        i = random.randint (0, len(untriedTeams)-1)
        print ("untriedTeams: ", untriedTeams.keys())
        print ("Trying: ", i)
        testTeamNumber = untriedTeams.keys()[i]
        print ("TestTeamNumber: ", testTeamNumber)
#        untriedTeams.remove(testTeamNumber)
#        untriedTeams.pop(testTeamNumber)
        del untriedTeams[testTeamNumber]
        if testTeamNumber == teamNumber: continue
        team = teams[teamNumber]
        if (not testTeamNumber in team.previousOpponents):
            team.opponent = testTeamNumber
            matchedTeams.append (team.number)
            matchedTeams.append (testTeamNumber)
            print ("matchedTeams: ", matchedTeams)
            break

print ("matchedTeams: ", matchedTeams)
print ("teams: ", teams)
for team in teams.values():
    print (team.names, " <=> ", teams[team.opponent].names)

