import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------- SKILL MATCH SCORE --------

def skill_match_score(resume_text, jd_text):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, jd_text])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])

    return similarity[0][0]


# -------- EXPERIENCE SCORE --------

def experience_score(exp_years):

    # assume 10 years = full score
    score = min(exp_years / 10, 1)

    return score


# -------- EDUCATION SCORE --------

def education_score(education):

    education = education.lower()

    if "phd" in education:
        return 1

    elif "m.tech" in education or "master" in education or "mba" in education:
        return 0.8

    elif "b.tech" in education or "bachelor" in education or "bsc" in education:
        return 0.6

    else:
        return 0.3


# -------- LOCATION SCORE --------

def location_score(candidate_location, jd_text):

    if candidate_location.lower() in jd_text.lower():

        return 1

    return 0.5


# -------- FINAL SCORE --------

def final_score(skill_score, exp_score, edu_score, loc_score):

    score = (
        skill_score * 0.50 +
        exp_score * 0.25 +
        edu_score * 0.10 +
        loc_score * 0.15
    )

    return round(score * 100, 2)