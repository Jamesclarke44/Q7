import streamlit as st
from helpers import label
from workshop import WORKSHOP

def render(data):
    st.subheader("📘 Workshop")

    categories = {}
    for name, spec in WORKSHOP.items():
        cat = spec["category"]
        if cat not in categories:
            categories[cat] = {}
        sub = spec.get("subcategory", "General")
        if sub not in categories[cat]:
            categories[cat][sub] = []
        categories[cat][sub].append((name, spec))

    for category, subcats in categories.items():
        st.markdown(f"## 🗂 {category}")
        for subcat, items in subcats.items():
            st.markdown(f"### {subcat}")
            for name, spec in items:
                with st.expander(label(name)):
                    if "fluid" in spec:
                        if isinstance(spec["fluid"], dict):
                            st.write("**Fluid:**")
                            for k, v in spec["fluid"].items():
                                st.write(f"- {label(k)}: {v}")
                        else:
                            st.write(f"**Fluid:** {spec['fluid']}")
                    if "capacity" in spec:
                        st.write(f"**Capacity:** {spec['capacity']}")
                    if "interval_km" in spec:
                        st.write(f"**Interval:** {spec['interval_km']} km")
                    if "torque" in spec:
                        st.write("**Torque Specs:**")
                        for k, v in spec["torque"].items():
                            st.write(f"- {label(k)}: {v}")
                    if "specs" in spec:
                        st.write("**Specifications:**")
                        for k, v in spec["specs"].items():
                            if isinstance(v, dict):
                                st.write(f"- {label(k)}:")
                                for k2, v2 in v.items():
                                    st.write(f"  - {label(k2)}: {v2}")
                            else:
                                st.write(f"- {label(k)}: {v}")
                    if "tools" in spec:
                        st.write("**Tools Needed:**")
                        for t in spec["tools"]:
                            st.write(f"- {t}")
                    if "references" in spec:
                        st.write("**Related Procedures:**")
                        for k, v in spec["references"].items():
                            st.write(f"- {v}")
                    if "workflow" in spec:
                        st.write("**Workflow:**")
                        for step in spec["workflow"]:
                            st.write(step)