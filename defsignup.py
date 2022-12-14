import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import json
import os
import hashlib

with open('users.json', 'r') as openfile:
	users = json.load(openfile)

def signup():
	#Finestra
	finestra = tk.Tk()
	titolo = tk.Label(text="\nWELCOME", font=("Times", 15, "bold"), bg="black", fg="white")
	titolo.pack(fill=tk.X)
	
	#Image
	logo = tk.PhotoImage(file="uriel-white.png")
	smallerlogo = logo.subsample(4, 4)
	uriel = tk.Label(image=smallerlogo, bg='black')
	uriel.pack(fill=tk.X)
	
	#Widgets
	username = tk.Label(text="\nUsername:")
	username.pack()
	
	entryuser = tk.Entry()
	entryuser.pack()
	
	password = tk.Label(text="\n\nPassword:")
	password.pack()
	
	entrypass = tk.Entry(show="•")
	entrypass.pack()
	
	reppassword = tk.Label(text="\n\nRepeat password:")
	reppassword.pack()
	
	entrypassrep = tk.Entry(show="•")
	entrypassrep.pack()
	
	empty = tk.Label().pack()
	
	def callportal():
		global users
		if entrypass.get() == entrypassrep.get():
			password = entrypass.get()
			user = entryuser.get()
			hashed_p = hashlib.blake2s(password.encode('utf-8')).hexdigest()
			hashed_u = hashlib.blake2s(user.encode('utf-8')).hexdigest()
			users[hashed_u] = hashed_p
			
			json_object = json.dumps(users, indent=4)
			with open("users.json", "w") as outfile:
				outfile.write(json_object)
			finestra.destroy()
			import urielportalgui 
		else:
			entryuser.delete("0", tk.END)
			entrypass.delete("0", tk.END)
			entrypassrep.delete("0", tk.END)
			showerror(title="Errore", message="Le due password non coincidono!")
			finestra.destroy()
			signup()
			
	signupbutton = ttk.Button(text="SIGN UP", command=callportal)
	signupbutton.pack()
	
	finestra.mainloop()

signup()

