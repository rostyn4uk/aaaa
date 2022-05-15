# import tkinter as tk
# root = tk.Tk()
# root.title("Hello World")
# root.geometry("600x400+500+200")
# root.iconbitmap("name.ico")
# #root.resizable(True, False)
# root.minsize(400, 300)
# root.maxsize(700, 500)
#
# # label_1 = tk.Label(font=("Arial", 32, "bold"),
# #                    text="Hello",
# #                    bg="blue",
# #                    fg="yellow",
# #                    padx=20,
# #                    pady=20,
# #                    width= 10,
# #                    height=3,
# #                    #justify=tk.RIGHT
# #                    anchor='center', # n - up  /  s - bottom / w - left  / e - right / center - center
# #                    relief=tk.RAISED,
# #                    bd=10
# #                    )
# # label_1.pack()
# def add():
#     entry.insert(0, "Hello World ")
# def clear():
#     entry.delete(0, tk.END)
#
# label_1 = tk.Label(font=("Arial",30,"bold"), text="Hello", bd=10)
# label_1.pack()
#
# entry = tk.Entry(width=35)
# entry.pack()
#
# button1 = tk.Button(text="Click", font=("Arial", 10, "bold"), bg="blue", fg="yellow", width=15, height=2, command=add)
# button1.pack(side=tk.LEFT, padx=10, pady=15)
#
# button2 = tk.Button(text="Delete", font=("Arial", 10, "bold"), bg="blue", fg="yellow", width=15, height=2, command=clear)
# button2.pack(side=tk.RIGHT, padx=10, pady=15)
#
#
#
#
#
#
# root.mainloop()
#


import tkinter as tk
root = tk.Tk()
root.title("Color")
root.geometry("240x260+650+260")
root.iconbitmap("name.ico")
root.minsize(200, 240)
root.maxsize(700, 500)

lebel = tk.Label(root, anchor='center')
lebel.pack()

entry = tk.Entry(root, justify='center', bd=4, width=30)
entry.pack()




root.mainloop()