play = 'Yes'
while play == 'Yes':


    str = input ("Enter the word: ").lower()
    c = len(str)
    p = c - 1
    index = 0

    if str[index]== str [p]:
        index = index + 1
        p = p - 1
        print("The entered word is a palindrome")
    else:
        print ("The entered word is not a palindrome")

    ahd = input('Do you want to play again?')
    if ahd == "No":
        play = "No"

