import time
import random  # For generating random damage

class Game:
    def __init__(self, player, health, power):
        self.player = player
        self.health = health
        self.power = power

    def attack(self, opponent):
        """Attack another player with randomized damage."""
        damage = random.randint(self.power - 5, self.power + 5)
        opponent.health -= damage
        print(f"{self.player} attacks {opponent.player} for {damage} damage!")
        if opponent.health < 0:
            opponent.health = 0  # Prevent negative health
        print(f"{opponent.player}'s remaining health: {opponent.health}")
        if opponent.health <= 0:
            print(f"{opponent.player} has been defeated!")

    def is_alive(self):
        """Return True if the player is still alive."""
        return self.health > 0

    def show_stats(self):
        """Display current stats of the player."""
        print(f"{self.player} | Health: {self.health} | Power: {self.power}")

# Create two players
a = Game("Hank", 100, 20)
b = Game("Shawn", 100, 30)

print("\n⚔️ Let the battle begin! ⚔️\n")
a.show_stats()
b.show_stats()

# Battle Phase
round_num = 1
while a.is_alive() and b.is_alive():
    print(f"\n🔄 Round {round_num}:")
    a.attack(b)
    if b.is_alive():
        b.attack(a)
    a.show_stats()
    b.show_stats()
    round_num += 1
    time.sleep(1)

# Declare the winner
if a.is_alive():
    print(f"\n🏆 {a.player} wins the battle!")
else:
    print(f"\n🏆 {b.player} wins the battle!")
