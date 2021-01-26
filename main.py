import shelve
from tkinter import *
import os

def write(filename, name, number):
    with shelve.open(filename) as base:
        base[name] = number


def read(filename, search):
    ans_names = []
    ans_numbers = []
    ans = []
    with shelve.open(filename) as base:
        names = list(base.keys())
        if search != "":
            for i in names:
                if search.lower() in i.lower():
                    ans_names.append((i, base[i]))

                elif search.lower() in base[i].lower():
                    ans_numbers.append((i, base[i]))
            if search.replace("+", "").isdigit():
                ans = (list(ans_numbers) + list(ans_names))[0:5]
            else:
                ans = (list(ans_names) + list(ans_numbers))[0:5]
            if ans != []:
                return ans
            else:
                return "Ничего не нашлось"
        else:
            return "Ничего не нашлось"


def find(event):
    global find_name, answer, base_path
    if int(event.type) == 4:
        text = " ".join(map(lambda i: i.capitalize(),
                            str(find_name.get()).split(" ")))
        ll = read(base_path, text)
        if ll != "Ничего не нашлось":
            reply_text = "Наш лось: \n"
            for i in ll:
                reply_text += f"{i[1]}  --   {i[0]}\n"
        else:
            reply_text = ll
        answer["text"] = reply_text


def add(event):
    global add_name, add_number, base_path
    name = " ".join(map(lambda i: i.capitalize(),
                        str(add_name.get()).split(" ")))
    number = str(add_number.get())
    if number.replace("+", "").isdigit() and number and name:
        write(base_path, name, number)
        add_name.delete(0, last=END)
        add_number.delete(0, last=END)


window = Tk()
window["bg"] = "#C2C2C2"

base_path = os.path.join("base", "database")

add_name = Entry(bg="#D6D6D6")
add_name.grid(column=0, row=0)

add_number = Entry(bg="#D6D6D6")
add_number.grid(column=1, row=0)

adding = Label(text="ADD", height=1, width=35, bg="#DBDBDB")
adding.grid(column=0, row=1, columnspan=2)

find_name = Entry(bg="#D6D6D6")
find_name.grid(column=0, row=2)


finding = Label(text="FIND", width=17, bg="#DBDBDB")
finding.grid(column=1, row=2)

answer = Label(text="", width=35, bg="#D6D6D6")
answer.grid(column=0, row=4, columnspan=2)


finding.bind("<Button-1>", find)
adding.bind("<Button-1>", add)
window.mainloop()
