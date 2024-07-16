# Importing the tkinter module
from tkinter import *
from PIL import Image, ImageTk  # Importing Pillow for image processing

# Importing date class from datetime module
from datetime import date

# Initializing tkinter
root = Tk()

# Setting the width and height of gui
root.geometry("700x500")

# Setting the title of gui
root.title("Age Calculator")

# Loading and resizing the image
original_image = Image.open("welcome.png")
resized_image = original_image.resize((200, 200), Image.LANCZOS)  # Resize to 200x200
photo = ImageTk.PhotoImage(resized_image)

# Creating a Label widget to show the image we load
myimage = Label(image=photo)

# Placing the image Label widget using grid method
myimage.grid(row=0, column=1)

# Defining function to calculate age according to the data given by the user 
def calculateAge():
    # Storing today's date in "today" variable
    today = date.today()
    # Getting birthdate using .get() method
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    # Calculating age by subtracting birthdate from today's date
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    # Creating a Label widget to show the calculated age using grid method
    Label(text=f"{nameValue.get()} , your age is {age}.").grid(row=6, column=1)

# Creating a label widget for asking user his/her name
Label(text="Name").grid(row=1, column=0, padx=90)

# Creating a label widget for asking user his/her year of birth
Label(text="Year").grid(row=2, column=0)

# Creating a label widget for asking user his/her month of birth
Label(text="Month").grid(row=3, column=0)

# Creating a label widget for asking user his/her day of birth
Label(text="Day").grid(row=4, column=0)

# Declaring a variable of string datatype to store the name value entered by the user
nameValue = StringVar()

# Declaring a variable of integer datatype to store the year value entered by the user
yearValue = IntVar()

# Declaring a variable of integer datatype to store the month value entered by the user
monthValue = IntVar()

# Declaring a variable of integer datatype to store the day value entered by the user
dayValue = IntVar()

# Creating an entry widget to take name value
nameEntry = Entry(root, textvariable=nameValue)

# Creating an entry widget to take year value
yearEntry = Entry(root, textvariable=yearValue)

# Creating an entry widget to take month value
monthEntry = Entry(root, textvariable=monthValue)

# Creating an entry widget to take day value
dayEntry = Entry(root, textvariable=dayValue)

# Placing the entry widgets
nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

# Creating and placing a button to calculate a show age on clicking on this button
Button(text="Calculate age", command=calculateAge).grid(row=5, column=1, pady=10)

# mainloop() is an infinite loop used to run the application when it's in ready state
root.mainloop()
