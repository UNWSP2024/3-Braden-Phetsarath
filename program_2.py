#get input : Person's age
#display age
#if age is in range 1 or less
#then display infant
#if age is in range greater than 1 , but less than 13
#then display child
#if age is in range 13 or greater but less than 20
#then display teenager
#if age is in range greater than 20
#then display adult

# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".

def categorize_age(age):
    ageCategory = "TBD"
    ######################
    # WRITE YOUR CODE HERE
    if age <= 1: ageCategory = "infant"
    if age >= 1 and age < 13: ageCategory = "child"
    if age >= 13 and age <20: ageCategory = "Teenager"
    if age >= 20: ageCategory ="adult"
    ######################


    return ageCategory


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
