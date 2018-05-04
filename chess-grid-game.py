import time
import random

def print_board(white=True):

    # y is file
    # x is rank
    for x in range(1,9):
        for y in range(1,9):
            if white:
                print chr(96+y) + str(9-x),
            else:
                print chr(105-y) + str(x),
        print "\n" # prints two newlines


def print_board_missing(white=True, rank=1, file=1):
    
    assert( rank > 0 and rank < 9 )
    assert( file > 0 and file < 9 )

    if white:
        target_rank = (9-rank)
        target_file = (file)
    else:
        target_rank = (rank)
        target_file = (9-file)
    # y = file
    # x = rank
    for x in range(1,9):
        for y in range(1,9):
            if x == target_rank and y == target_file:
                print "o ",
            else:
                print ". ",
        print "\n" # prints two newlines

def play_game(timeout=60, turns=5):
    assert( timeout > 0 and turns > 0 )

    starting_turns = turns
    start = time.time()
    score = 0
    while time.time() < (start + timeout) and turns > 0:
        print "Score: " + str(score)
        print "Time: " + str(int((start+timeout)-time.time()))
        print "Turns: " + str(turns)
        print "\n"

        turns -= 1
        r = random.randint(1,8)
        f = random.randint(1,8)
        white = bool(random.randint(0,1))
        if white:
            print "White"
        else:
            print "Black"

        print_board_missing(white,r,f)
        guess = ""
        while len(guess) != 2:
            guess = raw_input("> ")
        # TODO Print error or something if input fails to validate
        
        guess_file = ord(guess[0])-96
        guess_rank = int(guess[1])
        

        if guess_rank == r and guess_file == f:
            print "Correct!"
            score += 1
        else:
            print "Incorrect; answer was:"
            print chr(96+f) + str(r)

    print "Final score: " + str(score) + "/" + str(starting_turns) + " ("+ str(round(float(score)/starting_turns,2))+")"

play_game(60,5)
