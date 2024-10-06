from character import Enemy

dave = Enemy("Dave", "Hello")
dave.describe()

dave.set_conversation("Hi!")
dave.talk()
dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input("Enter item here: ")
dave.fight(fight_with.lower())