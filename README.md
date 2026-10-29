# Terence Ed Limpio | Autobiography and Portfolio (CSIT 349)

## A. Run it on your computer (first time)
1. Install Python 3.10+ from https://python.org (tick "Add Python to PATH").
2. Unzip this folder, e.g. to Desktop/portfolio.
3. Open a terminal IN that folder (Windows: type `cmd` in the folder's address bar).
4. (Recommended) Make a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - Mac/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
5. Install packages: `pip install -r requirements.txt`
6. Run: `streamlit run app.py`
7. Your browser opens at http://localhost:8501. Press Ctrl+C in the terminal to stop.

## B. Edit your content
Open app.py in VS Code / Notepad. Everything in PART 1 ("EDIT ME") is yours:
- NAME, SECTION, PROGRAM, SCHOOL, EMAIL, GITHUB, LINKEDIN
- SHORT_BIO, BACKGROUND, EDUCATION, INTERESTS, MILESTONES
- SKILLS (your own 0-100 numbers) and MONTHLY_HOURS
- PROJECTS: copy one { ... } block, paste it, change the values
- Photo: save your picture as profile.jpg next to app.py (it replaces the placeholder)
Save the file, then click "Rerun" in the browser.

You can also add a project from the Projects tab > "Add a project". It shows a
code snippet; paste that into PROJECTS to keep it permanently.

## C. Deploy for the +10 bonus
1. Make a free account at https://github.com.
2. New repository > Public > name it e.g. `my-portfolio`.
3. Upload app.py, requirements.txt, profile.jpg/png, and the .streamlit folder
   (drag and drop in "Add file > Upload files"). Do NOT upload .venv or secrets.
4. Go to https://share.streamlit.io, sign in with GitHub.
5. Click "Create app" > pick your repo, branch `main`, main file `app.py` > Deploy.
6. After ~2 minutes you get a link like https://yourname.streamlit.app. Submit it.
   To update later: edit the file on GitHub; the app redeploys automatically.

## D. Submit (Option A: zip)
Zip app.py, requirements.txt, profile image, .streamlit folder. Leave out .venv.
Put your name and section in the submission comment.
