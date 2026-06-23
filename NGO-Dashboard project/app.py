import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Community Impact Tracker",
    page_icon="🌍",
    layout="wide"
)

st.sidebar.title("Community Impact Tracker")
st.sidebar.markdown("Developed by Sean Chizhwende")

donors = pd.read_csv("data/donors.csv")
projects = pd.read_csv("data/projects.csv")
beneficiaries = pd.read_csv("data/beneficiaries.csv")
volunteers = pd.read_csv("data/volunteers.csv")

total_funding = donors["Amount"].sum()
active_projects = len(
    projects[projects["Status"] == "Active"]
)
total_beneficiaries = len(beneficiaries)
total_volunteers = len(volunteers)

st.title("🌍 Community Impact Tracker Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Funding Raised", f"${total_funding:,.0f}")
col2.metric("Active Projects", active_projects)
col3.metric("Beneficiaries", total_beneficiaries)
col4.metric("Volunteers", total_volunteers)

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Funding Sources")

    fig = px.bar(
        donors,
        x="Donor",
        y="Amount",
        title="Donations by Donor"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Project Status")

    fig2 = px.pie(
        projects,
        names="Status",
        title="Projects Overview"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("Recent Beneficiaries")
st.dataframe(beneficiaries)

st.subheader("Volunteer Contributions")
st.dataframe(volunteers)
