import csv

class ContactManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def add_contact(self, name, email, phone):
        new_contact = {'Name': name, 'Email': email, 'Phone': phone}
        contacts = self._read_contacts()
        contacts.append(new_contact)
        self._write_contacts(contacts)

    def _read_contacts(self):
        try:
            with open(self.csv_file, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                contacts = list(csv_reader)
            return contacts
        except FileNotFoundError:
            return []

    def _write_contacts(self, contacts):
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            fields = ['Name', 'Email', 'Phone']
            csv_writer = csv.DictWriter(file, fieldnames=fields)
            csv_writer.writeheader()
            csv_writer.writerows(contacts)
