# 🧠 Resume-to-Job Matching App

An AI-powered web application that matches resumes to job opportunities based on keyword similarity using Natural Language Processing (NLP). Built with `spaCy`, `NumPy`, and `Streamlit`, this tool helps recruiters and job seekers find the best matches efficiently.

---

## 📌 Features

- Match each job with the top 3 most relevant resumes
- View resume details: title, ID, keywords, and summary
- Simple and interactive UI with Streamlit
- Embeddings computed using `spaCy`'s `en_core_web_lg` model
- Euclidean distance for similarity scoring

---

## 🚀 Demo

📸 _Add a screenshot or GIF of your app here_

---

## 🛠 Technologies Used

- Python 3.x
- spaCy (`en_core_web_lg`)
- NumPy
- Streamlit

---

## 📂 Project Structure


├── resumes.json # List of resumes with title, text, keywords, etc.
├── job_opportunities.json # List of job descriptions and keywords
├── matcher_app.py # Main Streamlit app
├── README.md


---

## 📥 Installation

1. Clone the repository:

git clone https://github.com/your-username/resume-matching-app.git
cd resume-matching-app


Install dependencies:

pip install -r requirements.txt
python -m spacy download en_core_web_lg

Run the Streamlit app:

streamlit run matcher_app.py

📈 Example Output
When you select a job from the dropdown, you will see:

Job title

Job description

Keywords

Top 3 matching resumes with:

Resume title

Resume ID

Resume keywords

Resume summary

Similarity score (lower = more similar)

---

📄 Sample Data Format
resumes.json


[
  {
    "id": 1,
    "title": "Software Engineer Resume",
    "text": "Summary of experience in Python and web development...",
    "key_words": ["python", "django", "api", "backend", "software"]
  }
]
job_opportunities.json


[
  {
    "title": "Backend Developer",
    "text": "Looking for a backend developer with experience in Python and Django...",
    "key_words": ["backend", "python", "django", "rest", "sql"]
  }
]

---
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
---
📬 Contact
Feel free to reach out via LinkedIn or open an issue.
---
📝 License
This project is licensed under the MIT License.
