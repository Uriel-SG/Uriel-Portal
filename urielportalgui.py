#LOGIN PAGE
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import json
from kivy.core.clipboard import Clipboard
import os
import hashlib

with open('users.json', 'r') as openfile:
	users = json.load(openfile)

def urielcode():
		#Uriel Window
	window = tk.Tk()
	window.title("Uriel Code")
	window.configure(bg="grey")
	window.attributes("-fullscreen", True)
	
	#Menubar
	menubar = tk.Menu(window)
	file_menu = tk.Menu(menubar)
	
	def normal_theme():
		window.configure(bg="grey")
		title["fg"]="white"
		title["bg"]="black"
		cryptbutt["activebackground"]="white"
		decryptbutt["activebackground"]="white"
		copybutt["activebackground"]="white"
		pastebutt["activebackground"]="white"
	
	def dark_theme():
		window.configure(bg="black")
		title["fg"]="white"
		title["bg"]="black"
		cryptbutt["activebackground"]="black"
		decryptbutt["activebackground"]="black"
		copybutt["activebackground"]="black"
		pastebutt["activebackground"]="black"
		
	def bright_theme():
		window.configure(bg="white")
		title["fg"]="black"
		title["bg"]="white"
		cryptbutt["activebackground"]="white"
		decryptbutt["activebackground"]="white"
		copybutt["activebackground"]="white"
		pastebutt["activebackground"]="white"
		
	file_menu.add_command(label="Normal Theme", command=normal_theme)
	file_menu.add_command(label="Dark Theme", command=dark_theme)
	menubar.add_cascade(label="File", menu=file_menu)
	file_menu.add_command(label="Bright Theme", command=bright_theme)
	file_menu.add_command(label='Exit', command=window.destroy)
	
	window.config(menu=menubar)
	
	#Appearance
	title = tk.Label(text="URIEL CODE",
	fg= "white",
	bg= "black",
	font=("Times", 14, "bold"))
	title.pack(fill=tk.X)
	
	#Image
	logo = tk.PhotoImage(file="uriel-white.png")
	smallerlogo = logo.subsample(4, 4)
	uriel = tk.Label(image=smallerlogo, bg='black')
	uriel.pack(fill=tk.X)
	
	#Uriel-Code Dictionary
	alphabet = {
			" ": " ", 
			"a": "f ", 
			"à": "f ", 
			"á": "f ",
			"ã": "f ",
			"â": "f ",
			"ä": "f ",
			"b": "e ", 
			"c": "d ",
			"ç": "d ",
			"d": "3 ", 
			"e": "2 ", 
			"è": "2 ",
			"é": "2 ",
			"ê": "2 ",
			"ë": "2 ",
			"f": "1 ", 
			"g": "t ", 
			"h": "s ", 
			"i": "r ",
			"ì": "r ",
			"í": "r ",
			"î": "r ",
			"ï": "r ",
			"j": "q ", 
			"k": "p ", 
			"l": "o ", 
			"m": "n ", 
			"n": "10 ", 
			"o": "9 ",
			"ò": "9 ",
			"ó": "9 ",
			"ô": "9 ",
			"õ": "9 ",
			"ö": "9 ",
			"p": "8 ", 
			"q": "7 ", 
			"r": "6 ", 
			"s": "5 ", 
			"t": "4 ", 
			"u": "z ",
			"ù": "z ", 
			"ú": "z ",
			"û": "z ",
			"ü": "z ",
			"v": "y ", 
			"w": "x ", 
			"x": "13 ", 
			"y": "12 ", 
			"z": "11 ",
			".": ". ",
			"?": "? ",
			"0": "0 ",
			"1": "a ",
			"2": "b ",
			"3": "c ",
			"4": "g ",
			"5": "h ",
			"6": "i ",
			"7": "j ",
			"8": "k ",
			"9": "l "}
	
	#Functions
	def delete():
		text.delete("1.0", tk.END)
		text2["state"] = "normal"
		text2.delete("1.0", tk.END)
		text2["state"] = "disabled"
	
	def copy_to_clipboard():
		x = text2.get("1.0", tk.END)
		Clipboard.copy(x)
	
	def paste():
		text.insert(tk.END, Clipboard.paste())
	
	def crypt():
		string_to_convert = text.get("1.0", tk.END)
		lowered_string = string_to_convert.lower()
		for letter in lowered_string:
			if letter == "'":
				lowered_string = lowered_string.replace("'", " ")
		encryption = ""
		for letter in lowered_string:
			if letter in alphabet:
				encryption += alphabet[letter]
			else:
				encryption += letter + " "
		text2["state"] = "normal"
		text2.insert(tk.END, encryption)
		text2["state"] = "disabled"
		
	def decrypt():
		string_to_convert = text.get("1.0", tk.END)
		lowered_string = string_to_convert.lower()
		decryption = ""
		lowered_stringlist = lowered_string.split(" ")
		for element in lowered_stringlist:
			composed = element + " "
			for key in alphabet:
				if composed == alphabet[key]:
					decryption += key
		specials = ["à", "á", "ã", "â", "ä", "é", "è", "ë", "ê", "ì", "í", "î", "ï", "ò", "ó", "õ", "ô", "ö", "ú", "ù", "û", "ü", "ç"]
		for l in specials:
			if l in decryption:
				decryption = decryption.replace(l, "")
		text2["state"] = "normal"
		text2.insert(tk.END, decryption)
		text2["state"] = "disabled"
	
	#Buttons
	deletebutt = tk.Button(text="Clean", font=("Times", 5), activebackground="red", command=delete)
	deletebutt.pack({"side":"bottom"})
	
	copybutt = tk.Button(text="Copy", font=("Times", 5), activebackground="white", command=copy_to_clipboard)
	copybutt.pack({"side":"right"})
	
	pastebutt = tk.Button(text="Paste", font=("Times", 5), activebackground="white", command=paste)
	pastebutt.pack({"side":"left"})
	
	cryptbutt = tk.Button(text="Encrypt", font=("Times", 5), activebackground="white", command=crypt)
	cryptbutt.pack({"side":"top"})
	
	decryptbutt = tk.Button(text="Decrypt", font=("Times", 5), activebackground="white", command=decrypt)
	decryptbutt.pack({"side":"top"})
	
	#Text
	text = tk.Text(padx=15, pady=15, font=("Times", 5), height=12, width=38, wrap="word")
	text.pack({"side":"top"})
	
	text2 = tk.Text(padx=15, pady=15, font=("Times", 5), height=12, width=38, wrap="word", state="disabled")
	text2.pack({"side":"bottom"})
	
	window.mainloop()

user_name = ""
user_pass = ""
user_upk = ""

#PORTAL
def portal():
	def new():
		finestra.destroy()
		urielcode()

	finestra = tk.Tk()
	
	titolo = tk.Label(text="\nURIEL PORTAL", font=("Times", 15, "bold"), bg="black", fg="white")
	titolo.pack(fill=tk.X)
	
	#Image
	logo = tk.PhotoImage(file="uriel-white.png")
	smallerlogo = logo.subsample(4, 4)
	uriel = tk.Label(image=smallerlogo, bg='black')
	uriel.pack(fill=tk.X)
	
	def login():
		global user_name
		global user_pass
		user_name = entryuser.get()
		user_pass = entrypass.get()
		entryuser.delete("0", tk.END)
		entrypass.delete("0", tk.END)
		hashed_user = hashlib.blake2s(user_name.encode('utf-8')).hexdigest()
		hashed_pass = hashlib.blake2s(user_pass.encode('utf-8')).hexdigest()
		if hashed_user in users:
			key = users[hashed_user]
			hashed = hashlib.blake2s(user_pass.encode('utf-8')).hexdigest()
			if key == hashed:
				new()
			else:
				showerror(
		        title='Errore',
		        message="Nome utente o password errati"
		   	 )
		else:
				showerror(
		        title='Errore',
		        message="Nome utente o password errati"
		   	 )
		   
	username = tk.Label(text="\nUsername:")
	username.pack()
	
	entryuser = tk.Entry()
	entryuser.pack()
	
	password = tk.Label(text="\n\nPassword:")
	password.pack()
	
	entrypass = tk.Entry(show="•")
	entrypass.pack()
	
	empty = tk.Label().pack()
	
	loginbutton = ttk.Button(text="LOGIN", command=login)
	loginbutton.pack()
	
	def signup():
		global user_upk
		user_upk = upk.get()
		if user_upk == "16f5foyf4962" or user_upk == "z6r2od932":
			finestra.destroy()
			import defsignup
		else:
			upk.delete("0", tk.END)
			showerror(title="Errore", message="UPK inesistente. \nAssicurati di aver scritto \ncorrettamente.")
			
	sendbutton = ttk.Button(text="Send", command=signup)
	sendbutton.pack(side=tk.BOTTOM)
	
	upk = tk.Entry()
	upk.pack(side=tk.BOTTOM)
	
	noaccount = tk.Label(text="\nYou don't have an account yet?\nIn order to create an UrielAccount \nyou need a UPK ('UrielPassKey').\n\nYour UPK:", font=("Times", 6))
	noaccount.pack(side=tk.BOTTOM)
	
	finestra.mainloop()

portal()