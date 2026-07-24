class Contact:
    phone_directory=[]

    def __init__(self,name,phone_number):
        self.name = name
        self.phone_number = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f'Name: {self.name}\nPhone Number: {self.phone_number}'

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory)==0:
            print('No phone number')
        else:
            print('ALL CONTACTS IN PHONE DIRECTORY=>')
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.phone_number
        return f'No phone number found for {search_name}'


    @staticmethod
    def validate_number(number):
        if len(number)>=8 and number.isdigit():
            return True
        else:
            return False


n_contacts=int(input("how many contacts?:"))
for i in range(n_contacts):
    name=input("enter contact name:")
    phone_number=input("enter contact phone number:")
    if Contact.validate_number(phone_number):
        Contact(name,phone_number)
    else:
        print(f"invalid phone number for {name}")

# c1=Contact('sarthak',9301954564)
# c2=Contact('mishi',8602764175)
# # print(c1.show_contact())
# print(c2.show_contact())

# # Contact.show_all_contacts()
# print(Contact.search_contact("sarthak"))
# print(Contact.search_contact("mishii"))

Contact.show_all_contacts()
