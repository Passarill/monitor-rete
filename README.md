# monitor-rete

Script Python che verifica se una lista di server risponde in rete tramite ping e registra l'esito in un file di log con data e ora. L'ho realizzato per esercitarmi sui concetti di base del monitoraggio di rete, come quello svolto in una control room.

## Come è fatto

- `monitor.py`: il programma Python che esegue i ping e scrive il log.
- `Dockerfile`: le istruzioni per costruire l'immagine Docker, partendo da Python su Alpine Linux.
- `.github/workflows/pipeline.yml`: la pipeline di GitHub Actions, che a ogni push controlla il codice Python, costruisce l'immagine ed esegue il container.

## Come si usa

Serve Docker installato. Dalla cartella del progetto:

```
docker build -t monitor-rete .
docker run -v $(pwd):/app monitor-rete
```

Il primo comando costruisce l'immagine, il secondo esegue il programma in un container. L'opzione `-v` collega la cartella del progetto al container, così il file `log.txt` resta salvato sul computer.

## Limiti noti

- Su GitHub Actions il programma segnala tutti i server come non raggiungibili: la rete delle macchine di GitHub blocca il ping (protocollo ICMP) tramite firewall. L'esito dipende quindi dalla rete in cui il programma gira.
- Il programma termina sempre con codice di uscita 0, anche quando un server non risponde, e per questo la pipeline risulta sempre superata. Un possibile sviluppo è restituire un codice di errore quando un server non è raggiungibile.
