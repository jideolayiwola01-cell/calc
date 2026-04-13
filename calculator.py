import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

Row_count= len(button_values) #5
Column_count = len(button_values[0]) #4

colour_lightgrey = "#D4D4D2"
colour_black = "#1c1c1c"
colour_darkgrey ="#505050"
colour_Orange = "#FF0000"
Colour_White = "white"

#windows set up
Window = tkinter.Tk()
Window.title("Calculator")
Window.resizable( False,False)

Frame = tkinter.Frame(Window)
label = tkinter.Label(Frame, text ="0", font =("Ariel", 45), background= colour_black,
                      foreground= Colour_White, anchor="e", width=Column_count)

label.grid(row=0, column=0, columnspan=Column_count, sticky="we")

for row in range (Row_count):
    for column in range(Column_count):
        value = button_values[row][column]
        button = tkinter.Button(Frame, text=value, font=("Ariel", 30), 
                                width=Column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        

        if value in top_symbols:
            button.config(foreground=colour_black, background=colour_lightgrey)
        elif value in right_symbols:
            button.config(foreground= Colour_White, background=colour_Orange)
        else:
            button.config(foreground=Colour_White, background=colour_darkgrey)

        button.grid(row=row+1, column=column)
        
        

Frame.pack()

#making the buttons work 



def button_clicked(value):
    pass
# center the window

Window.update()
Window_width = Window.winfo_width()
Window_height= Window.winfo_height()
screen_width= Window.winfo_screenmmwidth()
screen_height=Window.winfo_screenheight()

window_x = int((screen_width/2) - (Window_width/2))
windoww_y = int((screen_height/2) - (Window_height/2))

#format "(w) x (h) + (x) +(y)"

## Window.geometry(f"{Window_width} x {Window_height} + {window_x}+{windoww_y}")


Window.mainloop()

