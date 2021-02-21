from tkinter import *
import tkinter.messagebox as tmsg
import random
import time

root = Tk()

def done():
	
	score.append(int(choice.get()))
	current = sum(score)	
	total = IntVar()
	total = int(current)
	comp = random.randint(1, 6)
	if comp == int(choice.get()):
		tmsg.showinfo('out', 'you are out')
		out = (True)
		time.sleep(1)
	        quit()
	else:
		tmsg.showinfo('status', f'you have choosed {choice.get()} \nand computer choosed {comp}')
	global last
	c = choice.get()
	last.set(f'last choice : {c}')
	t = total
	totals.set(f'total : {t}')
	root.update_idletasks()

score = IntVar()
score = []
out = BooleanVar()
out = (False)
l1 = Label(root, text = 'its your bat\n choose a number from 1 to 6', font = 'lucida 10 bold', bg = 'red')
l1.pack()
f = Frame(root, bg = 'black')
radio_bg = 'green'
choice = StringVar()
R1 = Radiobutton(f, text = '1', variable = choice, value = '1',  bg = radio_bg, borderwidth = 9)
R2 = Radiobutton(f, text = '2' , variable = choice, value = '2',  bg = radio_bg, borderwidth = 9)
R3= Radiobutton(f, text = '3' , variable = choice, value = '3', bg = radio_bg, borderwidth = 9)
R4 = Radiobutton(f, text = '4' , variable = choice, value = '4',  bg = radio_bg, borderwidth = 9)
R5 = Radiobutton(f, text = '5' , variable = choice, value = '5',  bg = radio_bg, borderwidth = 9)
R6 = Radiobutton(f, text = '6', variable = choice, value = '6',  bg = radio_bg, borderwidth = 9)

choice.set(1)
R1.pack(anchor ='w', padx = 20)
R2.pack(anchor ='w', padx = 20)
R3.pack(anchor ='w', padx = 20)
R4.pack(anchor ='w', padx = 20)
R5.pack(anchor ='w', padx = 20)
R6.pack(anchor ='w', padx = 20)
total = IntVar()
f.pack(anchor = 'w')

Button(root, text = 'done', command = done, bg = 'black', fg = 'white', borderwidth = 16).pack()

last = StringVar()
last.set(f'last choice : 0')
last_choice = Label(root, textvariable = last, bg = 'blue', fg = 'black' , borderwidth = 4, relief = SUNKEN).pack(side = LEFT, anchor = 'n', pady = 110 , padx = 5)

totals = StringVar()
totals.set('total is 0')
totalsc = Label(root, textvariable = totals, bg = 'blue', fg = 'black' , borderwidth = 4, relief = SUNKEN).pack(side = LEFT, pady = 30 , padx = 0)


root.configure(bg = 'red')
root.mainloop()

if __name__ == '__main__':
	while out == False:
		root.mainloop()
		
