import tkinter

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.config(padx=5, pady=5)

input = tkinter.Entry(width=10, )
input.insert(index="0", string="0")
input.grid(column=1, row=0)





is_equal_to_lebel = tkinter.Label(text="is equal to  ", font=("Arial", 15))
is_equal_to_lebel.grid(column=0, row=1)
miles = tkinter.Label(text="Miles", font=("Arial", 15))
miles.grid(column=2, row=0)
km = tkinter.Label(text="0", font=("Arial", 15))
km.grid(column=1, row=1)
km_text = tkinter.Label(text="Km", font=("Arial", 15))
km_text.grid(column=2, row=1)




def button_clicked():
    typed = input.get()
    ki_m = int(typed) * 1.60934
    km["text"] = str(round(ki_m, 2))



button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
