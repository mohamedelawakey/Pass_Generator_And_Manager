# 🔐 Password Generator & Strength Checker

A simple yet powerful **Python console application** that allows users to:

- ✅ Generate secure, random passwords (with customizable length & count).
- ✅ Check the strength of any password.
- ✅ Receive friendly suggestions if the password is weak.

The app ensures that generated passwords include a mix of:

- 🔡 Lowercase letters  
- 🔠 Uppercase letters  
- 🔢 Numbers  
- 🔣 Symbols  

It also follows common security rules to evaluate and rank password strength.

---

## 📌 Features

### 🧭 Interactive Menu
- Choose from:
  1. Generate Password(s)
  2. Check Password Strength
  3. Exit

### 🔐 Password Generator
- Set number of passwords (1–5)
- Set password length (8–16 characters)
- Automatically ensures all required character types are included

### 📊 Password Strength Checker
- Evaluates:
  - Length
  - Character diversity (upper, lower, number, symbol)
- Ranks the password as:
  - 🟢 Very Strong  
  - 🟡 Strong  
  - 🔴 Weak (with help prompt)

### 🤝 Friendly Help System
- If your password is weak, the app offers help to generate a better one

---

## 🧪 Unit Testing

Built-in tests using Python's `unittest` module.  
Tests cover:

- Menu selection
- Password generation rules
- Password strength evaluation
- Help system prompts

> ✅ No external libraries used

---

## ▶️ How to Run

```bash
# Run the main app
python Pass_Generator_And_Manager.py

# Run all tests
python -m unittest discover
```

---

# File Structure 📁 
```
project-root/
├── Pass_Generator_And_Manager.py             # Main application logic
├── Testing of pass generator/                # Unit test files
│   ├── test_menu.py                          # Tests menu input
│   ├── test_check_password_strength.py       # Tests strength checker
│   ├── test_ask_for_help.py                  # Tests help system
│   └── ...                                   # Other test files
└── README.md                                 # Project documentation
```


# 👨‍💻 Author
## Mohamed Alawakey

