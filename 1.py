import tkinter as tk

def click():
    global i
    global result1
    result1.delete(0, 'end')
    if i <= 10:
        result1.insert(0, i)
        i += 1
    else:
        result1.insert(0,"YOU LOSE")

i = 0
window = tk.Tk()
window.title('Hamster Kombat')
window.geometry('520x520')
window.resizable(False, False)
button_hamster = tk.Button(window, text='┈┈╱╲╱▔▔▔╲╱╲'
                                        '\n┈┈▏╮╭╮╭╮┈╭▕'
                                        '\n┈┈▔▏┊▋┊▋┈▕▔'
                                        '\n┈┈┈┈┈┈╱▔▉▔▔▔╲┈╲┈▂╱╲'
                                        '\n┈┈┈┈┈╲┳┳┳╯┈╱┈╱┈▏┈╱'
                                        '\n┈┈┈┈╱┗┻┛▔▔┈┈╲╱┈╱'
                                        '\n┈┈╱┈┈╭┈┈┈╮▕┈┈╱'
                                        '\n╱┈╱▏┊┈┈┈┊▕▔▔', foreground="blue", command=click)
button_hamster.place(x=150, y=150, width=230, height=230)
result1 = tk.Entry(window, width=38)
result1.place(x=150, y=100)
label1 = tk.Label(window, text='Coins')
label1.place(x=80, y=98)
label3 = tk.Label(window, text='Click on the hamster and earn coins')
label3.place(x=160, y=130)

window.mainloop()
