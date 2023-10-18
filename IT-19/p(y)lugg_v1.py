import random
import english_words
import swedish_words

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

def shuffle_dict(unshuffled_dict):
    #unshuffled_list = []
    for key in unshuffled_dict:
        #unshuffled_list.append(key)
        random.shuffle(unshuffled_dict[key])
    
    #shuffled_list = random.shuffle(unshuffled_list)
        
def sample(alternatives, correct_answer):
    sampled_list = []
    sampled_list = random.sample(alternatives, 4)
    sampled_list.append(correct_answer)
    random.shuffle(sampled_list)
    return sampled_list
    
def difficulty_check(difficulty, word, words_alternatives, words_correct):
    if difficulty == "1":
        sampled_alternatives = sample(words_alternatives, words_correct[word])
        answer = menu(word, "Val: ", list_to_dict(sampled_alternatives))
        if answer == "x":
            return answer
        else:
            return sampled_alternatives[int(answer) - 1]
    elif difficulty == "2":
        return menu(word, "Val: ", list_to_dict(words_alternatives[word]))
    

def word_test(options, words_correct, words_alternatives, difficulty):
    
    action = ""
    while action != "2" and action != "x":
        points = 0
        #shuffle_dict(words_correct)
        for word in words_correct:
            print()
            print("Tryck x för att avsluta")
            print()
            
            answer = difficulty_check(difficulty, word, words_alternatives, words_correct)
            #answer = menu(word, "Val: ", list_to_dict(words_alternatives[word]))
            
            if answer == "x":
                break
            points = points + word_check(word, answer, words_correct)
            
        print()
        print(f"Du fick {points} antal rätt!")
        print()
        action = menu("Vad vill du göra?", "Val: ", options)
        
def word_check(word, answer, words_correct):
    if answer == words_correct[word]:
        print()
        print("Rätt!")
        return 1
    else:
        print()
        print("Fel.")
        return 0


def main():
    options_main = {"1":"Svenska ord", "2":"Engelska-Svenska", "3":"Avsluta"}
    options_difficulty = {"1":"Lätt", "2":"Medel", "3":"Svårt"}
    options_again = {"1":"Kör igen", "2":"Tillbaka till meny"}
    
    swedish_words_correct = swedish_words.swedish_words_correct
    swedish_words_intermediate = swedish_words.swedish_words_intermediate
    swedish_words_easy = swedish_words.swedish_words_easy
    
    english_words_correct = english_words.english_words_correct
    english_words_easy = english_words.english_words_easy # Byt ut mot lista med andra ord
    
    action = ""
    while action != "3" and action != "x":
        splash()
        action = menu("Vad vill du p(y)lugga på?", "Val: ", options_main)
        
        if action == "1":
            difficulty = menu("Välj svårighetsgrad:", "Val: ", options_difficulty)
            if difficulty == "1":
                word_test(options_again, swedish_words_correct, swedish_words_easy, difficulty)
            elif difficulty == "2":
                word_test(options_again, swedish_words_correct, swedish_words_intermediate, difficulty)
        elif action == "2":
            #difficulty = menu("Välj svårighetsgrad:", "Val: ", {"1":"Lätt", "2":"Svårt"})
            # Lägg till if-sats för svårighetsgrad när svårt är implementerat
            word_test(options_again, english_words_correct, english_words_easy, difficulty)

            
main()