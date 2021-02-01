age = "27"
print(type(age))

n_age = int(age)
print(type(n_age))

# Make my functions
def say_hello():
  print("hello")
say_hello()

def hi(who) :
  print("Hello "+ who)
hi("sw")

def plus(a,b) :
  print(a+b)
plus(1,2)

#default argument
def hello(name="anonymous"):
  print("Hello " + name)
hello()
hello("sw")

#return
def Rplus(a, b):
  return a+b
test = Rplus(1,4)
print(test)