import random
print("Enjoy the fortune cookie!\n")
luckylist = ["Success follows you everywhere!", "You are the best in whatever you do.", "You are a great inspiration!", "Your talents will help build a better world for future generations.", "You are the life of the party!",
             "Because you stand for what is right, you are true hero.", "Learning is a breeze!", "Your good heart leads you to good things in life!", "You only fail if you don't try; have faith!", "Great advise will always be there to guide you."]

print("Your fortune reads\n>> ", random.choice(luckylist))
x = random.sample(range(1, 99), 5)
print("Your Lucky Numbers are", x)
