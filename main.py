import streamlit as st
import pandas as pd

from parser import *
from skills import extract_skills
from ranking import (
    skill_match_score,
    experience_score,
    education_score,
    location_score,
    final_score
)

st.title("AI Resume Ranking System")

jd = st.text_area("Paste Job Description")

files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

data = []
details = []

if st.button("Analyze Resumes"):

    if not jd:
        st.warning("Please enter Job Description")

    elif not files:
        st.warning("Please upload resumes")

    else:

        for file in files:

            # ---------- READ FILE ----------

            if file.name.endswith(".pdf"):
                text = read_pdf(file)
            else:
                text = read_docx(file)

            # ---------- PARSING ----------

            name = extract_name(text)
            email = extract_email(text)
            phone = extract_phone(text)
            skills = extract_skills(text)
            exp = extract_experience(text)
            education = extract_education(text)
            location = extract_location(text)

            # ---------- SCORING ----------

            skill_score = skill_match_score(text, jd)
            exp_score = experience_score(exp)
            edu_score = education_score(education)
            loc_score = location_score(location, jd)

            score = final_score(
                skill_score,
                exp_score,
                edu_score,
                loc_score
            )

            data.append({

                "Name": name,
                "Email": email,
                "Phone": phone,
                "Skills": ", ".join(skills),
                "Experience (Years)": exp,
                "Education": education,
                "Location": location,
                "Final Score": round(score,2)

            })

            # ranking engine ke liye store
            details.append({
                "name": name,
                "skill_score": round(skill_score,2),
                "exp_score": round(exp_score,2),
                "edu_score": round(edu_score,2),
                "loc_score": round(loc_score,2)
            })


        # ---------- DATAFRAME ----------

        df = pd.DataFrame(data)

        df = df.sort_values(by="Final Score", ascending=False)

        df["Rank"] = range(1, len(df) + 1)

        st.subheader("Candidate Ranking")

        st.dataframe(df)


        # ---------- RANKING ENGINE OUTPUT ----------

        st.subheader("5. Candidate Ranking Engine")

        for d in details:

            st.markdown(f"### {d['name']}")

            ranking_table = pd.DataFrame({

                "Factor": [
                    "Skills Match",
                    "Experience",
                    "Education",
                    "Location"
                ],

                "Weight": [
                    "50%",
                    "25%",
                    "10%",
                    "15%"
                ],

                "Result (%)": [
                    d["skill_score"],
                    d["exp_score"],
                    d["edu_score"],
                    d["loc_score"]
                ]

            })

            st.table(ranking_table)