import streamlit as st
import pandas as pd

# Load protocol data
df = pd.read_csv("ct_abd_pel_tidy.csv")

# Sidebar - Choose phase
phases = df['Phase'].unique().tolist()
selected_phase = st.sidebar.selectbox("Select Scan Phase", phases)

# Filter based on selected phase
filtered_df = df[df["Phase"] == selected_phase].copy()

st.title("CT Abdomen/Pelvis Protocol Editor")
st.markdown(f"Editing Phase: **{selected_phase}**")

# Editable table
edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True)

# Download edited CSV
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

csv = convert_df(edited_df)
st.download_button(
    "Download Edited Protocol as CSV",
    data=csv,
    file_name=f"ct_protocol_{selected_phase.lower().replace(' ', '_')}.csv",
    mime="text/csv",
)

