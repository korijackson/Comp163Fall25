#gather input from user; loop until input = DONE
print("Enter contact information (format: name|phone|email|address):" )
contact_list = []

while True:
    line = input()
    if line.upper() == "DONE":
        break
    else:
        contact_list.append(line.split("|"))

#print(contact_list)

#clean names
for contact in contact_list:
    name_list = contact[0].split()
    formatted_name = " ".join(name_list).title()
    contact[0] = formatted_name

    contact[3] = contact[3].strip().title()
    address_list = contact[3].split()
    address_list[-2] = address_list[-2].upper()
    formatted_address = " ".join(address_list)
    contact[3] = formatted_address

print(contact_list)