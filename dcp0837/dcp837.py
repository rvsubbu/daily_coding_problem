#!/usr/bin/env python3

#This problem was asked by Nest.

#Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

#We can consider a sentence valid if it conforms to the following rules:

#The sentence must start with a capital letter, followed by a lowercase letter or a space.
#All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
#There must be a single space between each word.
#The sentence must end with a terminal mark immediately following a word.


import argparse

SPACE = ' '
COMMA = ','
COLON = ':'
SEMICOLON = ';'
PERIOD = '.'
QUESTION_MARK = '?'
BANG = '!'

SEPARATORS = [SPACE, COMMA, COLON, SEMICOLON]
TERMINALS = [PERIOD, QUESTION_MARK, BANG]

def run(sentence):
    '''
    Check sentence for validity based on a few simple rules
    keyword args:
    sentence -- obvious
    '''
    if not sentence:
        return False
    if len(sentence) < 2:  # we need a capital letter to start, and a terminal to end
        return False

    # The sentence must start with a capital letter, followed by a lowercase letter or a space.
    # So we reject a sentence <"A."
    if not sentence[0].isupper():
        return False
    if not sentence[1].islower() and sentence[1] != SPACE:
        return False

    prev = sentence[1]
    for char in sentence[2:-1]:
        # All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
        if not char.islower() and char not in TERMINALS and char not in SEPARATORS:
            #import pdb; pdb.set_trace()
            return False
        # There must be a single space between each word.
        if char == SPACE and prev == SPACE:
            import pdb; pdb.set_trace()
            return False
        prev = char

    # The sentence must end with a terminal mark immediately following a word.
    if prev == SPACE:
        return False
    if sentence[-1] not in TERMINALS:
        return False

    return True

def sanity_test():
    sentence = "This problem was asked by Nest."  # invalid as the word Nest is capitalized
    assert(not run(sentence))

    sentence = "Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences."
    assert(run(sentence))

    sentence = "If a sentence is valid, the program should print it out."
    assert(run(sentence))

    sentence = "We can consider a sentence valid if it conforms to the following rules:"
    assert(not run(sentence))  # Doesn't end in a terminal

    sentence = "The sentence must start with a capital letter, followed by a lowercase letter or a space."
    assert(run(sentence))

    sentence = "All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!)."  # Invalid as it has parantheses
    assert(not run(sentence))  # Doesn't end in a terminal

    sentence = "There must be a single space between each word."
    assert(run(sentence))

    sentence = "The sentence must end with a terminal mark immediately following a word."
    assert(run(sentence))

    print("Sanity tests passed")

def more_tests():
    tests = []
    for test in tests:
        res, sentence = test
        #print("sentence=", sentence, "result=", res)
        assert(run(sentence) == res)
    print("All tests passed")

def test():
    sanity_test()
    more_tests()

def parse_args():
    parser = argparse.ArgumentParser(description = 'Daily Coding Problem 837: Simple sentence validity checker')
    parser.add_argument('-s', '--sentence', help='Sentence to check for validity', type=str)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.sentence:
        print("Result = ", run(args.sentence))
    else:
        # if no args, test
        test()

if __name__ == "__main__":
    main()
