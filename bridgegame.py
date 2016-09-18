import csv
import os
import random
import Team
import Table

def main():
    names = ["Chuck Alexander", "Shirley Alexander", "Dolores Bertrand", "Bob Bertrand", "Pam Bianchi", "Selwyn Edwards", "Anita Bittle", "Ray Bittle", "Barbara Calkins", "Ken Calkins", "Shirley Coen", "Mike Coen", "Ann Cornick", "Janet Graham", "Janay Downing", "Gail Reynolds", "Kathryn Elisha", "Norma Shuette", "Mary Fike", "Norma Whitney", "Jean Frazier", "Jan Sangster", "Janie Hawkins", "Jim Hawkins", "Betty Holling", "Doug Holling", "Diane Peck", "Henry Weibler", "Dick Radow", "Phil Steekley", "TBD", "TBD"]
    teams = {}
#    numMonths = 1
    numMonths = 6
    filename = "bridgegame.csv"

    for i in range(0, len(names), 2):
        t = Team.Team(i/2+1, names[i:i+2])
        print (t.number, t.names)
        teams[t.number] = t

        print (teams)

    if (os.path.isfile(filename)):
        os.remove(filename)
    writeFileHeader (filename)
    games = []
    for i in range(0, numMonths):
        tables = matchTeams (teams)
        randomTables = randomizeTables (tables)
        games.append (randomTables)
        writeFile (filename, i+1, randomTables)
#    writeFile (games)

#        for team in teams.values():
#            print (team.number, team.names, team.opponent)

def matchTeams (teams):
    unmatchedTeams = teams.copy()
    matchedTeams = []
    tableTeamList = []
    tables = {}
    print (unmatchedTeams)
    for teamNumber in teams.keys():
        if not (teamNumber in unmatchedTeams.keys()): continue
        untriedTeams = unmatchedTeams.copy()
        team = teams[teamNumber]
        print ("teamNumber: ", teamNumber, ", previousOpponents: ", team.previousOpponents)
        while True:
            i = random.randint (0, len(untriedTeams)-1)
            print ("untriedTeams: ", untriedTeams.keys())
            print ("Trying: ", i)
            testTeamNumber = untriedTeams.keys()[i]
            testTeam = teams[testTeamNumber]
            print ("TestTeamNumber: ", testTeamNumber, ", previousOpponents: ", testTeam.previousOpponents)
            del untriedTeams[testTeamNumber]
            if testTeamNumber == teamNumber: continue
            if (not testTeamNumber in team.previousOpponents):
                team.opponent = testTeamNumber
                if not team.opponent in team.previousOpponents:
                    team.previousOpponents = team.previousOpponents + [team.opponent]
                testTeam.opponent = team.number
                if not testTeam.opponent in testTeam.previousOpponents:
                    testTeam.previousOpponents = testTeam.previousOpponents + [team.number]
                matchedTeams.append (team.number)
                matchedTeams.append (testTeamNumber)
                if not team.number in tableTeamList:
                    tableTeamList.append (team.number)
                    if not team.opponent in tableTeamList:
                        tableTeamList.append (team.opponent)
                    retTable = Table.Table()
                    retTable.addTeam (team)
                    retTable.addTeam (teams[testTeamNumber])
                    tables[len(tables)] = retTable
                del unmatchedTeams[team.number]
                del unmatchedTeams[testTeamNumber]
                print ("unmatchedTeams: ", unmatchedTeams)
                print ("matchedTeams: ", matchedTeams)
                print ("tableTeamList: ", tableTeamList)
                break

    print ("matchedTeams: ", matchedTeams)
    print ("teams: ", teams)
    print ("tableTeamList: ", tableTeamList)
    for team in teams.values():
        print (team.names, " <=> ", teams[team.opponent].names)
    return tables

def randomizeTables (tables):
    print ("randomizeTables()")
    randomizedTables = {}
    unusedTables = tables.copy()
    for x in range(len(tables)):
        i = random.randint (0, len(unusedTables)-1)
        key = unusedTables.keys()[i]
        print ("i: ", i, "key: ", key, "keys: ", unusedTables.keys())
        randomizedTables[len(randomizedTables)+1] = unusedTables[key]
        del unusedTables[key]
    print ("randomizedTables: ", randomizedTables.keys())
    return randomizedTables

def writeFileHeader (filename):
    with open(filename, 'ab') as csvfile:
        csvwriter = csv.writer (csvfile, delimiter=',', quotechar='"',)
        row = ['game', 'table', 'team', 'players', 'team', 'players']
        csvwriter.writerow (row)

#def writeFile (games):
#    with open('bridgegame.csv', 'wb') as csvfile:
def writeFile (filename, gamecount, game):
#    with open('bridgegame.csv', 'wb') as csvfile:
    with open(filename, 'ab') as csvfile:
        csvwriter = csv.writer (csvfile, delimiter=',', quotechar='"',)
#        gamecount = 0
#        for game in games:
#            gamecount += 1
#        header = ["Game " + str(gamecount)]
#        csvwriter.writerow (header)
        for key in game.keys():
            table = game[key]
            row = []
            row.append (str(gamecount))
            row.append (str(key))
            for team in table.teams:
                row.append (team.number)
                row.append (" & ".join(team.names))
            csvwriter.writerow (row)
        csvwriter.writerow([])

if __name__ == "__main__":
    main()
