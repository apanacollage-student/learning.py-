import tkinter as tk

# Main window
app = tk.Tk()
app.title("Calculator")
app.geometry("320x420")
app.resizable(False, False)
app.configure(bg="#1e1e1e")

# Display
display = tk.Entry(
    app,
    font=("Segoe UI", 24),
    bd=0,
    relief="flat",
    justify="right",
    bg="#252526",
    fg="white"
)
display.pack(fill="x", ipady=20, padx=10, pady=10)

# Button click function
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear()
        display.insert(0, str(result))
    except:
        clear()
        display.insert(0, "Error")

# Buttons frame
btn_frame = tk.Frame(app, bg="#1e1e1e")
btn_frame.pack(expand=True, fill="both")

# Button layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            btn_frame, text=text, font=("Segoe UI", 16, "bold"),
            bg="#0e639c", fg="white",
            command=calculate
        )
    else:
        btn = tk.Button(
            btn_frame, text=text, font=("Segoe UI", 16),
            bg="#3c3c3c", fg="white",
            command=lambda t=text: click(t)
        )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
clear_btn = tk.Button(
    btn_frame, text="C", font=("Segoe UI", 16),
    bg="#c74e39", fg="white",
    command=clear
)
clear_btn.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Grid config
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for j in range(4):
    btn_frame.columnconfigure(j, weight=1)

# Run app
app.mainloop()
