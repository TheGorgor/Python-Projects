import tkinter as tk

#main window
root = tk.Tk()
root.geometry("400x250") #main window size
root.title("Main") #main window title

clicks = 0
click_points = 0
text_var = tk.StringVar()
text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")

factor = 1.0
def button_clicked():
    global clicks
    global factor
    global click_points
    click_points += 1 * factor
    clicks += 1
    text_var.set(f"You clicked {clicks} times.\nClick Points: {click_points}")  # update the label

#label widget with all options
label = tk.Label(root,
                 textvariable=text_var,
                 #anchor=tk.CENTER,
                 bg="lightblue",
                 height=3,
                 width=30,
                 #bd=3,
                 font=("Arial", 16, "bold"),
                 #cursor="hand2",
                 #fg="red",
                 padx=15,
                 pady=15,
                 #justify=tk.CENTER,
                 #relief=tk.RAISED,
                 #underline=0,
                 wraplength=250)

#pack the label into the window
label.pack(pady=20) #add padding to the top

# Creating a button with specified options
button = tk.Button(root,
                   text="Click Me",
                   command=button_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=50, pady=10)

root.mainloop() #run