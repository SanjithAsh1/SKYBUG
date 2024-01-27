import tkinter as tk
from tkinter import messagebox

class ContactsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts App")

        self.contacts = []

        self.contact_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contact_listbox.pack(pady=20)

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root, width=50)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_entry = tk.Entry(self.root, width=50)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_entry = tk.Entry(self.root, width=50)

        self.address_label = tk.Label(self.root, text="Address:")
        self.address_entry = tk.Entry(self.root, width=50)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_all_button = tk.Button(self.root, text="View All Contacts", command=self.view_all_contacts)
        self.view_all_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showerror("Error", "Name and phone number are required.")
            return

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        self.contacts.append(contact)
        self.contact_listbox.insert(tk.END, f"{name} ({phone})")
        self.clear_entries()

    def view_all_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            name = contact["name"]
            phone = contact["phone"]
            self.contact_listbox.insert(tk.END, f"{name} ({phone})")

    def search_contact(self):
        search_text = self.name_entry.get()
        results = [contact for contact in self.contacts if search_text.lower() in contact["name"].lower()]
        self.contact_listbox.delete(0, tk.END)
        for contact in results:
            name = contact["name"]
            phone = contact["phone"]
            self.contact_listbox.insert(tk.END, f"{name} ({phone})")

    def update_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if len(selected_contact_index) == 0:
            messagebox.showerror("Error", "Please select a contact to update.")
            return

        contact_index = selected_contact_index[0]
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not phone:
            messagebox.showerror("Error", "Name and phone number are required.")
            return

        self.contacts[contact_index] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        self.view_all_contacts()
        self.clear_entries()

    def delete_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if len(selected_contact_index) == 0:
            messagebox.showerror("Error", "Please select a contact to delete.")
            return

        contact_index = selected_contact_index[0]
        del self.contacts[contact_index]
        self.contact_listbox.delete(contact_index)
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
app = ContactsApp(root)
root.mainloop()