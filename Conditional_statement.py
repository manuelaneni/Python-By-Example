# 016

triggers = ["yes", "no"]
while True:
    user = input("Is it raining? yes or no: ").lower()
    if user not in triggers:
        print("Invalid input, Try again!")
    else:
        if user == "yes":
            windy = input("Is it windy? ")
            if windy == triggers[0]:
                print("It is too windy for an umbrella!")
            else:
                print("Take an umbrella!")
        else:
            print("Enjoy your day.")
        break
