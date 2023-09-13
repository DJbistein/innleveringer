def input_antall_personer():
    """Spør brukeren om antall personer og returnerer dette som en int."""
    while True:
        try:
            antallPersoner = int(input("Hvor mange personer skal på tur? "))
            if antallPersoner > 0:
                return antallPersoner
            else:
                print("Antall personer må være over 0")
        except ValueError:
            print("Du må taste inn et tall")

def beregn_bater(antallPersoner):
    """Returnerer antall nødvendige båter basert på antall personer."""
    return (antallPersoner - 1) // 30 + 1

def beregn_pris(antallPersoner, antallBater):
    """Beregner pris basert på antall personer og båter."""
    pris = antallPersoner * 200 + antallBater * 4000
    if pris > 6000:
        pris = pris - (pris - 6000) * 0.2
    return pris

def skriv_ut_pris(pris):
    """Skriver ut prisen til skjerm."""
    print(f"Prisen for turen er {pris} kroner")
    print("Takk for bestillingen")

def bestill_ørnesafari():
    antallPersoner = input_antall_personer()
    antallBater = beregn_bater(antallPersoner)
    pris = beregn_pris(antallPersoner, antallBater)
    skriv_ut_pris(pris)

def hovedmeny():
    """Hovedmenyen for programmet."""
    while True:
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
    hovedmeny()
