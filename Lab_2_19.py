'''


name: Adedeji Akingbola
PSID: 1793979

'''

if __name__ == '__main__':
    lemonCups = float(input("Enter amount of lemon juice (in cups): "))
    waterCups = float(input("Enter amount of water (in cups): "))
    agaveCups = float(input("Enter amount of agave nectar (in cups): "))
    servings = float(input("How many servings does this make?: "))
    print('Lemonade ingredients - yields {:.2f} servings'.format(servings))
    print('{:.2f} cup(s) lemon juice'.format(lemonCups))
    print('{:.2f}  cup(s) water'.format(waterCups))
    print('{:.2f} cup(s) agave nectar'.format(agaveCups))
    
    servings1 = float(input("How many servings does this make?: "))
    print('Lemonade ingredients - yields {:.2f} servings'.format(servings1))
    lemonCups1 = lemonCups * servings1 / servings
    print('{:.2f} cup(s) lemon juice'.format(lemonCups1))
    waterCups1 = waterCups * servings1 / servings
    print('{:.2f}  cup(s) water'.format(waterCups1))
    agaveCups1 = agaveCups * servings1 / servings
    print('{:.2f} cup(s) agave nectar'.format(agaveCups1))
    
    print('Lemonade ingredients - yields {:.2f} servings'.format(servings1))
    print('{:.2f} gallon(s) lemon juice'.format(lemonCups1 / 16))
    print('{:.2f}  gallon(s) water'.format(waterCups1 / 16))
    print('{:.2f} gallon(s) agave nectar'.format(agaveCups1 / 16))
    
