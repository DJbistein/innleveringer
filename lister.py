def hent_brukerdata():
    return [("jostein", "pass")]

def logg_inn():
    print("Logg inn:")
    brukernavn = input("Skriv inn brukernavn: ")
    passord = input("Skriv inn passord: ")

    brukerliste = hent_brukerdata()

    if (brukernavn, passord) in brukerliste:
        print("Innlogging vellykket!")
    else:
        print("Innlogging mislyktes. Feil brukernavn eller passord.")

if __name__ == "__main__":
    logg_inn()
