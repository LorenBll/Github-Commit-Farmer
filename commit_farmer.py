

def main ():
    
    #. inizio del programma
    while True:
        
        # chiedo quanti commit vuole fare
        numberOf_commits = int(input("Quanti commit vuoi fare? (CANCELOP per annullare): "))
        
        if numberOf_commits == "CANCELOP":
            exit()
        elif numberOf_commits <= 0:
            print("Inserisci un numero maggiore di 0")
            continue
        else:
            break
            
    while True:
        
        # chiedo il messaggio
        commitMsg = input("Inserisci il messaggio del commit (premi INVIO per usare il messaggio di default): ")
        
        if commitMsg == "":
            commitMsg = "Aggiornamento"
            break
        elif len(commitMsg) > 50:
            print("Il messaggio non può superare i 50 caratteri")
            continue
        else:
            break
        
    #. creazione dei commit
    import os
    
    for i in range(numberOf_commits):
        
        # quando arrivo al 10° commit, pulisco il file
        if i % 10 == 0:
            with open("file.txt", "w") as f:
                f.write("")
        
        else:
            # modifico il file file.txt aggiungendo un carattere
            with open("file.txt", "a") as f:
                f.write("a")
                
        # faccio il commit
        os.system("git add file.txt")
        os.system(f'git commit -m "{commitMsg}"')
        os.system("git push")
        
        print(f"Commit {i+1}/{numberOf_commits} effettuato con successo!")
        
    print(f"{numberOf_commits} commit effettuati con successo!")


if __name__ == '__main__':
    main()