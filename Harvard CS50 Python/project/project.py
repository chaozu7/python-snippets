class Cage():

    def __init__(self, user, film, character):
        self.user = user
        self.film = film
        self.character = character

    def __str__(self):
        return f"You are playin' in a {self.film} today and you are a {self.character}!"


    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        if not user:
            raise ValueError("Missing user")
        self._user = user

    @property
    def film(self):
        return self._film

    @film.setter
    def film(self, film):
        if not film:
            raise ValueError("Missing film")
        self._film = film

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        if not character:
            raise ValueError("Missing character")
        self._character = character



def main():
    print("Hello and welcome in \"Which Nicolas Cage are you today\"!")
    username()
    printuser()
    conversation()
    matchfilm()
    nick = Cage(user, film, character)
    print(nick)


films = ["Renfield",
            "Surfer",
            "Face/Off",
            "Birdy",
            "Wild at Heart",
            "Guarding Tess",
            "The Rock",
            "City of Angels",
            "National Treasure",
            "The Unbearable Weight of Massive Talent"]

characters = ["Vampire", "Surfer", "Gangster", "Kind of Positive Freak", "Lover", "Guardian","FBI Agent", "Oh, an Angel", "Treasure Hunter", "Actor"]


def username():
    global user
    user = input("What is your name Nicolas?: ")
    return user

def printuser():
    print(f"Nice to meet you Nic..{user} I mean. Which face will you put today?")


def conversation():
    print("Let's start")
    print("Use only 'yes' or 'no' respond")
    global respond
    global points
    points = 0
    questions = ["Do you feel fear of the dark?", "Do you like to eat near to the beach?", "Do you like the sound of the birds?", "Do you feel alive?", "Do you like purple","Do you believe in conspiracy theories?", "Do you like cheese?", "Private island sounds interesting for you?", "Do you like fast cars?"]
    for question in range(len(questions)):
        print(questions[question])
        respond = input("yes/no ")
        respond = respond.lower()
        if respond == 'yes':
            if points == 9:
                points = points
            else:
                points += 1
        elif respond == 'no':
            if points <= 0:
                points = 0
            else:
                points -= 1

        else:
            print("You can't play this game, no Caging today honey!")
            points = points
    return points


def matchfilm():
    global film
    global character
    filmList = list(zip(films, characters))
    my_score = filmList[points]
    film = my_score[0]
    character = my_score[1]
    return film, character

if __name__ == "__main__":
    main()
