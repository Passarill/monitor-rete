import subprocess
import datetime

indirizzi = ['8.8.8.8' , '1.1.1.1']

for indirizzo in indirizzi :

 risultato = subprocess.run (['ping', '-c' , '1' , indirizzo], capture_output=True)

 ora = datetime.datetime.now()

 with open ('log.txt' , 'a') as file: 



  if risultato.returncode == 0 :

      print (f'{indirizzo} il server risponde')

      file.write(f'{ora} {indirizzo} il server risponde\n')
     
     

  else :

      print (f'{indirizzo} il server non risponde')

      file.write(f'{ora} {indirizzo} il server non risponde\n')
