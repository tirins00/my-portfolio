"""
Terence Ed Limpio | Autobiography and Portfolio
CSIT 349 - Applied AI

HOW TO EDIT THIS APP
--------------------
Everything you will want to change is in PART 1 (the "EDIT ME" section below).
Change the text between the quotes, save the file, and the browser page
will offer a "Rerun" / "Always rerun" button. Click it to see your changes.

Do NOT edit PART 2 unless you want to change the layout.
"""

import json
import os
from datetime import date

import numpy as np
import pandas as pd
import streamlit as st

# =============================================================================
# PART 1 - EDIT ME  (your content lives here)
# =============================================================================

# ---- Basic info -------------------------------------------------------------
NAME = "Terence Ed Limpio"
COURSE = "CSIT 349 - Applied AI"                  
PROGRAM = "BS Information Technology - 4th year"            
SCHOOL = "Cebu Institute of Technology - University"   
SECTION = "G01"       
LOCATION = "Cebu City, Philippines"
EMAIL = "terins.0015@gmail.com"            
GITHUB = "https://github.com/tirins00" 
LINKEDIN = "https://linkedin.com/in/terence-ed-limpio-aba545378/" 
TAGLINE = "Aspiring AI developer who learns by building. | Trust the process."  

PHOTO_CANDIDATES = ["profile.jpg", "profile.jpeg", "profile.png"]

SHORT_BIO = (
    "Hi! I'm Terence, a student from Cebu who enjoys turning ideas into working "
    "software. I'm currently learning how applied AI can solve everyday problems, "
    "and this page is my first Streamlit app."
) 

BACKGROUND = """
This is a short background about me.  
"""  

EDUCATION = [
    # (period, school/level, details)  <- EDIT / add or remove rows
    ("2010 - 2016", "Athenaeum International School", "Elementary Graduate"),
    ("2016 - 2020", "Athenaeum International School", "With Honors, Junior High Graduate"),
    ("2020 - 2022", "University of San Jose - Recoletos", "Senior High Graduate"),
    ("2022 - Present", "Cebu Insitute of Technology - University", "BS Information Technology - 4th year"),
]

INTERESTS = [
    # <- EDIT: your real interests
    "Programming", "Artificial Intelligence", "Gaming", "Music", "Basketball",
]

MILESTONES = [
    (2022, "Started college", "Began my journey in the field of computing."),
    (2023, "Wrote my first real program", "It was a simple Java game called \"Knock Out!\""),
    (2024, "Joined a school project / org", "What did you learn from it?"),
    (2025, "Took Applied AI", "Built my first Streamlit app for CSIT 349."),
]

# ---- Skills: your own numbers (0-100) ---------------------------------------
SKILLS = {
    # skill: (level 0-100, category)   <- EDIT honestly, these power the chart
    "Python": (75, "Programming"),
    "SQL": (60, "Data"),
    "HTML/CSS": (65, "Web"),
    "JavaScript": (50, "Web"),
    "Pandas / NumPy": (60, "Data"),
    "Git & GitHub": (55, "Tools"),
    "Communication": (70, "Soft skill"),
    "Teamwork": (80, "Soft skill"),
}

# A second chart: e.g. hours you spent coding each month this year  <- EDIT
MONTHLY_HOURS = {
    "Jun": 20, "Jul": 28, "Aug": 35, "Sep": 40, "Oct": 52,
}

# ---- Projects (need at least 3) ---------------------------------------------
# To add a project: copy one block, paste it below, and change the values.
PROJECTS = [
    {
        "title": "Project One",                       # <- EDIT
        "role": "Lead developer",
        "tools": ["Python", "Pandas"],
        "category": "Data",
        "year": 2024,
        "outcome": "Describe what the project did and what result you got.",
        "link": "https://github.com/your-username/project-one",
    },
    {
        "title": "Project Two",
        "role": "Frontend developer",
        "tools": ["HTML/CSS", "JavaScript"],
        "category": "Web",
        "year": 2024,
        "outcome": "Describe what the project did and what result you got.",
        "link": "https://github.com/your-username/project-two",
    },
    {
        "title": "Project Three",
        "role": "Solo developer",
        "tools": ["Python", "Streamlit"],
        "category": "AI",
        "year": 2025,
        "outcome": "Describe what the project did and what result you got.",
        "link": "https://github.com/your-username/project-three",
    },
]

# =============================================================================
# PART 2 - THE APP  (you can leave this alone)
# =============================================================================

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Session state (memory that survives reruns) ----------------------
if "extra_projects" not in st.session_state:
    st.session_state.extra_projects = []   # projects added while the app runs
if "messages" not in st.session_state:
    st.session_state.messages = []         # feedback received
if "visits" not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1


def find_photo():
    for f in PHOTO_CANDIDATES:
        if os.path.exists(f):
            return f
    return None


def all_projects():
    return PROJECTS + st.session_state.extra_projects


def skills_df():
    return pd.DataFrame(
        [{"Skill": k, "Level": v[0], "Category": v[1]} for k, v in SKILLS.items()]
    )


# ---------- Sidebar -----------------------------------------------------------
with st.sidebar:
    photo = find_photo()
    if photo:
        st.image(photo, caption="Photo (replace profile.png with your own)")
    st.header(NAME)
    st.caption(f"{COURSE}\n\n{SECTION}")
    st.write(f"🎓 {PROGRAM}")
    st.write(f"📍 {LOCATION}")
    st.divider()

    st.subheader("⚙️ Page options")
    show_photo_note = st.checkbox("Show welcome banner", value=True)
    accent = st.selectbox(
        "Highlight color for headings",
        ["Blue", "Green", "Orange", "Pink"],
    )
    detail = st.radio("Project detail level", ["Compact", "Detailed"], horizontal=True)
    st.divider()

    st.subheader("🔗 Links")
    st.link_button("GitHub", GITHUB)
    st.link_button("LinkedIn", LINKEDIN)
    st.divider()
    st.caption(f"Page views this session: {st.session_state.visits}")

ACCENTS = {"Blue": "blue", "Green": "green", "Orange": "orange", "Pink": "red"}
color = ACCENTS[accent]

# ---------- Header ------------------------------------------------------------
st.title(f"👋 {NAME}")
st.markdown(f"#### :{color}[{TAGLINE}]")
st.caption(f"{COURSE}  ·  {SECTION}  ·  {PROGRAM}, {SCHOOL}")

if show_photo_note:
    st.info("Welcome to my autobiography and portfolio. Use the tabs below to explore.", icon="✨")

tab_home, tab_bio, tab_skills, tab_projects, tab_contact = st.tabs(
    ["🏠 Home", "📖 Autobiography", "🛠️ Skills", "💼 Projects", "✉️ Contact"]
)

# ---------- HOME --------------------------------------------------------------
with tab_home:
    left, right = st.columns([1, 2], gap="large")
    with left:
        photo = find_photo()
        if photo:
            st.image(photo, caption=f"{NAME}")
    with right:
        st.header(f":{color}[About me]")
        st.write(SHORT_BIO)

        m1, m2, m3 = st.columns(3)
        m1.metric("Projects", len(all_projects()))
        m2.metric("Skills tracked", len(SKILLS))
        avg = int(np.mean([v[0] for v in SKILLS.values()]))
        m3.metric("Avg. skill level", f"{avg}/100")

        st.subheader("Interests")
        st.write("  ".join(f"`{i}`" for i in INTERESTS))

    st.divider()
    st.subheader("Quick facts")
    facts = pd.DataFrame(
        {
            "Field": ["Name", "Program", "School", "Course", "Section", "Location"],
            "Details": [NAME, PROGRAM, SCHOOL, COURSE, SECTION, LOCATION],
        }
    )
    st.table(facts.set_index("Field"))

# ---------- AUTOBIOGRAPHY ----------------------------------------------------
with tab_bio:
    st.header(f":{color}[My story]")

    c1, c2 = st.columns([3, 2], gap="large")
    with c1:
        st.subheader("Background")
        st.markdown(BACKGROUND)

        with st.expander("🎓 Education", expanded=True):
            edu_df = pd.DataFrame(EDUCATION, columns=["Period", "School", "Details"])
            st.dataframe(edu_df, hide_index=True)

    with c2:
        st.subheader("Interests")
        picked = st.multiselect("Pick interests to highlight", INTERESTS, default=INTERESTS[:3])
        if picked:
            st.success("I enjoy: " + ", ".join(picked))
        else:
            st.warning("Select at least one interest.")

    st.divider()
    st.subheader("Milestones")
    years = [m[0] for m in MILESTONES]
    if len(years) > 1 and min(years) != max(years):
        year_range = st.slider(
            "Show milestones from year…",
            min_value=min(years),
            max_value=max(years),
            value=(min(years), max(years)),
        )
    else:
        year_range = (min(years), max(years))

    for yr, title, desc in MILESTONES:
        if year_range[0] <= yr <= year_range[1]:
            with st.container(border=True):
                a, b = st.columns([1, 6])
                a.markdown(f"### {yr}")
                b.markdown(f"**{title}**")
                b.write(desc)

    # Download the autobiography as a text file
    bio_text = (
        f"{NAME}\n{PROGRAM}, {SCHOOL}\n{COURSE} - {SECTION}\n\n"
        f"ABOUT\n{SHORT_BIO}\n\nBACKGROUND\n{BACKGROUND.strip()}\n\nMILESTONES\n"
        + "\n".join(f"{y} - {t}: {d}" for y, t, d in MILESTONES)
    )
    st.download_button(
        "⬇️ Download my autobiography (.txt)",
        data=bio_text,
        file_name="autobiography_terence_limpio.txt",
        mime="text/plain",
    )

# ---------- SKILLS ------------------------------------------------------------
with tab_skills:
    st.header(f":{color}[Skills]")
    st.write(
        "These numbers are my own self-assessment (0 = beginner, 100 = expert). "
        "Use the controls to explore them."
    )

    df = skills_df()
    f1, f2 = st.columns(2)
    with f1:
        cats = st.multiselect(
            "Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique())
        )
    with f2:
        min_level = st.slider("Minimum level", 0, 100, 0, step=5)

    view = df[df["Category"].isin(cats) & (df["Level"] >= min_level)].sort_values(
        "Level", ascending=False
    )

    t1, t2 = st.columns([1, 1], gap="large")
    with t1:
        st.subheader("Skill table")
        st.dataframe(
            view,
            hide_index=True,
            column_config={
                "Level": st.column_config.ProgressColumn(
                    "Level", min_value=0, max_value=100, format="%d"
                )
            },
        )
    with t2:
        st.subheader("Skill chart")
        if view.empty:
            st.warning("No skills match those filters.")
        else:
            st.bar_chart(view.set_index("Skill")["Level"])

    st.divider()
    st.subheader("Coding hours per month")
    hours = pd.DataFrame({"Month": list(MONTHLY_HOURS), "Hours": list(MONTHLY_HOURS.values())})
    h1, h2 = st.columns([2, 1])
    with h1:
        st.line_chart(hours.set_index("Month"))
    with h2:
        st.metric("Total hours", int(hours["Hours"].sum()))
        delta = int(hours["Hours"].iloc[-1] - hours["Hours"].iloc[0])
        st.metric("Growth since first month", f"{hours['Hours'].iloc[-1]} h", f"{delta:+d} h")

    st.subheader("Skill spotlight")
    spot = st.selectbox("Choose a skill", list(SKILLS.keys()))
    lvl, cat = SKILLS[spot]
    st.progress(lvl / 100, text=f"{spot} ({cat}): {lvl}/100")

# ---------- PROJECTS ----------------------------------------------------------
with tab_projects:
    st.header(f":{color}[Projects]")

    projects = all_projects()
    all_tools = sorted({t for p in projects for t in p["tools"]})
    all_cats = sorted({p["category"] for p in projects})

    p1, p2, p3 = st.columns(3)
    with p1:
        tool_filter = st.multiselect("Filter by tool", all_tools)
    with p2:
        cat_filter = st.selectbox("Category", ["All"] + all_cats)
    with p3:
        view_mode = st.radio("View as", ["Cards", "Table"], horizontal=True)

    shown = [
        p
        for p in projects
        if (not tool_filter or set(tool_filter) & set(p["tools"]))
        and (cat_filter == "All" or p["category"] == cat_filter)
    ]
    st.caption(f"Showing {len(shown)} of {len(projects)} projects")

    if view_mode == "Table":
        tdf = pd.DataFrame(shown)
        if not tdf.empty:
            tdf["tools"] = tdf["tools"].apply(", ".join)
            st.dataframe(
                tdf,
                hide_index=True,
                column_config={"link": st.column_config.LinkColumn("link")},
            )
    else:
        cols = st.columns(3)
        for i, p in enumerate(shown):
            with cols[i % 3]:
                with st.container(border=True):
                    st.subheader(p["title"])
                    st.caption(f"{p['category']} · {p['year']}")
                    st.write(f"**Role:** {p['role']}")
                    st.write("**Tools:** " + " ".join(f"`{t}`" for t in p["tools"]))
                    if detail == "Detailed":
                        st.write(f"**Outcome:** {p['outcome']}")
                    if p.get("link"):
                        st.link_button("View project", p["link"])

    st.divider()
    with st.expander("➕ Add a project (try it out!)"):
        st.write(
            "Fill this in to add a project to the page right now. It lasts until you refresh. "
            "To keep it forever, copy the code shown after you add it into the "
            "`PROJECTS` list near the top of `app.py`."
        )
        with st.form("add_project", clear_on_submit=True):
            n_title = st.text_input("Project title")
            n_role = st.text_input("Your role")
            n_tools = st.text_input("Tools used (separate with commas)")
            n_cat = st.selectbox("Category", ["Web", "Data", "AI", "Mobile", "Game", "Other"])
            n_year = st.number_input("Year", min_value=2000, max_value=2100, value=date.today().year)
            n_out = st.text_area("Outcome / what happened")
            n_link = st.text_input("Link (optional)")
            add = st.form_submit_button("Add project")

        if add:
            if not n_title.strip():
                st.error("Please enter a project title.")
            else:
                new = {
                    "title": n_title.strip(),
                    "role": n_role.strip() or "Developer",
                    "tools": [t.strip() for t in n_tools.split(",") if t.strip()] or ["N/A"],
                    "category": n_cat,
                    "year": int(n_year),
                    "outcome": n_out.strip() or "No description yet.",
                    "link": n_link.strip(),
                }
                st.session_state.extra_projects.append(new)
                st.toast("Project added!", icon="✅")
                st.success("Added! Copy this into the PROJECTS list in app.py to make it permanent:")
                st.code(json.dumps(new, indent=4) + ",", language="python")

        if st.session_state.extra_projects:
            if st.button("🗑️ Remove projects added this session"):
                st.session_state.extra_projects = []
                st.rerun()

# ---------- CONTACT -----------------------------------------------------------
with tab_contact:
    st.header(f":{color}[Contact & feedback]")
    c1, c2 = st.columns([1, 1], gap="large")

    with c1:
        st.subheader("Get in touch")
        st.write(f"📧 {EMAIL}")
        st.write(f"📍 {LOCATION}")
        st.write(f"🏫 {SCHOOL}")
        st.link_button("Visit my GitHub", GITHUB)

        st.subheader("Messages this session")
        if st.session_state.messages:
            for m in st.session_state.messages[-5:]:
                with st.container(border=True):
                    st.write(f"**{m['name']}** rated this page {'⭐' * m['rating']}")
                    st.write(m["text"])
        else:
            st.caption("No messages yet. Be the first!")

    with c2:
        st.subheader("Leave feedback")
        with st.form("feedback_form", clear_on_submit=True):
            f_name = st.text_input("Your name")
            f_email = st.text_input("Your email")
            f_type = st.selectbox("This is a…", ["Comment", "Question", "Job / collab offer"])
            f_rating = st.select_slider("How did you like this page?", [1, 2, 3, 4, 5], value=4)
            f_text = st.text_area("Message")
            f_agree = st.checkbox("You may reply to my email")
            sent = st.form_submit_button("Send")

        if sent:
            if not f_name.strip() or not f_text.strip():
                st.error("Please enter your name and a message.")
            else:
                st.session_state.messages.append(
                    {"name": f_name.strip(), "rating": f_rating, "text": f_text.strip()}
                )
                st.success(
                    f"Thank you, {f_name.strip()}! Your {f_type.lower()} was received."
                    + (" I'll reply by email." if f_agree and f_email.strip() else "")
                )
                st.balloons()

# ---------- Footer ------------------------------------------------------------
st.divider()
st.caption(f"© {date.today().year} {NAME} · {COURSE} · {SECTION} · Built with Streamlit")
