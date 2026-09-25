import streamlit as st
import random

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="My School App",
    page_icon="🎓",
    layout="centered"
)

# =========================================================
# QUESTION DATABASE
# =========================================================

if "questions" not in st.session_state:
    st.session_state.questions = {
        "Mathematics": [
            {
                "question": "What is 12 × 8?",
                "options": ["86", "96", "108", "112"],
                "answer": "96"
            },
            {
                "question": "What is 25 + 37?",
                "options": ["52", "62", "72", "82"],
                "answer": "62"
            }
        ],

        "English": [
            {
                "question": "What is the past tense of 'go'?",
                "options": ["Goed", "Gone", "Went", "Going"],
                "answer": "Went"
            }
        ],

        "Science": [
            {
                "question": "What organelle is known as the powerhouse of the cell?",
                "options": [
                    "Nucleus",
                    "Mitochondria",
                    "Ribosome",
                    "Cell wall"
                ],
                "answer": "Mitochondria"
            }
        ]
    }

# =========================================================
# SESSION STATE
# =========================================================

if "profile_created" not in st.session_state:
    st.session_state.profile_created = False

if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []

if "quiz_number" not in st.session_state:
    st.session_state.quiz_number = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

# =========================================================
# SIDEBAR MENU
# =========================================================

st.sidebar.title("🎓 My School App")

page = st.sidebar.radio(
    "Choose a page:",
    [
        "👤 My Profile",
        "🧮 Calculator",
        "📊 Grade Calculator",
        "🧠 Quiz Master",
        "✏️ Edit Questions"
    ]
)

# =========================================================
# PROFILE
# =========================================================

if page == "👤 My Profile":

    st.title("👋 My First Profile")
    st.write(
        "Fill in your information and create your profile!"
    )

    name = st.text_input("👤 Name")
    age = st.number_input(
        "🎂 Age",
        min_value=1,
        max_value=100,
        step=1
    )

    school = st.text_input("🏫 School")
    subject = st.text_input("📚 Favorite Subject")
    hobby = st.text_input("🎮 Favorite Hobby")

    if st.button("✨ Create My Profile"):

        if name and school and subject and hobby:

            st.session_state.profile_created = True

            st.success(
                "Profile created successfully!"
            )

            st.subheader(
                f"Hello! My name is {name}."
            )

            st.write(
                f"🎂 I am {age} years old."
            )

            st.write(
                f"🏫 I go to {school}."
            )

            st.write(
                f"📚 My favorite subject is {subject}."
            )

            st.write(
                f"🎮 I enjoy {hobby}."
            )

            st.balloons()

        else:

            st.warning(
                "Please fill in all the fields!"
            )

elif page == "🧮 Calculator":

    st.title("🧮 Calculator")
    st.write("Use the buttons below like a normal calculator!")

    # Calculator memory
    if "calc_display" not in st.session_state:
        st.session_state.calc_display = "0"

    if "calc_first" not in st.session_state:
        st.session_state.calc_first = None

    if "calc_operator" not in st.session_state:
        st.session_state.calc_operator = None

    if "calc_new_number" not in st.session_state:
        st.session_state.calc_new_number = False

    # Function for number buttons
    def add_number(number):
        if st.session_state.calc_new_number:
            st.session_state.calc_display = number
            st.session_state.calc_new_number = False
        elif st.session_state.calc_display == "0":
            st.session_state.calc_display = number
        else:
            st.session_state.calc_display += number

    # Function for operators
    def set_operator(operator):
        st.session_state.calc_first = float(
            st.session_state.calc_display
        )
        st.session_state.calc_operator = operator
        st.session_state.calc_new_number = True

    # Display
    st.text_input(
        "Display",
        value=st.session_state.calc_display,
        disabled=True,
        key="calculator_display"
    )

    st.write("")

    # Row 1
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("7", key="calc_7", use_container_width=True):
            add_number("7")

    with col2:
        if st.button("8", key="calc_8", use_container_width=True):
            add_number("8")

    with col3:
        if st.button("9", key="calc_9", use_container_width=True):
            add_number("9")

    with col4:
        if st.button("÷", key="calc_divide", use_container_width=True):
            set_operator("/")

    # Row 2
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("4", key="calc_4", use_container_width=True):
            add_number("4")

    with col2:
        if st.button("5", key="calc_5", use_container_width=True):
            add_number("5")

    with col3:
        if st.button("6", key="calc_6", use_container_width=True):
            add_number("6")

    with col4:
        if st.button("×", key="calc_multiply", use_container_width=True):
            set_operator("*")

    # Row 3
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("1", key="calc_1", use_container_width=True):
            add_number("1")

    with col2:
        if st.button("2", key="calc_2", use_container_width=True):
            add_number("2")

    with col3:
        if st.button("3", key="calc_3", use_container_width=True):
            add_number("3")

    with col4:
        if st.button("−", key="calc_minus", use_container_width=True):
            set_operator("-")

    # Row 4
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("0", key="calc_0", use_container_width=True):
            add_number("0")

    with col2:
        if st.button(".", key="calc_decimal", use_container_width=True):
            if "." not in st.session_state.calc_display:
                st.session_state.calc_display += "."

    with col3:
        if st.button("C", key="calc_clear", use_container_width=True):
            st.session_state.calc_display = "0"
            st.session_state.calc_first = None
            st.session_state.calc_operator = None
            st.session_state.calc_new_number = False

    with col4:
        if st.button("+", key="calc_plus", use_container_width=True):
            set_operator("+")

    # Equals button
    if st.button("=", key="calc_equals", use_container_width=True):

        if (
            st.session_state.calc_first is not None
            and st.session_state.calc_operator is not None
        ):

            first = st.session_state.calc_first
            second = float(st.session_state.calc_display)
            operator = st.session_state.calc_operator

            if operator == "+":
                result = first + second

            elif operator == "-":
                result = first - second

            elif operator == "*":
                result = first * second

            elif operator == "/":
                if second == 0:
                    st.error("❌ Cannot divide by zero!")
                    result = None
                else:
                    result = first / second

            if result is not None:

                # Remove .0 from whole numbers
                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                st.session_state.calc_display = str(result)

                st.session_state.calc_first = None
                st.session_state.calc_operator = None
                st.session_state.calc_new_number = True

# =========================================================
# GRADE CALCULATOR
# =========================================================

elif page == "📊 Grade Calculator":

    st.title("📊 Grade Calculator")

    st.write(
        "Enter your subjects and grades below."
    )

    number_of_subjects = st.number_input(
        "Number of subjects",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

    grades = []

    st.write("---")

    for i in range(number_of_subjects):

        col1, col2 = st.columns(2)

        with col1:

            subject_name = st.text_input(
                f"Subject {i + 1}",
                value=f"Subject {i + 1}",
                key=f"subject_name_{i}"
            )

        with col2:

            grade = st.number_input(
                f"Grade",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                key=f"grade_{i}"
            )

        grades.append(
            (subject_name, grade)
        )

    st.write("---")

    if st.button(
        "📊 Calculate Grades",
        use_container_width=True
    ):

        total = sum(
            grade for subject, grade in grades
        )

        average = total / number_of_subjects

        # GPA calculation
        gpa = average / 25

        st.subheader("📋 Results")

        # Results box
        with st.container(border=True):

            st.write("### Your Grades")

            for subject_name, grade in grades:

                st.write(
                    f"📚 **{subject_name}:** {grade:.1f}"
                )

            st.write("---")

            st.metric(
                "Average",
                f"{average:.1f}"
            )

            st.metric(
                "GPA",
                f"{gpa:.2f} / 4.00"
            )

        # Feedback
        if average >= 90:

            st.success(
                "🏆 Excellent! Keep up the amazing work!"
            )

        elif average >= 80:

            st.success(
                "🎉 Good job! You're doing really well!"
            )

        elif average >= 70:

            st.info(
                "👍 Nice work! Keep improving!"
            )

        elif average >= 60:

            st.warning(
                "💪 Nice try! You can improve with more practice."
            )

        else:

            st.error(
                "📚 Keep studying and don't give up!"
            )

# =========================================================
# QUIZ MASTER
# =========================================================

elif page == "🧠 Quiz Master":

    st.title("🧠 Quiz Master")

    st.write(
        "Test your knowledge!"
    )

    # Start screen
    if not st.session_state.quiz_questions:

        subject = st.selectbox(
            "📚 Choose a subject",
            list(
                st.session_state.questions.keys()
            )
        )

        max_questions = len(
            st.session_state.questions[subject]
        )

        number = st.number_input(
            "🔢 Number of questions",
            min_value=1,
            max_value=max_questions,
            value=1,
            step=1
        )

        if st.button(
            "🚀 Start Quiz",
            use_container_width=True
        ):

            st.session_state.quiz_questions = random.sample(
                st.session_state.questions[subject],
                number
            )

            st.session_state.quiz_number = 0
            st.session_state.quiz_score = 0

            st.rerun()

    # Active quiz
    else:

        questions = st.session_state.quiz_questions
        current = st.session_state.quiz_number

        # Quiz finished
        if current >= len(questions):

            score = st.session_state.quiz_score
            total = len(questions)

            percentage = (
                score / total
            ) * 100

            st.balloons()

            st.title("🏆 Quiz Complete!")

            st.metric(
                "Score",
                f"{score} / {total}"
            )

            st.metric(
                "Percentage",
                f"{percentage:.0f}%"
            )

            if percentage >= 80:

                st.success(
                    "🎉 Excellent! Good job!"
                )

            elif percentage >= 50:

                st.warning(
                    "👍 Nice try! Keep practicing!"
                )

            else:

                st.error(
                    "💪 Don't give up! Try again!"
                )

            if st.button(
                "🔄 Try Again",
                use_container_width=True
            ):

                st.session_state.quiz_questions = []
                st.session_state.quiz_number = 0
                st.session_state.quiz_score = 0

                st.rerun()

        # Question
        else:

            question = questions[current]

            st.progress(
                current / len(questions)
            )

            st.write(
                f"### Question {current + 1} "
                f"/ {len(questions)}"
            )

            st.info(
                question["question"]
            )

            answer = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"quiz_answer_{current}"
            )

            if st.button(
                "Next ➡️",
                use_container_width=True
            ):

                if answer == question["answer"]:

                    st.session_state.quiz_score += 1

                st.session_state.quiz_number += 1

                st.rerun()

# =========================================================
# EDIT QUESTIONS
# =========================================================

elif page == "✏️ Edit Questions":

    st.title("✏️ Edit Quiz Questions")

    st.write(
        "Add, edit, or delete questions."
    )

    subject = st.selectbox(
        "📚 Choose subject",
        list(
            st.session_state.questions.keys()
        )
    )

    st.write("---")

    # Existing questions
    st.subheader("Existing Questions")

    for i, question in enumerate(
        st.session_state.questions[subject]
    ):

        with st.expander(
            f"Question {i + 1}"
        ):

            new_question = st.text_input(
                "Question",
                question["question"],
                key=f"edit_q_{subject}_{i}"
            )

            new_a = st.text_input(
                "A",
                question["options"][0],
                key=f"edit_a_{subject}_{i}"
            )

            new_b = st.text_input(
                "B",
                question["options"][1],
                key=f"edit_b_{subject}_{i}"
            )

            new_c = st.text_input(
                "C",
                question["options"][2],
                key=f"edit_c_{subject}_{i}"
            )

            new_d = st.text_input(
                "D",
                question["options"][3],
                key=f"edit_d_{subject}_{i}"
            )

            options = [
                new_a,
                new_b,
                new_c,
                new_d
            ]

            current_answer = (
                question["answer"]
            )

            if current_answer in options:

                answer_index = options.index(
                    current_answer
                )

            else:

                answer_index = 0

            new_answer = st.selectbox(
                "✅ Correct Answer",
                options,
                index=answer_index,
                key=f"edit_answer_{subject}_{i}"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "💾 Save",
                    key=f"save_{subject}_{i}"
                ):

                    st.session_state.questions[
                        subject
                    ][i] = {
                        "question": new_question,
                        "options": options,
                        "answer": new_answer
                    }

                    st.success(
                        "Question saved!"
                    )

            with col2:

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{subject}_{i}"
                ):

                    st.session_state.questions[
                        subject
                    ].pop(i)

                    st.rerun()

    # Add question
    st.write("---")

    st.subheader("➕ Add New Question")

    new_question = st.text_input(
        "Question",
        key="add_question"
    )

    new_a = st.text_input(
        "A",
        key="add_a"
    )

    new_b = st.text_input(
        "B",
        key="add_b"
    )

    new_c = st.text_input(
        "C",
        key="add_c"
    )

    new_d = st.text_input(
        "D",
        key="add_d"
    )

    correct = st.selectbox(
        "✅ Correct Answer",
        ["A", "B", "C", "D"],
        key="add_correct"
    )

    if st.button(
        "➕ Add Question",
        use_container_width=True
    ):

        options = [
            new_a,
            new_b,
            new_c,
            new_d
        ]

        if new_question and all(options):

            correct_answer = options[
                ["A", "B", "C", "D"].index(correct)
            ]

            st.session_state.questions[
                subject
            ].append({
                "question": new_question,
                "options": options,
                "answer": correct_answer
            })

            st.success(
                "🎉 Question added successfully!"
            )

        else:

            st.warning(
                "Please fill in every field."
            )
