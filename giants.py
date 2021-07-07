# import this

def main():

    print()

    great_people_list = ['terry tao', 'john tate', 'alexander grothendieck',
                         'john von neumann', 'richard feynman', 'immanuel kant',
                         'plato', 'john archibald wheeler']

    print("The following are people with whom I'd most like to have a meal: ")
    print()
    for i, names in enumerate(great_people_list, 1):
        print(str(i) + ") " + names.title())
    print()

    messageTao = great_people_list[0].title() + ", you are the best" \
                " mathematician of this age.\n"

    print(messageTao)

    messageTate = great_people_list[1].title() + ", you're a brilliant number" \
                " theorist.\n"

    print(messageTate)

    messageGrothendieck = great_people_list[2].title() + ", you brought us to" \
                 " new horizons in pure mathematics.\n"

    print(messageGrothendieck)

    messageNeumann = great_people_list[3].title() + ", you're probably the" \
                 " smartest person to ever live. There's nothing you couldn't do.\n"

    print(messageNeumann)

    messageFeynman = great_people_list[4].title() + ", you're my intellectual hero.\n"

    print(messageFeynman)

    messageKant = great_people_list[5].title() + ", I find your works profoundly" \
                 " moving. Great motivation to beleive in the endeavors of\n" \
                 "\tPure Reason and rationality leaps cubistically from the page,\n" \
                 "\tinsipiring one to beleive in all Reason's promise.\n"

    print(messageKant)

    messagePlato = great_people_list[6].title() + ", I loved reading your works" \
                 " in the original.\n"

    print(messagePlato)

    messageWheeler = great_people_list[7].title() + ", the depths of your" \
                 " research into gravity, I can only now imagine.\n"

    print(messageWheeler)

    print("Well, I just found out " + great_people_list[6].title() + \
          " cannot come.")

    print("Here's who remains: ")

    del great_people_list[6]

    print()
    for i, names in enumerate(great_people_list, 1):
        print(str(i) + ") " + names.title())
    print()

    great_people_list.insert(0, "Harry Caray")

    print("It looks like", great_people_list[0].title(), "will be coming.")

    print("So, here's our new list")

    print()
    for i, names in enumerate(great_people_list, 1):
        print(str(i) + ") " + names.title())
    print()

    for i in range(0, len(great_people_list)):
        print("Dear " + great_people_list[i].title() + ", I'm delighted to\n", \
              "to request your presence at my dinner table.\n Please consider", \
              "this request as of a token of appreciation\n of your many", \
              "esteemed accomplishments")
        print()

    for guest in great_people_list:
        print(guest.title() + ", I look forward to your presence!")
    print()

    even_numbers = list(range(2, 21, 2))
    print(even_numbers)
    print()

    squares = []
    for value in even_numbers:
        squares.append(value**2)

    print(squares)
    print()



if __name__ == '__main__':
    main()
