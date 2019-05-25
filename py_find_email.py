try:
    fhand = open('mbox-short.txt')
except:
    print('Bad File.')
    exit()
count = 0

for line in fhand:
    # Check to see if the line starts with From
    if line.startswith('From'):
        # Split the line and take second word which is the email
        email = line.split()[1]
        # Find position of @ and take the items on the left
        pos = email.find('@')
        name = email[:pos]
        # Split the name string
        full_name_list = name.split('.')
        for name in full_name_list:
            first_name = full_name_list[0]
            # Check if the full_name_list has two names and then set second_name to the second index
            if len(full_name_list) is 2:
                second_name = full_name_list[1]
            else:
                # If there is no second name set second_name to None
                second_name = None
            if second_name is None:
                full_name = first_name
            else:

                full_name = first_name+' ' + second_name

        print(count, ':', '\nName', full_name, '\nEmail', email)
        # Increase counter
        count = count+1

print(count)
