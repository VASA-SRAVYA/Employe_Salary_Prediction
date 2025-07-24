💼 Employee Salary Prediction Web Application
A real-world machine learning web application built with Flask that predicts an employee’s salary based on user inputs like experience, age, gender, education, and job title. The app features a clean, animated, and user-friendly frontend.

🔍 Project Overview
This application:

✅ Predicts employee salary using a trained ML model

✅ Takes multiple input fields including categorical data

✅ Built with Flask for backend, HTML/CSS + Bootstrap for frontend

✅ Uses a Random Forest regression model saved as salary_model.pkl

✅ Interactive and beautiful UI with animations

🚀 Features
🔮 Real-time salary prediction based on user inputs

🧑‍💻 Responsive, modern, and animated frontend design

🛡️ Input validation with dropdown placeholders and required fields

📂 Well-organized Flask app structure with templates and static assets

🔧 Modular and easy to extend

🧠 ML Model Info
Algorithm Used: Random Forest Regressor

Dataset Size: Real-world dataset with thousands of records

Features:

Years of Experience, Age, Gender

Education Level, Job Title

EmployeeSalaryApp/
│
├── app.py                # 🎯 Flask backend application  
├── model_train.py        # 🧠 Script to train and save the ML model  
├── salary_model.pkl      # 🤖 Saved trained machine learning model  
├── Salary_Data.csv       # 📊 Dataset file (download separately)  
│
├── templates/            # 🎨 HTML templates  
│ ├── index.html          # 🏠 Home page template  
│ └── predict.html        # 💻 Prediction input and results page  
│
├── static/               # 💅 Static files (CSS for styling and animations)  
│ └── style.css           # 🎨 Custom styles  
│
├── requirements.txt      # 📦 Python dependencies  
└── README.md             # 📘 Project overview and instructions  

<img width="1906" height="895" alt="Screenshot 2025-07-23 214636" src="https://github.com/user-attachments/assets/370efa11-e804-4808-9d68-6030230c5a63" />
<img width="1903" height="894" alt="Screenshot 2025-07-23 214703" src="https://github.com/user-attachments/assets/b755944e-7575-4141-aa29-04b0c79fa7fa" />
