# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

def process_madlib(mad_lib):
    processed = ""
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    #term_length refers to the longest mad libs term (VERB, ADVERB)
    count = 0
    term_length = 4
    while count <= len(mad_lib):
        #catching if the box length would exceed mad_lib string length first
        if count == len(mad_lib) - term_length:
            #loop to shrink the box
            while term_length > 0:
                #box shrinks against length limit
                shrink_box = mad_lib[ -term_length : len(mad_lib) ]
                processed += word_transformer(shrink_box)
                term_length -= 1
            #end fucntion
            return processed
        #print count
        slice = mad_lib[ count : count + term_length]
        #print slice
        processed += word_transformer(slice)
        #print processed
        if len(word_transformer( slice) ) > 1:
            count += term_length
        else:
            count += 1
        #processed += word_transformer(slice)
        #count += 1
        #processed += word_transformer(slice)
        #print processed
    return processed

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
