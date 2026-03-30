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
    st.write(f"Simulated Moisture: {moisture}%")
