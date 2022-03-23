import random


class Card:
    def __init__(self, name, easiness, versatility, use, optimisation):
        self.name = name
        self.easiness = easiness
        self.versatility = versatility
        self.use = use
        self.optimisation = optimisation

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_easiness(self):
        return self.easiness

    def get_versatility(self):
        return self.versatility

    def get_use(self):
        return self.use

    def get_optimisation(self):
        return self.optimisation

    def display_stats(self):
        print(
            f"----------------------------\nName: {self.get_name()}\nEasiness: {self.get_easiness()}\nVersatility: "
            f"{self.get_versatility()}\nUse: "
            f"{self.get_use()}\nOptimisation: {self.get_optimisation()}")


def set_player_card(cards):
    card1 = random.choice(cards)
    return card1


def set_opponent_card(cards):
    card2 = random.choice(cards)
    return card2


def choose_attribute(person_card):
    person_card.display_stats()
    player_choice = input("\nPress 1 to choose easiness\n2 to choose versatility\n3 to choose use"
                          "\n4 to choose optimisation\n")
    while not (49 <= ord(player_choice) <= 52):
        player_choice = input("\nPress 1 to choose easiness\n2 to choose versatility\n3 to choose use"
                              "\n4 to choose optimisation\n")
    return int(player_choice)


def calculate_score(card, player_choice):
    if player_choice == 1:
        score = card.get_easiness()
        return score
    elif player_choice == 2:
        score = card.get_versatility()
        return score
    elif player_choice == 3:
        score = card.get_use()
        return score
    else:
        score = card.get_optimisation()
        return score


def compare_with_computer(score, attribute, computer_choice):
    if attribute == 1:
        computer_score = computer_choice.get_easiness()
    elif attribute == 2:
        computer_score = computer_choice.get_versatility()
    elif attribute == 3:
        computer_score = computer_choice.get_use()
    else:
        computer_score = computer_choice.get_optimisation()
    if score < computer_score:
        return "computer"
    elif score > computer_score:
        return "player"
    else:
        return "draw"


python = Card("Python", 9, 7, 7, 3)
c = Card("C", 2, 8, 9, 10)
csharp = Card("C#", 6, 6, 9, 8)
cpp = Card("C++", 2, 9, 8, 9)
assembly = Card("Assembly", 1, 5, 7, 10)
javascript = Card("JavaScript", 7, 9, 9, 5)
java = Card("Java", 6, 8, 9, 7)
go = Card("Go", 8, 7, 6, 5)
card_deck = [python, c, csharp, cpp, assembly, javascript, java, go]
computer_points = 0
player_points = 0
max_points = 5

while computer_points < max_points and player_points < max_points:
    player_card = set_player_card(card_deck)
    opponent_card = set_opponent_card(card_deck)
    choice = choose_attribute(player_card)
    player_score = calculate_score(player_card, choice)
    result = compare_with_computer(player_score, choice, opponent_card)
    if result == "player":
        player_points += 1
        if player_points < max_points: print("You won that round")
    elif result == "computer":
        computer_points += 1
        if computer_points < max_points: print("You lost that round")
    else:
        print("That round was a draw")

if player_points == max_points:
    print("You won")
else:
    print("You lost")
