# AI Resume Ranking System

An AI-powered Resume Screening and Candidate Ranking system built using **Python** and **Streamlit**.
The application extracts key information from uploaded resumes (PDF/DOCX), compares them with a Job Description, and ranks candidates based on multiple evaluation factors.

---

## 🚀 Features

* Upload multiple resumes (**PDF / DOCX**)
* Automatic resume parsing:

  * Full Name
  * Email Address
  * Phone Number
  * Skills
  * Years of Experience
  * Education
  * Location
* Job Description matching
* Skill similarity calculation using **TF-IDF + Cosine Similarity**
* Candidate ranking based on weighted scoring
* Interactive UI using **Streamlit**

---

## 🧠 Candidate Ranking Engine

Candidates are ranked using the following weighted scoring model:

| Factor       | Weight |
| ------------ | ------ |
| Skills Match | 50%    |
| Experience   | 25%    |
| Education    | 10%    |
| Location     | 15%    |

The final score is calculated using these weights and candidates are ranked accordingly.

---

## 📂 Project Structure

```
AI-Resume-Ranking-System
│
├── app.py              # Streamlit application
├── parser.py           # Resume text parsing logic
├── skills.py           # Skill extraction module
├── ranking.py          # Candidate scoring algorithm
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-resume-ranking-system.git
cd ai-resume-ranking-system
```

### 2️⃣ Create virtual environment (recommended)

If using **uv**

```bash
uv venv
```

Activate environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac / Linux**

```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
uv pip install -r requirements.txt
```

or

```bash
pip install -r requirements.txt
```

---

## 📦 Required Libraries

* streamlit
* pandas
* scikit-learn
* pdfplumber
* python-docx
* regex

---

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser.

---

## 📝 How It Works

1. User enters a **Job Description**.
2. User uploads one or more **resumes**.
3. The system extracts structured information from each resume.
4. Resume content is compared with the Job Description using **TF-IDF similarity**.
5. Each candidate receives a score based on:

   * Skill match
   * Experience
   * Education
   * Location
6. Candidates are **ranked automatically**.

---

## 📊 Output

The system displays:

### Candidate Ranking Table

Includes:

* Name
* Email
* Phone
* Skills
* Experience
* Education
* Location
* Final Score
* Rank

### Ranking Engine Breakdown

Shows how the score was calculated for each candidate.

---

## 🔧 Future Improvements

Possible enhancements:

* Better **Named Entity Recognition (NER)** for resume parsing
* Use **spaCy / NLP models** for accurate skill extraction
* Resume keyword highlighting
* Missing skill detection
* ATS-style resume scoring
* Export ranked candidates to **CSV/Excel**

---

## 📜 License

This project is for educational and demonstration purposes.

---

## 👨‍💻 Author

Developed as part of an **AI Resume Screening / Candidate Ranking System project** using Python and Streamlit.
