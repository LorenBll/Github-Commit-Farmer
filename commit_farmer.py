

def main ():
    
    #. inizio del programma
    while True:
        
        # chiedo quanti commit vuole fare
        try:
            numberOf_commits = int(input("Quanti commit vuoi fare? (CANCELOP per annullare): "))
        except:
            print("Inserisci un numero valido")
            continue
        
        if numberOf_commits == "CANCELOP":
            exit()
        elif numberOf_commits <= 0:
            print("Inserisci un numero maggiore di 0")
            continue
        elif numberOf_commits > 1000:
            print("Non puoi fare più di 1000 commit alla volta")
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
            os.system("git push")
        
        else:
            # modifico il file file.txt aggiungendo un carattere
            with open("file.txt", "a") as f:
                f.write("a")
                
        # faccio il commit senza mostrare l'output del terminale
        os.system("git add file.txt")
        os.system(f'git commit -m "{commitMsg}"')
        
    os.system("git push")
    os.system("cls")
    print(f"{numberOf_commits} commit effettuati con successo!")


if __name__ == '__main__':
    main()