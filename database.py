import sqlite3

conn = sqlite3.connect("./fazenda.db") # confira se o seu diretório está correto
cursor = conn.cursor()

createTable = """
  CREATE TABLE Vaca (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ordenhada TEXT CHECK (ordenhada IN ('S','N')) NOT NULL DEFAULT 'M',
    ult_ordenha TEXT default NULL,
    data_cadastro TEXT NOT NULL
  );
"""

cursor.execute(createTable)

conn.commit()
cursor.close()
conn.close()