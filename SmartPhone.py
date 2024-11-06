# SmartPhone.py

from Addr import Addr

class SmartPhone:
    def __init__(self):
        self.contacts = []  # 연락처 리스트 초기화

    def add_contact(self, contact):
        if len(self.contacts) < 10:
            self.contacts.append(contact)
            print(f"Contact added: {contact.name}")
        else:
            print("Contact list is full. Cannot add more contacts.")

    def show_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts available.")

    def delete_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact with name '{name}' has been deleted.")
                found = True
                break
        if not found:
            print(f"No contact found with name '{name}'.")

    def update_contact(self, name, new_contact):
        found = False
        for idx, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[idx] = new_contact
                print(f"Contact with name '{name}' has been updated.")
                found = True
                break
        if not found:
            print(f"No contact found with name '{name}'.")
