# Internship Domain Recommendation Engine

This project provides a **recommendation engine** for internship domains based on a user's profile (skills, interests, etc.), using content-based filtering in Python.

## Features

- Suggests internship domains tailored to your profile
- Simple web interface (Streamlit)
- Easily extendable with your own internship dataset

## Requirements

- Python 3.8+
- pandas
- scikit-learn
- streamlit

Install requirements:
```bash
pip install pandas scikit-learn streamlit
```

## Usage

### 1. Run the web app

```bash
streamlit run app.py
```

### 2. Enter your Profile

- Enter your skills, interests, or experience in the text area.
- Optionally upload your own `internship_domains.csv` file.
- Click **Get Recommendations** to see suggested domains.

### 3. Data

You can edit or replace `internship_domains.csv` with your own dataset. Format:

| domain                | description                                              | required_skills                    |
|-----------------------|---------------------------------------------------------|------------------------------------|
| Data Science          | Analyze datasets, build models, interpret data.         | Python, Data Analysis, Statistics  |

## Project Structure

- `recommendation_engine.py` – Core recommendation logic
- `app.py` – Streamlit app for user interface
- `internship_domains.csv` – Sample internship domains
- `README.md` – Documentation

## How it works

The engine uses **TF-IDF vectorization** to compare your profile text with domain descriptions, ranking the most relevant internship domains for you.

---

**Extend:**  
- Add collaborative filtering or hybrid methods  
- Add authentication/user profiles  
- Integrate with internship APIs

---

Enjoy exploring your career options!