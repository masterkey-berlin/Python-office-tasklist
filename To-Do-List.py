#Funktion zum Hinzufügen von Aufgaben

to_do_list = []


def add_item():
    task = input ("Bitte gib eine Aufgabe ein, die in deiner Aufgabenliste hinzugefügt werden soll")
    to_do_list.append(task)
    print(f"Die Aufgabe {task} wurde der Liste hinzugefügt")
    
def show_to_do_list():
    if to_do_list:
        print("Deine Aufgabenliste:")
        for task in to_do_list:
            print(task)
    else:       
        print("Aufgabenliste ist leer")

def main():

    while True:
        print("\n --- to_do_list ---")
        print("1. Aufgabe hinzufügen")
        print("2. To-Do-Liste anzeigen")
        print("3. Programm beenden ")
        choice = input("Bitte fügen Sie eine Aufgabe hinzu: \n")

        if choice == "1": 
            print("Sie haben task 1 gewählt!")
            add_task()
        elif choice == "2":
             print("Sie haben task 2 gewählt") 
            show_to-do-list()
        elif choice == "3":
            print("Bis zum nächsten mal!")
        break 

        else:
            print("Bitte wählen Sie zwischen Task 1. 2 oder 3!") 

    main()

    if __name__ == "__name__":
        main()


                   