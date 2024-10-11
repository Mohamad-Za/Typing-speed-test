"""the mane page which runs the code"""
import os
import functions

def main():
    """the main function gives a menu there the user can choose what he wants the code to run"""
    stop = False
    while not stop:
        os.system('clear')
        print('1. Train easy')
        print('2. Train medium')
        print('3. Train hard')
        print('4. See high score')
        print('q. Quit)')
        choice = input('Choose from the menu: ')

        if choice == 'q':
            stop = True

        elif choice == '1':
            functions.the_mode('/home/mohamad/dbwebb-kurser/python/me/kmom10/easy.txt')

        elif choice == '2':
            functions.the_mode('medium.txt')

        elif choice == '3':
            functions.the_mode('hard.txt')
            
        elif choice == '4':
            with open('score.txt') as scores:
                scores = scores.read()
            print(scores)

        else:
            print('\nNot a valid choice!')
            print('Choose from the menu please. \n')

        if not stop:
            input('Press enter to continue...')

if __name__ == "__main__":
    main()
