# Password Generator

## Description

This project is a Password Generator developed using Python. It creates secure and random passwords based on user preferences. Users can specify the password length, choose whether to include special characters, and generate multiple passwords at once. The application also evaluates the strength of the generated passwords.



## Features

* Generate secure random passwords
* User-defined password length
* Option to include or exclude special characters
* Supports uppercase letters
* Supports lowercase letters
* Supports numbers
* Generate multiple passwords in a single run
* Password strength checker (Weak, Medium, Strong)
* Input validation using exception handling
* Simple command-line interface



## Technologies Used

* Python 3
* Random Module
* String Module



## How to Run

1. Install Python 3 on your system.
2. Save the program as `password_generator.py`.
3. Open Terminal or Command Prompt.
4. Navigate to the project folder.
5. Run the following command:

```bash
python password_generator.py
```



## Usage

1. Enter the desired password length.
2. Choose whether to include special symbols.
3. Enter the number of passwords to generate.
4. View the generated password(s).
5. Check the password strength displayed with each password.


## Sample Output

```text
===== Strong Password Generator =====

Enter password length: 12
Include special symbols? (y/n): y
How many passwords do you want to generate? 2

Password 1: A@7mK#9qLp2!
Strength: Strong

Password 2: p$4Xz!8NqR1&
Strength: Strong
```



## Password Strength Levels
* Password Length is Less than 8 Characters 
So, The Strength of Password is Weak.

* Password Length is 8 to 11 Characters 
So, The Strength of Password is  Medium.

* Password Length is 12 or More Characters
So, The Strength of Password is Strong.



## Learning Outcomes

Through this project, the following concepts were learned:

* Random Password Generation
* String Manipulation
* User Input Handling
* Lists and Loops
* Conditional Statements
* Exception Handling
* Password Security Concepts
* Python Modules (Random and String)



## Project Structure

```text
password_generator.py
README.md
Report File
```



## Future Enhancements

* Copy Password to Clipboard
* Save Passwords to a File
* GUI Version using Tkinter
* Custom Character Sets
* Password Expiry Suggestions



## Author

Gourav Singh Rajpoot


## Internship

CODSOFT Python Programming Internship

Task 3 – Password Generator 