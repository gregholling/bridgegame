import Team
# Each table has one or two teams.
class Table:
    def __init__(self):
        self.teams = []
        
    def addTeam (self, team):
        self.teams.append (team)

def main():
    print ("Table::main")
    table = Table()
    table.addTeam(Team.Team(1, ["Greg", "Pam"]))
    table.addTeam(Team.Team(2, ["Carl", "Susan"]))
    print ("Teams: ", table.teams)

if __name__=="__main__":
    main()
