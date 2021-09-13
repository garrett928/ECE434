#!/usr/bin/env python3

# Text Based Etch-a-sketch
# Created: 9/12/21
# Author: Garrett Hart

# imports
import curses
import argparse

def main(stdscr):
    # argument setup
    parser = argparse.ArgumentParser(description='Simple Etch-a-sketch game')
    parser.add_argument('-x', type=int, help='Width of screen in chars')
    parser.add_argument('-y', type=int, help='Height of screen in chars')

    # screen constants and vars
    global SCREEN_WIDTH,SCREEN_HEIGHT
    global SCREEN_X, SCREEN_Y
    SCREEN_X = 3
    SCREEN_Y = 1
    Y_SCALE = 1 # scale x and y to make board look better
    X_SCALE = 3
    
    # parse args
    args = parser.parse_args()
    if(args.x and args.y):
        SCREEN_WIDTH = args.x
        SCREEN_HEIGHT = args.y
    else:
        SCREEN_WIDTH = 8
        SCREEN_HEIGHT = 8

    # clear screen and print "board"
    stdscr.clear()

    # print out etch-a-sketch board
    print_board(stdscr)
    stdscr.addstr(SCREEN_Y, SCREEN_X, 'X')

    # main board loop
    while True:
        # this is blocking and will wait for a button
        ch = stdscr.getch()
        if ch == ord('q'): break # exit program
        if ch == ord('c'): print_board(stdscr) # reset board
        if ch == curses.KEY_UP:
            # if we would go into or above first row
            if((SCREEN_Y - 1) <= 0 ):
                continue
            else:
                SCREEN_Y = (SCREEN_Y - 1)
        if ch == curses.KEY_DOWN:
            # if we would go below last row
            if((SCREEN_Y + 1)  > SCREEN_HEIGHT ):
                continue
            else:
                SCREEN_Y = (SCREEN_Y + 1)
        if ch == curses.KEY_RIGHT:
            # if we would go past the last column
            if((SCREEN_X + 1) >= SCREEN_WIDTH ):
                continue
            else:
                SCREEN_X = (SCREEN_X + 1)
        if ch == curses.KEY_LEFT:
            # if we would go past the last column
            if((SCREEN_X - 1) <= 0):
                continue
            else:
                SCREEN_X = (SCREEN_X - 1)



        stdscr.addstr(SCREEN_Y * Y_SCALE, SCREEN_X * X_SCALE, 'X')
        stdscr.refresh()

def print_board(stdscr):
    stdscr.clear()
    for x in range(1,SCREEN_WIDTH):
        # print out board x heading
        stdscr.addstr(0,x*3, str(x))
    for y in range(SCREEN_HEIGHT):
        # print out board y heading
        tmp = str(y) + ':'
        stdscr.addstr(y+1, 0, str(tmp))
    SCREEN_X = 2
    SCREEN_Y = 1
    stdscr.refresh()
    
# doing it this way prevents terminal being left in curses mode
# if program crashes
curses.wrapper(main)

