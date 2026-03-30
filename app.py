import streamlit as st
import random
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Soil Moisture Lab", page_icon="🌱", layout="centered")

# Title
st.title("🌱 Soil Moisture Virtual Lab")

# -------------------------------
# 🌱 SOIL MOISTURE SIMULATOR
# -------------------------------
st.header("🌾 Soil Moisture Simulator")

moisture = st.slider("Select Soil Moisture (%)", 0, 100, 50)

crop = st.selectbox("Select Crop", ["Rice", "Wheat", "Maize"])

# Status logic
if moisture < 30:
    status = "Dry"
    suggestion = "⚠️ Irrigation Needed"
elif moisture <= 70:
    status = "Optimal"
    suggestion = "✅ No Action Needed"
else:
    status = "Wet"
    suggestion = "💧 Stop Irrigation"

st.subheader(f"Status: {status}")
st.write(suggestion)

# Crop advice
if crop == "Rice" and moisture < 50:
    st.info("🌾 Rice needs more water")
elif crop == "Wheat" and moisture > 70:
    st.warning("⚠️ Too much water for Wheat")
elif crop == "Maize" and moisture < 40:
    st.info("🌽 Maize needs moderate watering")
else:
    st.success("✅ Conditions are acceptable")

# Graph
fig, ax = plt.subplots()
ax.bar(["Moisture"], [moisture])
ax.set_ylim(0, 100)
ax.set_ylabel("Moisture %")
st.pyplot(fig)

# Simulate button
if st.button("🔄 Simulate Sensor"):
    moisture = random.randint(10, 90)
    st.write(f"Simulated Moisture: {moisture}%")

# -------------------------------
# 🤖 AI ASSISTANT
# -------------------------------
st.header("🤖 AI Soil Assistant")

user_question = st.text_input("Ask about soil, irrigation, or crops:")

def simple_ai_response(question):
    question = question.lower()

    if "soil moisture" in question:
        return "Soil moisture is the amount of water present in soil and is essential for plant growth."
    elif "irrigation" in question:
        return "Irrigation should be applied when soil moisture drops below optimal levels."
    elif "rice" in question:
        return "Rice grows best in water-rich conditions and needs frequent irrigation."
    elif "wheat" in question:
        return "Wheat requires moderate water and well-drained soil."
    elif "maize" in question:
        return "Maize needs balanced watering and cannot tolerate excess water."
    else:
        return "Try asking about soil moisture, irrigation, or crops like rice, wheat, or maize."

if user_question:
    st.success(simple_ai_response(user_question))

# -------------------------------
# 🧠 QUIZ SECTION
# -------------------------------
st.header("🧠 Soil Knowledge Quiz")

questions = [
    {
        "question": "What is the ideal soil moisture range?",
        "options": ["0-20%", "30-70%", "80-100%"],
        "answer": "30-70%"
    },
    {
        "question": "Which crop requires more water?",
        "options": ["Wheat", "Rice", "Maize"],
        "answer": "Rice"
    },
    {
        "question": "What happens if soil is too wet?",
        "options": ["Better growth", "Root damage", "No effect"],
        "answer": "Root damage"
    }
]

score = 0

for i, q in enumerate(questions):
    st.subheader(q["question"])
    user_ans = st.radio("Choose your answer:", q["options"], key=i)

    if st.button(f"Check Answer {i+1}", key=f"btn{i}"):
        if user_ans == q["answer"]:
            st.success("Correct ✅")
        else:
            st.error(f"Wrong ❌ Correct answer: {q['answer']}")

st.write("🎯 Try all questions and test your knowledge!")import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("🌱 Soil Moisture Virtual Lab")

moisture = st.slider("Select Soil Moisture (%)", 0, 100, 50)

crop = st.selectbox("Select Crop", ["Rice", "Wheat", "Maize"])

if moisture < 30:
    status = "Dry"
    suggestion = "⚠️ Irrigation Needed"
elif moisture <= 70:
    status = "Optimal"
    suggestion = "✅ No Action Needed"
else:
    status = "Wet"
    suggestion = "💧 Stop Irrigation"

st.subheader(f"Status: {status}")
st.write(suggestion)

if crop == "Rice" and moisture < 50:
    st.write("Rice needs more water 🌾")
elif crop == "Wheat" and moisture > 70:
    st.write("Too much water for Wheat ⚠️")
else:
    st.write("Conditions are acceptable")

fig, ax = plt.subplots()
ax.bar(["Moisture"], [moisture])
ax.set_ylim(0, 100)
st.pyplot(fig)

if st.button("Simulate Sensor"):
    moisture = random.randint(10, 90)
    st.write(f"Simulated Moisture: {moisture}%")st.header("🤖 AI Soil Moisture Assistant")

user_question = st.text_input("Ask about soil moisture, irrigation, or crops:")

def simple_ai_response(question):
    question = question.lower()

    if "soil moisture" in question:
        return "Soil moisture refers to the amount of water present in the soil, crucial for plant growth."
    elif "irrigation" in question:
        return "Irrigation should be done when soil moisture is low to maintain optimal crop health."
    elif "rice" in question:
        return "Rice requires high water levels and grows best in wet soil conditions."
    elif "wheat" in question:
        return "Wheat grows best in moderate moisture and cannot tolerate waterlogging."
    elif "maize" in question:
        return "Maize requires well-drained soil and moderate watering."
    else:
        return "Please ask about soil moisture, irrigation, or crops like rice, wheat, or maize."

if user_question:
    st.success(simple_ai_response(user_question))import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("🌱 Soil Moisture Virtual Lab")

moisture = st.slider("Select Soil Moisture (%)", 0, 100, 50)

crop = st.selectbox("Select Crop", ["Rice", "Wheat", "Maize"])

if moisture < 30:
    status = "Dry"
    suggestion = "⚠️ Irrigation Needed"
elif moisture <= 70:
    status = "Optimal"
    suggestion = "✅ No Action Needed"
else:
    status = "Wet"
    suggestion = "💧 Stop Irrigation"

st.subheader(f"Status: {status}")
st.write(suggestion)

if crop == "Rice" and moisture < 50:
    st.write("Rice needs more water 🌾")
elif crop == "Wheat" and moisture > 70:
    st.write("Too much water for Wheat ⚠️")
else:
    st.write("Conditions are acceptable")

fig, ax = plt.subplots()
ax.bar(["Moisture"], [moisture])
ax.set_ylim(0, 100)
st.pyplot(fig)

if st.button("Simulate Sensor"):
    moisture = random.randint(10, 90)
    st.write(f"Simulated Moisture: {moisture}%")
