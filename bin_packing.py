#import driver
import random
import math
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
    rectangles.sort(key=lambda tup: tup[1], reverse=True)

    lowest_legal_height = []
    widthGuess = round(guess_good_width(rectangles))


    for i in range (0,widthGuess):
        lowest_legal_height.append(0)
    placement = []
    upper_left_x = 0
    upper_left_y = 0
    forward_pass = True
    for rectangle in rectangles:
        cur_rect_width = rectangle[0]
        cur_rect_height = rectangle[1]

        if(forward_pass):
            if(upper_left_x+cur_rect_width>=widthGuess):#reached the end of the line on forward pass
                upper_left_x = widthGuess-1- cur_rect_width
                upper_left_y = lowest_legal_height_in_width_range(upper_left_x,widthGuess-1,lowest_legal_height)
                forward_pass = not forward_pass
                coordinate = (upper_left_x, upper_left_y)   # make a tuple
                placement.append(coordinate)             # insert tuple at front of list
                
                #update lowest_legal_height
                for i in range(upper_left_x,upper_left_x+cur_rect_width):
                    lowest_legal_height[i] = upper_left_y+cur_rect_height
            else:#regular placement
                upper_left_y = lowest_legal_height_in_width_range(upper_left_x,upper_left_x+cur_rect_width,lowest_legal_height)
                coordinate = (upper_left_x, upper_left_y)   # make a tuple
                placement.append( coordinate)             # insert tuple at front of list

                #update lowest_legal_height
                for i in range(upper_left_x,upper_left_x+cur_rect_width):
                    lowest_legal_height[i] = upper_left_y+cur_rect_height
                
                #update upper_left_x for next rect
                upper_left_x += cur_rect_width
                
        else: #backward pass
            if(upper_left_x-cur_rect_width<1):#reached the end of the line on backward pass
                upper_left_x = 0
                upper_left_y = lowest_legal_height_in_width_range(upper_left_x,upper_left_x+cur_rect_width,lowest_legal_height)
                coordinate = (upper_left_x, upper_left_y)   # make a tuple
                placement.append( coordinate)             # insert tuple at front of list
                
                #update lowest_legal_height
                for i in range(upper_left_x,upper_left_x+cur_rect_width):
                    lowest_legal_height[i] = upper_left_y+cur_rect_height

                upper_left_x += cur_rect_width
                forward_pass = not forward_pass
                
                
            else:#regular placement
                upper_left_x = upper_left_x - cur_rect_width
                upper_left_y = lowest_legal_height_in_width_range(upper_left_x,upper_left_x+cur_rect_width,lowest_legal_height)
                coordinate = (upper_left_x, upper_left_y)   # make a tuple
                placement.append( coordinate)             # insert tuple at front of list
                
                #update lowest_legal_height
                for i in range(upper_left_x,upper_left_x+cur_rect_width):
                    lowest_legal_height[i] = upper_left_y+cur_rect_height
        #end of loop through rectangles

    return placement



def lowest_legal_height_in_width_range(left,right,llh):
    if(left<0):
        left = 0
    counter = left
    min = -1
    if(right>len(llh)-1):
        right = len(llh)-1
    while(counter<right):
        if min<llh[counter]:
            min = llh[counter]
        counter += 1
    return min

def guess_good_width(rectangles):
    total_area = 0
    area_increase = 1.5
    for rectangle in rectangles:
        total_area += rectangle[0]*rectangle[1]
    guess = math.ceil(math.sqrt(total_area*area_increase))

    return guess