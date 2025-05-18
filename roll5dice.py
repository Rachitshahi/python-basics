import random
c = 0
def rolldice():
  return random.randint(1,6)
sum=0
for i in range(5):
  dice_roll = rolldice()
  print(f"Dice_roll {i+1}:{dice_roll}")
  sum+=dice_roll
print(f"final number = {sum}")