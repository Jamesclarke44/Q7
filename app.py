import streamlit as st
from data_manager import load_data

data = load_data()

st.set_page_config(page_title="Audi Q7 Manual", layout="centered")
st.title("🚗 Audi Q7 — Workshop OS")

menu = st.radio(
    "",
    [
        "⚡ Quick Lookups",
        "📊 Dashboard",
        "🛠 Service Mode",
        "📘 Workshop",
        "🔧 Torque Lookup",
        "🧰 Parts Database",
        "📅 Maintenance Timeline",
        "📒 History"
    ]
)

if menu == "⚡ Quick Lookups":
    from ui.quick_lookups import render
elif menu == "📊 Dashboard":
    from ui.dashboard import render
elif menu == "🛠 Service Mode":
    from ui.service_mode import render
elif menu == "📘 Workshop":
    from ui.workshop_view import render
elif menu == "🔧 Torque Lookup":
    from ui.torque_lookup import render
elif menu == "🧰 Parts Database":
    from ui.parts_database import render
elif menu == "📅 Maintenance Timeline":
    from ui.timeline import render
elif menu == "📒 History":
    from ui.history import render

render(data)