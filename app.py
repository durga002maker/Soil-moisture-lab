import streamlit as st
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
