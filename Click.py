import tkinter as tk

root = tk.Tk()
root.title("Click")
root.geometry("400x400")

count = 0

def click():
    global count
    count += 1
    label.config(text=f"Click {count} times")

def reset():
    global count
    count = 0
    label.config(text="Click 0 times")

label = tk.Label(root, text="Click 0 times", font=("Arial", 30))
label.pack(pady=10)

but1 = tk.Button(root, text="Click", font=("Arial", 100), bg="yellow", relief="raised", bd=5, cursor="hand2", command=click)
but1.pack(pady=10)
but2 = tk.Button(root, text="Reset", font=("Arial", 16), bg="lightcoral", cursor="hand2", command=reset)
but2.pack(pady=10)

root.mainloop()