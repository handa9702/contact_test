# Addr.py

class Addr:
    def __init__(self, name, phone, email, address, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.group = group

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}, Group: {self.group}"
