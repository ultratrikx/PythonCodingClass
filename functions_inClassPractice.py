name1 = "rohanth"
name2 = 'medhansh'
name3 = 'jiohn'
name4 = 'hasdf'


def greeting(name):
    print('Hello', name)


greeting(name1)
greeting(name2)
greeting(name3)
greeting(name4)


def doubler(num):
    print('The Answer is', num*2)


doubler(7)

new_number = doubler(12)
new_number


def sayhello():
    print('type your name :')
    name = input('>> ')
    print('hi', name)
    print('how are you?')
    howTheyAre = input('>> ')
    if howTheyAre == 'good':
        print('thats good to hear')
    elif howTheyAre == 'okay':
        print('ah, i see')
    elif howTheyAre == 'bad':
        print('sorry to hear that, hope you feel better')
    else:
        print('thanks for letting me know!!')


sayhello()
