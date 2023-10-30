# Importing needed libraries
import random
import english_words
import swedish_words

def splash():
    print()
    print(r" ______  __    __  _                   ")            
    print(r" | ___ \/ /    \ \| |                  ")                
    print(r" | |_/ / |_   _ | | |_   _  __ _  __ _ ")
    print(r" |  __/| | | | || | | | | |/ _` |/ _` |")
    print(r" | |   | | |_| || | | |_| | (_| | (_| |")
    print(r" \_|   | |\__, || |_|\__,_|\__, |\__, |")
    print(r"       \_\__/ /_ /          __/ | __/ |")
    print(r"         |___/             |___/ |___/ ")
    print()
                                          
# Function for multiple choice input, returns user choice
def menu(title, prompt, options):
    print(title)
    print()
    for option in options:
        print(f"  {option}) {options[option]}")
    
    print()
    action = input(prompt)
    # Makes sure input is valid
    while action not in options and action != "x":
        if action == "x":
            return action
        action = input(prompt)
    
    return action

# Turns a list into a dictionary with numbered keys
def list_to_dict(ls):
    x = 1
    ds = {}
    for item in ls:
        ds[str(x)] = item
        x = x + 1
    return ds

# Randomizes order of a dictionary
def shuffle_dict(unshuffled_dict):
    unshuffled_list = []
    # Adds key to a list, and if the value of said key is a list, shuffle that list
    for key in unshuffled_dict:
        unshuffled_list.append(key)
        if type(unshuffled_dict[key]) is list:
            random.shuffle(unshuffled_dict[key])
    # Shuffle the newly created list
    random.shuffle(unshuffled_list)
    
    shuffled_dict = {}
    # Add all values from the old dictionary into the new one
    for item in unshuffled_list:
        shuffled_dict[item] = unshuffled_dict[item]
    return shuffled_dict

# Picks out 4 random words from a list and shuffles them with one chosen word (correct_answer)
def sample(alternatives, correct_answer):
    sampled_list = []
    # Picks out 4 random words from the given alternatives
    sampled_list = random.sample(alternatives, 4)
    # Appends the correct answer
    sampled_list.append(correct_answer)
    # Shuffles the order
    random.shuffle(sampled_list)
    return sampled_list

# Checks chosen difficulty layer and then asks the question appropriately
def difficulty_check(difficulty, word, words_alternatives, words_correct):
    # Easy difficulty
    if difficulty == "1":
        # Sample alternatives
        sampled_alternatives = sample(words_alternatives, words_correct[word])
        # Store answer returned from menu function
        answer = menu(word, "Val: ", list_to_dict(sampled_alternatives))
        # x means quit
        if answer == "x":
            return answer
        else:
            return sampled_alternatives[int(answer) - 1]
    # Intermediate difficulty
    elif difficulty == "2":
        answer = menu(word, "Val: ", list_to_dict(words_alternatives[word]))
        if answer == "x":
            return answer
        else:
            return words_alternatives[word][int(answer) - 1]
    # Hard difficulty
    else:
        return input(f"{word}: ")
        
    
# Function that runs the word test
def word_test(options, words_correct, words_alternatives, difficulty):
    
    action = ""
    while action != "2" and action != "x":
        points = 0
        # Shuffle dictionaries
        words_correct = shuffle_dict(words_correct)
        if difficulty == "2":
            words_alternatives = shuffle_dict(words_alternatives)
        elif difficulty == "1":
            random.shuffle(words_alternatives)
        
        counter = 0
        for word in words_correct:
            print()
            print("Tryck x för att gå tillbaka till menyn")
            print()
            
            answer = difficulty_check(difficulty, word, words_alternatives, words_correct)
            
            if answer == "x":
                break
            points = points + word_check(word, answer, words_correct, difficulty)
            counter = counter + 1
            
        print()
        print(f"Du fick {points} antal rätt av {counter} möjliga!")
        print()
        action = menu("Vad vill du göra?", "Val: ", options)
        
# Checks if the answer is correct
def word_check(word, answer, words_correct, difficulty):
    if answer.lower() == words_correct[word].lower():
        print()
        print("Rätt!")
        return 1
    else:
        print()
        if difficulty == "1":
            print(f"Fel. Rätt svar är \"{words_correct[word].lower()}\"")
        else:
            print("Fel.")
        return 0



# Main
def main():
    # Variables
    options_main = {"1":"Svenska ord", "2":"Engelska-Svenska", "3":"Avsluta"}
    options_difficulty = {"1":"Lätt", "2":"Medel", "3":"Svårt"}
    options_again = {"1":"Kör igen", "2":"Tillbaka till meny"}
    
    swedish_words_correct = swedish_words.swedish_words_correct
    swedish_words_intermediate = swedish_words.swedish_words_intermediate
    swedish_words_easy = swedish_words.swedish_words_easy
   
    english_words_correct = english_words.english_words_correct
    english_words_easy = english_words.english_words_easy 
    
    action = ""
    while action != "3" and action != "x":
        splash()
        action = menu("Vad vill du p(y)lugga på?", "Val: ", options_main)
        
        if action == "1":
            difficulty = menu("Välj svårighetsgrad:", "Val: ", options_difficulty)
            if difficulty == "1":
                word_test(options_again, swedish_words_correct, swedish_words_easy, difficulty)
            else:
                word_test(options_again, swedish_words_correct, swedish_words_intermediate, difficulty)
        elif action == "2":
            difficulty = menu("Välj svårighetsgrad:", "Val: ", {"1":"Lätt", "3":"Svårt"})
            word_test(options_again, english_words_correct, english_words_easy, difficulty)

            
main()