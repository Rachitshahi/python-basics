class Person:
  def __init__(self,name):
    self.name = name
  def greet(self):
    print(f"hello my name is {name}. ")
#creating an object
p= Person('Alice')
p.greet()