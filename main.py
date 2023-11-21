from tkinter import *
from tkinter import messagebox
import random
import pyperclip


FILE = "data.txt.txt"

#Generate password
def generate_password():
    password_form.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    LENGHT_PASSWORD = 20

    generated_password_list = [random.choice(letters + numbers + symbols) for digit in range(LENGHT_PASSWORD)]
    generated_password = "".join(generated_password_list)
    password_form.insert(0, f"{generated_password}")
    pyperclip.copy(generated_password)


#Save Data

def save_data():
    data_file = open(FILE,"a")
    new_password = password_form.get()
    new_email = email_form.get()
    new_website = website_form.get()


    if len(new_website) == 0 or len(new_password) == 0 or len(new_email) == 0:
        messagebox.showinfo(title="Invalid Input", message="Oh oh, you forgot a field")

    elif len(new_website) != 0 and len(new_password) != 0 and len(new_email) != 0:
        decision_to_save = messagebox.askokcancel(title=new_website, message=f"\nThese are the details that you inserted:\nEmail: {new_email}"
                                                                             f"\nPassword: {new_password}\nShould I save this?")
        if decision_to_save:
            data_file.write(f" {new_website} | {new_email} | {new_password} \n")
            data_file.close()
            password_form.delete(0,END)
            email_form.delete(0,END)
            website_form.delete(0,END)





#UI


main_window = Tk()
main_window.title("Password Generator")
main_window.minsize(400,300)
main_window.config(pady=50,padx=50,bg="white")

#Image
canvas = Canvas(width=200,height=200, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100,115,image=logo)
canvas.grid(row=0,column=1,pady=0,padx=0)

#Labels

#website_Label
website_label = Label(text="Website:")
website_label.config(bg="white")
website_label.grid(column=0,row=1,pady=0,padx=0)

#email_Label
email_label = Label(text="Email/Username:")
email_label.config(bg="white")
email_label.grid(column=0,row=2,pady=0,padx=0)

#password_label

password_label = Label(text="Password:")
password_label.config(bg="white")
password_label.grid(column=0,row=3,pady=0,padx=0)

#Forms

#website_form
website_form = Entry()
website_form.config(width=35,bg="white")
website_form.grid(column=1,row=1,columnspan=2,pady=0,padx=0)
website_form.focus

#Email Form
email_form = Entry()
email_form.config(width=35,bg="white")
email_form.grid(column=1,row=2,columnspan=2,pady=0,padx=0)
email_form.insert(0,"henriquealexandremelo@hotmail.com")

#Password Form
password_form = Entry()
password_form.config(width=21,bg="white")
password_form.grid(column=1,row=3,pady=0,padx=0)

#Buttons

#Generate Password Button
generate_password_button = Button(command=generate_password)
generate_password_button.config(text="Generate Password",bg="white")
generate_password_button.grid(column=2,row=3,pady=0,padx=0)

#Add_Button
add_button = Button(command=save_data)
add_button.config(text="Add",bg="white",width=36)
add_button.grid(column=1,row=4,columnspan=2,pady=0,padx=0)



main_window.mainloop()