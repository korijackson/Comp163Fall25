#gather input from user; loop until input = DONE

print("Enter contact information (format: name|phone|email|address):" )
contact_list = []

while True:
    line = input()
    if line.upper() == "DONE":
        break
    else:
        contact_list.append(line.split("|"))

print(contact_list)