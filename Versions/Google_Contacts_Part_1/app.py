from flask import Flask, render_template, request
from contact import ContactManager

# Path to the embedded CSV file in the folder
csv_file_path = r'E:\Versions\Google_Contacts_Part_1\contacts.csv'

def add_contact(name_ctt, email_ctt, phone_ctt):
    contact_manager = ContactManager(csv_file_path)
    contact_manager.add_contact(name_ctt, email_ctt, phone_ctt)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact_form.html')

@app.route('/save_contact', methods=['POST'])
def save_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')

    add_contact(name, email, phone)

    return render_template('contact_form.html', message="Contact saved successfully!")

if __name__ == '__main__':
    app.run(debug=True)
