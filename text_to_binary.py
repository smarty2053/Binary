import tkinter

root = tkinter.Tk()
root.title("Binary")

#Function
def convert_to_binary():
	teststr = str(entry_teststr.get())
	print("The original string is : " + str(teststr)) 
	res = ''.join(format(ord(i), 'b') for i in teststr) 
	binary = str(res) 
	label_result['text'] = f"BINARY: {binary}"


#GUI	

label_teststr = tkinter.Label(root, text="Text: ")
label_teststr.grid(column=0, row=0)

entry_teststr = tkinter.Entry(root)
entry_teststr.grid(column=1, row=0)

button_convert = tkinter.Button(root, text="Convert", command=convert_to_binary)
button_convert.grid(column=0, row=2)

label_result = tkinter.Label(root, text="BINARY: ")
label_result.grid(column=1, row=2)


root.mainloop()
