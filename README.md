# PickMotivationalQuotes



Questo Script cambia ogni giorno, il messaggio MOTD (Message Of The Day ) presente sul blog goldenbyte.it ( lo script gira a 0:00 tramite cron)
Il DB  in formato ExCel è stato recuperato da https://sharpquotes.com/ e poi è stato importato in un DB su MariaDB presente in un container docker privato.

La struttura del DB è la seguente:

Field | Type | Null | Key | Default | Extra
----- | ---- | ---- | ----|---------|------
Quotes |  mediumtext   | YES  |     | NULL                  
Author | varchar(255) | YES  |     | NULL    
Category | varchar(255) | YES  |     | NULL    
ID | int(11)      | NO   | PRI | NULL    | auto_increment

La LandingPage del Blog ( anchessa in un container)  ha un inclusione di due sottopagine che sono condivise con l'host e che vengono sovrascritte da questo script

 -  quotes.html
 -  author.html
 
 Al termine della scrittura poi il DB viene chiuso e il container del BLOG viene restartato per applicare le modifiche
