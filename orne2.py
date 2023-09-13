def bestill_ørnesafari():
    # Spør etter antall personer
    while True:
        try:
            antallPersoner = int(input("Hvor mange personer skal på tur? "))
            if antallPersoner > 0:
                break
            else:
                print("Antall personer må være over 0")
        except ValueError:
            print("Du må taste inn et tall")

    # Beregn behovet for antall båter, en båt tar maks 30 personer
    antallBater = (antallPersoner - 1) // 30 + 1

    # Beregn pris
    pris = antallPersoner * 200 + antallBater * 4000

    # Sjekk om prisen er over 6000
    if pris > 6000:
        # Regn ut rabatt og ny pris
        pris = pris - (pris - 6000) * 0.2

    # Skriv ut prisen til skjerm
    print(f"Prisen for turen er {pris} kroner")
    print("Takk for bestillingen")

def main():
    while True:
        # Meny, spør om bestilling eller avslutt
        print("1: Legg inn bestilling for ørnesafari")
        print("0: Avslutt")
        try:
            svar = int(input("Svar: "))
        except ValueError:
            svar = -1

        if svar == 0:
            break
        elif svar == 1:
            bestill_ørnesafari()
        else:
            print("Ugyldig valg")

if __name__ == "__main__":
    main()
