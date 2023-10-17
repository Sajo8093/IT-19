def splash():
    print()
    print(" ______  __    __  _                   ")            
    print(" | ___ \/ /    \ \| |                  ")                
    print(" | |_/ / |_   _ | | |_   _  __ _  __ _ ")
    print(" |  __/| | | | || | | | | |/ _` |/ _` |")
    print(" | |   | | |_| || | | |_| | (_| | (_| |")
    print(" \_|   | |\__, || |_|\__,_|\__, |\__, |")
    print("       \_\__/ /_ /          __/ | __/ |")
    print("         |___/             |___/ |___/ ")
    print()
                                          

def menu(title, prompt, options):
    print(title)
    print()
    for option in options:
        print(f"  {option}) {options[option]}")
    
    print()
    action = input(prompt)
    while action not in options and action != "x":
        if action == "x":
            return action
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
    

def word_test(options, words_correct, words_alternatives):
    
    action = ""
    while action != "2" and action != "x":
        points = 0
        for word in words_alternatives:
            print()
            print("Tryck x för att avsluta")
            print()
            answer = menu(word, "Val: ", list_to_dict(words_alternatives[word]))
            if answer == "x":
                break
            points = points + word_check(word, answer, words_alternatives, words_correct)
            
        print()
        print(f"Du fick {points} antal rätt!")
        print()
        action = menu("Vad vill du göra?", "Val: ", options)
        
def word_check(word, answer, words_alternatives, words_correct):
    if words_alternatives[word][int(answer) - 1] == words_correct[word]:
        print()
        print("Rätt!")
        return 1
    else:
        print()
        print("Fel.")
        return 0


def main():
    import english_words
    options_main = {"1":"Svenska ord", "2":"Engelska-Svenska", "3":"Avsluta"}
    options_difficulty = {"1":"Lätt", "2":"Medel", "3":"Svårt"}
    options_again = {"1":"Kör igen", "2":"Tillbaka till meny"}
    
    swedish_words_correct = {"förespråka":"rekommendera", "obefogad":"grundlös", "emballage":"förpackning", "tidvis":"ibland","framfusig":"påträngande", "extravagans":"överdåd", "ge sig till tåls":"lugnt invänta något", "baryton":"röstläge", "rågad":"överfull", "maxim":"levnadsregel"}
    swedish_words_alternatives = {"förespråka":["reflektera", "reservera", "rekommendera", "resonera", "regissera"], "obefogad":["grundlös", "maktlös", "ansvarslös", "gränslös", "meningslös"], "emballage":["symbol", "förpackning", "underhåll", "avspärrning","handelsförbud"], "tidvis":["ofta", "förut", "punktlig", "ibland", "numera"], "framfusig":["nytänkande", "självsäker", "uppjagad", "förväntansfull", "påträngande"], "extravagans":["överdåd", "värdighet", "merkostnad", "passion", "övermod"], "ge sig till tåls":["ta sitt ansvar", "vara i underläge", "fatta ett beslut", "lugnt invänta något", "visa sin styrka"], "baryton":["notställ", "pianostycke", "röstläge", "slagverkare", "taktpinne"], "rågad":["kraftig", "bristfällig", "åtgärdad", "överfull", "avslutad"], "maxim":["reaktion", "jämvikt", "slutresultat", "förbindelse", "levnadsregel"]}
    
    english_words_correct = english_words.words_dict
    
    action = ""
    while action != "3" and action != "x":
        splash()
        action = menu("Vad vill du p(y)lugga på?", "Val: ", options_main)
        #difficulty = menu("Välj svårighetsgrad:", "Val: ", options_difficulty)
        if action == "1":
            word_test_intermediate(options_again, swedish_words_correct, swedish_words_alternatives)
        elif action == "2":
            word_test_easy(options_again, english_words_correct, english_words_correct)
            
main()
                                          

