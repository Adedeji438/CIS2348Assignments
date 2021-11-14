if __name__ == "__main__":
    dict_predict = {}
    i = 1
    count = 1
    for i in range(1, 6):
        jersey_num = int(input('Enter player {}\'s jersey number:\n' .format(i)))
        rating = int(input('Enter player {}\'s rating:\n' .format(i)))
        print()
        if jersey_num < 0 and jersey_num > 99 and rating < 0 and rating > 9:
            print('invalid entry')
            break
        else:
            dict_predict[jersey_num] = rating
    print("ROSTER")
    for jersey_num, rating in sorted(dict_predict.items()):
        print("Jersey number: {}, Rating: {}".format(jersey_num, rating))
    print()
    option = ''
    while option.upper() != 'Q':
        print('MENU')
        print('a - Add player')
        print('d - Remove player')
        print('u - Update player rating')
        print('r - Output players above a rating')
        print('o - Output roster')
        print('q - Quit\n')
        option = input('Choose an option:')
        if option == 'a':
            jersey_num = int(input('Enter a new player\'s jersey number:\n' .format(i)))
            rating = int(input('Enter the players\'s rating:\n'.format(i)))
            dict_predict[jersey_num] = rating
        elif option == 'd':
            jersey_num = int(input('Enter a jersey number:\n'))
            if jersey_num in dict_predict.keys():
                del dict_predict[jersey_num]
        elif option == 'u':
            jersey_num = int(input('Enter a jersey number:\n'))
            if jersey_num in dict_predict.keys():
                rating = int(input('Enter a new rating for player:\n'))
                dict_predict[jersey_num] = rating
        elif option == 'r':
            rating_input = int(input('Enter a rating:\n'))
            print('ABOVE {}'.format(rating_input))
            for jersey_num, rating in sorted(dict_predict.items()):
                if rating > rating_input:
                    print("Jersey number: {}, Rating: {}".format(jersey_num, rating))
        elif option == 'o':
            print("ROSTER")
            for jersey_num, rating in sorted(dict_predict.items()):
                print("Jersey number: {}, Rating: {}".format(jersey_num, rating))
        print()

