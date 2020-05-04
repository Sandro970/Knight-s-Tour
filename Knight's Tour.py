#Sandro Šafar

from tkinter import *
import time
import operator
import tkinter as tk
from tkinter import messagebox
main_menu=Tk()

bg_image = PhotoImage(file="Background.png")

w = bg_image.width()
h = bg_image.height()

main_menu.geometry("%dx%d+600+300" % (w, h))

cv = Canvas(main_menu,width=w, height=h)
cv.pack(side=TOP, fill=BOTH, expand=True)
cv.create_image(0, 0, image=bg_image, anchor=NW)

main_menu.resizable(False,False)
main_menu.title("Knight's tour ")


# Comment code
# You can start from wherever
# Are you sure you want to quit? - DONE
# Background scoreboard - DONE
# Limit input of name
# Scoreboard trophies like lichess
#
# EASY:
# 1  2  3
# 4  5  6
# 7  8  9
# 10 11 12
#
# MEDIUM:
# 1  2  3  4  5 
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25 
# 26 27 28 29 30
#
# HARD:
# 1  2  3  4  5  6  7  8
# 9  10 11 12 13 14 15 16
# 17 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31 32
# 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48
# 49 50 51 52 53 54 55 56
# 57 58 59 60 61 62 63 64

def no_legal_moves():
    messagebox.showerror(title="Game over!",message="There are no more legal moves! Try again.")
    main_menu.deiconify()

def X_event():
    #stops players from hitting the X button to quit 
    pass

########################################################################################DEFINE_MOVE#########################################################################################################################################

#Move - Easy (4x3)
def move(button):
    target_square=dictionary[button]
    global knight
      
    if knight-target_square != -1 and knight-target_square != -5 and knight-target_square != -7 and knight-target_square != 1 and knight-target_square != 5 and knight-target_square != 7: #if the user doesn't play an L shape move
        global invalid_move
        invalid_move=True
        
    for j in range(0,len(L)):
        if target_square==L[j]:
            if knight == target_square: #if the user clicks his position
               global current_position
               current_position = True
            else:
               global square_visited
               square_visited = True
            
    if knight-target_square == -1 or knight-target_square == 1:
        if knight+target_square != 7 and knight+target_square != 13 and knight+target_square != 19: #exceptions = from 3 to 4 ; from 6 to 7 ; from 9 to 10
            invalid_move=True
    if knight-target_square == -7 or knight-target_square == 7:
        if knight+target_square == 13: #fixing a bug where you could go from 3 to 10 because the difference is 7
            invalid_move=True
        
    if invalid_move == False and current_position == False and square_visited == False: #if the move is legal, move the knight to that square
       button.configure(image=picture, height=79,width=65)

       global picture2
       picture2=PhotoImage(file="Square.png")
       
       list_keys=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12]
       previous_square=list_keys[knight-1] #list_keys starts with 0, not 1
       previous_square.configure(image=picture2,width=65,height=79,bg="red") #paint the last square red
    
       knight=target_square #the new square becomes i
       L.append(target_square) #add to list that checks which squares have been visited
       if len(L) == 12: #win condition - all squares visited
           win_easy()


       if len(L)<12:     #check if there is no more legal moves left by going through the list of visited squares
           is_there_legal_moves = 1
           if knight==1 and 6 in L and 8 in L:
                           is_there_legal_moves = 0
           if knight==2 and 7 in L and 9 in L:
                           is_there_legal_moves = 0
           if knight==3 and 4 in L and 8 in L:
                           is_there_legal_moves = 0
           if knight==4 and 3 in L and 9 in L and 11 in L:
                                   is_there_legal_moves = 0
           if knight==5 and 10 in L and 12 in L:
                           is_there_legal_moves = 0
           if knight==6 and 1 in L and 7 in L and 11 in L:
                                   is_there_legal_moves = 0
           if knight==7 and 2 in L and 6 in L and 12 in L:
                                   is_there_legal_moves = 0
           if knight==8 and 3 in L and 1 in L:
                           is_there_legal_moves = 0
           if knight==9 and 2 in L and 4 in L and 10 in L:
                                   is_there_legal_moves = 0
           if knight==10 and 5 in L and 9 in L:
                           is_there_legal_moves = 0
           if knight==11 and 4 in L and 6 in L:
                           is_there_legal_moves = 0
           if knight==12 and 5 in L and 7 in L:
                           is_there_legal_moves = 0
                           
           if is_there_legal_moves == 0: #if there is no more legal moves
               no_legal_moves()
               easy_game.withdraw() #the game ends

    if current_position==True:
        messagebox.showinfo(title="Notice", message="This is your current position.")
    elif invalid_move==True:
        messagebox.showerror(title="ERROR", message="That move is not legal!")
    elif square_visited==True:
        messagebox.showerror(title="ERROR", message="You have already visited that square!")
        
    current_position=False #reset for next move
    invalid_move=False
    square_visited=False

#Move - Medium(6x5)
def move1(button):
    target_square=dictionary1[button]
    global knight

    #if the user doesn't play an L shape move
    if knight-target_square != -7 and knight-target_square != -3 and knight-target_square != -11 and knight-target_square != -9 and knight-target_square != 3 and knight-target_square != 11 and knight-target_square != 9 and knight-target_square != 7:
        global invalid_move
        invalid_move=True

        
    for j in range(0,len(L1)):
        if target_square==L1[j]:
            if knight == target_square: #if the user clicks his position
               global current_position
               current_position=True
            else: #user has already been here
                global square_visited
                square_visited=True
        
    #checking for illegal moves
    if target_square==1 or target_square==6 or target_square==11 or target_square==16 or target_square==21 or target_square==26:
        if knight+target_square == 5 or knight+target_square == 11 or knight+target_square == 15 or knight+target_square == 21 or knight+target_square == 25 or knight+target_square == 31 or knight+target_square == 35 or knight+target_square == 41 or knight+target_square == 45 or knight+target_square == 51 or knight+target_square == 55:
            invalid_move=True
    if target_square==2 or target_square==7 or target_square==12 or target_square==17 or target_square==22 or target_square==27:
        if knight+target_square == 7 or knight+target_square == 17 or knight+target_square == 27 or knight+target_square == 37 or knight+target_square == 47 or knight+target_square == 57:
            invalid_move=True
    if target_square==4 or target_square==9 or target_square==14 or target_square==19 or target_square==24 or target_square==29:
        if knight+target_square == 5 or knight+target_square == 15 or knight+target_square == 25 or knight+target_square == 35 or knight+target_square == 45 or knight+target_square == 55:
            invalid_move=True
    if target_square==5 or target_square==10 or target_square==15 or target_square==20 or target_square==22 or target_square==30:
        if knight+target_square == 7 or target_square==11 or knight+target_square == 17 or target_square==21 or knight+target_square == 27 or target_square==31 or knight+target_square == 37 or target_square==41 or knight+target_square == 47 or target_square==51 or knight+target_square == 57:
            invalid_move=True
    

    
    if invalid_move == False and current_position == False: #if the move is legal
       button.configure(image=picture, height=79,width=65)

       picture2=PhotoImage(file="Square.png")

       list_keys=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26,button27,button28,button29,button30]
       previous_square=list_keys[knight-1]
       previous_square.configure(image=picture2,width=65,height=79,bg="red") 
    
       knight=target_square
       L1.append(target_square)
       
       if len(L1) == 30:
           win_medium()
           
       if len(L1)<30:
           
           is_there_legal_moves1 = 1
           
           if knight==1 and 8 in L1 and 12 in L1:
                           is_there_legal_moves1 = 0
           if knight==5 and 8 in L1 and 14 in L1:
                           is_there_legal_moves1 = 0    
           if knight==26 and 17 in L1 and 23 in L1:
                           is_there_legal_moves1 = 0
           if knight==30 and 19 in L1 and 23 in L1:
                           is_there_legal_moves1 = 0              
           if knight==2 and 9 in L1 and 11 in L1 and 13 in L1:
                           is_there_legal_moves1 = 0
           if knight==4 and 7 in L1 and 13 in L1 and 15 in L1:
                           is_there_legal_moves1 = 0
           if knight==6 and 3 in L1 and 13 in L1 and 17 in L1:
                           is_there_legal_moves1 = 0
           if knight==10 and 3 in L1 and 13 in L1 and 19 in L1:
                           is_there_legal_moves1 = 0
           if knight==25 and 14 in L1 and 18 in L1 and 28 in L1:
                           is_there_legal_moves1 = 0
           if knight==29 and 18 in L1 and 20 in L1 and 22 in L1:
                           is_there_legal_moves1 = 0
           if knight==27 and 16 in L1 and 18 in L1 and 24 in L1:
                           is_there_legal_moves1 = 0
           if knight==21 and 12 in L1 and 18 in L1 and 28 in L1:
                           is_there_legal_moves1 = 0
           if knight==3 and 6 in L1 and 12 in L1 and 14 in L1 and 10 in L1:
                           is_there_legal_moves1 = 0
           if knight==11 and 2 in L1 and 8 in L1 and 18 in L1 and 22 in L1:
                           is_there_legal_moves1 = 0
           if knight==16 and 7 in L1 and 13 in L1 and 23 in L1 and 27 in L1:
                           is_there_legal_moves1 = 0
           if knight==28 and 17 in L1 and 19 in L1 and 21 in L1 and 25 in L1:
                           is_there_legal_moves1 = 0
           if knight==20 and 9 in L1 and 13 in L1 and 23 in L1 and 29 in L1:
                           is_there_legal_moves1 = 0
           if knight==15 and 4 in L1 and 8 in L1 and 18 in L1 and 24 in L1:
                           is_there_legal_moves1 = 0
           if knight==7 and 4 in L1 and 14 in L1 and 16 in L1 and 18 in L1:
                           is_there_legal_moves1 = 0
           if knight==9 and 2 in L1 and 12 in L1 and 18 in L1 and 20 in L1:
                           is_there_legal_moves1 = 0
           if knight==22 and 11 in L1 and 13 in L1 and 19 in L1 and 29 in L1:
                           is_there_legal_moves1 = 0
           if knight==24 and 13 in L1 and 15 in L1 and 17 in L1 and 27 in L1:
                           is_there_legal_moves1 = 0
           if knight==15 and 4 in L1 and 8 in L1 and 18 in L1 and 24 in L1:
                           is_there_legal_moves1 = 0
           if knight==8 and 1 in L1 and 5 in L1 and 11 in L1 and 15 in L1 and 17 in L1 and 19 in L1:
                           is_there_legal_moves1 = 0
           if knight==23 and 12 in L1 and 14 in L1 and 16 in L1 and 20 in L1 and 26 in L1 and 30 in L1:
                           is_there_legal_moves1 = 0
           if (knight==12 or knight==17) and knight-11 in L1 and knight-9 in L1 and knight-3 in L1 and knight+7 in L1 and knight+11 in L1 and knight+9 in L1:
                           is_there_legal_moves1 = 0
           if (knight==14 or knight==19) and knight-11 in L1 and knight-9 in L1 and knight+3 in L1 and knight-7 in L1 and knight+11 in L1 and knight+9 in L1:
                           is_there_legal_moves1 = 0
           if (knight==13 or knight==18) and knight-11 in L1 and knight-9 in L1 and knight-3 in L1 and knight+7 in L1 and knight+11 in L1 and knight+9 in L1 and knight+3 in L1 and knight-7 in L1:
                           is_there_legal_moves1 = 0

           if is_there_legal_moves1==0: #if there is no more legal moves
               no_legal_moves()
               medium_game.withdraw() #the game ends

    if current_position==True:
        messagebox.showinfo(title="Notice", message="This is your current position.")
    elif invalid_move==True:
        messagebox.showerror(title="ERROR", message="That move is not legal!")
    elif square_visited==True:
        messagebox.showerror(title="ERROR", message="You have already visited that square!")
    current_position=False
    invalid_move=False
    square_visited=False

#Move - hard(8x8)
def move2(button):
    target_square=dictionary2[button]
    global knight
    if knight-target_square != 6:
        if knight-target_square != 10:
            if knight-target_square != 15:
                if knight-target_square != 17:
                    if knight-target_square != -6:
                        if knight-target_square != -10:
                            if knight-target_square != -15:
                                if knight-target_square != -17:
                                  global invalid_move
                                  invalid_move=True
                                else:
                                    if knight+target_square == 33 or knight+target_square == 49 or knight+target_square == 65 or knight+target_square == 81 or knight+target_square == 97:
                                        invalid_move=True
                            else:
                                 if knight+target_square == 17 or knight+target_square == 33 or knight+target_square == 49 or knight+target_square == 65 or knight+target_square == 81 or knight+target_square == 97 or knight+target_square == 113:
                                      invalid_move=True
                        else:
                            if knight+target_square == 24 or knight+target_square == 26 or knight+target_square == 40 or knight+target_square == 42 or knight+target_square == 56 or knight+target_square == 58 or knight+target_square == 72 or knight+target_square == 74 or knight+target_square == 88 or knight+target_square == 90 or knight+target_square == 104 or knight+target_square == 106:
                                invalid_move=True
                    else:
                        if knight+target_square == 8 or knight+target_square == 10 or knight+target_square == 24 or knight+target_square == 26 or knight+target_square == 40 or knight+target_square == 42 or knight+target_square == 56 or knight+target_square == 58 or knight+target_square == 72 or knight+target_square == 74 or knight+target_square == 88 or knight+target_square == 90 or knight+target_square == 104 or knight+target_square == 106 or knight+target_square == 120 or knight+target_square == 122:
                            invalid_move=True
                else:
                    if knight+target_square == 33 or knight+target_square == 49 or knight+target_square == 65 or knight+target_square == 81 or knight+target_square == 97:
                        invalid_move=True
            else:
                if knight+target_square == 17 or knight+target_square == 33 or knight+target_square == 49 or knight+target_square == 65 or knight+target_square == 81 or knight+target_square == 97 or knight+target_square == 113:
                    invalid_move=True
        else:
             if knight+target_square == 24 or knight+target_square == 26 or knight+target_square == 40 or knight+target_square == 42 or knight+target_square == 56 or knight+target_square == 58 or knight+target_square == 72 or knight+target_square == 74 or knight+target_square == 88 or knight+target_square == 90 or knight+target_square == 104 or knight+target_square == 106:
                 invalid_move=True
    else:
         if knight+target_square == 8 or knight+target_square == 10 or knight+target_square == 24 or knight+target_square == 26 or knight+target_square == 40 or knight+target_square == 42 or knight+target_square == 56 or knight+target_square == 58 or knight+target_square == 72 or knight+target_square == 74 or knight+target_square == 88 or knight+target_square == 90 or knight+target_square == 104 or knight+target_square == 106 or knight+target_square == 120 or knight+target_square == 122:
             invalid_move=True
        
                                
        
    for j in range(0,len(L2)):
        if target_square==L2[j]:
            if knight==target_square:
               global current_position
               current_position=True
            else:
                global square_visited
                square_visited=True
        
    if invalid_move == False and current_position == False and square_visited == False:
       button.configure(image=picture, height=79,width=65)

       picture2=PhotoImage(file="Square.png")

       list_keys=[button1,button2,button3,button4,button5,button6,button7,button8,button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26,button27,button28,button29,button30,button31,button32,button33,button34,button35,button36,button37,button38,button39,button40,button41,button42,button43,button44,button45,button46,button47,button48,button49,button50,button51,button52,button53,button54,button55,button56,button57,button58,button59,button60,button61,button62,button63,button64]
       previous_square=list_keys[knight-1]
       previous_square.configure(image=picture2,width=65,height=79,bg="red") 
        
       
       knight=target_square       
       L2.append(target_square)
       if len(L2) == 64:
           win_hard()

    ####
       if len(L2)<64:
           is_there_legal_moves2 = 1
           if knight == 1 and knight+17 in L2 and knight+10 in L2:
               is_there_legal_moves2 = 0
           if knight == 2 and knight+15 in L2 and knight+10 in L2 and knight+17 in L2:
               is_there_legal_moves2 = 0
           if (knight == 3 or knight == 4 or knight == 5 or knight == 6) and knight+6 in L2 and knight+10 in L2 and knight+15 in L2 and knight+17 in L2:
               is_there_legal_moves2 = 0
           if knight == 7 and knight+15 in L2 and knight+6 in L2 and knight+17 in L2:
               is_there_legal_moves2 = 0
           if knight == 8 and knight+15 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0
           if knight == 9 and knight+17 in L2 and knight+10 in L2 and knight-6 in L2:
               is_there_legal_moves2 = 0                       
           if (knight == 17 or knight == 25 or knight == 33 or knight == 41) and knight-6 in L2 and knight+10 in L2 and knight-15 in L2 and knight+17 in L2:
               is_there_legal_moves2 = 0
           if knight == 49 and knight-15 in L2 and knight-6 in L2 and knight+10 in L2:
               is_there_legal_moves2 = 0
           if knight == 57 and knight-15 in L2 and knight-6 in L2:
               is_there_legal_moves2 = 0
           if knight == 58 and knight-15 in L2 and knight-17 in L2 and knight-6 in L2:
               is_there_legal_moves2 = 0
           if knight == 63 and knight-15 in L2 and knight-10 in L2 and knight-17 in L2:
               is_there_legal_moves2 = 0
           if knight == 56 and knight-17 in L2 and knight-10 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0
           if knight == 16 and knight+15 in L2 and knight+6 in L2 and knight-10 in L2:
               is_there_legal_moves2 = 0
           if knight == 64 and knight-10 in L2 and knight-17 in L2:
               is_there_legal_moves2 = 0
           if (knight == 24 or knight == 48 or knight == 32 or knight == 40)  and knight-17 in L2 and knight-10 in L2 and knight+15 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0
           if (knight == 59 or knight == 60 or knight == 61 or knight == 62)  and knight-17 in L2 and knight-10 in L2 and knight-15 in L2 and knight-6 in L2:
               is_there_legal_moves2 = 0
           if knight == 10 and knight+10 in L2 and knight+17 in L2 and knight+15 in L2 and knight-6 in L2:
               is_there_legal_moves2 = 0
           if knight == 15 and knight+17 in L2 and knight-10 in L2 and knight+15 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0
           if knight == 50 and knight+10 in L2 and knight-17 in L2 and knight-15 in L2 and knight-6 in L2:
               is_there_legal_moves2 = 0
           if knight == 55 and knight-10 in L2 and knight-17 in L2 and knight-15 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0   
           if (knight == 51 or knight == 52 or knight == 53 or knight == 54)  and knight-17 in L2 and knight+10 in L2 and knight-15 in L2 and knight-6 in L2 and knight-10 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0
           if (knight == 18 or knight == 26 or knight == 42 or knight == 34)  and knight-17 in L2 and knight+10 in L2 and knight-15 in L2 and knight-6 in L2 and knight+17 in L2 and knight+15 in L2:
               is_there_legal_moves2 = 0
           if (knight == 11 or knight == 12 or knight == 13 or knight == 14)  and knight+17 in L2 and knight+10 in L2 and knight+15 in L2 and knight-6 in L2 and knight-10 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0
               
           if (knight == 23 or knight == 31 or knight == 39 or knight == 47)  and knight-17 in L2 and knight-10 in L2 and knight-15 in L2 and knight+6 in L2 and knight+17 in L2 and knight+15 in L2:
               is_there_legal_moves2 = 0
               
           if (knight == 19 or knight==20 or knight==21 or knight==22 or knight==27 or knight==28 or knight==29 or knight==30 or knight == 35 or knight==36 or knight==37 or knight == 38 or knight == 43 or knight == 44 or knight == 45 or knight == 46) and knight-17 in L2 and knight+17 in L2 and knight-15 in L2 and knight+15 in L2 and knight-10 in L2 and knight+10 in L2 and knight-6 in L2 and knight+6 in L2:
               is_there_legal_moves2 = 0

           if is_there_legal_moves2 == 0:
               no_legal_moves()
               hard_game.withdraw()                                                                

    if current_position==True:
        messagebox.showinfo(title="Notice", message="This is your current position.")
    elif invalid_move==True:
        messagebox.showerror(title="ERROR", message="That move is not legal!")
    elif square_visited==True:
        messagebox.showerror(title="ERROR", message="You have already visited that square!")
    current_position=False
    invalid_move=False
    square_visited=False

########################################################################################CREATE_GAME#########################################################################################################################################
#Create game - Easy(4x3)

def create_easy_game():
    main_menu.withdraw()
    global knight
    knight = 1
    
    global current_position
    current_position=False
    
    global invalid_move
    invalid_move=False

    global square_visited
    square_visited=False
    
    global L
    L=[1]
    
    global easy_game
    easy_game=tk.Toplevel(main_menu)
    easy_game.resizable(False,False)
    easy_game.protocol("WM_DELETE_WINDOW", X_event)
    
    global picture
    picture=PhotoImage(file="Knight.png")
    
    buttons=StringVar()

    global button1
    button1=Button(easy_game,command=lambda:move(button1))
    button1.configure(image=picture,height=79, width=65, bg="brown")
    button1.grid(row=1,column=1)

    global button2               
    button2=Button(easy_game, height=5, width=9,command=lambda:move(button2))
    button2.grid(row=1,column=2)

    global button3               
    button3=Button(easy_game, height=5, width=9,command=lambda:move(button3))
    button3.configure(bg="brown")
    button3.grid(row=1,column=3)

    global button4               
    button4=Button(easy_game, height=5, width=9,command=lambda:move(button4))
    button4.grid(row=2,column=1)

    global button5               
    button5=Button(easy_game, height=5, width=9,command=lambda:move(button5))
    button5.configure(bg="brown")
    button5.grid(row=2,column=2)

    global button6               
    button6=Button(easy_game, height=5, width=9,command=lambda:move(button6))
    button6.grid(row=2,column=3)

    global button7               
    button7=Button(easy_game, height=5, width=9,command=lambda:move(button7))
    button7.configure(bg="brown")
    button7.grid(row=3,column=1)

    global button8
    button8=Button(easy_game, height=5, width=9,command=lambda:move(button8))
    button8.grid(row=3,column=2)

    global button9               
    button9=Button(easy_game, height=5, width=9,command=lambda:move(button9))
    button9.configure(bg="brown")
    button9.grid(row=3,column=3)

    global button10               
    button10=Button(easy_game, height=5, width=9,command=lambda:move(button10))
    button10.grid(row=4,column=1)

    global button11               
    button11=Button(easy_game, height=5, width=9,command=lambda:move(button11))
    button11.configure(bg="brown")
    button11.grid(row=4,column=2)

    global button12               
    button12=Button(easy_game, height=5, width=9,command=lambda:move(button12))
    button12.grid(row=4,column=3)
  
    global dictionary
    dictionary={button1:1,button2:2,button3:3,button4:4,button5:5,button6:6,button7:7,button8:8,button9:9,button10:10,button11:11,button12:12}

    global start
    start = time.time()


    knight=1
    
#Create game - Medium (6x5)
def create_medium_game():
    main_menu.withdraw()
    
    global knight
    knight=1
    
    global current_position
    current_position=False
    
    global invalid_move
    invalid_move=False

    global square_visited
    square_visited=False
    
    
    global L1
    L1=[1]

    global medium_game
    medium_game=tk.Toplevel(main_menu)
    medium_game.resizable(False,False)
    medium_game.protocol("WM_DELETE_WINDOW", X_event)
    
    global picture
    picture=PhotoImage(file="Knight.png")
    
    buttons=StringVar()

    global button1
    button1=Button(medium_game,command=lambda:move2(button1))
    button1=Button(medium_game, height=5, width=9,command=lambda:move1(button1))
    button1.configure(image=picture,height=79,width=65,bg="brown")
    button1.grid(row=1,column=1)

    global button2               
    button2=Button(medium_game, height=5, width=9,command=lambda:move1(button2))
    button2.grid(row=1,column=2)

    global button3               
    button3=Button(medium_game, height=5, width=9,command=lambda:move1(button3))
    button3.configure(bg="brown")
    button3.grid(row=1,column=3)

    global button4               
    button4=Button(medium_game, height=5, width=9,command=lambda:move1(button4))
    button4.grid(row=1,column=4)

    global button5               
    button5=Button(medium_game, height=5, width=9,command=lambda:move1(button5))
    button5.configure(bg="brown")
    button5.grid(row=1,column=5)

    global button6               
    button6=Button(medium_game, height=5, width=9,command=lambda:move1(button6))
    button6.grid(row=2,column=1)

    global button7               
    button7=Button(medium_game, height=5, width=9,command=lambda:move1(button7))
    button7.configure(bg="brown")
    button7.grid(row=2,column=2)

    global button8
    button8=Button(medium_game, height=5, width=9,command=lambda:move1(button8))
    button8.grid(row=2,column=3)

    global button9               
    button9=Button(medium_game, height=5, width=9,command=lambda:move1(button9))
    button9.configure(bg="brown")
    button9.grid(row=2,column=4)

    global button10               
    button10=Button(medium_game, height=5, width=9,command=lambda:move1(button10))
    button10.grid(row=2,column=5)

    global button11               
    button11=Button(medium_game, height=5, width=9,command=lambda:move1(button11))
    button11.configure(bg="brown")
    button11.grid(row=3,column=1)

    global button12               
    button12=Button(medium_game, height=5, width=9,command=lambda:move1(button12))
    button12.grid(row=3,column=2)

    global button13               
    button13=Button(medium_game, height=5, width=9,command=lambda:move1(button13))
    button13.configure(bg="brown")
    button13.grid(row=3,column=3)

    global button14               
    button14=Button(medium_game, height=5, width=9,command=lambda:move1(button14))
    button14.grid(row=3,column=4)

    global button15               
    button15=Button(medium_game, height=5, width=9,command=lambda:move1(button15))
    button15.configure(bg="brown")
    button15.grid(row=3,column=5)
    
    global button16               
    button16=Button(medium_game, height=5, width=9,command=lambda:move1(button16))
    button16.grid(row=4,column=1)
    
    global button17               
    button17=Button(medium_game, height=5, width=9,command=lambda:move1(button17))
    button17.configure(bg="brown")
    button17.grid(row=4,column=2)
    
    global button18               
    button18=Button(medium_game, height=5, width=9,command=lambda:move1(button18))
    button18.grid(row=4,column=3)
    
    global button19               
    button19=Button(medium_game, height=5, width=9,command=lambda:move1(button19))
    button19.configure(bg="brown")
    button19.grid(row=4,column=4)
    
    global button20               
    button20=Button(medium_game, height=5, width=9,command=lambda:move1(button20))
    button20.grid(row=4,column=5)
    
    global button21               
    button21=Button(medium_game, height=5, width=9,command=lambda:move1(button21))
    button21.configure(bg="brown")
    button21.grid(row=5,column=1)
    
    global button22               
    button22=Button(medium_game, height=5, width=9,command=lambda:move1(button22))
    button22.grid(row=5,column=2)
    
    global button23               
    button23=Button(medium_game, height=5, width=9,command=lambda:move1(button23))
    button23.configure(bg="brown")
    button23.grid(row=5,column=3)
    
    global button24               
    button24=Button(medium_game, height=5, width=9,command=lambda:move1(button24))
    button24.grid(row=5,column=4)
    
    global button25               
    button25=Button(medium_game, height=5, width=9,command=lambda:move1(button25))
    button25.configure(bg="brown")
    button25.grid(row=5,column=5)
    
    global button26               
    button26=Button(medium_game, height=5, width=9,command=lambda:move1(button26))
    button26.grid(row=6,column=1)
    
    global button27               
    button27=Button(medium_game, height=5, width=9,command=lambda:move1(button27))
    button27.configure(bg="brown")
    button27.grid(row=6,column=2)
    
    global button28               
    button28=Button(medium_game, height=5, width=9,command=lambda:move1(button28))
    button28.grid(row=6,column=3)
    
    global button29               
    button29=Button(medium_game, height=5, width=9,command=lambda:move1(button29))
    button29.configure(bg="brown")
    button29.grid(row=6,column=4)
    
    global button30           
    button30=Button(medium_game, height=5, width=9,command=lambda:move1(button30))
    button30.grid(row=6,column=5)

    global dictionary1
    dictionary1={button1:1,button2:2,button3:3,button4:4,button5:5,button6:6,button7:7,
                   button8:8,button9:9,button10:10,button11:11,button12:12,button13:13,
                   button14:14,button15:15,button16:16,button17:17,button18:18,button19:19,
                   button20:20,button21:21,button22:22,button23:23,button24:24,button25:25,
                   button26:26,button27:27,button28:28,button29:29,button30:30}

    global start
    start = time.time()

#Create game - Hard (8x8)
def create_hard_game():
    main_menu.withdraw()
    global knight
    knight=5
    
    global current_position
    current_position=False
    
    global invalid_move
    invalid_move=False

    global square_visited
    square_visited=False
    
    global L2
    L2=[5]

    global hard_game
    hard_game=tk.Toplevel(main_menu)
    hard_game.resizable(False,False)
    hard_game.protocol("WM_DELETE_WINDOW", X_event)
    
    global picture
    picture=PhotoImage(file="Knight.png")
    
    buttons=StringVar()

    global button1
    button1=Button(hard_game,command=lambda:move2(button1))
    button1=Button(hard_game, height=5, width=9,command=lambda:move2(button1))
    button1.configure(bg="brown")
    button1.grid(row=1,column=1)

    global button2               
    button2=Button(hard_game, height=5, width=9,command=lambda:move2(button2))
    button2.grid(row=1,column=2)

    global button3               
    button3=Button(hard_game, height=5, width=9,command=lambda:move2(button3))
    button3.configure(bg="brown")
    button3.grid(row=1,column=3)

    global button4               
    button4=Button(hard_game, height=5, width=9,command=lambda:move2(button4))
    button4.grid(row=1,column=4)

    global button5               
    button5=Button(hard_game, height=5, width=9,command=lambda:move2(button5))
    button5.configure(image=picture,height=79, width=65, bg="brown")
    button5.grid(row=1,column=5)

    global button6               
    button6=Button(hard_game, height=5, width=9,command=lambda:move2(button6))
    button6.grid(row=1,column=6)

    global button7               
    button7=Button(hard_game, height=5, width=9,command=lambda:move2(button7))
    button7.configure(bg="brown")
    button7.grid(row=1,column=7)

    global button8
    button8=Button(hard_game, height=5, width=9,command=lambda:move2(button8))
    button8.grid(row=1,column=8)

    global button9               
    button9=Button(hard_game, height=5, width=9,command=lambda:move2(button9))
    button9.grid(row=2,column=1)

    global button10               
    button10=Button(hard_game, height=5, width=9,command=lambda:move2(button10))
    button10.configure(bg="brown")
    button10.grid(row=2,column=2)

    global button11               
    button11=Button(hard_game, height=5, width=9,command=lambda:move2(button11))
    button11.grid(row=2,column=3)

    global button12               
    button12=Button(hard_game, height=5, width=9,command=lambda:move2(button12))
    button12.configure(bg="brown")
    button12.grid(row=2,column=4)

    global button13               
    button13=Button(hard_game, height=5, width=9,command=lambda:move2(button13))
    button13.grid(row=2,column=5)

    global button14               
    button14=Button(hard_game, height=5, width=9,command=lambda:move2(button14))
    button14.configure(bg="brown")
    button14.grid(row=2,column=6)

    global button15               
    button15=Button(hard_game, height=5, width=9,command=lambda:move2(button15))
    button15.grid(row=2,column=7)
    
    global button16               
    button16=Button(hard_game, height=5, width=9,command=lambda:move2(button16))
    button16.configure(bg="brown")
    button16.grid(row=2,column=8)
    
    global button17               
    button17=Button(hard_game, height=5, width=9,command=lambda:move2(button17))
    button17.configure(bg="brown")
    button17.grid(row=3,column=1)
    
    global button18               
    button18=Button(hard_game, height=5, width=9,command=lambda:move2(button18))
    button18.grid(row=3,column=2)
    
    global button19               
    button19=Button(hard_game, height=5, width=9,command=lambda:move2(button19))
    button19.configure(bg="brown")
    button19.grid(row=3,column=3)
    
    global button20               
    button20=Button(hard_game, height=5, width=9,command=lambda:move2(button20))
    button20.grid(row=3,column=4)
    
    global button21               
    button21=Button(hard_game, height=5, width=9,command=lambda:move2(button21))
    button21.configure(bg="brown")
    button21.grid(row=3,column=5)
    
    global button22               
    button22=Button(hard_game, height=5, width=9,command=lambda:move2(button22))
    button22.grid(row=3,column=6)
    
    global button23               
    button23=Button(hard_game, height=5, width=9,command=lambda:move2(button23))
    button23.configure(bg="brown")
    button23.grid(row=3,column=7)
    
    global button24               
    button24=Button(hard_game, height=5, width=9,command=lambda:move2(button24))
    button24.grid(row=3,column=8)
    
    global button25               
    button25=Button(hard_game, height=5, width=9,command=lambda:move2(button25))
    button25.grid(row=4,column=1)
    
    global button26               
    button26=Button(hard_game, height=5, width=9,command=lambda:move2(button26))
    button26.configure(bg="brown")
    button26.grid(row=4,column=2)
    
    global button27               
    button27=Button(hard_game, height=5, width=9,command=lambda:move2(button27))
    button27.grid(row=4,column=3)
    
    global button28               
    button28=Button(hard_game, height=5, width=9,command=lambda:move2(button28))
    button28.configure(bg="brown")
    button28.grid(row=4,column=4)
    
    global button29               
    button29=Button(hard_game, height=5, width=9,command=lambda:move2(button29))
    button29.grid(row=4,column=5)
    
    global button30           
    button30=Button(hard_game, height=5, width=9,command=lambda:move2(button30))
    button30.configure(bg="brown")
    button30.grid(row=4,column=6)
    
    global button31               
    button31=Button(hard_game, height=5, width=9,command=lambda:move2(button31))
    button31.grid(row=4,column=7)
    
    global button32               
    button32=Button(hard_game, height=5, width=9,command=lambda:move2(button32))
    button32.configure(bg="brown")
    button32.grid(row=4,column=8)
    
    global button33               
    button33=Button(hard_game, height=5, width=9,command=lambda:move2(button33))
    button33.configure(bg="brown")
    button33.grid(row=5,column=1)
    
    global button34               
    button34=Button(hard_game, height=5, width=9,command=lambda:move2(button34))
    button34.grid(row=5,column=2)
    
    global button35               
    button35=Button(hard_game, height=5, width=9,command=lambda:move2(button35))
    button35.configure(bg="brown")
    button35.grid(row=5,column=3)
    
    global button36               
    button36=Button(hard_game, height=5, width=9,command=lambda:move2(button36))
    button36.grid(row=5,column=4)
    
    global button37               
    button37=Button(hard_game, height=5, width=9,command=lambda:move2(button37))
    button37.configure(bg="brown")
    button37.grid(row=5,column=5)
    
    global button38               
    button38=Button(hard_game, height=5, width=9,command=lambda:move2(button38))
    button38.grid(row=5,column=6)
    
    global button39               
    button39=Button(hard_game, height=5, width=9,command=lambda:move2(button39))
    button39.configure(bg="brown")
    button39.grid(row=5,column=7)
    
    global button40               
    button40=Button(hard_game, height=5, width=9,command=lambda:move2(button40))
    button40.grid(row=5,column=8)
    
    global button41               
    button41=Button(hard_game, height=5, width=9,command=lambda:move2(button41))
    button41.grid(row=6,column=1)
    
    global button42               
    button42=Button(hard_game, height=5, width=9,command=lambda:move2(button42))
    button42.configure(bg="brown")
    button42.grid(row=6,column=2)
    
    global button43               
    button43=Button(hard_game, height=5, width=9,command=lambda:move2(button43))
    button43.grid(row=6,column=3)
    
    global button44               
    button44=Button(hard_game, height=5, width=9,command=lambda:move2(button44))
    button44.configure(bg="brown")
    button44.grid(row=6,column=4)
    
    global button45              
    button45=Button(hard_game, height=5, width=9,command=lambda:move2(button45))
    button45.grid(row=6,column=5)
    
    global button46               
    button46=Button(hard_game, height=5, width=9,command=lambda:move2(button46))
    button46.configure(bg="brown")
    button46.grid(row=6,column=6)
    
    global button47               
    button47=Button(hard_game, height=5, width=9,command=lambda:move2(button47))
    button47.grid(row=6,column=7)

    global button48               
    button48=Button(hard_game, height=5, width=9,command=lambda:move2(button48))
    button48.configure(bg="brown")
    button48.grid(row=6,column=8)
    
    global button49               
    button49=Button(hard_game, height=5, width=9,command=lambda:move2(button49))
    button49.configure(bg="brown")
    button49.grid(row=7,column=1)
    
    global button50               
    button50=Button(hard_game, height=5, width=9,command=lambda:move2(button50))
    button50.grid(row=7,column=2)
    
    global button51               
    button51=Button(hard_game, height=5, width=9,command=lambda:move2(button51))
    button51.configure(bg="brown")
    button51.grid(row=7,column=3)
    
    global button52               
    button52=Button(hard_game, height=5, width=9,command=lambda:move2(button52))
    button52.grid(row=7,column=4)
    
    global button53               
    button53=Button(hard_game, height=5, width=9,command=lambda:move2(button53))
    button53.configure(bg="brown")
    button53.grid(row=7,column=5)
    
    global button54               
    button54=Button(hard_game, height=5, width=9,command=lambda:move2(button54))
    button54.grid(row=7,column=6)
    
    global button55               
    button55=Button(hard_game, height=5, width=9,command=lambda:move2(button55))
    button55.configure(bg="brown")
    button55.grid(row=7,column=7)
    
    global button56               
    button56=Button(hard_game, height=5, width=9,command=lambda:move2(button56))
    button56.grid(row=7,column=8)
    
    global button57               
    button57=Button(hard_game, height=5, width=9,command=lambda:move2(button57))
    button57.grid(row=8,column=1)
    
    global button58               
    button58=Button(hard_game, height=5, width=9,command=lambda:move2(button58))
    button58.configure(bg="brown")
    button58.grid(row=8,column=2)
    
    global button59               
    button59=Button(hard_game, height=5, width=9,command=lambda:move2(button59))
    button59.grid(row=8,column=3)
    
    global button60               
    button60=Button(hard_game, height=5, width=9,command=lambda:move2(button60))
    button60.configure(bg="brown")
    button60.grid(row=8,column=4)
    
    global button61               
    button61=Button(hard_game, height=5, width=9,command=lambda:move2(button61))
    button61.grid(row=8,column=5)
    
    global button62               
    button62=Button(hard_game, height=5, width=9,command=lambda:move2(button62))
    button62.configure(bg="brown")
    button62.grid(row=8,column=6)
    
    global button63               
    button63=Button(hard_game, height=5, width=9,command=lambda:move2(button63))
    button63.grid(row=8,column=7)
    
    global button64               
    button64=Button(hard_game, height=5, width=9,command=lambda:move2(button64))
    button64.configure(bg="brown")
    button64.grid(row=8,column=8)
    

    
  
    global dictionary2
    dictionary2={button1:1,button2:2,button3:3,button4:4,button5:5,button6:6,button7:7,
                   button8:8,button9:9,button10:10,button11:11,button12:12,button13:13,
                   button14:14,button15:15,button16:16,button17:17,button18:18,button19:19,
                   button20:20,button21:21,button22:22,button23:23,button24:24,button25:25,
                   button26:26,button27:27,button28:28,button29:29,button30:30,button31:31,
                   button32:32,button33:33,button34:34,button35:35,button36:36,button37:37,
                   button38:38,button39:39,button40:40,button41:41,button42:42,button43:43,
                   button44:44,button45:45,button46:46,button47:47,button48:48,button49:49,
                   button50:50,button51:51,button52:52,button53:53,button54:54,button55:55,
                   button56:56,button57:57,button58:58,button59:59,button60:60,button61:61,
                   button62:62,button63:63,button64:64}

    global start
    start = time.time()
#############################################################################################SCOREBOARDS####################################################################################################################################
#Easy scoreboard
def scoreboard():
    scoreboard=tk.Toplevel(main_menu) #creates window
    scoreboard.resizable(True, True) 

    global bg_image_easy_sc
    bg_image_easy_sc = PhotoImage(file="ScoreboardBackground.png")

    w = bg_image_easy_sc.width()
    h = bg_image_easy_sc.height()

    scoreboard.geometry("%dx%d+600+300" % (w, h)) #sets window size

    cv_easy_sc = Canvas(scoreboard,width=w, height=h)
    cv_easy_sc.pack(side=TOP, fill=BOTH, expand=True)
    cv_easy_sc.create_image(0, 0, image=bg_image_easy_sc, anchor=NW) #creates background image on window
    
    
    n="Anonymous"
    a=b=c=d=e=f=g=h=i=j=""
    if winners == False:
        global LabelText
        LabelText=Label(cv_easy_sc, bg = "white", text="No champions yet!")
        LabelText.pack(expand=True)
    else:
       LabelText.pack_forget()
       for i in range(10):
        if winners != False and len(winners)>i:
            if str(winners[i][0])=="":
                a=str(n+" - "+str(list_times[i]))+"s"
                labelText1=Label(cv_easy_sc, bg = "white",text=str(i+1)+". "+a)
                labelText1.pack(expand=True)
            else:
                a=str(winners[i][0])+" - "+str(list_times[i])+"s"
                labelText1=Label(cv_easy_sc, bg = "white",text=str(i+1)+". "+a)
                labelText1.pack(expand=True)

    scoreboard.title("Easy scoreboard")
    
#Medium scoreboard
def scoreboard1():
    scoreboard1=tk.Toplevel(main_menu)
    scoreboard1.resizable(True, True)

    global bg_image_medium_sc
    bg_image_medium_sc = PhotoImage(file="ScoreboardBackground.png")

    w = bg_image_medium_sc.width()
    h = bg_image_medium_sc.height()

    scoreboard1.geometry("%dx%d+600+300" % (w, h))

    cv_medium_sc = Canvas(scoreboard1,width=w, height=h)
    cv_medium_sc.pack(side=TOP, fill=BOTH, expand=True)
    cv_medium_sc.create_image(0, 0, image=bg_image_medium_sc, anchor=NW)
    
    
    n="Anonymous"
    a=b=c=d=e=f=g=h=i=j=""
    if winners1 == False:
        global LabelText
        LabelText=Label(cv_medium_sc, bg = "white", text="No champions yet!")
        LabelText.pack(expand=True)
    else:
       LabelText.pack_forget()
       for i in range(10):
        if winners1 != False and len(winners1)>i:
            if str(winners1[i][0])=="":
                a=str(n+" - "+str(list_times1[i]))+"s"
                labelText1=Label(cv_medium_sc, bg = "white",text=str(i+1)+". "+a)
                labelText1.pack(expand=True)
            else:
                a=str(winners1[i][0])+" - "+str(list_times1[i])+"s"
                labelText1=Label(cv_medium_sc, bg = "white",text=str(i+1)+". "+a)
                labelText1.pack(expand=True)

    scoreboard1.title("Medium scoreboard")
    
#Hard scoreboard
def scoreboard2():
    scoreboard2=tk.Toplevel(main_menu)
    scoreboard2.resizable(True, True)

    global bg_image_hard_sc
    bg_image_hard_sc = PhotoImage(file="ScoreboardBackground.png")

    w = bg_image_hard_sc.width()
    h = bg_image_hard_sc.height()

    scoreboard2.geometry("%dx%d+600+300" % (w, h))

    cv_hard_sc = Canvas(scoreboard2,width=w, height=h)
    cv_hard_sc.pack(side=TOP, fill=BOTH, expand=True)
    cv_hard_sc.create_image(0, 0, image=bg_image_hard_sc, anchor=NW)
    
    
    n="Anonymous"
    a=b=c=d=e=f=g=h=i=j=""
    if winners2 == False:
        global LabelText
        LabelText=Label(cv_hard_sc, bg = "white", text="No champions yet!")
        LabelText.pack(expand=True)
    else:
       LabelText.pack_forget()
       for i in range(10):
        if winners2 != False and len(winners2)>i:
            if str(winners2[i][0])=="":
                a=str(n+" - "+str(list_times2[i]))+"s"
                labelText1=Label(cv_hard_sc, bg = "white",text=str(i+1)+". "+a)
                labelText1.pack(expand=True)
            else:
                a=str(winners2[i][0])+" - "+str(list_times2[i])+"s"
                labelText1=Label(cv_hard_sc, bg = "white",text=str(i+1)+". "+a)
                labelText1.pack(expand=True)

    scoreboard2.title("Hard scoreboard")

            
########################################################################################TUTORIAL############################################################################################################################################ 

def move_tutorial(button):
    global dictionary2
    target_square=dictionary2[button]
    global knight
    global a
    a=0
    global b
    b=0
    global picture
    picture=PhotoImage(file="Knight.png")
    about.withdraw()

    
    if knight==0:
        global list_values
        list_values=[1,2,3,4,5,6]
        global list_keys
        list_keys=[button1,button2,button3,button4,button5,button6]
        knight=1
        
    
    if knight==target_square:
        messagebox.showerror("ERROR","You cannot move to your current position.")
        current_square=list_keys[knight-1]
        current_square=Button(tutorial,command=lambda:move_tutorial(current_square))
    
        if knight==1:
            current_square.configure(image=picture,height=79, width=65, bg="brown")
            a=1
            b=1
            dictionary2={current_square:1,button2:2,button3:3,button4:4,button5:5,button6:6}
            list_keys=[current_square,button2,button3,button4,button5,button6]
        elif knight==2:
            current_square.configure(image=picture,height=79, width=65)
            a=3
            b=2
            dictionary2={button1:1,current_square:2,button3:3,button4:4,button5:5,button6:6}
            list_keys=[button1,current_square,button3,button4,button5,button6]
        elif knight==3:
            current_square.configure(image=picture,height=79, width=65, bg="brown")
            a=5
            b=3
            dictionary2={button1:1,button2:2,current_square:3,button4:4,button5:5,button6:6}
            list_keys=[button1,button2,current_square,button4,button5,button6]
        elif knight==4:
            current_square.configure(image=picture,height=79, width=65)
            a=4
            b=5
            dictionary2={button1:1,button2:2,button3:3,current_square:4,button5:5,button6:6}
            list_keys=[button1,button2,button3,current_square,button5,button6]
        elif knight==5:
            current_square.configure(image=picture,height=79, width=65, bg="brown")
            a=2
            b=6
            dictionary2={button1:1,button2:2,button3:3,button4:4,current_square:5,button6:6}
            list_keys=[button1,button2,button3,button4,current_square,button6]
            
        current_square.grid(row=a,column=b)
        
    elif knight-target_square != -1:
        messagebox.showerror("ERROR","That move is not legal!\nThe knight moves in an L shape.")
        current_square=list_keys[knight-1]
        current_square=Button(tutorial,command=lambda:move_tutorial(current_square))
    
        if knight==1:
            current_square.configure(image=picture,height=79, width=65, bg="brown")
            a=1
            b=1
            dictionary2={current_square:1,button2:2,button3:3,button4:4,button5:5,button6:6}
            list_keys=[current_square,button2,button3,button4,button5,button6]
        elif knight==2:
            current_square.configure(image=picture,height=79, width=65)
            a=3
            b=2
            list_keys=[button1,current_square,button3,button4,button5,button6]
            dictionary2={button1:1,current_square:2,button3:3,button4:4,button5:5,button6:6}
        elif knight==3:
            current_square.configure(image=picture,height=79, width=65, bg="brown")
            a=5
            b=3
            list_keys=[button1,button2,current_square,button4,button5,button6]
            dictionary2={button1:1,button2:2,current_square:3,button4:4,button5:5,button6:6}
        elif knight==4:
            current_square.configure(image=picture,height=79, width=65)
            a=4
            b=5
            list_keys=[button1,button2,button3,current_square,button5,button6]
            dictionary2={button1:1,button2:2,button3:3,current_square:4,button5:5,button6:6}
        elif knight==5:
            current_square.configure(image=picture,height=79, width=65, bg="brown")
            a=2
            b=6
            dictionary2={button1:1,button2:2,button3:3,button4:4,current_square:5,button6:6}
            list_keys=[button1,button2,button3,button4,current_square,button6]
        current_square.grid(row=a,column=b)
        
    if knight-target_square == -1:
        picture2=PhotoImage(file="Square.png")
        previous_square=list_keys[knight-1]
        previous_square.config(image=picture2,width=65,height=79,bg="red")
        list_keys[target_square-1].configure(image=picture, height=79,width=65)
        knight=target_square
        if knight==6:
            messagebox.showinfo("Victory!","Congratulations, you have successfully finished the Tutorial!\nGood luck with future games! :)")
            tutorial.withdraw()
            main_menu.deiconify()
            
def create_tutorial():
    global tutorial
    about.withdraw()
    tutorial=tk.Toplevel(main_menu)
    tutorial.config(bg="black")
    tutorial.resizable(False,False)
    tutorial.protocol("WM_DELETE_WINDOW", X_event)
    
    global knight
    knight=0
    
    global picture
    picture=PhotoImage(file="Knight.png")
    
    global button1
    button1=Button(tutorial,command=lambda:move_tutorial(button1))
    button1.configure(image=picture,height=79, width=65, bg="brown")
    button1.grid(row=1,column=1)

    global button2               
    button2=Button(tutorial, height=5, width=9,command=lambda:move_tutorial(button2))
    button2.grid(row=3,column=2)

    global button3               
    button3=Button(tutorial, height=5, width=9,command=lambda:move_tutorial(button3))
    button3.configure(bg="brown")
    button3.grid(row=5,column=3)

    global button4               
    button4=Button(tutorial, height=5, width=9,command=lambda:move_tutorial(button4))
    button4.grid(row=4,column=5)

    global button5               
    button5=Button(tutorial, height=5, width=9,command=lambda:move_tutorial(button5))
    button5.configure(bg="brown")
    button5.grid(row=2,column=6)

    global button6               
    button6=Button(tutorial, height=5, width=9,command=lambda:move_tutorial(button6))
    button6.grid(row=1,column=4)

    global dictionary2
    dictionary2={button1:1,button2:2,button3:3,button4:4,button5:5,button6:6}

#About the game
def aboutt():
    main_menu.withdraw()
    
    global about
    about=tk.Toplevel(main_menu)
    about.protocol("WM_DELETE_WINDOW", X_event)

    global bg_image1
    bg_image1 = PhotoImage(file="AboutBackground.png")

    w = bg_image1.width()
    h = bg_image1.height()

    about.geometry("%dx%d+600+300" % (w, h))

    cv1 = Canvas(about,width=w, height=h)
    cv1.pack(side=TOP, fill=BOTH, expand=True)
    cv1.create_image(0, 0, image=bg_image1, anchor=NW)

    
    about.resizable(True,True)
    
    about.title("About ")
   
    Button_tutorial=Button(cv1,text="Tutorial", bg = "white",height=3,width=20,command=lambda:create_tutorial())
    Button_tutorial.pack(expand=True)

    labelTekst=Label(cv1, bg = "white", text="The objective of the game is to use the knight's movement to visit every square, but only once!\n\nMovement: The knight moves in the shape of the letter L:\n\ta) one square vertically and two squares horizontally\n\tb) two squares vertically and one square horizontally\n\nThis also means that the knight alternates between light and dark squares.\n\nA square that has been visited by the knight will be marked red.\n\nFor a quick demonstration, play the 'Tutorial'.")
    labelTekst.pack(expand=True)

###################################################################################################Victory conditions#######################################################################################################################

def win_easy():
        end = time.time()
        full_time=round(end-start,2)
        winning_message="Congratulations "+Name.get()+"!\nYou beat Easy with the time of "+str(full_time)+" seconds :)\nYour score has been added to Easy Scoreboard! "
        messagebox.showinfo("Victory!",winning_message)
        main_menu.deiconify()

        contestant_name = Name.get()
        contestant_time = full_time
         
        contestant_score={contestant_name:contestant_time}

        print("Score (Easy): ",contestant_score)

        list_names.append(contestant_name)
        list_times.append(contestant_time)

        for i in range(len(list_times)):
            list_times.sort()

        contestants[contestant_name]=contestant_time

        global winners
        winners=sorted(contestants.items(),key=operator.itemgetter(1))
        easy_game.withdraw()
        
def win_medium():
        end = time.time()
        full_time = round(end-start,2)
        winning_message="Congratulations "+Name.get()+"!\nYou beat Medium with the time of "+str(full_time)+" seconds :)\nYour score has been added to Medium Scoreboard! "
        messagebox.showinfo("Victory!",winning_message)
        main_menu.deiconify()
        
        contestant_name1 = Name.get()
        contestant_time1 = full_time
         
        contestant_score1={contestant_name1:contestant_time1}
        
        print("Score (Medium): ",contestant_score1)

        list_names1.append(contestant_name1)
        list_times1.append(contestant_time1)
        
        for i in range(len(list_times1)):
            list_times1.sort()

        contestants1[contestant_name1]=contestant_time1

        global winners1
        winners1=sorted(contestants1.items(),key=operator.itemgetter(1))
        medium_game.withdraw()
        
def win_hard():
        end = time.time()
        full_time = round(end-start,2)
        winning_message = "Congratulations "+Name.get()+"!\nYou beat Hard with the time of "+str(full_time)+" seconds :)\nYour score has been added to Hard Scoreboard! "
        messagebox.showinfo("Victory!",winning_message)
        main_menu.deiconify()
        
        contestant_name2=Name.get()
        contestant_time2=full_time
         
        contestant_score2={contestant_name2:contestant_time2}
        print("Score (Hard): ",contestant_score2)

        list_names2.append(contestant_name2)
        list_times2.append(contestant_time2)
        
        for i in range(len(list_times2)):
            list_times2.sort()
        

        contestants2[contestant_name2]=contestant_time2

        global winners2
        winners2=sorted(contestants2.items(),key=operator.itemgetter(1))
        hard_game.withdraw()

#.................................................................................................MAIN......................................................................................................................................
    
winners=False
winners1=False
winners2=False
        
LabelName=Label(cv, bg = "white", text="Name:",font="Arial 13")
LabelName.pack()

global list_times
list_times=[]

global list_names
list_names=[]

global sorted_list_names
sorted_list_names=[]

global contestants
contestants={}

global list_times1
list_times1=[]

global list_names1
list_names1=[]

global sorted_list_names1
sorted_list_names1=[]

global contestants1
contestants1={}

global list_times2
list_times2=[]

global list_names2
list_names2=[]

global sorted_list_names2
sorted_list_names2=[]

global contestants2
contestants2={}

Name=Entry(cv, justify = 'center')
Name.pack()

button=Button(cv,text="Easy\n(3x4)", bg = "white",height=5,width=50,command=lambda:create_easy_game())
button.pack(expand=True)

button1=Button(cv,text="Medium\n(5x6)", bg = "white",height=5,width=50,command=lambda:create_medium_game())
button1.pack(expand=True)

button2=Button(cv,text="Hard\n(8x8)", bg = "white", height=5,width=50,command=lambda:create_hard_game())
button2.pack(expand=True)
    
def quit_msg():
    quit_window=tk.Toplevel(main_menu)
    
    global bg_image_quit
    bg_image_quit = PhotoImage(file="QuitBackground.png")

    w = bg_image_quit.width()
    h = bg_image_quit.height()

    quit_window.geometry("%dx%d+800+500" % (w, h))
    
    canvas_quit = Canvas(quit_window, width=w, height=h)
    canvas_quit.pack(side=TOP, fill=BOTH, expand=True)
    canvas_quit.create_image(0, 0, image=bg_image_quit, anchor=NW)
    
    lbl = Label(canvas_quit, bg = "white", text="Are you sure you want to quit?")
    lbl.pack(padx = 20, pady=30)
    yes_btn = Button(canvas_quit, text="Yes", bg="white",command=main_menu.destroy, height = 2, width=10)
    yes_btn.pack(padx=20, pady=7 , side=LEFT)
    no_btn = Button(canvas_quit, text="No", bg="white", command=quit_window.destroy, height = 2, width=10)
    no_btn.pack(padx=20, pady=7, side=LEFT)
    quit_window.mainloop()
    
button3=Button(cv, text = "Quit", bg = "white", height = 2, width = 21, command = lambda:quit_msg())
button3.pack(expand=True)

menu=Menu(main_menu)
submenu=Menu(menu)
submenu.add_command(label="Easy Scoreboard",command=lambda:scoreboard())
submenu.add_command(label="Medium Scoreboard",command=lambda:scoreboard1())
submenu.add_command(label="Hard Scoreboard",command=lambda:scoreboard2())
submenu.add_command(label="About",command=lambda:aboutt())
menu.add_cascade(label="Menu",menu=submenu)
main_menu.config(menu=menu)
main_menu.protocol("WM_DELETE_WINDOW", X_event)

main_menu.mainloop()
