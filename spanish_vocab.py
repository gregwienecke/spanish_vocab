import random
import os

words = {
    "Segun": "According to",
    "Sobre": "About",
    "Acerca de": "About",
    "Desde": "Since",
    "Aunque": "Though",
    "Ademas": "Besides",
    "Entonces": "Then",
    "Casi": "Almost",
    "Cualquier": "Any/whichever",
    "Ningun": "Any/negative",
    "Algun": "Any/some",
    "Aun": "Still/yet/even",
    "Mayor": "Older",
    "Mejor": "Better",
    "Menor": "Younger",
    "Peor": "Worse",
    "Tan": "So",
    "Tanto": "So much",
    "Adelante": "Forward",
    "Demasiado": "Too much",
    "Jamas": "Never!",
    "Ya": "Already",
    "Apenas": "Barely",
    "El techo": "Ceiling/roof",
    "La pared": "Wall",
    "El sotano": "Basement",
    "Algo": "Something",
    "Quedar": "To remain",
    "tratar de": "To try",
    "tratar": "to treat",
    "Alcanzar": "To reach",
    "Anadir": "To add",
    "Perder": "To lose",
    "Pedir": "To ask/order",
    "Lograr": "To achieve",
    "Asi": "Like this",
    "Regalar": "To give away",
    "astrasado": "late",
    "el estanque": "pond",
    "el rincon": "corner",
    "la hoja": "leaf",
    "la brizna": "strand",
    "la ley": "law",
    "venir": "to come",
    "volver": "to return",
    "llegar": "to arrive",
    "todavia": "still",
    "hacia": "toward",
    "siquiera": "at least",
    "bastante": "enough",
    "herido": "wounded",
    "el ruido": "noise",
    "la rueda": "wheel",
    "el rumbo": "course/direction",
    "la raiz": "root",
    "la huella": "footprint",
    "el paso": "footstep",
    "la fracasa": "failure",
    "dejar": "to leave behind/let",
    "el orgullo": "pride",
    "acabar": "to end/finish",
    "el suelo": "ground",
    "amargar": "to make bitter",
    "el ombligo": "navel",
    "la dicha": "happiness",
    "la niebla": "fog/mist",
    "la cita": "meeting/date",
    "el ancho": "width",
    "el trueno": "thunder",
    "sin embargo": "however",
    "a traves de": "through",
    "colgar": "to hang",
    "aca": "here",
    "susurrar": "to whisper",
    "el nido": "nest",
    "la aguja": "needle",
    "el crepusculo": "dusk",
    "la madrugada": "dawn",
    "golpear": "to hit",
    "el barro": "mud",
    "el lodo": "mud",
    "el ladrillo": "brick",
    "el abanico": "fan",
    "la viga": "rafter",
    "el racimo": "cluster",
    "trenzar": "to braid",
    "la nave": "ship",
    "el siglo": "century",
    "rogar": "to beg",
    "titubeante": "hesitant",
    "la maleza": "weeds",
    "pegar": "to stick/hit",
    "la yedra": "ivy",
    "la plata": "silver",
    "la amapola": "poppy",
    "el desarrollo": "development",
    "desenfrenado": "unbridled",
    "atar": "to tie/bind",
    "desquiciado": "deranged",
    "el ramo": "bouquet",
    "el gusano": "worm",
    "acabar de": "just",
    "la pradera": "prairie/meadow",
    "pertenecer": "to belong to",
    "el trigo": "wheat",
    "pasajero": "passenger/fleeting",
    "el estio": "summer",
    "apagar": "to turn off",
    "el arrebol": "red glow",
    "la ceniza": "ash",
    "enlutar": "to sadden",
    "el pasto": "grass",
    "colocar": "to place",
    "evitar": "to avoid",
    "borrar": "to erase",
    "comodo": "comfortable",
    "silvestre": "wild/natural",
    "salvaje": "wild/savage",
    "atras": "behind/backwards",
    "tras": "after",
    "el hallazgo": "discovery",
    "luchar": "to struggle",
    "la meta": "goal/objective",
    "el dirigente": "leader",
    "arrasar": "to destroy",
    "el yermo": "barren/wasteland",
    "a pesar de": "in spite of",
    "allanar": "to flatten",
    "el delito": "crime",
    "compartir": "to share",
    "el mito": "myth",
    "disponible": "available",
    "despertar": "to awake",
    "dispuesto": "ready",
    "el sueldo": "salary",
    "desatender": "to neglect",
    "el estante": "shelf",
    "por lo tanto": "therefore",
    "asustar": "to frighten",
    "ligero": "light/subtle",
    "disparar": "to shoot",
    "el condado": "county",
    "la granja": "farm",
    "ubicar": "to locate",
    "el alambre": "wire",
    "involucrar": "to involve",
    "la cerca": "fence",
    "alejado": "distant",
    "a medida que": "as",
    "de hecho": "in fact",
    "la tasa": "rate/tax",
    "el suceso": "event",
    "hoy en dia": "nowadays",
    "tal": "such",
    "ya que": "now that/since",
    "alquilar": "to rent",
    "la ducha": "shower",
    "a punto de": "about to",
    "nitida": "sharp/clear",
    "desbancar": "to oust/replace",
    "menudo": "small/insignificant",
    "a menudo": "often",
    "la trama": "plot",
    "no obstante": "however",
    "amenazar": "to threaten",
    "ciego": "blind",
    "las moscas": "flies",
    "recoger": "to pick up",
    "la condena": "sentence",
    "el anfitrion": "host",
    "reclutar": "to recruit",
    "el alojamiento": "lodging",
    "pleno": "full",
    "la bala": "bullet",
    "la huelga": "strike",
    "entregar": "to deliver/submit",
    "la uNa": "nail",
    "el ambito": "field/area/scope",
    "el hueco": "hole",
    "apresurar": "to hurry",
    "el chiste": "joke",
    "incluso": "even",
    "demas": "other",
    "el charco": "puddle",
    "lodoso": "muddy",
    "enmarcar": "to frame",
    "instar": "to urge",
    "escabroso": "rough",
    "atropellar": "to run over",
    "huir": "to escape",
    "el lector": "reader",
    "la jaula": "cage",
    "la herramienta": "tool",
    "confiar": "to confide/trust",
    "probar": "to test",
    "surgir": "to arise",
    "hace poco": "recently",
    "el sosten": "bra",
    "la aula": "classroom",
    "el mueble": "furniture",
    "el inmueble": "building/property",
    "abarcar": "to cover",
    "el rastro": "trace",
    "el rasgo": "feature",
    "el riesgo": "risk",
    "el rostro": "face",
    "difundir": "to spread",
    "enganar": "to deceive",
    "destacar": "to emphasize",
    "cumplir": "to achieve",
    "proferir": "to utter",
    "lidiar": "to deal with",
    "el apoyo": "support",
    "el punado": "handful",
    "el plazo": "term/period",
    "multar": "to fine",
    "eolico": "wind",
    "dizque": "supposedly/apparently",
    "la apuesta": "bet",
    "la espada": "sword",
    "la pieza": "piece",
    "el alfil": "bishop",
    "la finca": "property",
    "la viuda": "widow",
}

misses = []

def get_word(words):
    word = random.choice(words.keys())
    return word

def get_english_word(words):
    word = random.choice(words.values())
    return word

def get_spanish_match(english_word, words):
    for word in words.keys():
        if words[word] == english_word:
            return word

def show_misses():
    os.system("clear")
    print "MISSES:"
    if len(misses) == 0:
        print "No misses yet"
    else:
        for i in range(0, len(misses)-1, 2):
            print "{}, {}".format(misses[i], misses[i+1])

def quit_game():
    os.system("clear")
    print "Bye"

os.system("clear")
print ""
print "Type 'quit' to exit"
print "Type 'misses' to view all missed words"
print "Type 'english' or 'spanish' at any time to switch starting language"
print ""
starting_lang = raw_input('Start with English or Spanish? ').lower()


while True:
    # English to Spanish translation----
    if starting_lang == "english":
        english_word = get_english_word(words)
        print ""
        print english_word

        spanish_match = get_spanish_match(english_word, words)
        answer = raw_input('Translation: ').lower()

        if answer == spanish_match.lower():
            os.system("clear")
            print "Correct"
        elif answer == "misses":
            show_misses()
        elif answer == "quit":
            quit_game()
            break
        elif answer == 'spanish':
            starting_lang = 'spanish'
        else:
            print "Wrong. The answer is \"{}\"".format(spanish_match)
            misses.append(english_word)
            misses.append(spanish_match)

    # Spanish to English translation----
    elif starting_lang == "spanish":
        spanish_word = get_word(words)
        print ""
        print spanish_word

        answer = raw_input('Translation: ').lower()

        if answer == words[spanish_word].lower():
            os.system("clear")
            print "Correct"
        elif answer == "misses":
            show_misses()
        elif answer == "quit":
            quit_game()
            break
        elif answer == 'english':
            starting_lang = 'english'
        else:
            print "Wrong. The answer is \"{}\"".format(words[spanish_word])
            misses.append(spanish_word)
            misses.append(words[spanish_word])
