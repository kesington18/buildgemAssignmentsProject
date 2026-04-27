userData = {}
users = []

def add_user():
    userData.update({"firstName": input("Enter your FirstName: "),
                     "lastName": input("Enter your LastName: "),
                     "age": input("Enter your Age: "),
                     "marital_status": input("Enter your Marital Status: (single / married / complicated) ")})
    users.append(userData)
    return "user created successfully"

def edit_user():
    firstName = input("Enter your First Name: ")
    lastName = input("Enter your Last Name: ")
    age = input("Enter your Age: ")
    marital_status = input("Enter your Marital Status (single / married / complicated) ")

    for user in users:
        if firstName == user["firstName"] and lastName == user["lastName"]:
            user["firstName"] = firstName
            user["lastName"] = lastName
            user["age"] = age
            user["marital_status"] = marital_status
            return "User updated successfully"
        else:
            return "User not found"
    # if userData:
    #     userData.update({"firstName": input("Enter your FirstName: "),
    #                      "lastName": input("Enter your LastName: "),
    #                      "age": input("Enter your Age: "),
    #                      "marital_status": input("Enter your Marital Status: (single / married / complicated) ")})
    #     return "User updated successfully"

def del_user():
    if userData != True:
        return 'User "entry value" not found'
    else:
        userData.clear()
        return "data successfully deleted"

def view_user():
    if userData:
        return users

    else:
        return "User not found"

print(add_user())
# print(add_user())
# print(add_user())
print(view_user())
print(edit_user())
print(view_user())
# print(del_user())
# def edit_user(fname, lname, age, marital_status):



# def