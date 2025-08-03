# qa_python_page_object
## Project Description
This project contains a list of automated test using selenium for future reference. It aims to implement atomated tests in the DOM to help mantaining the test code of a website and improving readibility, the web site represents a log in and an instagram type application.

## Technologies
- Selenium WebDriver
- Pytest
- Python
- Pycharm IDE
- Javascript

## How to run this code?
1. Install PyCharm, check https://www.jetbrains.com/pycharm/
2. Make sure you create a virtual environment, follow this steps:
    - Open PyCharm and click New Project.
    - On the left, select Pure Python.
    - On the right, under Python Interpreter, choose New environment using and select Virtualenv.
    - Choose a location for the virtual environment.
    - Make sure the Base interpreter is set (e.g., Python 3.11).
3. Install pytest using ```pip install pytest``` in your console
4. Install the requests packages using ```pip install requests``` in your console

## page_object_methods1.py
In the project, a method called ```add_new_place()``` was implemented to streamline the process of adding a new location to Around's homepage. This method combines a sequence of actions: it clicks the "Add new place" button, enters the name of the location, inserts the image link into the corresponding field, and finally saves the entry by clicking the "Save" button. By consolidating these steps into a single function, the process of creating a new place is automated and simplified. This ensures efficiency and reduces manual interaction in the test or implementation workflow.

## page_object_method2.py
In the project, it is presented a complete use of a test using selenium webdriver, a method called ```register()``` was implemented within the ```RegistrationPageAround``` class to automate the user registration process. This method performs the following sequence: it fills in the Email field with the provided input, enters the password into the Password field, and then clicks the Sign Up button. By combining these actions into a single method, the registration flow is executed efficiently, ensuring a seamless and repeatable process for testing or user interaction. This approach minimizes manual steps and enhances test reliability.

---

## page_object_practice_task1.py
In the project, an automated test was implemented to validate the **Occupation** text field following the Page Object Model (POM) pattern. The test was structured within the **HomePageAround** class, which was completed and utilized for this purpose.  

The test performed the following steps:  
1. **Waited for the homepage to load** using the `wait_for_load_home_page()` method to ensure proper synchronization.  
2. **Located the Occupation field** using a class-based selector.  
3. **Stored the field's value** in a variable named `description`.  
4. **Verified the stored value** using an `assert` statement to confirm that the input was correctly captured.  

The **LoginPageAround** class, already present in the codebase, was used as part of the setup to ensure proper authentication before accessing the homepage. This approach maintained clean separation between page interactions and test logic, adhering to POM best practices while ensuring reliable test execution.

## page_object_practice_task1.py
In the project, an automated test verified that the user's email appears in the header after login.  

A **`HeaderPageAround`** class was created with:  
- A locator for the email element.  
- A **`wait_for_load_header()`** method to ensure proper loading.  
- A check to confirm the email is displayed.  

The test:  
1. Logged in using an existing method.  
2. Waited for the header to load.  
3. Asserted that the correct email was visible.  

This kept the test clean and followed POM structure.

## page_object_registration_locator.py
This project contains a basic use of the selectos and defines a list of methods like ```find_element()``` and obtain properties like ```.text```.
