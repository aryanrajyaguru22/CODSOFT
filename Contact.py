import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []


        self.setup_ui()

    def setup_ui(self):

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.name_label = tk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self.frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)


        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=10)


        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.pack(padx=10, pady=10)


        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contacts.append({"name": name, "phone": phone, "email": email})
            self.refresh_treeview()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item)
            self.contacts[index] = {
                "name": self.name_entry.get(),
                "phone": self.phone_entry.get(),
                "email": self.email_entry.get()
            }
            self.refresh_treeview()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update")

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item)
            del self.contacts[index]
            self.refresh_treeview()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")

    def refresh_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for contact in self.contacts:
            self.tree.insert("", tk.END, values=(contact["name"], contact["phone"], contact["email"]))

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            index = self.tree.index(selected_item)
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact["phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact["email"])


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()