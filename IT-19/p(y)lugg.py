def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|                             |")
    print("|           P(y)lugg          |")
    print("|                             |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

def menu(title, prompt, options):
    print(title)
    print()
    for option in options:
        print(f"  {option}) {options[option]}")
    
    print()
    action = input(prompt)
    while action not in options:
        action = input(prompt)
    
    return action

def list_to_dict(ls):
    x = 1
    ds = {}
    for item in ls:
        ds[str(x)] = item
        x = x + 1
    return ds

#def shuffle_dict():
    

def swedish(options):
    swedish_words = ["förespråka", "obefogad", "emballage"]
    swedish_words_correct = {"förespråka":"rekommendera", "obefogad":"grundlös", "emballage":"förpackning", "tidvis":"ibland","framfusig":"påträngande", "extravagans":"överdåd", "ge sig till tåls":"lugnt invänta något", "baryton":"röstläge", "rågad":"överfull", "maxim":"levnadsregel"}
    swedish_words_alternatives = {"förespråka":["reflektera", "reservera", "rekommendera", "resonera", "regissera"], "obefogad":["grundlös", "maktlös", "ansvarslös", "gränslös", "meningslös"], "emballage":["symbol", "förpackning", "underhåll", "avspärrning","handelsförbud"], "tidvis":["ofta", "förut", "punktlig", "ibland", "numera"], "framfusig":["nytänkande", "självsäker", "uppjagad", "förväntansfull", "påträngande"], "extravagans":["överdåd", "värdighet", "merkostnad", "passion", "övermod"], "ge sig till tåls":["ta sitt ansvar", "vara i underläge", "fatta ett beslut", "lugnt invänta något", "visa sin styrka"], "baryton":["notställ", "pianostycke", "röstläge", "slagverkare", "taktpinne"], "rågad":["kraftig", "bristfällig", "åtgärdad", "överfull", "avslutad"], "maxim":["reaktion", "jämvikt", "slutresultat", "förbindelse", "levnadsregel"]}
    
    action = ""
    while action != "2":
        points = 0
        for word in swedish_words_alternatives:
            print()
            answer = menu(word, "Val: ", list_to_dict(swedish_words_alternatives[word]))
            if swedish_words_alternatives[word][int(answer) - 1] == swedish_words_correct[word]:
                print()
                print("Rätt!")
                points = points + 1
            else:
                print()
                print("Fel.")
        print()
        print(f"Du fick {points} antal rätt!")
        print()
        action = menu("Vad vill du göra?", "Val: ", options)
    
#def words(words):
    



def main():
    options_main = {"1":"Svenska ord", "2":"Engelska-Svenska", "3":"Avsluta"}
    options_difficulty = {"1":"Lätt", "2":"Medel", "3":"Svårt"}
    options_again = {"1":"Kör igen", "2":"Tillbaka till meny"}
    
    
    action = ""
    while action != "3":
        splash()
        action = menu("Vad vill du p(y)lugga på?", "Val: ", options_main)
        #difficulty = menu("Välj svårighetsgrad:", "Val: ", options_difficulty)
        if action == "1":
            swedish(options_again)
            
main()