import Table
# A group is a group of tables.  There will always be two tables in a group.
class Group:
    def __init__(self):
        self.tables = []

    def addTable (self, table):
        self.tables.append (table)

def main():
    print ("Group::main")
    g = Group()
    table = Table.Table()
    table2 = Table.Table()
    g.addTable (table)
    g.addTable (table2)
    print ("Tables: ", g.tables)

if __name__=="__main__":
    main()
