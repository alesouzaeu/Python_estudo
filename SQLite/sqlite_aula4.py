import sqlite3


nome = "Juliana"

idade = 28

email = "juliana@gmail.com"


banco = sqlite3.connect('primeiro_banco.db') #objeto de conexão com o banco

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")


cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')")

banco.commit()


""" cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) """


