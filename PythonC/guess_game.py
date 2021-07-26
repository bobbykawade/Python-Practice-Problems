guess_no = int(input("Enter your guess:"))
def guess(a):
    co=1
    key = 50
    while a != key:
        a = int(input("Enter your guess:"))
        co=co+1
        if a < key:
            print("Your guess is less")
        elif a > key:
            print("Your guess is more")
    else:
        print("You have entered right key")
        print("you took {} iterations".format(co))
guess(guess_no)