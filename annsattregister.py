#START
#Initialiser en dictionary som lagrer ansatte
#VIS meny til brukeren
#MENS brukeren ikke velger "Avslutt"
#HVIS brukeren velger "Legg inn ny ansatt"
#SPØRR fornavn, etternavn, stillingstittel, og avdeling
#LAGRE den nye ansatten
#ELLERS HVIS brukeren velger "Rediger ansatt"
#SPØRR hvilken ansatt de vil redigere
#SPØRR hva de vil endre
#OPPDATER ansattens informasjon
#ELLERS HVIS brukeren velger "Slett ansatt"
#SPØRR hvilken ansatt de vil slette
#SLETT den ansatten
#ELLERS HVIS brukeren velger "List ut alle ansatte"
#VIS alle ansatte
#ELLERS HVIS brukeren velger "Avslutt"
#AVSLUTT programmet
#SLUTT

def show_menu():
    print("""
    1. Legg inn ny ansatt
    2. Rediger ansatt
    3. Slett ansatt
    4. List ut alle ansatte
    5. Avslutt
    """)

def add_employee(employees):
    fornavn = input("Fornavn: ")
    etternavn = input("Etternavn: ")
    stillingstittel = input("Stillingstittel: ")
    avdeling = input("Avdeling: ")

    employees[f'{fornavn} {etternavn}'] = {
        "fornavn": fornavn,
        "etternavn": etternavn,
        "stillingstittel": stillingstittel,
        "avdeling": avdeling
    }

def edit_employee(employees):
    name = input("Hvilken ansatt vil du redigere? (Fornavn Etternavn): ")
    if name in employees:
        options = ["fornavn", "etternavn", "stillingstittel", "avdeling"]
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option.capitalize()}")

        choice = int(input("Hva vil du endre? "))
        if 0 < choice <= 4:
            employees[name][options[choice-1]] = input(f"Ny {options[choice-1]}: ")
        else:
            print("Ugyldig valg")
    else:
        print("Ansatte ikke funnet.")

def delete_employee(employees):
    name = input("Hvilken ansatt vil du slette? (Fornavn Etternavn): ")
    employees.pop(name, print("Ansatte slettet."))

def list_employees(employees):
    for employee in employees.values():
        print(f"{employee['fornavn']} {employee['etternavn']}, Stilling: {employee['stillingstittel']}, Avdeling: {employee['avdeling']}")

def main():
    employees = {}

    actions = [add_employee, edit_employee, delete_employee, list_employees]

    while True:
        show_menu()
        choice = int(input("Velg en handling: "))

        if 0 < choice <= 4:
            actions[choice-1](employees)
        elif choice == 5:
            break
        else:
            print("Ugyldig valg.")

if __name__ == "__main__":
    main()