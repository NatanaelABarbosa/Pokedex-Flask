import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='N4ellean.'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `pokedex`;")

cursor.execute("CREATE DATABASE `pokedex`;")

cursor.execute("USE `pokedex`;")

# criando tabelas
TABLES = {}
TABLES['Pokemon'] = ('''
      CREATE TABLE `pokemon` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `tipo` varchar(15) NOT NULL,
      `abilidade` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Status'] = ('''
      CREATE TABLE `pokemon_status` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `pokemon_id` int(11) NOT NULL,
      `hp` int(3) NOT NULL,
      `atk` int(3) NOT NULL,
      `def` int(3) NOT NULL,
      `spatk` int(3) NOT NULL,
      `spdef` int(3) NOT NULL,
      `spd` int(3) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`pokemon_id`) REFERENCES `pokemon`(`id`) ON DELETE CASCADE
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Treinadores'] = ('''
      CREATE TABLE `Treinadores` (
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')
            
# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()