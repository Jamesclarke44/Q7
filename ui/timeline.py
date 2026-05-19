import streamlit as st
from helpers import label
from workshop import WORKSHOP
from config import MAX_KM, SOON_THRESHOLD

def render(data):
    st.subheader("📅 Maintenance Timeline")
    km_now = st.number_input("Current KM", 0, step=100)

    for name, spec in WORKSHOP.items():
        interval = spec.get("interval_km")
        if not interval:
            continue

        with st.expander(f"{spec.get('subcategory', spec['category'])} — {label(name)}"):
            last = data["last_service"].get(name)
            st.write(f"**Interval:** {interval} km")
            if last:
                st.write(f"**Last Service:** {last} km")
            else:
                st.write("**Last Service:** —")

            points = []
            km_point = interval
            while km_point <= MAX_KM:
                points.append(km_point)
                km_point += interval

            for p in points:
                if last and last >= p:
                    status = "✅ done"
                elif km_now and km_now >= p:
                    status = "🔴 overdue"
                elif km_now and p - km_now <= SOON_THRESHOLD:
                    status = "🟠 soon"
                else:
                    status = "⚪ upcoming"
                st.write(f"- {p} km {status}")