from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip      #used to copy the generated password



#.......................add button working and file use to save everyhting to file 
def save():
  
  website=website_entry.get()
  email=email_entry.get()
  password=password_entry.get()

  
  if len(website)==0 or len(password)==0 or len(email)==0:
    messagebox.showinfo(title="oops",message="something is wrong")
  else:
     is_ok=messagebox.askokcancel(title="confirmation",message=f"email: {email} \npassword: {password}")
     if is_ok:
      with open("data.txt","w") as data_file:
       data_file.write(f"website is: {website}  | email is: {email}  | password is: {password}\n")
       website_entry.delete(0,END)
       email_entry.delete(0,END)
       password_entry.delete(0,END)
   

#..................................password generator code
def Generate_func(): 
 letters = list(string.ascii_letters )
 numbers=list( string.digits)
 sybmols=list(string.punctuation)

 rn_letters=random.randint(8,10)
 num_char=random.randint(2,4)
 sym_char=random.randint(2,4)  
 password_letters=[random.choice(letters) for _ in range(rn_letters)]
 password_symbols=[random.choice(sybmols) for _ in range(sym_char)]
 password_numbers=[random.choice(numbers) for _ in range(num_char)]

 pass_list=password_letters + password_numbers + password_symbols
 random.shuffle(pass_list)
 password="".join(pass_list)
 password_entry.delete(0, END)
 password_entry.insert(0, password)
 pyperclip.copy(password)


window=Tk()
window.title("Passwork Manager")
window.config(padx=40,pady=40)
canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="lock.png")
logo_img = logo_img.subsample(6, 6)
canvas.create_image(150,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0,pady=5)
email_label=Label(text="Email")
email_label.grid(row=2,column=0,pady=5)
password_label=Label(text="password")
password_label.grid(row=3,column=0,pady=5)

website_entry=Entry(width=56)
website_entry.grid(row=1,column=1,columnspan=2,padx=5)

email_entry=Entry(width=56)
email_entry.grid(row=2,column=1,columnspan=2,padx=15)
password_entry=Entry(width=33)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="Generate Password",width=14,command=Generate_func)
generate_password_button.grid(row=3,column=2 )
add_button=Button(text="Add",width=47,command=save)
add_button.grid(row=4,column=1,columnspan=2,pady=5)

window.mainloop()

