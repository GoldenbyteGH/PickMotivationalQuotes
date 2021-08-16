# PickMotivationalQuotes



This Script sets every day the MOTD (Message Of The Day) on the goldenbyte.it blog (the script runs at 0:00 via cron). 
The DB  (ExCel format )has been retrieved from https://sharpquotes.com/ and then it was imported into a MariaDB installed private docker container.

MotQuotes:

Field | Type | Null | Key | Default | Extra
----- | ---- | ---- | ----|---------|------
Quotes |  mediumtext   | YES  |     | NULL                  
Author | varchar(255) | YES  |     | NULL    
Category | varchar(255) | YES  |     | NULL    
ID | int(11)      | NO   | PRI | NULL    | auto_increment

The Blog's Page has two inclusions of subpages which are shared with the host. 

 -  quotes.html
 -  author.html
 
At the end , the script close everythingd and restart the Blog's container to apply the changes. 
