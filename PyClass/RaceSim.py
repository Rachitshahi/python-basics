import time
import random

# Base Car class
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed  # Speed in units per step
        self.distance_covered = 0
        self.finish_time = None

    def move(self):
        """Move the car forward by its speed (with a bit of randomness)."""
        movement = random.randint(self.speed - 2, self.speed + 2)  # Add variation
        self.distance_covered += max(movement, 1)

# Child classes for different car models
class SportsCar(Car):
    def __init__(self, name):
        super().__init__(name, speed=20)

class Sedan(Car):
    def __init__(self, name):
        super().__init__(name, speed=12)

class SUV(Car):
    def __init__(self, name):
        super().__init__(name, speed=15)

# Initialize race
race_distance = 100
cars = [
    SportsCar("Ferrari"),
    Sedan("Toyota Corolla"),
    SUV("Range Rover"),
    SportsCar("Lamborghini"),
    Sedan("Hyundai Elantra")
]

print("\n🏁 The race has started! 🏁\n")

# Race loop
step = 0
finished = []

while len(finished) < len(cars):
    print(f"\n--- Step {step + 1} ---")
    for car in cars:
        if car not in finished:
            car.move()
            print(f"{car.name} -> {car.distance_covered}/{race_distance} units")

            if car.distance_covered >= race_distance:
                car.finish_time = step
                finished.append(car)
                print(f"🚩 {car.name} has finished the race!")

    step += 1
    time.sleep(1)

# Sort cars by who finished first
finished.sort(key=lambda x: x.finish_time)

# Display final standings
print("\n🏆 Final Race Results:")
for i, car in enumerate(finished, start=1):
    print(f"{i}. {car.name} (Speed: {car.speed}, Finish Time: Step {car.finish_time + 1})")
