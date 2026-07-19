import streamlit as st
import google.generativeai as genai
import os
# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title='LearnWise AI',
    page_icon='🎓',
    layout='wide'
)
# -------------------------
# Gemini Configuration
# -------------------------

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")
print(model.model_name)
# Custom CSS
# -------------------------
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(135deg,#eef2ff,#ffffff,#f3e8ff);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#2563eb,#6d28d9);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Navbar */
.navbar{
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(12px);
    padding: 18px 35px;
    border-radius: 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 8px 25px rgba(0,0,0,.08);
    margin-bottom: 40px;
}

.logo{
    font-size: 28px;
    font-weight: 700;
    color: #2563eb;
}

.menu{
    display: flex;
    gap: 28px;
    font-size: 15px;
    font-weight: 500;
    color: #475569;
}

/* Hero */
.hero{
    padding: 90px 70px;
    border-radius: 30px;
    text-align: center;
    background: linear-gradient(135deg,#2563eb,#4f46e5,#7c3aed);
    color: white;
    box-shadow: 0 18px 45px rgba(79,70,229,.25);
    margin-bottom: 55px;
}

.hero h1{
    font-size: 68px;
    font-weight: 800;
    margin-bottom: 18px;
}

.hero p{
    font-size: 23px;
    opacity: .95;
    margin-bottom: 35px;
}

/* Stats Cards */
.stats-card{
    background: white;
    border-radius: 22px;
    padding: 35px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,.08);
    transition: .35s;
    border: 1px solid rgba(99,102,241,.08);
}

.stats-card:hover{
    transform: translateY(-10px);
    box-shadow: 0 18px 45px rgba(79,70,229,.18);
}

.stats-number{
    font-size: 40px;
    font-weight: 700;
    background: linear-gradient(90deg,#2563eb,#7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stats-title{
    color: #64748b;
    margin-top: 10px;
    font-size: 16px;
}

/* Feature Cards */
.feature-card{
    background: white;
    border-radius: 22px;
    padding: 42px;
    box-shadow: 0 12px 28px rgba(0,0,0,.08);
    transition: .35s;
    border: 1px solid rgba(99,102,241,.08);
    min-height: 240px;
}

.feature-card:hover{
    transform: translateY(-10px);
    box-shadow: 0 20px 50px rgba(79,70,229,.18);
}

.feature-title{
    font-size: 26px;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 18px;
}

.feature-text{
    color: #64748b;
    line-height: 1.8;
}

/* Footer */
.footer{
    margin-top: 80px;
    text-align: center;
    color: #64748b;
    font-size: 15px;
}

/* Responsive */
@media (max-width: 768px){
    .hero{
        padding: 60px 30px;
    }

    .hero h1{
        font-size: 42px;
    }

    .hero p{
        font-size: 18px;
    }

    .menu{
        display: none;
    }
}
</style>
''', unsafe_allow_html=True)

# -------------------------
# Sidebar Navigation (FIX FOR ERROR)
# -------------------------
st.sidebar.title('🎓 LearnWise AI')

page = st.sidebar.radio(
    'Navigation',
    [
        'Home',
        'Dashboard',
        'Roadmap Generator',
        'Quiz Generator',
        'Career Coach'
    ]
)

# -------------------------
# HOME PAGE
# -------------------------
if page == 'Home':

    # Navbar
    st.markdown('''
    <div class="navbar">
        <div class="logo">LearnWise AI</div>
        <div class="menu">
            <span>Home</span>
            <span>Dashboard</span>
            <span>Roadmap</span>
            <span>Quiz</span>
            <span>Career Coach</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)

    # Hero
    st.markdown('''
    <div class="hero">
        <h1>LearnWise AI</h1>
        <p>Your Personal AI Learning Mentor</p>
    </div>
    ''', unsafe_allow_html=True)

    # CTA Button
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        st.button('Start Learning', use_container_width=True)

    st.write('')
    st.write('')

    # Statistics
    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown('''
        <div class="stats-card">
            <div class="stats-number">125+</div>
            <div class="stats-title">Roadmaps Generated</div>
        </div>
        ''', unsafe_allow_html=True)

    with s2:
        st.markdown('''
        <div class="stats-card">
            <div class="stats-number">250+</div>
            <div class="stats-title">Quizzes Created</div>
        </div>
        ''', unsafe_allow_html=True)

    with s3:
        st.markdown('''
        <div class="stats-card">
            <div class="stats-number">80+</div>
            <div class="stats-title">Career Sessions</div>
        </div>
        ''', unsafe_allow_html=True)

    with s4:
        st.markdown('''
        <div class="stats-card">
            <div class="stats-number">98%</div>
            <div class="stats-title">User Satisfaction</div>
        </div>
        ''', unsafe_allow_html=True)

    st.write('')
    st.write('')

    # Feature Cards
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('''
        <div class="feature-card">
            <div class="feature-title">AI Roadmap</div>
            <div class="feature-text">
                Build personalized learning paths with AI-generated step-by-step roadmaps to master any skill.
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with c2:
        st.markdown('''
        <div class="feature-card">
            <div class="feature-title">AI Quiz</div>
            <div class="feature-text">
                Instantly generate quizzes to test your knowledge, improve retention, and monitor your learning.
            </div>
        </div>
        ''', unsafe_allow_html=True)

    with c3:
        st.markdown('''
        <div class="feature-card">
            <div class="feature-title">AI Career Coach</div>
            <div class="feature-text">
                Receive personalized career guidance, interview preparation, and skill recommendations.
            </div>
        </div>
        ''', unsafe_allow_html=True)

    # Footer
    st.markdown('''
    <div class="footer">
        Developed with ❤️ by Anamika Keshri
    </div>
    ''', unsafe_allow_html=True)

# -------------------------
# DASHBOARD
# -------------------------
elif page == "Dashboard":

    st.title("📊 LearnWise AI Dashboard")
    st.caption("Monitor your learning progress.")

    # Session State
    if "roadmaps" not in st.session_state:
        st.session_state["roadmaps"] = []

    if "quiz_attempts" not in st.session_state:
        st.session_state["quiz_attempts"] = 0

    if "best_score" not in st.session_state:
        st.session_state["best_score"] = 0

    if "last_skill" not in st.session_state:
        st.session_state["last_skill"] = "None"

    # Top Metrics
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🛣️ Roadmaps", len(st.session_state["roadmaps"]))

    with c2:
        st.metric("📝 Quizzes", st.session_state["quiz_attempts"])

    with c3:
        st.metric("🏆 Best Score", f"{st.session_state['best_score']:.1f}%")

    st.divider()

    # Recent Activity
    st.subheader("📌 Recent Activity")

    if st.session_state["roadmaps"]:
        st.success(f"Last Roadmap Generated: **{st.session_state['last_skill']}**")
    else:
        st.info("No roadmap generated yet.")

    st.divider()

    # Skills Learned
    st.subheader("📚 Skills Learned")

    if st.session_state["roadmaps"]:
        for skill in st.session_state["roadmaps"]:
            st.write(f"✅ {skill}")
    else:
        st.write("No skills added yet.")

    st.divider()

    # Achievements
    st.subheader("🏅 Achievements")

    if len(st.session_state["roadmaps"]) >= 1:
        st.success("🎉 First Roadmap Generated")

    if st.session_state["quiz_attempts"] >= 1:
        st.success("📝 First Quiz Completed")

    if st.session_state["best_score"] >= 80:
        st.success("🏆 Excellent Performer")
# -------------------------
# AI ROADMAP GENERATOR
# -------------------------

elif page == "Roadmap Generator":

    st.title("🛣️Roadmap Generator")
    st.write("Create a personalized AI learning roadmap.")

    skill = st.text_input("Enter Skill")

    level = st.selectbox(
        "Current Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    hours = st.selectbox(
        "Weekly Study Hours",
        [
            "2-4 Hours",
            "5-8 Hours",
            "8-12 Hours",
            "12+ Hours"
        ]
    )

    if st.button("Generate Roadmap", use_container_width=True):

        # Validation
        if skill.strip() == "":
            st.warning("Please enter a skill.")
            st.stop()

        if not GEMINI_API_KEY:
            st.error("Gemini API key not configured.")
            st.stop()

        prompt = f"""
You are an expert AI mentor.

Create a complete learning roadmap.

Skill: {skill}
Current Level: {level}
Weekly Study Hours: {hours}

Include:

1. Beginner-friendly roadmap

2. Weekly learning schedule

3. Best free resources
   (YouTube, Courses, Documentation)

4. Practice projects

5. Estimated completion time

Format nicely using Markdown headings and bullet points.
"""

        try:

            with st.spinner("Generating your roadmap..."):

                response = model.generate_content(prompt)

                roadmap = response.text

            st.markdown(
                f"""
                <div style="
                    background:white;
                    padding:30px;
                    border-radius:18px;
                    box-shadow:0 8px 25px rgba(0,0,0,0.08);
                    border:1px solid #e5e7eb;
                    margin-top:20px;
                ">
                {roadmap}
                </div>
                """,
                unsafe_allow_html=True,
            )

        except Exception as e:

            st.error("Failed to generate roadmap.")

            st.exception(e)

# -------------------------
# AI QUIZ GENERATOR
# -------------------------
elif page == "Quiz Generator":

    import re

    st.title("📝 Quiz Generator")
    st.write("Generate AI-powered quizzes using Google Gemini.")

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = []

    topic = st.text_input("📘 Enter Topic")

    difficulty = st.selectbox(
        "🎯 Select Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    num_questions = st.slider(
        "📝 Number of Questions",
        1,
        10,
        5
    )

    if st.button("🚀 Generate Quiz", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a topic.")
            st.stop()

        prompt = f"""
Generate exactly {num_questions} multiple choice questions.

Topic: {topic}
Difficulty: {difficulty}

Return ONLY in this format:

Q1: Question
A) Option A
B) Option B
C) Option C
D) Option D
Answer: A
Explanation: Short explanation

Repeat for every question.
Do not use markdown.
"""

        try:

            with st.spinner("Generating Quiz..."):

                response = model.generate_content(prompt)

            quiz_text = response.text

            questions = re.findall(
                r"Q\d+:.*?(?=Q\d+:|$)",
                quiz_text,
                re.DOTALL
            )

            quiz = []

            for q in questions:

                lines = [
                    line.strip()
                    for line in q.split("\n")
                    if line.strip()
                ]

                if len(lines) >= 7:

                    quiz.append({
                        "question": lines[0],
                        "options": lines[1:5],
                        "answer": lines[5].replace("Answer:", "").strip().upper(),
                        "explanation": lines[6].replace("Explanation:", "").strip()
                    })

            if len(quiz) == 0:

                st.error("Unable to read Gemini response.")
                st.text(quiz_text)

            else:

                st.session_state.quiz_data = quiz
                st.rerun()

        except Exception as e:

            st.error("Quiz generation failed.")
            st.exception(e)

    if st.session_state.quiz_data:

        with st.form("quiz_form"):

            user_answers = []

            for i, q in enumerate(st.session_state.quiz_data):

                st.markdown(f"### {i+1}. {q['question']}")

                ans = st.radio(
                    "Choose your answer:",
                    q["options"],
                    key=f"quiz_{i}"
                )

                user_answers.append(ans)

                st.divider()

            submit = st.form_submit_button(
                "✅ Submit Quiz",
                use_container_width=True
            )

        if submit:

            score = 0
            total = len(st.session_state.quiz_data)

            st.header("📊 Quiz Results")

            for i, q in enumerate(st.session_state.quiz_data):

                selected = user_answers[i][0].upper()
                correct = q["answer"]

                st.markdown(f"### Question {i+1}")

                if selected == correct:

                    score += 1
                    st.success("✅ Correct")

                else:

                    st.error(
                        f"❌ Wrong! Correct Answer: {correct}"
                    )

                st.info(
                    "💡 " + q["explanation"]
                )

                st.divider()

            percentage = (score / total) * 100

            # Dashboard Statistics
            st.session_state["quiz_attempts"] = (
                st.session_state.get("quiz_attempts", 0) + 1
            )

            if percentage > st.session_state.get("best_score", 0):
                st.session_state["best_score"] = percentage

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "🏆 Score",
                    f"{score}/{total}"
                )

            with col2:
                st.metric(
                    "📈 Percentage",
                    f"{percentage:.1f}%"
                )

            st.progress(score / total)

            if percentage == 100:
                st.balloons()
                st.success("🌟 Perfect Score!")

            elif percentage >= 80:
                st.success("🎉 Excellent Performance!")

            elif percentage >= 60:
                st.info("👍 Good Job!")

            else:
                st.warning("📚 Keep Practicing!")

        if st.button("🔄 Generate New Quiz"):

            st.session_state.quiz_data = []
            st.rerun()
elif page == "AI Roadmap Generator":
    
    st.title("🛣️ AI Roadmap Generator")
    st.write("Create a personalized AI learning roadmap.")

    skill = st.text_input("📘 Enter Skill")

    level = st.selectbox(
        "🎯 Current Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    hours = st.selectbox(
        "⏰ Weekly Study Hours",
        [
            "2-4 Hours",
            "5-8 Hours",
            "8-12 Hours",
            "12+ Hours"
        ]
    )

    if st.button("🚀 Generate Roadmap", use_container_width=True):

        if skill.strip() == "":
            st.warning("Please enter a skill.")
            st.stop()

        prompt = f"""
You are an expert AI mentor.

Create a detailed learning roadmap.

Skill: {skill}
Current Level: {level}
Weekly Study Hours: {hours}

Include:

1. Learning roadmap
2. Weekly plan
3. Best free resources
4. Practice projects
5. Estimated completion time

Use Markdown.
"""

        try:

            with st.spinner("Generating Roadmap..."):

                response = model.generate_content(prompt)

            roadmap = response.text

            # -----------------------------
            # Save Dashboard Statistics
            # -----------------------------
            if "roadmaps" not in st.session_state:
                st.session_state["roadmaps"] = []

            st.session_state["roadmaps"].append(skill)

            st.session_state["last_skill"] = skill

            from datetime import datetime
            st.session_state["last_generated"] = datetime.now().strftime("%d %b %Y")

            # -----------------------------
            # Display Roadmap
            # -----------------------------
            st.success("✅ Roadmap Generated Successfully!")

            st.markdown(roadmap)

            st.divider()

            st.subheader("📌 Roadmap Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "🛣️ Total Roadmaps",
                    len(st.session_state["roadmaps"])
                )

            with col2:
                st.metric(
                    "📚 Current Skill",
                    skill
                )

        except Exception as e:

            st.error("Failed to generate roadmap.")
            st.exception(e)
# -------------------------
# CAREER COACH
# -------------------------
elif page == "Career Coach":

    st.title("💼 Career Coach")
    st.write("Get personalized AI career guidance based on your interests and goals.")

    career = st.text_input("🎯 Dream Career")

    education = st.selectbox(
        "🎓 Current Education",
        [
            "School Student",
            "Diploma",
            "B.Tech",
            "BCA",
            "MCA",
            "Other"
        ]
    )

    level = st.selectbox(
        "📚 Current Skill Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("🚀 Get Career Guidance", use_container_width=True):

        if career.strip() == "":
            st.warning("Please enter your dream career.")
            st.stop()

        prompt = f"""
You are an experienced career mentor.

Provide complete career guidance.

Career Goal: {career}

Education: {education}

Current Skill Level: {level}

Give the response in Markdown with the following headings:

# 🎯 Career Overview

Explain what this career is.

# 🛠 Required Skills

List technical and soft skills.

# 🗺 Learning Roadmap

Explain step by step what the student should learn.

# 📚 Best Free Learning Resources

Recommend YouTube channels, free courses and official documentation.

# 💻 Beginner Projects

Suggest 4-5 portfolio projects.

# 🏆 Recommended Certifications

Suggest valuable certifications.

# 💼 Top Companies Hiring

Mention popular companies hiring for this role.

# 💰 Expected Salary in India

Give Fresher, Mid-Level and Experienced salary ranges.

# 🎤 Interview Preparation

Mention interview topics and preparation tips.

# 💡 Final Advice

Motivate the student with practical advice.

Keep the response well formatted using bullet points.
"""

        try:

            with st.spinner("Generating Career Guidance..."):

                response = model.generate_content(prompt)

            advice = response.text

            st.success("✅ Career Guidance Generated Successfully!")

            st.markdown(advice)

            st.divider()

            st.subheader("📌 Career Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("🎯 Career", career)

            with col2:
                st.metric("🎓 Education", education)

            with col3:
