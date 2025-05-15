import os
import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import ttk, messagebox,filedialog

def save_book_data():
    with open("library_data.txt", "a") as file:
        file.write(f"Book Title: {booktitle_var.get()}, Author: {author_var.get()}, Price: {price_var.get()}\n")

def save_member_data():
    with open("library_data.txt", "a") as file:
        file.write(f"Name: {title_var.get()} {firstname_var.get()} {surname_var.get()}, Member Type: {member_var.get()}, Address: {address_var.get()}, City: {city_var.get()}, Pin: {pin_var.get()}, Phone: {phone_var.get()}\n")
        file.write("="*50)

# Functions for clearing fields
def clear_book_fields():
    booktitle_var.set("")
    author_var.set("")
    price_var.set("")

def clear_member_fields():
    title_var.set("")
    firstname_var.set("")
    surname_var.set("")
    member_var.set("")
    address_var.set("")
    city_var.set("")
    pin_var.set("")
    phone_var.set("")

# Functions for managing books
def add_book():
    book_tree.insert("", "end", values=(booktitle_var.get(), author_var.get(), price_var.get()))
    save_book_data()
    clear_book_fields()

def update_book():
    selected = book_tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No book selected!")
        return
    book_tree.item(selected, values=(booktitle_var.get(), author_var.get(), price_var.get()))

def delete_book():
    selected = book_tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No book selected!")
        return
    for item in selected:
        book_tree.delete(item)

# Functions for managing members
def add_member():
    member_tree.insert("", "end", values=(
        title_var.get(), firstname_var.get(), surname_var.get(), 
        member_var.get(), address_var.get(), city_var.get(), 
        pin_var.get(), phone_var.get()
    ))
    save_member_data()
    clear_member_fields()

def update_member():
    selected = member_tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No member selected!")
        return
    member_tree.item(selected, values=(
        title_var.get(), firstname_var.get(), surname_var.get(), 
        member_var.get(), address_var.get(), city_var.get(), 
        pin_var.get(), phone_var.get()
    ))

def delete_member():
    selected = member_tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "No member selected!")
        return
    for item in selected:
        member_tree.delete(item)

root = Tk()
root.title("Library Management System")
root.geometry("1300x800")


# Create a frame to hold labels and entry fields
frame1 = Frame(root)
frame1.pack(anchor=W, pady=5, padx=10)

label_title = Label(frame1, text="Title:",font="lucida 10 bold")
label_title.grid(row=0, column=0, padx=5, pady=5, sticky=W)

label_fname = Label(frame1, text="First Name:",font="lucida 10 bold")
label_fname.grid(row=1, column=0, padx=5, pady=5, sticky=W)

label_surname = Label(frame1, text="Surname:",font="lucida 10 bold")
label_surname.grid(row=2, column=0, padx=5, pady=5, sticky=W)

label_member = Label(frame1, text="Member Type:",font="lucida 10 bold")
label_member.grid(row=3, column=0, padx=5, pady=5, sticky=W)

label_address = Label(frame1, text="Address:",font="lucida 10 bold")
label_address.grid(row=4, column=0, padx=5, pady=5, sticky=W)

label_city = Label(frame1, text="City:",font="lucida 10 bold")
label_city.grid(row=5, column=0, padx=5, pady=5, sticky=W)

label_pin = Label(frame1, text="Pin code:",font="lucida 10 bold")
label_pin.grid(row=6, column=0, padx=5, pady=5, sticky=W)

label_phone = Label(frame1, text="Phone no:",font="lucida 10 bold")
label_phone.grid(row=7, column=0, padx=5, pady=5, sticky=W)

# StringVar for storing input values
title_var = tk.StringVar()
firstname_var = tk.StringVar()
surname_var = tk.StringVar()
member_var = tk.StringVar()
address_var = tk.StringVar()
city_var = tk.StringVar()
pin_var = tk.StringVar()
phone_var = tk.StringVar()

# Title Combobox
titleoption = ["Mr", "Ms"]
titlecombobox = ttk.Combobox(frame1, textvariable=title_var, values=titleoption, state="readonly")
titlecombobox.grid(row=0, column=1, padx=5, pady=5)
# member combobox
memberoption = ["STUDENT","LECTURER","STAFF"]
membercombobox = ttk.Combobox(frame1, textvariable=member_var, values=memberoption, state="readonly")
membercombobox.grid(row=3, column=1, padx=5, pady=5)

# Entry fields
entry_fname = Entry(frame1, textvariable=firstname_var,width=23)
entry_fname.grid(row=1, column=1, padx=5, pady=5)

entry_surname = Entry(frame1, textvariable=surname_var,width=23)
entry_surname.grid(row=2, column=1, padx=5, pady=5)

entry_address = Entry(frame1, textvariable=address_var,width=23)
entry_address.grid(row=4, column=1, padx=5, pady=5)

entry_city = Entry(frame1, textvariable=city_var,width=23)
entry_city.grid(row=5, column=1, padx=5, pady=5)

entry_pin = Entry(frame1, textvariable=pin_var,width=23)
entry_pin.grid(row=6, column=1, padx=5, pady=5)

entry_phone = Entry(frame1, textvariable=phone_var,width=23)
entry_phone.grid(row=7, column=1, padx=5, pady=5)

# Book information

label_booktitle = Label(frame1, text="Book Title:",font="lucida 10 bold")
label_booktitle.grid(row=0, column=5, padx=5, pady=5, sticky=W)

label_author = Label(frame1, text="Author:",font="lucida 10 bold")
label_author.grid(row=1, column=5, padx=5, pady=5, sticky=W)

label_dateborrow = Label(frame1, text="Date Borrowed:",font="lucida 10 bold")
label_dateborrow.grid(row=3, column=5, padx=5, pady=5, sticky=W)

label_datedue = Label(frame1, text="Date Due:",font="lucida 10 bold")
label_datedue.grid(row=2, column=5, padx=5, pady=5, sticky=W)

label_loan = Label(frame1, text="Days On Loan:",font="lucida 10 bold")
label_loan.grid(row=4, column=5, padx=5, pady=5, sticky=W)

label_latefine = Label(frame1, text="Late Return Fine:",font="lucida 10 bold")
label_latefine.grid(row=5, column=5, padx=5, pady=5, sticky=W)

label_datedue = Label(frame1, text="Date Over Due:",font="lucida 10 bold")
label_datedue.grid(row=6, column=5, padx=5, pady=5, sticky=W)

label_price = Label(frame1, text="Price:",font="lucida 10 bold")
label_price.grid(row=7, column=5, padx=5, pady=5, sticky=W)

booktitle_var = tk.StringVar()
author_var = tk.StringVar()
dateborrow_var = tk.StringVar()
datedue_var = tk.StringVar()
daysloan_var = tk.StringVar()
latefine_var = tk.StringVar()
dateoverdue_var = tk.StringVar()
price_var = tk.StringVar()


# Entry fields
entry_booktitle = Entry(frame1, textvariable=booktitle_var,width=23)
entry_booktitle.grid(row=0, column=7, padx=5, pady=5)

entry_author = Entry(frame1, textvariable=author_var,width=23)
entry_author.grid(row=1, column=7, padx=5, pady=5)

entry_dateborrow = Entry(frame1, textvariable=dateborrow_var,width=23)
entry_dateborrow.grid(row=2, column=7, padx=5, pady=5)

entry_datedue = Entry(frame1, textvariable=datedue_var,width=23)
entry_datedue.grid(row=3, column=7, padx=5, pady=5)

entry_daysloan = Entry(frame1, textvariable=daysloan_var,width=23)
entry_daysloan.grid(row=4, column=7, padx=5, pady=5)

entry_latefine = Entry(frame1, textvariable=latefine_var,width=23)
entry_latefine.grid(row=5, column=7, padx=5, pady=5)

entry_dayoverdue = Entry(frame1, textvariable=dateoverdue_var,width=23)
entry_dayoverdue.grid(row=6, column=7, padx=5, pady=5)

entry_price = Entry(frame1, textvariable=price_var,width=23)
entry_price.grid(row=7, column=7, padx=5, pady=5)

# Book Treeview
tree_frame = Frame(frame1)
tree_frame.grid(row=0, column=20, rowspan=10, padx=10, pady=5, sticky=NE)

tree_scroll_y = Scrollbar(tree_frame, orient=VERTICAL)
tree_scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)

book_tree = ttk.Treeview(
    tree_frame, 
    columns=("Book Title", "Author", "Price"), 
    show="headings", 
    height=7, 
    yscrollcommand=tree_scroll_y.set, 
    xscrollcommand=tree_scroll_x.set
)

tree_scroll_y.config(command=book_tree.yview)
tree_scroll_x.config(command=book_tree.xview)

tree_scroll_y.pack(side=RIGHT, fill=Y)
tree_scroll_x.pack(side=BOTTOM, fill=X)

book_tree.column("Book Title", width=150)
book_tree.column("Author", width=100)
book_tree.column("Price", width=80)

book_tree.heading("Book Title", text="Book Title")
book_tree.heading("Author", text="Author")
book_tree.heading("Price", text="Price")

book_tree.pack()

# Member Treeview
member_frame = Frame(root)
member_frame.pack(pady=10)

member_scroll = Scrollbar(member_frame)
member_scroll.pack(side=RIGHT, fill=Y)

member_tree = ttk.Treeview(
    member_frame, 
    yscrollcommand=member_scroll.set, 
    columns=("Title", "First Name", "Surname", "Member Type", "Address", "City", "Pin Code", "Phone no"), 
    show='headings'
)
member_tree.pack(fill=X)

member_scroll.config(command=member_tree.yview)

member_tree.heading("Title", text="Title")
member_tree.heading("First Name", text="First Name")
member_tree.heading("Surname", text="Surname")
member_tree.heading("Member Type", text="Member Type")
member_tree.heading("Address", text="Address")
member_tree.heading("City", text="City")
member_tree.heading("Pin Code", text="Pin Code")
member_tree.heading("Phone no", text="Phone no")

member_tree.column("Title", width=50, anchor=CENTER)
member_tree.column("First Name", width=150, anchor=W)
member_tree.column("Surname", width=100, anchor=CENTER)


# Buttons for Book Management
book_button_frame = Frame(tree_frame)
book_button_frame.pack(pady=10)

btn_add_book = Button(book_button_frame, text="Add", width=12, font="lucida 10 bold", bg="lightblue", command=add_book)
btn_add_book.grid(row=0, column=0, padx=5)

btn_update_book = Button(book_button_frame, text="Update", width=12, font="lucida 10 bold", bg="lightgreen", command=update_book)
btn_update_book.grid(row=0, column=1, padx=5)

btn_delete_book = Button(book_button_frame, text="Delete", width=12, font="lucida 10 bold", bg="lightcoral", command=delete_book)
btn_delete_book.grid(row=0, column=2, padx=5)

btn_clear_book = Button(book_button_frame, text="Clear", width=12, font="lucida 10 bold", bg="lightgray", command=clear_book_fields)
btn_clear_book.grid(row=0, column=3, padx=5)


# Buttons for Member Management
member_button_frame = Frame(root)
member_button_frame.pack(pady=10)

btn_add_member = Button(member_button_frame, text="Add", width=12, font="lucida 10 bold", bg="lightblue", command=add_member)
btn_add_member.grid(row=0, column=0, padx=5)

btn_update_member = Button(member_button_frame, text="Update", width=12, font="lucida 10 bold", bg="lightgreen", command=update_member)
btn_update_member.grid(row=0, column=1, padx=5)

btn_delete_member = Button(member_button_frame, text="Delete", width=12, font="lucida 10 bold", bg="lightcoral", command=delete_member)
btn_delete_member.grid(row=0, column=2, padx=5)

btn_clear_member = Button(member_button_frame, text="Clear", width=12, font="lucida 10 bold", bg="lightgray", command=clear_member_fields)
btn_clear_member.grid(row=0, column=3, padx=5)

#files add,delete,open
# papers=[]

# def add_paper():
#     filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")])
#     if not filepath:
#         return
    
#     title = os.path.basename(filepath)
#     author = author_entry.get()
    
#     papers.append((title, author, filepath))
#     messagebox.showinfo("Success", "Paper added successfully!")
#     update_book()

    
# def open_paper():
#     selected = listbox.curselection()
#     if not selected:
#         return
#     index = selected[0]
#     paper = papers[index]
#     webbrowser.open(paper[2]) 
# def delete_paper():
#     selected = listbox.curselection()
#     if not selected:
#         return
#     index = selected[0]
#     papers.pop(index)  # Remove from memory
#     # update_book()
#     messagebox.showinfo("Deleted", "Paper removed successfully!")


# tk.Label(frame1, text="Author:").grid(row=0,column=45)
# author_entry = tk.Entry(frame1)
# author_entry.grid(row=1,column=45)

# tk.Button(frame1, text="Add Paper",font="lucida 10 bold", bg="lightblue",command=add_paper).grid(row=2,column=45)
# tk.Button(frame1, text="Open Paper", font="lucida 10 bold", bg="lightgreen",command=open_paper).grid(row=3,column=45)
# tk.Button(frame1, text="Delete Paper", font="lucida 10 bold", bg="lightcoral", command=delete_paper).grid(row=4,column=45)

# listbox = tk.Listbox(frame1, width=50, height=10)
# listbox.grid(row=5,column=45)

root.mainloop()