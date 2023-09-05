# Program for bestilling av ørnesafari 

 
 

# Spør etter antall personer 

antall = int(input("Hvor mange skal på tur: ")) 

# antall = int(antall) 

 
 

# Sjekk om antall personer er over 30 

# Hvis antall er over 30 

if antall > 30: 

     # Skriv ut melding til skjerm om maks antall 

     print ("Det er for mange personer, båten tar maks 30") 

# Ellers sett at antall båter er 1 

else: 

    antallbater = 1 

    # Beregn pris 

    pris = (200*antall) + 4000 

    # Sjekk om prisen er over 6000 

    if pris > 6000: 

        pris = pris - pris * 20/100 

        # pris = pris * 0.8 

        #Regn ut rabatt og ny pris 

        print("Du får rabatt") 

 
 

    # Skriv ut prisen til skjerm 

    print(f'Prisen for turen er kr: {pris}') 