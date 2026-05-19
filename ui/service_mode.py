import streamlit as st
from datetime import datetime
from helpers import label
from workshop import WORKSHOP
from data_manager import save_data

def render(data):
    st.subheader("🛠 Service Mode")

    display_map = {}
    for k, spec in WORKSHOP.items():
        cat = spec.get("subcategory", spec["category"])
        display_map[f"{cat} — {label(k)}"] = k

    service_display = st.selectbox("Select Service", sorted(display_map.keys()))
    service = display_map[service_display]

    km = st.number_input("Current KM", 0, step=100)
    notes = st.text_area("Notes")

    spec = WORKSHOP[service]

    st.markdown(f"## 🔧 {label(service)}")
    st.write(f"**Category:** {spec['category']}")
    if "subcategory" in spec:
        st.write(f"**Section:** {spec['subcategory']}")

    if "fluid" in spec:
        if isinstance(spec["fluid"], dict):
            st.markdown("### 🛢 Fluid")
            for k, v in spec["fluid"].items():
                st.write(f"**{label(k)}:** {v}")
        else:
            st.write(f"**Fluid:** {spec['fluid']}")

    if "capacity" in spec:
        st.write(f"**Capacity:** {spec['capacity']}")

    if "interval_km" in spec:
        st.write(f"**Interval:** {spec['interval_km']} km")

    if "torque" in spec:
        st.markdown("### 🔧 Torque Specs")
        for k, v in spec["torque"].items():
            st.write(f"- {label(k)}: {v}")

    if "specs" in spec:
        st.markdown("### 📐 Specifications")
        for k, v in spec["specs"].items():
            if isinstance(v, dict):
                st.write(f"**{label(k)}:**")
                for k2, v2 in v.items():
                    st.write(f"  - {label(k2)}: {v2}")
            else:
                st.write(f"- {label(k)}: {v}")

    if "tools" in spec:
        st.markdown("### 🧰 Tools Needed")
        for t in spec["tools"]:
            st.write(f"- {t}")

    if "references" in spec:
        st.markdown("### 🔗 Related Procedures")
        for k, v in spec["references"].items():
            st.write(f"- {v}")

    st.markdown("### 📋 Workflow")
    workflow = spec.get("workflow", [])
    if workflow:
        for step in workflow:
            st.write(step)
    else:
        st.write("— No workflow defined —")

    if st.button("✔ Save Service"):
        data["logs"].append({
            "service": service,
            "km": km,
            "date": str(datetime.now()),
            "notes": notes
        })
        data["last_service"][service] = km
        save_data(data)
        st.success("Saved ✔")