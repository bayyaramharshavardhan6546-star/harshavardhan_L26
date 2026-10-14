Here is your code converted into a Streamlit Python application for mechanical workshop shaft diameter insp

Save the code as `shaft_inspection.py`.

python
```

import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Shaft Diameter Inspection",
    page_icon="⚙️",
    layout="wide"
)

# Title
st.title("⚙️ Mechanical Workshop - Shaft Diameter Inspection")
st.write("Inspect shaft diameters against the nominal diameter and tolerance limit.")

# Input measurements
diameters = [50.02, 49.97, 50.08, 49.95, 50.01, 50.06]

# Nominal diameter and tolerance
nominal_diameter = 50.0
tolerance = 0.05

# Sidebar
st.sidebar.header("Inspection Settings")
nominal_diameter = st.sidebar.number_input(
    "Nominal Diameter (mm)",
    value=50.0,
    step=0.01,
    format="%.2f"
)
tolerance = st.sidebar.number_input(
    "Tolerance (± mm)",
    value=0.05,
    min_value=0.0,
    step=0.01,
    format="%.2f"
)

# Calculate results using Python built-in functions
number_of_shafts = len(diameters)
total_diameter = sum(diameters)
maximum = max(diameters)
minimum = min(diameters)
sorted_diameters = sorted(diameters)

deviations = list(
    map(lambda d: round(d - nominal_diameter, 2), diameters)
)

out_of_tolerance = list(
    filter(
        lambda x: abs(x[1]) > tolerance,
        zip(range(1, len(diameters) + 1), deviations)
    )
)

shaft_diameter_pairs = list(
    zip(range(1, len(diameters) + 1), diameters)
)

# Summary metrics
st.subheader("Inspection Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Shafts Inspected", number_of_shafts)
col2.metric("Average Diameter", f"{total_diameter / number_of_shafts:.3f} mm")
col3.metric("Maximum Diameter", f"{maximum:.2f} mm")
col4.metric("Minimum Diameter", f"{minimum:.2f} mm")

st.divider()

# Detailed inspection table
st.subheader("Shaft Measurement Results")

data = {
    "Shaft Number": range(1, number_of_shafts + 1),
    "Measured Diameter (mm)": diameters,
    "Nominal Diameter (mm)": [nominal_diameter] * number_of_shafts,
    "Deviation (mm)": deviations,
    "Status": [
        "OUT OF TOLERANCE"
        if abs(d) > tolerance
        else "PASS"
        for d in deviations
    ]
}

df = pd.DataFrame(data)

st.dataframe(
    df.style.map(
        lambda value: (
            "color: red; font-weight: bold"
            if value == "OUT OF TOLERANCE"
            else "color: green; font-weight: bold"
            if value == "PASS"
            else ""
        ),
        subset=["Status"]
    ),
    use_container_width=True,
    hide_index=True
)

# Tolerance results
st.subheader("Tolerance Inspection")

if out_of_tolerance:
    st.error(f"{len(out_of_tolerance)} shaft(s) are outside the tolerance limit.")
    for shaft, deviation in out_of_tolerance:
        st.write(f"Shaft {shaft}: Deviation = {deviation:+.2f} mm")
else:
    st.success("All shafts are within the specified tolerance.")

# Diameter chart
st.subheader("Diameter Comparison")

chart_df = pd.DataFrame({
    "Shaft": [f"Shaft {i}" for i in range(1, number_of_shafts + 1)],
    "Measured Diameter": diameters,
    "Nominal Diameter": [nominal_diameter] * number_of_shafts
}).set_index("Shaft")

st.line_chart(chart_df)

# Additional Python function results
with st.expander("View Python Function Results"):
    st.write("**Total diameter:**", f"{total_diameter:.2f} mm")
    st.write("**Sorted diameters:**", sorted_diameters)
    st.write("**Data type:**", str(type(diameters)))
    st.write("**Shaft number and diameter pairs:**", shaft_diameter_pairs)
    st.write("**Deviations:**", deviations)
    st.write("**Out-of-tolerance shafts:**", out_of_tolerance)

# Download report
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Inspection Report (CSV)",
    data=csv,
    file_name="shaft_inspection_report.csv",
    mime="text/csv"
)

st.caption("Mechanical Workshop | Shaft Quality Inspection")
```

## How to run the application

1. Install Python if it is not already installed.
2. Install the required packages in your terminal:

bash
```
pip install streamlit pandas
```

3. Save the code as `shaft_inspection.py`.
4. Run the application:

bash
```
streamlit run shaft_inspection.py
```

5. Streamlit will open the dashboard in your browser.

## Features included

- Interactive nominal diameter and tolerance settings.
- Summary metrics for the six shafts.
- Measurement and deviation table with pass/fail status.
- Diameter comparison chart.
- Results demonstrating Python built-in functions.
- CSV download for the inspection report.

Note: The six measured diameters are currently fixed in the code. The nominal diameter and tolerance are adjustable from the sidebar. The application treats deviations exactly equal to the tolerance limit as acceptable.
