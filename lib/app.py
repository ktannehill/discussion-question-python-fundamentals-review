import ipdb

ipdb.set_trace()

def greet(name):
  print(f"Hello, {name}")

greet("Steven") #=> ?

# input name str
# print string "Steven"
# return None if no return statement



def love_this_veggie(vegetable):
  if vegetable == "broccoli":
    return "Nah, thanks"
  else:
    return "I love it!"
  
# input str or anything else, return str



fruits = ["apple", "pear", "face", "champagne", "palm tree", "aardvark", "pineapple"]

# initialize empty list, loop through array, condition if element has substr push
# list comprehension 
    # starts with thing you don't have
    # in thing you do have
    # that meets a condition

fruits_start_with_a = [fruit for fruit in fruits if fruit[0] == "a"]
fruits_start_with_a = [fruit for fruit in fruits if fruit.startswith("a")]



word_count("Hi, isn't this a great and interesting sentence??")
 # => 8

def word_count(str):
  return len(str.split(' '))
# default for split is " " if left out will still do



def friendly_greeting(name=None):
  name = name or "friend"
  print(f"Hey there, {name}")

# None is default, false
# would print "friend" or arg
# no return statement, returns None



best_animal = "cat"
favorite_animal = best_animal
print(favorite_animal)
# => cat



def my_favorite_animal():
  return "cat"

best_animal = my_favorite_animal

print(best_animal)

# function reference
    # <function my_favorite_animal at akjv;IAV>



"Blink" + 182
# TypeError



foods = {
  "pie": "delicious",
  "broccoli": "not delicious",
  "carrots": "not delicious",
  "apples": "delicious",
  "peanut butter": "delicious"
}

# loop through
# evaluate value

# gives back tuples
for food, rating in foods.items():
  if rating == "delicious":
    print(food)
  pass

# cannot modify size of object as you iterate
    # must create a copy
    # modify original
for food, rating in foods.copy().items():
  if rating != "delicious":
    # dictionary at key
    del foods[food]
  pass

# Alternatively: 
els_to_remove = [food for food, rating in food.items() if rating != "delicious"]
for item in els_to_remove:
  # del removes key-value pairs from object
  del foods[item]



character_names = ["Daenerys Targaryen", "Jon Snow" ,"Arya Stark", "Tyrion Lannister", "Sansa Stark", "Cersei Lannister", "Margaery Tyrell"]

def downcase_all(list_of_strings):
  for one_string in list_of_strings:
    one_string.lower()

# no return value, None
    # no implicit returns



# generate random number
# built in random module
import random

# random number between two values
number = random.uniform(a, b)
# random choice from list
choice = random.choice(my_list)
# shuffle a list randomly
random.shuffle(my_list)

def get_random_quote():
    quotes = cooper.get("quotes", [])
    if quotes:
        return random.choice(quotes)
    # return cooper["quotes"][random.randint(0, len(cooper["quotes"]) - 1)]

