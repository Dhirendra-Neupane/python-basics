import tkinter as tk

window = tk.Tk()

window.title("Calculator-1st Project")

window.geometry("450x600")

def click(value):
    print(value)

button1 = tk.Button(window, text = "1", width = 4, height = 4,
                     font = ("Arial", 20),  bg = "black", fg = "white")
button1.grid(row = 0, column = 1)




window.mainloop()



click(7) 