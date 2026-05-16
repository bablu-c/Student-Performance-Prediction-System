import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

n = 1000

data = {
    "prior_gpa": np.round(np.random.uniform(2.0, 4.0, n), 2),
    "attendance_pct": np.random.randint(40, 100, n),
    "quiz_avg": np.random.randint(30, 100, n),
    "assign_avg": np.random.randint(35, 100, n),
    "midterm": np.random.randint(30, 100, n),
    "study_hours_wk": np.random.randint(1, 20, n),
    "on_time_submit_pct": np.random.randint(40, 100, n),
    "lms_logins_wk": np.random.randint(1, 30, n),
    "forum_posts": np.random.randint(0, 20, n),
    "commute_min": np.random.randint(5, 120, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "school_type": np.random.choice(["Private", "Government"], n),
    "parent_edu": np.random.choice(["HighSchool", "UG", "PG"], n)
}

df = pd.DataFrame(data)

df["passed"] = (
    (df["attendance_pct"] > 60) &
    (df["quiz_avg"] > 50) &
    (df["assign_avg"] > 50)
).astype(int)

df.to_csv("data/students.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())