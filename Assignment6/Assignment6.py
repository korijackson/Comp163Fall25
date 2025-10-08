#gather input from user; loop until input = DONE
print("Enter contact information (format: name|phone|email|address):" )
contact_list = []

while True:
    line = input()
    if line.upper() == "DONE":
        break
    else:
        contact_list.append(line.split("|"))

#clean names and addresses
for contact in contact_list:
    #format names
    name_list = contact[0].split()
    formatted_name = " ".join(name_list).title()
    contact[0] = formatted_name

    #format address
    contact[3] = contact[3].strip().title()
    address_list = contact[3].split()
    for index, part in enumerate(address_list):
        if len(part) == 2 and part.isalpha():
            address_list[index] = part.upper()
    formatted_address = " ".join(address_list)
    contact[3] = formatted_address

    #format phone numbers
    for char in contact[1]:
        if not char.isdigit():
            contact[1] = contact[1].replace(char, "")
    contact[1] = f"({contact[1][0:3]}) {contact[1][3:6]}-{contact[1][6:]}"

    #format email
    contact[2] = contact[2].lower().strip()


print(contact_list)



