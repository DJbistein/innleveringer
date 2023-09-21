def hent_brukerdata():
    # Returnerer en dictionary med brukernavn som nøkkel og passord som verdi
    return {"jostein": "pass"}

def legg_til_bruker(brukernavn, passord, brukerdata):
    # Legger til en ny bruker til brukerdata
    brukerdata[brukernavn] = passord

def slett_bruker(brukernavn, brukerdata):
    # Sletter en bruker fra brukerdata
    if brukernavn in brukerdata:
        del brukerdata[brukernavn]

def vis_brukernavn():
    brukerdata = hent_brukerdata()
    print("Brukernavn i systemet:")
    for brukernavn in brukerdata:
        print(brukernavn)

def logg_inn():
    print("Logg inn:")
    brukernavn = input("Skriv inn brukernavn: ")
    passord = input("Skriv inn passord: ")

    brukerdata = hent_brukerdata()

    if brukernavn in brukerdata and brukerdata[brukernavn] == passord:
        print("Innlogging vellykket!")
        svar = input("Ønsker du å slette din bruker? (ja/nei) ")
        if svar.lower() == "ja":
            slett_bruker(brukernavn, brukerdata)
            print("Brukeren ble slettet.")
    else:
        print("Innlogging mislyktes. Feil brukernavn eller passord.")
        svar = input("Ønsker du å opprette en ny konto? (ja/nei) ")
        if svar.lower() == "ja":
            if brukernavn in brukerdata:
                print("Brukernavnet eksisterer allerede. Velg et annet brukernavn.")
            else:
                legg_til_bruker(brukernavn, passord, brukerdata)
                print("Ny bruker opprettet!")

if __name__ == "__main__":
    logg_inn()
    vis_brukernavn()