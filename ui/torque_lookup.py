import streamlit as st
from helpers import label
from workshop import WORKSHOP

def render(data):
    st.subheader("🔧 Torque Lookup")

    # Build torque entries grouped by subcategory
    grouped = {}
    for name, spec in WORKSHOP.items():
        if "torque" in spec:
            sub = spec.get("subcategory", spec["category"])
            if sub not in grouped:
                grouped[sub] = []
            for item, value in spec["torque"].items():
                grouped[sub].append({
                    "Service": label(name),
                    "Part Tightened": label(item),
                    "Torque": value
                })

    # Dropdown to select section
    sections = ["All"] + sorted(grouped.keys())
    selected = st.selectbox("Select section", sections)

    # Search
    query = st.text_input("Search", placeholder="e.g. 'caliper', 'bleeder', 'cylinder'")

    # Display
    for subcategory, items in grouped.items():
        if selected != "All" and subcategory != selected:
            continue

        if query:
            q = query.lower()
            items = [i for i in items if q in i["Part Tightened"].lower() or q in i["Service"].lower()]

        if items:
            st.markdown(f"## {subcategory}")
            for item in items:
                with st.expander(f"{item['Part Tightened']} — {item['Torque']}"):
                    st.write(f"**Service:** {item['Service']}")
                    st.write(f"**Torque:** {item['Torque']}")
            st.markdown("---")

    if query and not any(
        items for sub, items in grouped.items()
        if selected in ("All", sub)
        for i in items if query.lower() in i["Part Tightened"].lower()
    ):
        st.info("No torque specs match your search.")