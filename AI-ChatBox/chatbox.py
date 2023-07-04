from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello" or user == "what's up" or user == "Hey There" or user == "sup"):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?"+ "\n")
	elif (user == "hi" or user == "hii" or user == "hiiii" or user == "hey"):
		txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?"+ "\n")
	elif (user == "how are you"):
		txt.insert(END, "\n" + "Bot -> fine! and you")
	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you." + "\n")
	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !")
	elif (user == "Do you have something for me?"):
		txt.insert(END, "\n" + "Bot -> Depends on what you're asking" + "\n")
	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line" or user == "can you tell me a joke"):
		txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! "+ "\n")
	elif (user == "goodbye" or user == "see you later" or user == "see yaa" or user == "bye"):
		txt.insert(END, "\n" + "Bot -> Have a nice day!")
	elif (user == "Tell me something" or user == "Tell me about yourself"):
		txt.insert(END, "\n" + "Bot ->I'm a simple AI Chatbox built by A.ChrisTopher, I'm still a work in progress for i don't have much data and information "+ "\n")
    
	else:
		txt.insert(END, "\n" + "Bot -> This is me telling you i didn't understand what you just said, i'm learning, you see. Could you try again? " + "\n")

	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="ChatBox", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
