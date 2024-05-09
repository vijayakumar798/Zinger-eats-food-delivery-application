import customtkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date
import db
import json


class Database:
    def __init__(self):
        self.receipts = []

    def get_product_prices(self):
        # Replace this with your actual implementation
        return [10, 15, 20], [2, 3, 4]

    def save_receipt(self, receipt_data):
        self.receipts.append(receipt_data)
        self.save_to_json()
        messagebox.showinfo('Receipt Saved', 'Receipt has been saved successfully.')

    def save_to_json(self):
        with open('receipts.json', 'w') as json_file:
            json.dump(self.receipts, json_file)


# Instantiate the Database class
db = Database()

app = customtkinter.CTk()
app.title('Zinger Eats')
app.geometry('900x550')
app.config(bg='white')
app.resizable(False, False)

font1 = ('Times New Roman', 20, 'bold')
font2 = ('Times New Roman', 20, 'bold')


def show_message():
    messagebox.showinfo("Message", "Hello, Zinger Eats!")


def reset_entries_labels():
    # Reset all entries to empty strings
    customer_name_entry.delete(0, END)
    customer_address_entry.delete(0, END)
    Cheeseburger_entry.delete(0, END)
    Chicken_entry.delete(0, END)
    Pizza_entry.delete(0, END)
    Orange_entry.delete(0, END)
    Grape_entry.delete(0, END)
    Apple_entry.delete(0, END)

    # Reset all labels to empty strings
    meals_total_label.configure(text='')
    drinks_total_label.configure(text='')
    total_label.configure(text='')
    date_label.configure(text='')


def receipt():
    meals_entries = [Cheeseburger_entry, Chicken_entry, Pizza_entry]
    drinks_entries = [Apple_entry, Orange_entry, Grape_entry]
    try:
        meals_quantities = [int(entry.get()) if entry.get() else 0 for entry in meals_entries]
        drinks_quantities = [int(entry.get()) if entry.get() else 0 for entry in drinks_entries]

        meals_prices, drinks_prices = db.get_product_prices()
        meals_total = sum(quantity * price for quantity, price in zip(meals_quantities, meals_prices))
        drinks_total = sum(quantity * price for quantity, price in zip(drinks_quantities, drinks_prices))
        total = meals_total + drinks_total
        todays_date = date.today().strftime('%d %m %Y')

        if total == 0:
            messagebox.showerror('Error', 'Choose at least 1 product.')
        else:
            meals_total_label.configure(text=f'Meals Total: {meals_total}$')
            drinks_total_label.configure(text=f'Drinks Total:{drinks_total}$')
            total_label.configure(text=f'Total Price:{total}$')
            date_label.configure(text=f'Date:{todays_date}')
            return meals_total, drinks_total, total, todays_date

    except ValueError:
        messagebox.showerror('Error', 'Entered values should be integers.')


def save_receipt():
    receipt_data = {
        'customer_name': customer_name_entry.get(),
        'customer_address': customer_address_entry.get(),
        'meals_total': int(meals_total_label.cget("text").split(":")[1][:-1]),
        'drinks_total': int(drinks_total_label.cget("text").split(":")[1][:-1]),
        'total': int(total_label.cget("text").split(":")[1][:-1]),
        'date': date_label.cget("text").split(":")[1][:]
    }
    db.save_receipt(receipt_data)


# Customer Details Frame
customer_frame = customtkinter.CTkFrame(app, bg_color='white', fg_color='white', corner_radius=10, border_width=1,
                                        border_color='black', width=850, height=100)
customer_frame.place(x=25, y=15)

customer_name_label = customtkinter.CTkLabel(customer_frame, font=font1, text='Customer Name:', text_color='black',
                                             bg_color='white')
customer_name_label.place(x=20, y=10)

customer_name_entry = customtkinter.CTkEntry(customer_frame, font=font1, text_color='black', fg_color='white',
                                              border_color='black', border_width=2, width=180)
customer_name_entry.place(x=250, y=10)

customer_address_label = customtkinter.CTkLabel(customer_frame, font=font1, text='Customer Address:',
                                                text_color='black', bg_color='white')
customer_address_label.place(x=20, y=50)

customer_address_entry = customtkinter.CTkEntry(customer_frame, font=font1, text_color='black', fg_color='white',
                                                 border_color='black', border_width=2, width=240)
customer_address_entry.place(x=250, y=50)

# Products and Receipt Frames
meals_frame = customtkinter.CTkFrame(app, bg_color='white', fg_color='white', corner_radius=10, border_width=1,
                                     border_color='black', width=280, height=250)
meals_frame.place(x=25, y=140)

# Rest of the code remains unchanged


title1_label = customtkinter.CTkLabel(meals_frame, font=font2, text='Meals', text_color='black', bg_color='white')
title1_label.place(x=60, y=40)
print(title1_label)
image_path = '1.png'
img = Image.open(image_path)
img = img.resize((80, 80))

tk_img = ImageTk.PhotoImage(img)

image1_label = customtkinter.CTkLabel(meals_frame, image=tk_img, bg_color='white')
image1_label.image = tk_img
image1_label.place(x=150, y=5)

Cheeseburger_label = customtkinter.CTkLabel(meals_frame, font=font1, text='Cheeseburger:', text_color='black',
                                            bg_color='white')
Cheeseburger_label.place(x=20, y=100)

Cheeseburger_entry = customtkinter.CTkEntry(meals_frame, font=font1, text_color='black', fg_color='white',
                                            border_color='black', border_width=2, width=80)
Cheeseburger_entry.place(x=170, y=100)

Chicken_label = customtkinter.CTkLabel(meals_frame, font=font1, text='Chicken:', text_color='black', bg_color='white')
Chicken_label.place(x=20, y=140)

Chicken_entry = customtkinter.CTkEntry(meals_frame, font=font1, text_color='black', fg_color='white',
                                       border_color='black', border_width=2, width=80)
Chicken_entry.place(x=170, y=140)

Pizza_label = customtkinter.CTkLabel(meals_frame, font=font1, text='Pizza:', text_color='black', bg_color='white')
Pizza_label.place(x=20, y=180)

Pizza_entry = customtkinter.CTkEntry(meals_frame, font=font1, text_color='black', fg_color='white',
                                     border_color='black', border_width=2, width=80)
Pizza_entry.place(x=170, y=180)

# Correcting the placement of drinks_frame
drinks_frame = customtkinter.CTkFrame(app, bg_color='white', fg_color='white', corner_radius=10, border_width=1,
                                      border_color='black', width=280, height=250)
drinks_frame.place(x=315, y=140)

title2_label = customtkinter.CTkLabel(drinks_frame, font=font2, text='Drinks', text_color='black', bg_color='white')
title2_label.place(x=60, y=40)

image_path = '2.png'
img = Image.open(image_path)
img = img.resize((80, 80), resample=Image.LANCZOS)

tk_img = ImageTk.PhotoImage(img)

image2_label = customtkinter.CTkLabel(drinks_frame, image=tk_img, bg_color='white')
image2_label.image = tk_img
image2_label.place(x=150, y=5)

Orange_label = customtkinter.CTkLabel(drinks_frame, font=font2, text='Orange:', text_color='black', bg_color='white')
Orange_label.place(x=20, y=100)

Orange_entry = customtkinter.CTkEntry(drinks_frame, font=font2, text_color='black', fg_color='white',
                                      border_color='black', border_width=2, width=80)
Orange_entry.place(x=170, y=100)

Grape_label = customtkinter.CTkLabel(drinks_frame, font=font2, text='Grape:', text_color='black', bg_color='white')
Grape_label.place(x=20, y=140)

Grape_entry = customtkinter.CTkEntry(drinks_frame, font=font2, text_color='black', fg_color='white',
                                     border_color='black', border_width=2, width=80)
Grape_entry.place(x=170, y=140)

Apple_label = customtkinter.CTkLabel(drinks_frame, font=font1, text='Apple:', text_color='black', bg_color='white')
Apple_label.place(x=20, y=180)

Apple_entry = customtkinter.CTkEntry(drinks_frame, font=font1, text_color='black', fg_color='white',
                                     border_color='black', border_width=2, width=80)
Apple_entry.place(x=170, y=180)

receipt_frame = customtkinter.CTkFrame(app, bg_color='white', fg_color='white', corner_radius=10, border_width=1,
                                       border_color='black', width=250, height=250)
receipt_frame.place(x=620, y=140)

title3_label = customtkinter.CTkLabel(receipt_frame, font=font2, text='Receipt', text_color='black', bg_color='white')
title3_label.place(x=60, y=40)

meals_total_label = customtkinter.CTkLabel(receipt_frame, font=font1, text='', text_color='black', bg_color='white')
meals_total_label.place(x=10, y=80)

drinks_total_label = customtkinter.CTkLabel(receipt_frame, font=font1, text='', text_color='black', bg_color='white')
drinks_total_label.place(x=10, y=120)

total_label = customtkinter.CTkLabel(receipt_frame, font=font1, text='', text_color='black', bg_color='white')
total_label.place(x=10, y=160)

date_label = customtkinter.CTkLabel(receipt_frame, font=font1, text='', text_color='black', bg_color='white')
date_label.place(x=10, y=200)

receipt_button = customtkinter.CTkButton(app, command=receipt, font=font2, text_color='black', text='Receipt',
                                         fg_color='#088561', hover_color='#047152', bg_color='white', cursor='hand2',
                                         corner_radius=25, width=150)
receipt_button.place(x=190, y=400)

save_button = customtkinter.CTkButton(app, command=save_receipt, font=font2, text_color='black', text='Save',
                                      fg_color='#078C01', hover_color='#057700', bg_color='white', cursor='hand2',
                                      corner_radius=25, width=150)
save_button.place(x=360, y=400)

new_button = customtkinter.CTkButton(app, command=reset_entries_labels, font=font2, text_color='black', text='New',
                                     fg_color='#E93E05', hover_color='#A82A00', bg_color='white', cursor='hand2',
                                     corner_radius=25, width=150)
new_button.place(x=530, y=400)

app.mainloop()
