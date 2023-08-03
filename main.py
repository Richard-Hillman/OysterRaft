import tkinter as tk

# Function to change the tag color of a bag
def change_color(event, row, col):
    color = color_vars[row][col].get()
    bags[row][col]['bg'] = color

# Function to update the date for a bag
def update_date(row, col):
    date = date_vars[row][col].get()
    dates[row][col]['text'] = date

# Create the main application window
root = tk.Tk()
root.title("Oyster Bag Tracker")

# Adjust row and column weights to make the layout responsive
for row in range(4):
    root.grid_rowconfigure(row, weight=1)
for col in range(12):
    root.grid_columnconfigure(col, weight=1)

# Create a 2D list to store the bags
bags = [[None for _ in range(12)] for _ in range(4)]
dates = [[None for _ in range(12)] for _ in range(4)]

# Create a 2D list to store color variables
color_vars = [[None for _ in range(12)] for _ in range(4)]
date_vars = [[None for _ in range(12)] for _ in range(4)]

# Available colors for the drop-down menu
colors = ["white", "blue", "red", "green", "yellow", "purple", "orange"]

# Create and arrange the bag squares in a grid
for row in range(4):
    for col in range(12):
        color_vars[row][col] = tk.StringVar()
        color_vars[row][col].set("white")  # Default color is white

        date_vars[row][col] = tk.StringVar()

        bags[row][col] = tk.Frame(root, width=80, height=80, bg="white", borderwidth=1, relief=tk.SOLID)
        bags[row][col].grid(row=row, column=col, sticky="nsew")
        bags[row][col].bind("<Button-1>", lambda event, row=row, col=col: change_color(event, row, col))  # Bind the click event to the function

        # Create and attach the drop-down menu
        color_menu = tk.OptionMenu(bags[row][col], color_vars[row][col], *colors)
        color_menu.config(width=8)
        color_menu.grid(row=0, column=0, sticky="nsew")

        # Create and attach the date input field
        date_entry = tk.Entry(bags[row][col], textvariable=date_vars[row][col], font=("Helvetica", 14))
        date_entry.grid(row=1, column=0, sticky="nsew")

        dates[row][col] = tk.Label(bags[row][col], text="", font=("Helvetica", 12, "bold"))
        dates[row][col].grid(row=2, column=0, sticky="nsew")

        # Create and attach the update date button
        update_button = tk.Button(bags[row][col], text="Update Date", command=lambda row=row, col=col: update_date(row, col), font=("Helvetica", 12))
        update_button.grid(row=3, column=0, sticky="nsew")

# Make the bags expand and fill available space
for row in range(4):
    bags[row][0].grid_columnconfigure(0, weight=1)

# Make the window resizable and fit the content
root.resizable(True, True)

root.mainloop()
