from flask import Flask, render_template, request

from career_engine import recommend_careers, predict_career

app = Flask(__name__)


# ==========================================
# 1. SKILL GAP ANALYZER
# ==========================================

def analyze_skill_gap(recommendations):

    for item in recommendations:

        matched = item.get("matched_skills", [])
        missing = item.get("missing_skills", [])

        total_skills = len(matched) + len(missing)

        if total_skills > 0:
            skill_readiness = round(
                (len(matched) / total_skills) * 100
            )
        else:
            skill_readiness = 0

        if skill_readiness < 40:
            readiness_level = "Needs Improvement"

        elif skill_readiness < 70:
            readiness_level = "Developing"

        elif skill_readiness < 90:
            readiness_level = "Good Foundation"

        else:
            readiness_level = "Strong Foundation"

        item["skill_readiness"] = skill_readiness

        item["skill_gap_count"] = len(missing)

        item["readiness_level"] = readiness_level

        item["gap_summary"] = (
            f"You have {len(matched)} required skills "
            f"and need to learn {len(missing)} more skills."
        )

    return recommendations


# ==========================================
# 2. PERSONALIZED LEARNING SCHEDULE
# ==========================================

def generate_learning_schedule(missing_skills, days=30):

    learning_topics = {

        "python": [
            "Python Fundamentals",
            "Variables and Data Types",
            "Conditional Statements",
            "Loops and Functions",
            "Object Oriented Programming",
            "File Handling",
            "Exception Handling",
            "Mini Python Project"
        ],

        "java": [
            "Java Fundamentals",
            "Variables and Data Types",
            "Control Statements",
            "Classes and Objects",
            "Inheritance and Polymorphism",
            "Exception Handling",
            "Collections Framework",
            "Java Mini Project"
        ],

        "sql": [
            "Introduction to Databases",
            "SQL Basics",
            "SELECT and WHERE Queries",
            "ORDER BY and GROUP BY",
            "SQL Joins",
            "Subqueries",
            "Database Design",
            "SQL Practice Project"
        ],

        "html": [
            "HTML Fundamentals",
            "HTML Elements and Tags",
            "Forms and Tables",
            "Semantic HTML",
            "Building Web Pages"
        ],

        "css": [
            "CSS Fundamentals",
            "Selectors and Properties",
            "Box Model",
            "Flexbox",
            "CSS Grid",
            "Responsive Web Design"
        ],

        "javascript": [
            "JavaScript Fundamentals",
            "Variables and Data Types",
            "Functions",
            "DOM Manipulation",
            "Events",
            "Arrays and Objects",
            "JavaScript Mini Project"
        ],

        "git": [
            "Introduction to Git",
            "Git Installation and Setup",
            "Git Commands",
            "Git Branching",
            "GitHub Repositories",
            "Push and Pull Operations"
        ],

        "data structures": [
            "Introduction to Data Structures",
            "Arrays",
            "Linked Lists",
            "Stacks and Queues",
            "Searching Algorithms",
            "Sorting Algorithms",
            "Trees and Graphs",
            "Problem Solving Practice"
        ]
    }

    schedule = []

    if not missing_skills:
        missing_skills = ["Practical Project"]

    for day in range(1, days + 1):

        skill = missing_skills[
            (day - 1) % len(missing_skills)
        ]

        skill_key = skill.lower()

        topics = None

        for key in learning_topics:

            if key in skill_key:

                topics = learning_topics[key]
                break

        if topics is None:

            topics = [
                f"Introduction to {skill}",
                f"Learn the fundamentals of {skill}",
                f"Understand important concepts in {skill}",
                f"Practice {skill} exercises",
                f"Work on a mini project using {skill}"
            ]

        topic_index = (
            ((day - 1) // len(missing_skills)) % len(topics)
        )

        schedule.append({

            "day": day,

            "skill": skill,

            "topic": topics[topic_index],

            "duration": "1.5 hours",

            "status": "Pending"

        })

    return schedule


# ==========================================
# 3. HOME PAGE AND CAREER PREDICTION
# ==========================================

@app.route("/", methods=["GET", "POST"])

def home():

    profile = None

    recommendations = []

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        education = request.form.get(
            "education", ""
        ).strip()

        career_goal = request.form.get(
            "career_goal", ""
        ).strip()

        skills = request.form.get(
            "skills", ""
        ).strip()

        interests = request.form.get(
            "interests", ""
        ).strip()

        profile = {

            "name": name,

            "education": education,

            "career_goal": career_goal,

            "skills": skills,

            "interests": interests

        }

        # Career Recommendation

        if career_goal.lower() == "not sure yet":

            recommendations = recommend_careers(
                skills,
                interests
            )

        else:

            prediction = predict_career(
                career_goal,
                skills,
                interests
            )

            if prediction:

                recommendations = [prediction]

        # Skill Gap Analysis

        if recommendations:

            recommendations = analyze_skill_gap(
                recommendations
            )

        # Personalized 30-Day Learning Schedule

        for item in recommendations:

            item["learning_plan"] = generate_learning_schedule(

                item.get("missing_skills", []),

                days=30

            )

    return render_template(

        "index.html",

        profile=profile,

        recommendations=recommendations

    )

# ==========================================
# 4. CAREER-SPECIFIC READINESS ASSESSMENT
# ==========================================

COMMON_QUESTIONS = [

    {
        "question": "Which data structure follows LIFO?",
        "options": ["Queue", "Array", "Stack", "Linked List"],
        "answer": "Stack",
        "skill": "DSA"
    },

    {
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
        "answer": "O(log n)",
        "skill": "DSA"
    },

    {
        "question": "Which SQL command retrieves data?",
        "options": ["INSERT", "UPDATE", "SELECT", "DELETE"],
        "answer": "SELECT",
        "skill": "SQL"
    },

    {
        "question": "Which Git command uploads local commits?",
        "options": ["git pull", "git clone", "git push", "git init"],
        "answer": "git push",
        "skill": "Git"
    },

    {
        "question": "Which OOP principle hides implementation details?",
        "options": [
            "Inheritance",
            "Encapsulation",
            "Abstraction",
            "Polymorphism"
        ],
        "answer": "Abstraction",
        "skill": "OOP"
    }

]


# ==========================================
# CAREER-SPECIFIC QUESTION BANK
# ==========================================

CAREER_QUESTIONS = {

    "python": [

        {
            "question": "Which keyword defines a function in Python?",
            "options": ["function", "def", "fun", "define"],
            "answer": "def",
            "skill": "Python"
        },

        {
            "question": "Which data type stores key-value pairs?",
            "options": ["List", "Tuple", "Set", "Dictionary"],
            "answer": "Dictionary",
            "skill": "Python"
        },

        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#",
            "skill": "Python"
        },

        {
            "question": "Which keyword is used for inheritance in Python?",
            "options": ["extends", "inherits", "class", "super"],
            "answer": "class",
            "skill": "Python OOP"
        },

        {
            "question": "Which function returns the length of a list?",
            "options": ["size()", "count()", "len()", "length()"],
            "answer": "len()",
            "skill": "Python"
        }

    ],


    "java": [

        {
            "question": "Which keyword creates an object in Java?",
            "options": ["class", "new", "this", "static"],
            "answer": "new",
            "skill": "Java"
        },

        {
            "question": "Which method is the entry point of a Java program?",
            "options": ["start()", "run()", "main()", "execute()"],
            "answer": "main()",
            "skill": "Java"
        },

        {
            "question": "Which keyword is used for inheritance in Java?",
            "options": ["implements", "extends", "inherits", "super"],
            "answer": "extends",
            "skill": "Java OOP"
        },

        {
            "question": "Which collection does not allow duplicate elements?",
            "options": ["List", "ArrayList", "Set", "LinkedList"],
            "answer": "Set",
            "skill": "Java Collections"
        },

        {
            "question": "Which keyword prevents method overriding?",
            "options": ["static", "final", "private", "abstract"],
            "answer": "final",
            "skill": "Java"
        }

    ],


    "web": [

        {
            "question": "Which HTML tag creates a hyperlink?",
            "options": ["<link>", "<a>", "<href>", "<url>"],
            "answer": "<a>",
            "skill": "HTML"
        },

        {
            "question": "Which CSS property changes text colour?",
            "options": ["font", "background", "color", "text-style"],
            "answer": "color",
            "skill": "CSS"
        },

        {
            "question": "Which language adds interactivity to web pages?",
            "options": ["HTML", "CSS", "JavaScript", "SQL"],
            "answer": "JavaScript",
            "skill": "JavaScript"
        },

        {
            "question": "Which HTML tag creates an unordered list?",
            "options": ["<ol>", "<ul>", "<li>", "<list>"],
            "answer": "<ul>",
            "skill": "HTML"
        },

        {
            "question": "Which CSS layout system is one-dimensional?",
            "options": ["Grid", "Flexbox", "Table", "Float"],
            "answer": "Flexbox",
            "skill": "CSS"
        }

    ],


    "software": [

        {
            "question": "Which programming concept allows code reuse?",
            "options": ["Inheritance", "Compilation", "Debugging", "Execution"],
            "answer": "Inheritance",
            "skill": "Programming"
        },

        {
            "question": "Which testing checks individual program components?",
            "options": [
                "System Testing",
                "Unit Testing",
                "Acceptance Testing",
                "Integration Testing"
            ],
            "answer": "Unit Testing",
            "skill": "Software Testing"
        },

        {
            "question": "Which SDLC phase involves identifying requirements?",
            "options": [
                "Testing",
                "Maintenance",
                "Requirement Analysis",
                "Deployment"
            ],
            "answer": "Requirement Analysis",
            "skill": "Software Engineering"
        },

        {
            "question": "Which tool is commonly used for version control?",
            "options": ["Git", "Excel", "PowerPoint", "Paint"],
            "answer": "Git",
            "skill": "Version Control"
        },

        {
            "question": "What does API stand for?",
            "options": [
                "Application Programming Interface",
                "Advanced Programming Internet",
                "Application Process Integration",
                "Automated Program Instruction"
            ],
            "answer": "Application Programming Interface",
            "skill": "Software Development"
        }

    ],

    "cybersecurity": [

    {
        "question": "What does CIA stand for in cybersecurity?",
        "options": [
            "Central Intelligence Agency",
            "Confidentiality, Integrity, Availability",
            "Cyber Internet Access",
            "Control Information Authority"
        ],
        "answer": "Confidentiality, Integrity, Availability",
        "skill": "Cybersecurity Fundamentals"
    },

    {
        "question": "Which tool is commonly used for network packet analysis?",
        "options": ["Wireshark", "Photoshop", "Excel", "Git"],
        "answer": "Wireshark",
        "skill": "Network Security"
    },

    {
        "question": "What is phishing?",
        "options": [
            "A programming language",
            "A type of cyberattack using deceptive messages",
            "A database system",
            "A network protocol"
        ],
        "answer": "A type of cyberattack using deceptive messages",
        "skill": "Cyber Threats"
    },

    {
        "question": "Which encryption technique uses public and private keys?",
        "options": [
            "Symmetric encryption",
            "Asymmetric encryption",
            "Hashing",
            "Encoding"
        ],
        "answer": "Asymmetric encryption",
        "skill": "Cryptography"
    },

    {
        "question": "Which tool is commonly used for vulnerability scanning?",
        "options": ["Nmap", "MS Word", "PowerPoint", "Notepad"],
        "answer": "Nmap",
        "skill": "Vulnerability Assessment"
    }

],

    "cloud": [

    {
        "question": "What is cloud computing?",
        "options": [
            "Storing data only on a local computer",
            "Delivering computing services over the internet",
            "A programming language",
            "A database query"
        ],
        "answer": "Delivering computing services over the internet",
        "skill": "Cloud Fundamentals"
    },

    {
        "question": "Which of the following is an example of IaaS?",
        "options": [
            "Amazon EC2",
            "Gmail",
            "Google Docs",
            "Microsoft Word"
        ],
        "answer": "Amazon EC2",
        "skill": "Cloud Infrastructure"
    },

    {
        "question": "What is virtualization?",
        "options": [
            "Creating virtual versions of computing resources",
            "Deleting computer files",
            "Writing programming code",
            "Encrypting passwords"
        ],
        "answer": "Creating virtual versions of computing resources",
        "skill": "Virtualization"
    },

    {
        "question": "Which technology is commonly used for containerization?",
        "options": [
            "Docker",
            "Photoshop",
            "Excel",
            "Notepad"
        ],
        "answer": "Docker",
        "skill": "Containerization"
    },

    {
        "question": "What is the main purpose of cloud IAM?",
        "options": [
            "Managing user identities and access permissions",
            "Increasing screen resolution",
            "Editing images",
            "Creating presentations"
        ],
        "answer": "Managing user identities and access permissions",
        "skill": "Cloud Security"
    }

],


    "data_analyst": [

        {
            "question": "Which Python library is commonly used for data analysis?",
            "options": ["Pandas", "Flask", "Turtle", "Pygame"],
            "answer": "Pandas",
            "skill": "Python Data Analysis"
        },

        {
            "question": "Which SQL clause filters records?",
            "options": ["ORDER BY", "WHERE", "GROUP BY", "JOIN"],
            "answer": "WHERE",
            "skill": "SQL"
        },

        {
            "question": "What is the median?",
            "options": [
                "Most frequent value",
                "Middle value",
                "Average value",
                "Largest value"
            ],
            "answer": "Middle value",
            "skill": "Statistics"
        },

        {
            "question": "Which chart is useful for comparing categories?",
            "options": [
                "Bar Chart",
                "Scatter Plot",
                "Line Chart",
                "Histogram"
            ],
            "answer": "Bar Chart",
            "skill": "Data Visualization"
        },

        {
            "question": "Which function calculates the average in Excel?",
            "options": ["SUM()", "COUNT()", "AVERAGE()", "MAX()"],
            "answer": "AVERAGE()",
            "skill": "Data Analysis"
        }

    ]

}


# ==========================================
# IDENTIFY CAREER TYPE
# ==========================================

def get_career_key(career):

    career = career.lower()

    if "cyber" in career or "security" in career:
        return "cybersecurity"

    elif "cloud" in career:
        return "cloud"

    elif "python" in career:
        return "python"

    elif "java" in career:
        return "java"

    elif "web" in career or "frontend" in career or "front-end" in career:
        return "web"

    elif "data analyst" in career or "analyst" in career or "data scientist" in career or "scientist" in career:
        return "data_analyst"

    else:
        return "software"


# ==========================================
# ASSESSMENT ROUTE
# ==========================================

@app.route("/assessment", methods=["GET", "POST"])
def assessment():

    # Get the selected career from the submitted form or URL.
    if request.method == "POST":
        career = request.form.get(
            "career",
            "Software Developer"
        )
    else:
        career = request.args.get(
            "career",
            "Software Developer"
        )

    career_key = get_career_key(career)

    # Combine common questions with career-specific questions.
    career_questions = CAREER_QUESTIONS[career_key]
    questions = COMMON_QUESTIONS + career_questions

    # GET request: display the assessment questions.
    if request.method == "GET":
        return render_template(
            "assessment.html",
            questions=questions,
            career=career
        )

    # POST request: evaluate submitted answers.
    score = 0
    total = len(questions)
    results = []

    for index, question in enumerate(questions):

        selected = request.form.get(f"q{index}")
        correct = selected == question["answer"]

        if correct:
            score += 1

        results.append({
            "question": question["question"],
            "selected": selected or "Not Answered",
            "correct_answer": question["answer"],
            "is_correct": correct,
            "skill": question["skill"]
        })

        # Calculate overall assessment percentage.
    percentage = round((score / total) * 100) if total > 0 else 0

    if percentage >= 80:
        readiness = "Excellent"
    elif percentage >= 60:
        readiness = "Good"
    elif percentage >= 40:
        readiness = "Developing"
    else:
        readiness = "Needs Improvement"

    # Calculate performance separately for every skill.
    skill_performance = {}

    for result in results:

        skill = result["skill"]

        if skill not in skill_performance:
            skill_performance[skill] = {
                "total": 0,
                "correct": 0
            }

        skill_performance[skill]["total"] += 1

        if result["is_correct"]:
            skill_performance[skill]["correct"] += 1

    # Calculate percentage and performance level for each skill.
    for skill, data in skill_performance.items():

        if data["total"] > 0:
            data["percentage"] = round(
                (data["correct"] / data["total"]) * 100
            )
        else:
            data["percentage"] = 0

        if data["percentage"] >= 70:
            data["level"] = "Strong"

        elif data["percentage"] >= 40:
            data["level"] = "Moderate"

        else:
            data["level"] = "Needs Improvement"

    # Generate Personalized Improvement Suggestions.
    improvement_suggestions = []

    for skill, data in skill_performance.items():

        skill_percentage = data["percentage"]

        if skill_percentage < 40:

            suggestion = (
                f"Your {skill} fundamentals need improvement. "
                "Start with basic concepts and practise beginner-level problems."
            )

        elif skill_percentage < 70:

            suggestion = (
                f"You have developing knowledge in {skill}. "
                "Practise intermediate problems and work on small projects."
            )

        elif skill_percentage < 90:

            suggestion = (
                f"You have a good understanding of {skill}. "
                "Practise advanced concepts to strengthen your knowledge."
            )

        else:

            suggestion = (
                f"Excellent performance in {skill}! "
                "Continue practising advanced concepts and real-world projects."
            )

        improvement_suggestions.append({
            "skill": skill,
            "percentage": skill_percentage,
            "suggestion": suggestion
        })

    # Display the completed assessment results.
    return render_template(
        "assessment_result.html",
        score=score,
        total=total,
        percentage=percentage,
        readiness=readiness,
        results=results,
        career=career,
        skill_performance=skill_performance,
        improvement_suggestions=improvement_suggestions
    )

# ==========================================
# 5. RUN FLASK APPLICATION
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)
