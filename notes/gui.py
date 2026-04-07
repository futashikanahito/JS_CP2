# JS, 1st, GUI with Tkinter
import tkinter as tk

root = tk.Tk()
root.title("Testing/Notes")
root.configure(background="lightpink")
root.minsize(500, 500)
root.maxsize(1000, 1000)
root.geometry("300x300+1125+750")

label = tk.Label(root, text="This is currently working!", font=("Times New Roman", 14, "italic"))
label.config(background="lightpink", fg="black")

image = tk.PhotoImage(file="csvs, txts, sprites/bread.gif")
tk.Label(root, image=image).pack()

# ----------------- Button --------------------
root.count = 0

def add():
    root.count += 1
    num["text"] = root.count

btn = tk.Button(root, text="ADD", command=add)
btn.pack()

num = tk.Label(root, text="0")
num.pack()

label.pack()
root.mainloop()