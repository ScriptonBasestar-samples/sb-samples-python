import pypyodbc


connection = pypyodbc.connect('Driver = {SQL Server};' 'Server=ipipipipipdomain;' 'Database=dbdbdbnamanamer;' 'uid=ussserrrname;pwd=padsssword')
connection.close()

cursor = connection.cursor()
SQLCommand = ("INSERT INTO Customers "
                "(firstName, lastName, city) "
                "VALUES (?,?,?)")
Values = ['Susan','Ibach','Toronto']
cursor.execute(SQLCommand,Values)
connection.commit()
connection.close()

