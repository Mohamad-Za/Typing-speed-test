"""the functions file where the majority of the code is written"""
import os
import time
from operator import itemgetter

def file_handler(file_name):
    """filehandler functions to open files easily"""
    with open(file_name, 'r') as file_content:
        file_content = file_content.read()
    return file_content


def the_mode(file_name):
    """the_mode functions is imported in the main file and runs the whole of the code there"""
    try:
        with open ('inputs.txt', 'w') as reset:
            reset = reset.write('')

        file_content = file_handler(file_name)
        lines = file_content.splitlines()

        time_started = time.time()
        for line in lines:
            os.system('clear')
            print(line)
            user_inp = input('')
            with open ('inputs.txt', 'a') as appended:
                appended = appended.write(user_inp + '\n')
        time_ended = time.time()
        os.system('clear')

        ord_precision(file_name)
        tecken_precision(file_name)
        character_sorting()
        time_taken(time_started, time_ended)
        the_scores(file_name)
        
    except FileNotFoundError:
        print("The file does not exist!")


incorrect_words = 0
word_precision = 0
def ord_precision(file_name):
    """calculating the precision of words"""
    file_content = file_handler(file_name)
    original_text = file_content.splitlines()

    input_file = file_handler('inputs.txt')
    inputs_txt = input_file.splitlines()
    global incorrect_words
    incorrect_words = 0
    total_right_words = 0
    for line in range(min(len(inputs_txt), len(original_text))):
        input_lines = inputs_txt[line].split()
        original_lines = original_text[line].split()

        if len(input_lines) > len(original_lines):
            extra_words = len(input_lines) - len(original_lines)
            total_right_words = total_right_words - extra_words 
            incorrect_words += extra_words
        right_words = 0
        for word_index in range(min(len(input_lines), len(original_lines))):
            if input_lines[word_index] == original_lines[word_index]:
                right_words += 1
            else:
                incorrect_words += 1
        total_right_words += right_words

    total_words = len(file_content.split())
    global word_precision
    word_precision = round((total_right_words / total_words) * 100, 2)
    print(f"Word precision: {word_precision}%")



wrong_letters = ''
def tecken_precision(file_name):
    """calculating the precision of the letters"""
    original_file = file_handler(file_name)
    original_text = original_file.splitlines()

    input_file = file_handler('inputs.txt')
    inputs_txt = input_file.splitlines()

    extra_words = 0
    right_letters = 0
    extra_letters = 0
    global wrong_letters
    wrong_letters = ''
    extra_letters_in_extra_words = 0
    for line in range(min(len(inputs_txt), len(original_text))):
        user_words = inputs_txt[line].split()
        org_words = original_text[line].split()
        if len(user_words) > len(org_words):
            extra_words += 1
            extras = user_words[-extra_words:]
            for i in extras:
                extra_letters_in_extra_words += len(i)
        elif len(user_words) < len(org_words):
            non_ex = len(org_words) - len(user_words)
            for orden in org_words[-non_ex:]:
                for i in orden:
                    wrong_letters += i
                    
        
        for word_index in range(min(len(user_words), len(org_words))):
            user_word = user_words[word_index]
            org_word = org_words[word_index]

            if len(user_word) > len(org_word):
                extra_letters_in_each = len(user_word) - len(org_word)
                extra_letters += extra_letters_in_each
                extra_letters += extra_letters_in_extra_words

            elif len(user_word) < len(org_word):
                non_ex_letter = len(org_word) - len(user_word)

                for i in org_word[-non_ex_letter:]:
                    wrong_letters += i

            for letter_index in range(min(len(user_word), len(org_word))):
                if user_word[letter_index] == org_word[letter_index]:
                    right_letters += 1

                elif user_word[letter_index] not in org_word[letter_index]:
                    wrong_letters += org_word[letter_index]
    
    total_letters = len(original_file.replace(' ', '').replace('\n', ''))
    total_right_letters = right_letters - extra_letters
    letter_precision = round((total_right_letters / total_letters) * 100, 2)
    print(f"Letter Precision: {letter_precision}%")



def character_sorting():
    """sorting the wrong characters"""
    chars_dict = {}
    for chars in wrong_letters:
        if chars in chars_dict:
            chars_dict[chars] += 1
        else:
            chars_dict[chars] = 1
    
    sorted_chars_dict = sorted(chars_dict.items(), key=itemgetter(1), reverse=True)
    print("Felstavade tecken: ")
    for chars, count in sorted_chars_dict:
        print(f'{chars}: {count}')


def the_scores(file_name):
    """opens a file named 'score.txt' and saves the scores there"""
    users_name = input('Enter username to add to highscore: ')
    if users_name == '':
        users_name = 'Anonym'
    
    if file_name.endswith('.txt'):
        file_name = file_name[:-4]
    with open ('score.txt', 'a') as write_score:
        write_score = write_score.write(f'{users_name}    {word_precision}    {file_name} \n')
        return(write_score)




def time_taken(starting, ending):
    """taking the time from when the user starts the program
    (when the user chooses betweeb 1-3 from the menu) to the last input"""
    result = ending - starting
    mins = result // 60
    secs = result % 60
    print(f'Det tog {mins} minuter och {secs} sekunder')

    if result < 60:
        avrundade_minuter = 1

    elif result % 60 >= 30:
        avrundade_minuter = result // 60 + 1
    else:
        avrundade_minuter = result // 60

    input_file = file_handler('inputs.txt')
    total_words = len(input_file.split())
    
    grosswpm = total_words / avrundade_minuter
    print('Gross WPM: ', grosswpm)

    netwpm = grosswpm - (incorrect_words / avrundade_minuter) 
    print('Net WPM: ', netwpm)

    if netwpm <= 10:
        print('Sengångare')
    elif 10 < netwpm <= 20:
        print("Snigel")
    elif 20 < netwpm <= 30:
        print("Sjöko")
    elif 30 < netwpm <= 40:
        print("Människa")
    elif 40 < netwpm <= 50:
        print("Gasell")
    elif 50 < netwpm <= 60:
        print('Struts')
    elif 60 < netwpm <= 70:
        print("Gepard")
    elif 70 < netwpm <= 80:
        print("Svärdfisk")
    elif 80 < netwpm <= 90:
        print("Sporrgås")
    elif 90 < netwpm <= 100:
        print("Taggstjärtseglare")
    elif 100 < netwpm <= 120:
        print("Kungsörn")
    elif netwpm > 120:
        print("Pilgrimsfalk")
