from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json
import csv

# Contact data container class
class Contact:
    def __init__(self, full_name, email, phone_number, is_friend):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend
    
    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone_number} {'(Friend)' if self.is_friend else ''}"


# Our base class for reading file data
class FileReader(ABC) :
    def __init__(self, file_name):
        self.file_name = file_name

    abstractmethod
    def read(self) -> str:
        pass

# Abstract base class for all Contact Data Adapters
class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source
    
    abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass


# Specific implementation of the adapter to read XML Source data
class XMLContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        # Parse XML data into an ElementTree object
        root = ET.fromstring(self.data_source.read()) # Read XML data from a file
        # Extract contact information from the XML and create Contact objects
        contacts = []
        for elem in root.iter():
            if elem.tag == 'contact':
                full_name = elem.find('full_name').text
                email = elem.find('email').text
                phone_number = elem.find('phone_number').text
                is_friend = elem.find('is_friend').text.lower() == 'true'
                contact = Contact(full_name, email, phone_number, is_friend)
                contacts.append(contact)
        return contacts

# Specific implementation of the adapter to read JSON Source data
class JSONContactsAdapter(ContactsAdapter):
    def get_contacts(self):
        # Parse JSON data into a dictionary
        data_dict = json.loads(self.data_source.read()) # Read JSON data from a file
        # Extract contact information from the dictionary and create Contact objects
        contacts = []
        for contact_data in data_dict['contacts']:
            full_name = contact_data['full_name']
            email = contact_data['email']
            phone_number = contact_data['phone_number']
            is_friend = contact_data['is_friend']
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)
        return contacts
    
# Specific implementation of the adapter to read CSV Source data
class CSVContactsAdapter(ContactsAdapter):
  def get_contacts(self):
    # Parse CSV data into a list of contacts
    csv_data = self.data_source.read().strip().split('\n')
    # Extract headers and data rows
    headers = csv_data[0].split(',')
    data_rows = csv_data[1:]
    # Extract contact information from each row and create Contact objects
    contacts = []
    for row in data_rows:
      values = row.split(',')
      contact_data = dict(zip(headers, values))
      full_name = contact_data['full_name']
      email = contact_data['email']
      phone_number = contact_data['phone_number']
      is_friend = contact_data['is_friend'].lower() == 'true'
      contact = Contact(full_name, email, phone_number, is_friend)
      contacts.append(contact)
    return contacts

# Specific implementation of the file reader to be used with XML Files
class XMLReader(FileReader):
    def read(self):
        # Read the contents of the XML file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()

# Specific implementation of the file reader to be used with JSON files
class JSONReader(FileReader):
    def read(self):
        # Read the contents of the JSON file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()

# Specific implementation of the file reader to be used with CSV files
class CSVReader(FileReader):
    def read(self):
        # Read the contents of the CSV file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()
        
# Simple display routine to display Contact data to the console      
def print_contact_data(contacts_source : ContactsAdapter):
    # Print the Contact objects
    for contact in contacts_source.get_contacts():
        print(contact) # we can do it because Contact has __str__ method

# Example usage
xml_reader = XMLReader('adapter\contacts.xml')
# Create an XML adapter and convert the data to a list of Contact objects
xml_adapter = XMLContactsAdapter(xml_reader)
# Print the Contact objects
print_contact_data(xml_adapter)

json_reader = JSONReader('adapter\contacts.json')
# Create a JSON adapter and convert the data to a list of Contact objects
json_adapter = JSONContactsAdapter(json_reader)
# Print the Contact objects
print_contact_data(json_adapter)

csv_reader = CSVReader('adapter\contacts.csv')
# Create a CSV adapter and convert the data to a list of Contact objects
csv_adapter = CSVContactsAdapter(csv_reader)
# Print the Contact objects
print_contact_data(csv_adapter)
