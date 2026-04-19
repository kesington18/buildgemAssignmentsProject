userData = {}

def add_user():
    userData.update({"firstName": input("Enter your FirstName: "),
                     "lastName": input("Enter your LastName: "),
                     "age": input("Enter your Age: "),
                     "marital_status": input("Enter your Marital Status: (single / married / complicated) ")})
    return "user created successfully"

def edit_user():
    if userData:
        userData.update({"firstName": input("Enter your FirstName: "),
                         "lastName": input("Enter your LastName: "),
                         "age": input("Enter your Age: "),
                         "marital_status": input("Enter your Marital Status: (single / married / complicated) ")})
        return "User updated successfully"

def del_user():
    if userData != True:
        return 'User "entry value" not found'
    else:
        userData.clear()
        return "data successfully deleted"

def view_user():
    if userData:
        return userData
    else:
        return "User not found"

print(add_user())
# print(edit_user())
# print(del_user())
print(view_user())
# def edit_user(fname, lname, age, marital_status):



# def