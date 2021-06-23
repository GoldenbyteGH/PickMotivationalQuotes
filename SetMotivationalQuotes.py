#!/usr/bin/python3


"""
Questo Script cambia ogni giorno, il messaggio MOTD (Message Of The Day ) presente sul blog goldenbyte.it ( lo script gira a 0:00 tramite cron)
Il DB  in formato ExCel è stato recuperato da https://sharpquotes.com/ e poi è stato importato in un DB su MariaDB presente in un container docker privato.

MotQuotes:

+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| Quotes   | mediumtext   | YES  |     | NULL    |                |
| Author   | varchar(255) | YES  |     | NULL    |                |
| Category | varchar(255) | YES  |     | NULL    |                |
| ID       | int(11)      | NO   | PRI | NULL    | auto_increment |
+----------+--------------+------+-----+---------+----------------+


La LandingPage del Blog ( anchessa in un container)  ha un inclusione di due sottopagine che sono condivise con l'host e che vengono sovrascritte da questo script

 -  quotes.html
 -  author.html
 
 Al termine della scrittura poi il DB viene chiuso e il container del BLOG viene restartato per applicare le modifiche

"""
import mysql.connector
import configparser
import os,sys,random

#Inizializzo la lista di categorie che mi interessano e l'indice della riga nella tabella

RangeIndex = []			#Lista degli indici da cui verrà pecsato il quote causale 
Categories = ['change','computers','courage','failure','fear','inspirational','learning']


# Connect to MariaDB Platform

config = configparser.ConfigParser()
config.read('config.ini')                       #Read Credentials of DB

try:
    conn = mysql.connector.connect(
        user=config['mariaDB']['user'],
        password=config['mariaDB']['psw'],
        host=config['mariaDB']['host'],
        database=config['mariaDB']['db'])

except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


# Get Cursor
cur = conn.cursor()

#Scelgo una categoria causale dalla lista
RandomCategory = random.choice(Categories)

#Creo la query in base alla categoria scelta
#Per selezionare un quote a caso in base alla categoria scelta ( anch'essa così a caso ), scelgo un numero compreso tra l'ID della FIRST_ROW e della LAST_ROW ottenuta tramite la seguente UNION 

query = ('(SELECT ID FROM MotQuotes WHERE Category =  "'+RandomCategory+'" order by ID ASC LIMIT 1)UNION(SELECT ID FROM MotQuotes WHERE Category =  "'+RandomCategory+'" order by ID DESC LIMIT 1)')

# eseguo la prima query
cur.execute(query)
myresult = cur.fetchall()

for x in myresult:
  RangeIndex.append(x[0])

#Scelgo a caso l'ID del quote tra il range in RangeIndex
IDQuote = random.randint(RangeIndex[0],RangeIndex[1])


# eseguo la seconda query
query = 'SELECT Quotes,Author FROM MotQuotes WHERE ID = '+str(IDQuote)
cur.execute(query)
myresult = cur.fetchall()


#Scrivo  su file
f_quote  = open("quotes.html", "w")
f_author = open("author.html", "w")
f_quote.write(str(myresult[0][0]))
f_author.write(str(myresult[0][1]))
f_quote.close()
f_author.close()

# Chiudo connessione al DB
cur.close()
conn.close()

# Restarto il container per refreshare la lendingpage del Blog
os.system('docker restart Goldenblog')
