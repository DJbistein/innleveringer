from pymongo import MongoClient

# Database setup
client = MongoClient('localhost', 27017)  
db = client['employee_database']  
employees_collection = db['employees']  

def show_menu():
    print("""
    1. Legg inn ny ansatt
    2. Rediger ansatt
    3. Slett ansatt
    4. List ut alle ansatte
    5. Avslutt
    """)

def add_employee():
    fornavn = input("Fornavn: ")
    etternavn = input("Etternavn: ")
    stillingstittel = input("Stillingstittel: ")
    avdeling = input("Avdeling: ")

    employee = {
        "fornavn": fornavn,
        "etternavn": etternavn,
        "stillingstittel": stillingstittel,
        "avdeling": avdeling
    }
    
    employees_collection.insert_one(employee)

def edit_employee():
    name = input("Hvilken ansatt vil du redigere? (Fornavn Etternavn): ")
    fornavn, etternavn = name.split()
    
    employee = employees_collection.find_one({"fornavn": fornavn, "etternavn": etternavn})
    
    if employee:
        options = ["fornavn", "etternavn", "stillingstittel", "avdeling"]
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option.capitalize()}")

        choice = int(input("Hva vil du endre? "))
        if 0 < choice <= 4:
            new_value = input(f"Ny {options[choice-1]}: ")
            employees_collection.update_one({"fornavn": fornavn, "etternavn": etternavn}, {"$set": {options[choice-1]: new_value}})
        else:
            print("Ugyldig valg")
    else:
        print("Ansatte ikke funnet.")

def delete_employee():
    name = input("Hvilken ansatt vil du slette? (Fornavn Etternavn): ")
    fornavn, etternavn = name.split()
    
    result = employees_collection.delete_one({"fornavn": fornavn, "etternavn": etternavn})
    
    if result.deleted_count > 0:
        print("Ansatte slettet.")
    else:
        print("Ansatte ikke funnet.")

def list_employees():
    for employee in employees_collection.find():
        print(f"{employee['fornavn']} {employee['etternavn']}, Stilling: {employee['stillingstittel']}, Avdeling: {employee['avdeling']}")

def main():
    actions = [add_employee, edit_employee, delete_employee, list_employees]

    while True:
        show_menu()
        choice = int(input("Velg en handling: "))

        if 0 < choice <= 4:
            actions[choice-1]()
        elif choice == 5:
            break
        else:
            print("Ugyldig valg.")

if __name__ == "__main__":
    main()


