'''import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Salary Prediction", layout="centered", initial_sidebar_state="collapsed")

# ---------- REMOVE SIDEBAR ----------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="collapsedControl"] {display: none;}
</style>
""", unsafe_allow_html=True)

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.stApp {
    background-color: #111827;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3, label {
    color: #FFFFFF !important;
}


.stSelectbox > div > div {
    background-color: white !important;
    color: black !important;
}

.stNumberInput input {
    background-color: white !important;
    color: black !important;
}

.stButton>button {
    background-color: #3b82f6;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
}

.result-box {
    background-color: #16a34a;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 30px;
}

.info-text {
    text-align: center;
    margin-top: 20px;
    font-size: 15px;
    color: #e5e7eb;
}

.company-card {
    background:#1f2937;
    padding:18px;
    border-radius:10px;
    margin-bottom:12px;
    border-left:5px solid #3b82f6;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = pd.read_csv("Salary_prediction.csv")
df.columns = df.columns.str.strip()

X = df[["years_experience"]]
y = df["salary_per annum"]

model = LinearRegression()
model.fit(X, y)

# ==============================
# HOME PAGE
# ==============================
if st.session_state.page == "home":

    st.title(" 💼 Salary Prediction")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    role = st.selectbox("Select Your Role", df["Role"].unique())
    experience = st.number_input("Enter YourYears of Experience", min_value=0.0, step=0.1,value=None,format="%.1f")
    expected_salary = st.number_input("Enter Your Expected Salary (Optional)", min_value=0.0, step=10000.0,value=None,format="%.1f")

    if st.button("🚀 Predict Salary"):

        predicted_salary = model.predict([[experience]])[0]
        
        
            # Clean display values (remove .00)
        exp_display = str(experience).rstrip('0').rstrip('.') if experience is not None else ""
        expected_display = str(expected_salary).rstrip('0').rstrip('.') if expected_salary else ""


        st.session_state.predicted_salary = predicted_salary
        st.session_state.role = role
        st.session_state.experience = experience
        st.session_state.expected_salary = expected_salary

    st.markdown('</div>', unsafe_allow_html=True)

    # Show result only after prediction
    if "predicted_salary" in st.session_state:

        salary_display = str(round(st.session_state.predicted_salary, 2)).rstrip('0').rstrip('.')

        st.markdown(
            f'<div class="result-box">Predicted Salary: ₹ {salary_display}</div>',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="info-text">If you want to explore companies based on your input</div>',
            unsafe_allow_html=True
        )

        if st.button("🔎 Explore Companies"):
            st.session_state.page = "explore"
            st.rerun()

# ==============================
# EXPLORE PAGE
# ==============================
elif st.session_state.page == "explore":

    st.title("🏢 Company Opportunities")

    role = st.session_state.role
    experience = st.session_state.experience
    expected_salary = st.session_state.expected_salary
    predicted_salary = st.session_state.predicted_salary

    base_salary = expected_salary if expected_salary > 0 else predicted_salary
    range_value = 300000  # ±3 lakh range

    matches = df[
        (df["Role"] == role) &
        (df["years_experience"] >= experience - 1) &
        (df["years_experience"] <= experience + 1) &
        (df["salary_per annum"] >= base_salary - range_value) &
        (df["salary_per annum"] <= base_salary + range_value)
    ]

    if matches.empty:
        st.warning("No companies found in this range.")
    else:
        for _, row in matches.iterrows():
            st.markdown(
                f"""
                <div class="company-card">
                    <b>{row['Company_Name']}</b><br>
                    Role: {row['Role']}<br>
                    Experience: {row['years_experience']} Years<br>
                    Salary: ₹ {int(row['salary_per annum']):,}
                </div>
                """,
                unsafe_allow_html=True
            )

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()'''

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Salary Prediction", layout="centered", initial_sidebar_state="collapsed")

# ---------- REMOVE SIDEBAR ----------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
[data-testid="collapsedControl"] {display: none;}

.stApp {
    background-color: #111827;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

h1, h2, h3, label {
    color: #FFFFFF !important;
}

.stSelectbox > div > div {
    background-color: white !important;
    color: black !important;
}

.stNumberInput input {
    background-color: white !important;
    color: black !important;
}

.stButton>button {
    background-color: #3b82f6;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
}

.result-box {
    background-color: #16a34a;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 30px;
}

.message-box {
    margin-top: 15px;
    padding: 15px;
    border-radius: 8px;
    text-align: center;
    font-weight: 500;
}

.success { background-color: #065f46; }
.warning { background-color: #92400e; }
.info { background-color: #1e40af; }

.info-text {
    text-align: center;
    margin-top: 20px;
    font-size: 15px;
    color: #e5e7eb;
}

.company-card {
    background:#1f2937;
    padding:18px;
    border-radius:10px;
    margin-bottom:12px;
    border-left:5px solid #3b82f6;
}
</style>
""", unsafe_allow_html=True)

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- LOAD DATA ----------
df = pd.read_csv("Salary_prediction.csv")
df.columns = df.columns.str.strip()

X = df[["years_experience"]]
y = df["salary_per annum"]

model = LinearRegression()
model.fit(X, y)

# ==============================
# HOME PAGE
# ==============================
if st.session_state.page == "home":

    st.title("💼 Salary Prediction")

    role = st.selectbox("Select Your Role", df["Role"].unique())

    experience = st.number_input(
        "Enter Your Years of Experience",
        min_value=0.0,
        step=0.1,
        value=None,
        format="%.1f"
    )

    expected_salary = st.number_input(
        "Enter Your Expected Salary (Optional)",
        min_value=0.0,
        step=10000.0,
        value=None,
        format="%.0f"
    )

    if st.button("🚀 Predict Salary"):

        predicted_salary = model.predict([[experience]])[0]

        st.session_state.predicted_salary = predicted_salary
        st.session_state.role = role
        st.session_state.experience = experience
        st.session_state.expected_salary = expected_salary

        # -------- Salary Comparison Logic --------
        message = ""
        message_class = "info"

        if expected_salary and expected_salary > 0:

            diff = predicted_salary - expected_salary

            if abs(diff) <= 50000:
                message = "✅ Your expected salary is realistic and achievable."
                message_class = "success"

            elif diff > 50000:
                message = "🔥 Based on your experience, you may earn MORE than your expected salary."
                message_class = "success"

            elif diff < -50000:
                message = "⚠️ Your expected salary is higher than predicted. Consider gaining more experience."
                message_class = "warning"

        st.session_state.salary_message = message
        st.session_state.message_class = message_class

    # -------- Show Prediction --------
    if "predicted_salary" in st.session_state:

        salary_display = str(round(st.session_state.predicted_salary, 2)).rstrip('0').rstrip('.')

        st.markdown(
            f'<div class="result-box">Predicted Salary: ₹ {salary_display}</div>',
            unsafe_allow_html=True
        )

        # Show message if exists
        if st.session_state.salary_message:
            st.markdown(
                f'<div class="message-box {st.session_state.message_class}">{st.session_state.salary_message}</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            '<div class="info-text">If you want to explore companies based on your input</div>',
            unsafe_allow_html=True
        )

        if st.button("🔎 Explore Companies"):
            st.session_state.page = "explore"
            st.rerun()

# ==============================
# EXPLORE PAGE
# ==============================
elif st.session_state.page == "explore":

    st.title("🏢 Company Opportunities")

    role = st.session_state.role
    experience = st.session_state.experience
    expected_salary = st.session_state.expected_salary
    predicted_salary = st.session_state.predicted_salary

    base_salary = expected_salary if expected_salary and expected_salary > 0 else predicted_salary
    range_value = 300000

    matches = df[
        (df["Role"] == role) &
        (df["years_experience"] >= experience - 1) &
        (df["years_experience"] <= experience + 1) &
        (df["salary_per annum"] >= base_salary - range_value) &
        (df["salary_per annum"] <= base_salary + range_value)
    ]

    if matches.empty:
        st.warning("No companies found in this range.")
    else:
        for _, row in matches.iterrows():
            st.markdown(
                f"""
                <div class="company-card">
                    <b>{row['Company_Name']}</b><br>
                    Role: {row['Role']}<br>
                    Experience: {row['years_experience']} Years<br>
                    Salary: ₹ {int(row['salary_per annum'])}
                </div>
                """,
                unsafe_allow_html=True
            )

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
