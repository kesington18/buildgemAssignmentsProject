userFirstName = input("Enter your FirstName: ")
userLastName = input("Enter your LastName: ")
userAge = input("Enter your Age: ")
userMaritalStatus = input("Enter your Marital Status: (single / married / complicated) ")

userData = []
users = {}

def add_user(fname, lname, age, marital_status):
    userData.append({
        "firstName": fname,
        "lastName": lname,
        "age": age,
        "marital_status": marital_status
    })
    return userData
print(add_user(userFirstName, userLastName, userAge, userMaritalStatus))
# def edit_user(fname, lname, age, marital_status):



# def