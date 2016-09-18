import random
import Team

def main():
    names = ["Chuck Alexander", "Shirley Alexander", "Dolores Bertrand", "Bob Bertrand", "Pam Bianchi", "Selwyn Edwards", "Anita Bittle", "Ray Bittle", "Barbara Calkins", "Ken Calkins", "Shirley Coen", "Mike Coen", "Ann Cornick", "Janet Graham", "Janay Downing", "Gail Reynolds", "Kathryn Elisha", "Norma Shuette", "Mary Fike", "Norma Whitney", "Jean Frazier", "Jan Sangster", "Janie Hawkins", "Jim Hawkins", "Betty Holling", "Doug Holling", "Diane Peck", "Henry Weibler", "Dick Radow", "Phil Steekley", "TBD", "TBD"]
    teams = {}
    numMonths = 1
#    numMonths = 6
    for i in range(0, len(names), 2):
        t = Team.Team(i/2+1, names[i:i+2])
        print (t.number, t.names)
        teams[t.number] = t

        print (teams)

    for i in range(0, numMonths):
        matchTeams (teams)
        for team in teams.values():
            print (team.number, team.names, team.opponent)

def matchTeams (teams):
    unmatchedTeams = teams.copy()
    matchedTeams = []
    print (unmatchedTeams)
    for teamNumber in teams.keys():
        if not (teamNumber in unmatchedTeams.keys()): continue
        untriedTeams = unmatchedTeams.copy()
        while True:
            i = random.randint (0, len(untriedTeams)-1)
            print ("untriedTeams: ", untriedTeams.keys())
            print ("Trying: ", i)
            testTeamNumber = untriedTeams.keys()[i]
            print ("TestTeamNumber: ", testTeamNumber)
            del untriedTeams[testTeamNumber]
            if testTeamNumber == teamNumber: continue
            team = teams[teamNumber]
            if (not testTeamNumber in team.previousOpponents):
                team.opponent = testTeamNumber
                teams[testTeamNumber].opponent = team.number
                matchedTeams.append (team.number)
                matchedTeams.append (testTeamNumber)
                del unmatchedTeams[team.number]
                del unmatchedTeams[testTeamNumber]
                print ("unmatchedTeams: ", unmatchedTeams)
                print ("matchedTeams: ", matchedTeams)
                break

    print ("matchedTeams: ", matchedTeams)
    print ("teams: ", teams)
    for team in teams.values():
        print (team.names, " <=> ", teams[team.opponent].names)

if __name__ == "__main__":
    main()
