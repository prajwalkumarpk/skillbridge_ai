CAREER_PROFILES = {

    "Software Developer": {
        "skills": ["python", "java", "c", "javascript", "html", "css", "sql"],

        "skill_weights": {
            "python": 1.5,
            "java": 1.5,
            "c": 1.2,
            "javascript": 1.3,
            "html": 1.0,
            "css": 1.0,
            "sql": 1.0
        },

        "interests": [
            "programming",
            "web development",
            "problem solving"
        ],

        "roadmap": [
            "Learn programming fundamentals",
            "Master Data Structures and Algorithms",
            "Learn Object Oriented Programming",
            "Develop web applications",
            "Build real-world projects",
            "Apply for software internships"
        ]
    },

    "Data Scientist": {
        "skills": ["python", "sql", "statistics", "machine learning", "excel"],

        "skill_weights": {
            "python": 1.5,
            "sql": 1.3,
            "statistics": 1.5,
            "machine learning": 1.5,
            "excel": 1.0
        },

        "interests": [
            "data analysis",
            "statistics",
            "problem solving"
        ],

        "roadmap": [
            "Learn Python programming",
            "Study statistics and mathematics",
            "Master SQL",
            "Learn data visualization",
            "Study Machine Learning",
            "Build data science projects"
        ]
    },

    "AI/ML Engineer": {
        "skills": ["python", "machine learning", "statistics", "sql"],

        "skill_weights": {
            "python": 1.5,
            "machine learning": 1.8,
            "statistics": 1.5,
            "sql": 1.0
        },

        "interests": [
            "artificial intelligence",
            "machine learning",
            "research"
        ],

        "roadmap": [
            "Learn Python",
            "Study mathematics",
            "Understand Machine Learning",
            "Explore Deep Learning",
            "Build AI projects",
            "Apply for AI internships"
        ]
    },

    "Cybersecurity Analyst": {
        "skills": ["networking", "linux", "python", "security", "sql"],

        "skill_weights": {
            "networking": 1.5,
            "linux": 1.5,
            "python": 1.2,
            "security": 1.8,
            "sql": 1.0
        },

        "interests": [
            "cybersecurity",
            "ethical hacking",
            "networking"
        ],

        "roadmap": [
            "Learn networking fundamentals",
            "Learn Linux commands",
            "Study cybersecurity basics",
            "Practice ethical hacking in legal labs",
            "Build security projects",
            "Prepare for cybersecurity certifications"
        ]
    },

    "Cloud Engineer": {
        "skills": ["linux", "python", "networking", "sql", "javascript"],

        "skill_weights": {
            "linux": 1.5,
            "python": 1.2,
            "networking": 1.5,
            "sql": 1.0,
            "javascript": 1.0
        },

        "interests": [
            "cloud computing",
            "networking",
            "technology"
        ],

        "roadmap": [
            "Learn Linux",
            "Understand networking",
            "Study cloud computing",
            "Learn AWS or Azure",
            "Explore Docker",
            "Build cloud projects"
        ]
    }
}


# -----------------------------------
# SKILL ALIASES
# -----------------------------------

SKILL_ALIASES = {

    "python": ["python", "py"],

    "java": ["java", "core java"],

    "javascript": [
        "javascript",
        "js",
        "ecmascript"
    ],

    "html": [
        "html",
        "html5"
    ],

    "css": [
        "css",
        "css3"
    ],

    "sql": [
        "sql",
        "mysql",
        "structured query language"
    ],

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "statistics": [
        "statistics",
        "stats"
    ],

    "networking": [
        "networking",
        "computer networking",
        "computer networks"
    ],

    "linux": [
        "linux",
        "linux commands"
    ],

    "security": [
        "security",
        "information security",
        "cyber security",
        "cybersecurity"
    ],

    "excel": [
        "excel",
        "ms excel",
        "microsoft excel"
    ]
}


# -----------------------------------
# INTEREST ALIASES
# -----------------------------------

INTEREST_ALIASES = {

    "artificial intelligence": [
        "ai",
        "artificial intelligence",
        "ai/ml",
        "ai ml"
    ],

    "machine learning": [
        "ml",
        "machine learning"
    ],

    "programming": [
        "coding",
        "programming",
        "software programming"
    ],

    "web development": [
        "web development",
        "website development",
        "web designing",
        "frontend development",
        "front end development"
    ],

    "problem solving": [
        "problem solving",
        "logical thinking",
        "analytical thinking"
    ],

    "data analysis": [
        "data analysis",
        "data analytics",
        "data science"
    ],

    "cybersecurity": [
        "cybersecurity",
        "cyber security",
        "information security"
    ],

    "ethical hacking": [
        "ethical hacking",
        "penetration testing",
        "hacking"
    ],

    "cloud computing": [
        "cloud computing",
        "cloud technology",
        "cloud services"
    ],

    "networking": [
        "networking",
        "computer networks"
    ]
}


# -----------------------------------
# NORMALIZATION
# -----------------------------------

def prepare_list(value):

    if isinstance(value, str):

        return [
            item.strip().lower()
            for item in value.split(",")
            if item.strip()
        ]

    if not value:
        return []

    return [
        str(item).strip().lower()
        for item in value
        if str(item).strip()
    ]


def normalize_skill(skill):

    skill = skill.strip().lower()

    for standard, aliases in SKILL_ALIASES.items():

        if skill in aliases:
            return standard

    return skill


def normalize_interest(interest):

    interest = interest.strip().lower()

    for standard, aliases in INTEREST_ALIASES.items():

        if interest in aliases:
            return standard

    return interest


# -----------------------------------
# SMART CAREER EVALUATION
# -----------------------------------

def evaluate_career(career_name, career, skills, interests):

    student_skills = set(
        normalize_skill(skill)
        for skill in prepare_list(skills)
    )

    student_interests = set(
        normalize_interest(interest)
        for interest in prepare_list(interests)
    )

    # Match skills

    matched_skills = [
        skill for skill in career["skills"]
        if skill in student_skills
    ]

    missing_skills = [
        skill for skill in career["skills"]
        if skill not in student_skills
    ]

    # Match interests

    matched_interests = [
        interest for interest in career["interests"]
        if normalize_interest(interest) in student_interests
    ]

    # Weighted skill calculation

    weights = career.get("skill_weights", {})

    total_weight = sum(
        weights.get(skill, 1.0)
        for skill in career["skills"]
    )

    matched_weight = sum(
        weights.get(skill, 1.0)
        for skill in matched_skills
    )

    skill_score = (
        matched_weight / total_weight
        if total_weight else 0
    )

    # Interest calculation

    interest_score = (
        len(matched_interests) / len(career["interests"])
        if career["interests"] else 0
    )

    # Overall compatibility

    match_percentage = round(
        (skill_score * 70) +
        (interest_score * 30)
    )

    # Personalized explanation

    reasons = []

    if matched_skills:

        reasons.append(
            "Your skills in " +
            ", ".join(matched_skills) +
            " match this career."
        )

    if matched_interests:

        reasons.append(
            "Your interests in " +
            ", ".join(matched_interests) +
            " align with this career."
        )

    if not reasons:

        reasons.append(
            "This career could be explored "
            "by developing its foundational skills."
        )

    explanation = " ".join(reasons)

    return {

        "career": career_name,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "matched_interests": matched_interests,

        "skill_score": skill_score,

        "interest_score": interest_score,

        "match": match_percentage,

        "explanation": explanation,

        "roadmap": career["roadmap"],

        "score_breakdown": {
            "skill_percentage": round(skill_score * 100),
            "interest_percentage": round(interest_score * 100)
        }
    }


# -----------------------------------
# PREDICT SELECTED CAREER
# -----------------------------------

def predict_career(career_goal, skills, interests):

    career = CAREER_PROFILES.get(career_goal)

    if not career:
        return None

    return evaluate_career(
        career_goal,
        career,
        skills,
        interests
    )


# -----------------------------------
# RECOMMEND TOP THREE CAREERS
# -----------------------------------

def recommend_careers(skills, interests):

    recommendations = []

    for career_name, career in CAREER_PROFILES.items():

        result = evaluate_career(
            career_name,
            career,
            skills,
            interests
        )

        recommendations.append(result)

    # Rank careers by compatibility

    recommendations.sort(
        key=lambda item: (
            item["match"],
            item["skill_score"],
            item["interest_score"]
        ),
        reverse=True
    )

    return recommendations[:3]


# -----------------------------------
# SKILL GAP ANALYSIS
# -----------------------------------

def analyze_skill_gap(recommendations):

    for item in recommendations:

        matched = item["matched_skills"]

        missing = item["missing_skills"]

        total_skills = len(matched) + len(missing)

        if total_skills > 0:

            skill_readiness = round(
                (len(matched) / total_skills) * 100
            )

        else:

            skill_readiness = 0

        if skill_readiness < 40:

            readiness = "Needs Improvement"

        elif skill_readiness < 70:

            readiness = "Developing"

        elif skill_readiness < 90:

            readiness = "Good Foundation"

        else:

            readiness = "Strong Foundation"

        item["skill_readiness"] = skill_readiness

        item["skill_gap_count"] = len(missing)

        item["readiness_level"] = readiness

        item["gap_summary"] = (
            f"You have {len(matched)} required skills "
            f"and need to learn {len(missing)} more skills."
        )

    return recommendations