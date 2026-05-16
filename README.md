# 🎓 Student Performance Prediction System

An industry-oriented Machine Learning project that predicts student academic performance using attendance, quizzes, assignments, study behavior, and engagement analytics.

This system helps educational institutions identify at-risk students early and take preventive academic interventions.

---

# 🚀 Features

- 📊 Student performance prediction
- ⚠️ Risk detection system
- 🤖 Machine Learning pipeline
- 🔍 Feature engineering
- ⚡ FastAPI prediction API
- 📈 Evaluation metrics
- 🧠 Synthetic educational dataset generation
- 🌐 Next.js dashboard integration
- 📦 Modular project structure

---

# 🏗️ Project Architecture

```text
Student Data
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
ML Model Training
      ↓
Prediction Engine
      ↓
FastAPI API
      ↓
Next.js Dashboard

🛠️ Tech Stack
Backend
Python
FastAPI
Uvicorn
Machine Learning
Pandas
NumPy
Scikit-learn
XGBoost
Optuna
SHAP
Frontend
Next.js
Tailwind CSS
Tools
Git
GitHub
VS Code
📂 Folder Structure
Student-Performance-Prediction/
│
├── data/
│   └── students.csv
│
├── notebooks/
│   ├── 01_ingest.py
│   ├── 02_eda.py
│   └── analysis.ipynb
│
├── src/
│   ├── pipeline.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   └── utils.py
│
├── serving/
│   └── app.py
│
├── models/
│   └── student_perf_model.joblib
│
├── outputs/
│   ├── plots/
│   ├── reports/
│   └── predictions.csv
│
├── images/
│   └── dashboard.png
│
├── generate_data.py
├── requirements.txt
├── README.md
└── main.py
📊 Dataset Features

The model uses the following features:

Prior GPA
Attendance Percentage
Quiz Average
Assignment Average
Midterm Score
Study Hours Per Week
LMS Logins
Forum Activity
Submission Percentage
Commute Time
Gender
School Type
Parent Education
🧠 Machine Learning Workflow
1️⃣ Data Collection

Synthetic student data generation using NumPy and Pandas.

2️⃣ Data Preprocessing
Missing value handling
Scaling
Encoding categorical features
3️⃣ Model Training

Models used:

Logistic Regression
Random Forest
XGBoost
4️⃣ Evaluation

Metrics:

Accuracy
Precision
Recall
F1 Score
5️⃣ Prediction API

FastAPI endpoint for real-time predictions.

⚙️ Installation Guide
Clone Repository
git clone https://github.com/yourusername/Student-Performance-Prediction-System.git
cd Student-Performance-Prediction-System
Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux/Mac
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
▶️ Generate Dataset
python generate_data.py
🏋️ Train Model
python src/train.py
🚀 Run FastAPI Server
uvicorn serving.app:app --reload
📘 API Documentation

Open in browser:

http://127.0.0.1:8000/docs
🔍 Example Prediction Request
{
  "prior_gpa": 3.2,
  "attendance_pct": 75,
  "quiz_avg": 65,
  "assign_avg": 70,
  "midterm": 68,
  "study_hours_wk": 10,
  "on_time_submit_pct": 80,
  "lms_logins_wk": 12,
  "forum_posts": 4,
  "commute_min": 20,
  "gender": "Male",
  "school_type": "Private",
  "parent_edu": "UG"
}
✅ Example Response
{
  "prediction": 1,
  "risk_probability": 0.91
}
📈 Model Performance
Metric	Score
Accuracy	99%
Precision	1.00
Recall	0.99
F1 Score	0.99
📸 Screenshots to Add

Add screenshots of:

Swagger API Docs
Model Training Output
Prediction Results
Dashboard UI
Feature Importance Graph
Correlation Heatmap
🌍 Real-World Applications
Universities
Coaching Institutes
Online Learning Platforms
EdTech Companies
Student Retention Systems
Academic Risk Monitoring
🔮 Future Improvements
Real student dataset integration
Deep Learning models
Explainable AI dashboard
Student intervention recommendation engine
Docker deployment
CI/CD pipeline
Cloud deployment
🤝 Contribution

Contributions are welcome!

Fork the repository and submit a pull request.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Bablu kumar

B.Tech CSE Student | Machine Learning Enthusiast | Data Science Learner

⭐ Support

If you like this project, give it a ⭐ on GitHub!