import streamlit as st
from helpers import label, get_next_due_status
from workshop import WORKSHOP

def render(data):
    st.subheader("📊 Dashboard")

    km = st.number_input("Current KM", 0, step=100)

    if km:
        st.markdown("### ✅ Next-Due Summary")

        overdue = []
        soon = []
        never = []
        ok = []

        for name, spec in WORKSHOP.items():
            last = data["last_service"].get(name)
            status = get_next_due_status(km, name, spec, last)
            if not status:
                continue
            if status["status"] == "overdue":
                overdue.append(status)
            elif status["status"] == "soon":
                soon.append(status)
            elif status["status"] == "never":
                never.append(status)
            else:
                ok.append(status)

        if overdue:
            st.markdown("#### 🔴 Overdue")
            for s in overdue:
                st.error(f"{label(s['service'])} — DUE (was due at {s['due_km']} km)")

        if soon:
            st.markdown("#### 🟠 Due Soon (≤ 5,000 km)")
            for s in soon:
                st.warning(f"{label(s['service'])} — {s['remaining']} km remaining (due at {s['due_km']} km)")

        if never:
            st.markdown("#### 🟡 Never Serviced")
            for s in never:
                st.warning(f"{label(s['service'])} — never logged")

        if not overdue and not soon and not never:
            st.success("All interval-based services are up to date.")

        st.markdown("---")
        st.markdown("### 📋 Detailed Status")

        for name, spec in WORKSHOP.items():
            interval = spec.get("interval_km")
            last = data["last_service"].get(name)

            if interval:
                if last is None:
                    st.warning(f"⚠️ {label(name)} never serviced")
                else:
                    due = last + interval
                    if km >= due:
                        st.error(f"⚠️ {label(name)} DUE (was due at {due} km)")
                    else:
                        remaining = due - km
                        st.info(f"{label(name)}: {remaining} km remaining (due at {due} km)")