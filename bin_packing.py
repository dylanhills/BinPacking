#import driver
import random

"""
FIND_SOLUTION:
    Define this function in BinPacking.py, along with any auxiliary
functions that you need.  Do not change the Driver.py file at all.
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
    w1 = width of rectangle 1,
    l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
         e.g. [(x1, y1), ... (xn, yn)] where
         x1 = top left x coordinate of rectangle 1 placement
         y1 = top left y coordinate of rectangle 1 placement, etc.
         safia
         dylan
"""

def find_solution(rectangles):
    lowest_legal_height = []
    widthGuess = round(guess_good_width(rectangles))

    print("Width Guess: "+str(widthGuess))

    for i in range (0,widthGuess):
        lowest_legal_height.append(0)
    placement = []
    upper_left_x = 0
    upper_left_y = 0

    for rectangle in rectangles:
        cur_rect_width = rectangle[0]
        cur_rect_height = rectangle[1]

        if(cur_rect_width+upper_left_x>widthGuess):
            upper_left_x = 0

        upper_left_y = lowest_legal_height_in_width_range(upper_left_x,upper_left_x+cur_rect_width,lowest_legal_height)

        coordinate = (upper_left_x, upper_left_y)   # make a tuple
        placement.insert(0, coordinate)             # insert tuple at front of list
        
        for i in range(upper_left_x,upper_left_x+cur_rect_width):
            lowest_legal_height[i] = upper_left_y+cur_rect_height
        upper_left_x = upper_left_x + cur_rect_width
        
    placement.reverse()                             # original order
    return placement

def lowest_legal_height_in_width_range(left,right,llh):
    #print(str(llh[0]))
    counter = left
    min = -1
    while(counter<=right):
        if min<llh[counter]:
            min = llh[counter]
        counter += 1
    return min

def guess_good_width(rectangles):
    guess = 0
    for rectangle in rectangles:
        guess+= rectangle[0]
    guess*=10
    guess/=len(rectangles)
    return guess
