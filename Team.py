# A team is a couple.  Each team will have one or two names and a number.

class Team:
    def __init__ (self, number, names):
        self.number = number
        self.names = names
        self.opponent = None
        self.previousOpponents = []

def main():
    t = Team(1, ["Greg", "Pam"])
    print ("Team::main", t.number, t.names)

if __name__=="__main__":
    main()

    
