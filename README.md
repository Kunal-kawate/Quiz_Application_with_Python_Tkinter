# Quiz_Application_with_Python_Tkinter

This is a comprehensive quiz application built using Python and the Tkinter module. The application supports user account creation, secure login, and an admin interface for adding quiz questions. All functionalities are implemented within a single `main.py` file, and quiz questions are stored using JSON files.

![URL or path to image](https://github.com/Kunal-kawate/Quiz_Application_with_Python_Tkinter/blob/main/images/Screenshot%20(77).png)

## Features

- **Admin Login for Adding Questions**:
  - Admins can securely log in to add new quiz questions.
![admin login window]([URL or path to image](https://github.com/Kunal-kawate/Quiz_Application_with_Python_Tkinter/blob/main/images/Screenshot%20(75).png))
![GUI for add questions on quiz app](https://github.com/Kunal-kawate/Quiz_Application_with_Python_Tkinter/blob/main/images/Screenshot%20(76).png)

- **User Signup and Account Creation**:
  - Users can create an account by providing a username and password.
![window for creating user account]([URL or path to image](https://github.com/Kunal-kawate/Quiz_Application_with_Python_Tkinter/blob/main/images/Screenshot%20(74).png))

- **User Login to Take the Quiz**:
  - After creating an account, users can log in with their credentials.
  - Successful login redirects users to the quiz window automatically.
![Main Window of quiz application]([URL or path to image](https://github.com/Kunal-kawate/Quiz_Application_with_Python_Tkinter/blob/main/images/Screenshot%20(73).png))

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/quiz-application.git
    cd quiz-application
    ```

2. **Install Tkinter**:
    Tkinter is included with Python's standard library, but if it's not installed, you can install it using:
    ```bash
    pip install tk
    pip install json
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Admin Login**:
   - Access the admin login to add new questions.
   - Use the credentials username: admin and password: admin for admin access.

2. **User Signup**:
   - Create a new account by providing a username and password.

3. **User Login**:
   - Log in with your username and password.
   - Upon successful login, you will be redirected to the quiz window.

## File Structure

- `main.py`: The main file containing all the required code for the application.

## Data Storage

- **JSON Files**: The application uses JSON files to store quiz questions and user data. The `json` module in Python is used to handle these files.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the contributors and the open-source community for their support and contributions.
