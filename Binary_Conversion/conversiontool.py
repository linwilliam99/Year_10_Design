import tkinter as tk

print("Stage 1")


#process for when you press enter
def process(*args):
	print(process) 

	val = ent_value.get()
	print(val)

	#Check if string is 1's and 0's
	check = checkValue(val)
	print(check)

	if(check == True):

		
		#LEFT OF HERE



	#If val is 1's and 0's (valid)

		#remove left most 0

		#convert to base 10

		#display conversion

	#else
		#update with error message


	#clear entry box

	ent_value.delete(0,tk.END)

def checkValue(str):
	value0 = str.count("0")
	value1 = str.count("1")

	if value0 + value1 == len(str):
		return True
	else:
		return False


root = tk.Tk()

#constructing tkinter widgets
lab_instructions = tk.Label(root, text ="Binary")
ent_value = tk.Entry(root)
lab_results = tk.Label(root, text ="--")

#configure widgits


#add the widgets to the window
lab_instructions.pack()
ent_value.pack()
lab_results.pack()

root.bind("<Return>",process)
root.mainloop()

