skills_list = [
"python",
"java",
"sql",
"machine learning",
"react",
"node",
"aws",
"docker",
"data analysis"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_list:

        if skill in text:
            found.append(skill)

    return found