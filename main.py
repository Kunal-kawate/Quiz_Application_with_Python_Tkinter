import tkinter as tk
from tkinter import messagebox
import json
account_data = {} 

app = tk.Tk()
app.title("Login")
app.geometry("300x250")

class QuizApp:
    def __init__(self, root,):
        self.root = root
        self.root.title("Quiz App")
        
        
        self.questions = self.load_question_json()


        # self.questions = [
        #     {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
        #     {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
        #     {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
        #     {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"}
        # ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value="", indicatoron=0)
            btn.pack(pady=5,anchor="center")
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, value=option)

            self.var.set("")

    def submit_answer(self):
        selected_answer = self.var.get()
        if selected_answer == self.questions[self.current_question_index]["answer"]:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your score is: {self.score}/{len(self.questions)}")
            app.deiconify()
            self.root.destroy()
    
    def load_question_json(self):
        f = open('questions.json')
        data = json.load(f)
        return data

# -------------------------------------------- x----------------------------------------------------

class QuestionEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Question Entry App")

        self.questions = []

        # Question Label and Entry
        self.question_label = tk.Label(root, text="Question:")
        self.question_label.pack(pady=5)
        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.pack(pady=5)

        # Option Labels and Entries
        self.option_labels = []
        self.option_entries = []
        for i in range(4):
            label = tk.Label(root, text=f"Option {i+1}:")
            label.pack(pady=5)
            entry = tk.Entry(root, width=50)
            entry.pack(pady=5)
            self.option_labels.append(label)
            self.option_entries.append(entry)

        # Answer Label and Entry
        self.answer_label = tk.Label(root, text="Answer:")
        self.answer_label.pack(pady=5)
        self.answer_entry = tk.Entry(root, width=50)
        self.answer_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Question", command=self.add_question)
        self.add_button.pack(pady=20)

        self.save_button = tk.Button(root, text="Save Questions", command=self.save_questions)
        self.save_button.pack(pady=5)

        self.save_exit = tk.Button(root, text="exit", command=self.exit)
        self.save_exit.pack(pady=5)

    def add_question(self):
        question_text = self.question_entry.get()
        options = [entry.get() for entry in self.option_entries]
        answer = self.answer_entry.get()

        if not question_text or not all(options) or not answer:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        if answer not in options:
            messagebox.showwarning("Input Error", "The answer must be one of the options.")
            return

        question_data = {
            "question": question_text,
            "options": options,
            "answer": answer
        }

        self.questions.append(question_data)
        messagebox.showinfo("Success", "Question added successfully!")

        self.clear_entries()

    def clear_entries(self):
        self.question_entry.delete(0, tk.END)
        for entry in self.option_entries:
            entry.delete(0, tk.END)
        self.answer_entry.delete(0, tk.END)

    def save_questions(self):
        if not self.questions:
            messagebox.showwarning("No Questions", "No questions to save.")
            return

        file_path = "questions.json"
        with open(file_path, "w") as file:
            json.dump(self.questions, file, indent=4)

        messagebox.showinfo("Success", f"Questions saved to {file_path}.")
    
    def exit(self):
        app.deiconify()
        self.root.destroy()



def quiz_exam_UI():
    root = tk.Tk()
    root.geometry("300x300")
    app03 = QuizApp(root)
    root.mainloop()


# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in account_data and account_data[username] == password:
        messagebox.showinfo("Login", "Login Successful!")
        app.withdraw()
        quiz_exam_UI()
    else:
        messagebox.showerror("Login", "Invalid username or password")

def admin():
    app.withdraw()
    app02 = tk.Tk()
    app02.title("Admin Login")
    app02.geometry("300x200")
    
    def add_quiz():
        username02 = entry_username02.get()
        password02 = entry_password02.get()
        if (username02=='admin' and password02=='admin'):
            app02.withdraw()
            root = tk.Tk()
            app03 = QuestionEntryApp(root)
            root.mainloop()
        else:
            messagebox.showerror("Login", "Invalid username or password")

    # Create UI elements
    label_username02 = tk.Label(app02, text="Username:")
    label_username02.pack(pady=5)
    entry_username02 = tk.Entry(app02)
    entry_username02.pack(pady=5)

    label_password02 = tk.Label(app02, text="Password:")
    label_password02.pack(pady=5)
    entry_password02 = tk.Entry(app02, show="*")
    entry_password02.pack(pady=5)

    button_login = tk.Button(app02, text="Login", command=add_quiz)
    button_login.pack(pady=5)


# Function to handle new account creation
def Sign_Up():
    # tk.first_window.title("Login System")
    app.withdraw()
    app01 = tk.Tk()
    app01.title("Login System")
    app01.geometry("300x200")

    def create_account():
        username = entry_username01.get()
        password = entry_password01.get()
        if username in account_data:
            messagebox.showerror("Login", "Account already exist!")
        else:
            account_data[username]=password
            messagebox.showinfo("Create Account", f"Account created for {username}!")
            app01.destroy()
            app.deiconify()
        
    # Create UI elements
    label_username01 = tk.Label(app01, text="Username:")
    label_username01.pack(pady=5)
    entry_username01 = tk.Entry(app01)
    entry_username01.pack(pady=5)

    label_password01 = tk.Label(app01, text="Password:")
    label_password01.pack(pady=5)
    entry_password01 = tk.Entry(app01, show="*")
    entry_password01.pack(pady=5)

    button_create_account01 = tk.Button(app01, text="Create Account", command=create_account)
    button_create_account01.pack(pady=5)

    app01.mainloop()
    # new_username = entry_username.get()
    # new_password = entry_password.get()
    
    # # Add logic to save the new account details
    # # In a real application, you would save these details in a database
    # messagebox.showinfo("Create Account", f"Account created for {new_username}!")





# Create UI elements



label_username = tk.Label(app, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(app)
entry_username.pack(pady=5)

label_password = tk.Label(app, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(app, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(app, text="Login", command=login)
button_login.pack(pady=5)

button_sign_up = tk.Button(app, text="SignUp", command=Sign_Up)
button_sign_up.pack(pady=5)

button_admin = tk.Button(app, text="Admin Login", command=admin)
button_admin.pack(pady=5)
# Run the application
app.mainloop()
