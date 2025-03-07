import random
def func(word: str):
    print(word)
print(func("word"))

name= "word"
popped_name = list(name)
print(popped_name.pop(random.randint()))
print(popped_name)




# I wanted to randomize the letters in "word", but didn't know how to do that by using pop. I also didn't know how to randomize my function.