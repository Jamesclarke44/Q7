import streamlit as st
from helpers import label

def render(data):
    st.subheader("📒 Service History")

    if not data["logs"]:
        st.info("No records yet")
    else:
        for log in reversed(data["logs"]):
            st.markdown(f"### {label(log['service'])}")
            st.write(f"KM: {log['km']}")
            st.write(f"Date: {log['date']}")
            if log.get("notes"):
                st.write(f"Notes: {log['notes']}")
            st.markdown("---")