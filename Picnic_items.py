from tkinter import*
import random

root = Tk()
root.title("List of Picnic items")
root.geometry("700x300")

label_list = Label(root)
label_item = Label(root)

items_list= ["Water", "Lunch", "ID Card", "Chocolates", "Eatables", "Appropriate Tickets", "Towel", "Smartphone"]
label_list["text"] = "Listed Items: " + str(items_list)

def itemLister():
    random_item = random.sample(range(1, 7), 1)
    label_item["text"] = "Put item no. " + str(random_item) + " In Bag"
    
label_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn = Button(root, text = "Which item to carry?", command = itemLister)

btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label_item.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()