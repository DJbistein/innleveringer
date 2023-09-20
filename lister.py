def hent_brukerdata():
    # Returnerer en liste med tupler (brukernavn, passord)
    return [("jostein", "pass")]

def legg_til_bruker(brukernavn, passord, brukerliste):
    # Legger til en ny bruker til brukerlisten
    brukerliste.append((brukernavn, passord))
    return brukerliste

def slett_bruker(brukernavn, brukerliste):
    # Sletter en bruker fra brukerlisten
    brukerliste = [bruker for bruker in brukerliste if bruker[0] != brukernavn]
    return brukerliste

def vis_brukernavn():
    brukerliste = hent_brukerdata()
    print("Brukernavn i systemet:")
    for bruker in brukerliste:
        print(bruker[0])

def logg_inn():
    print("Logg inn:")
    brukernavn = input("Skriv inn brukernavn: ")
    passord = input("Skriv inn passord: ")

    brukerliste = hent_brukerdata()

    if (brukernavn, passord) in brukerliste:
        print("Innlogging vellykket!")
        svar = input("Ønsker du å slette din bruker? (ja/nei) ")
        if svar.lower() == "ja":
            brukerliste = slett_bruker(brukernavn, brukerliste)
            print("Brukeren ble slettet.")
    else:
        print("Innlogging mislyktes. Feil brukernavn eller passord.")
        svar = input("Ønsker du å opprette en ny konto? (ja/nei) ")
        if svar.lower() == "ja":
            if any(bruker[0] == brukernavn for bruker in brukerliste):
                print("Brukernavnet eksisterer allerede. Velg et annet brukernavn.")
            else:
                brukerliste = legg_til_bruker(brukernavn, passord, brukerliste)
                print("Ny bruker opprettet!")

if __name__ == "__main__":
    logg_inn()
    vis_brukernavn()
