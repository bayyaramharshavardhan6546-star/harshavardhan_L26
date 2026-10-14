python
```

import streamlit as st

st.set_page_config(
    page_title="Fluid Mechanics Calculator",
    page_icon="💧",
    layout="centered"
)

st.title("💧 Fluid Mechanics Calculator")
st.write("Calculate important fluid mechanics parameters easily.")

st.divider()

choice = st.sidebar.selectbox(
    "Select Calculation",
    [
        "Pressure",
        "Fluid Velocity",
        "Discharge",
        "Reynolds Number",
        "Dynamic Pressure"
    ]
)

if choice == "Pressure":
    st.header("Pressure Calculator")
    st.latex(r"P = \rho g h")

    rho = st.number_input(
        "Fluid density (kg/m³)",
        min_value=0.0,
        value=1000.0
    )
    g = st.number_input(
        "Gravitational acceleration (m/s²)",
        min_value=0.0,
        value=9.81
    )
    h = st.number_input(
        "Height / Depth (m)",
        min_value=0.0,
        value=1.0
    )

    if st.button("Calculate Pressure"):
        P = rho * g * h
        st.success(f"Pressure = {P:,.4f} Pa")

elif choice == "Fluid Velocity":
    st.header("Fluid Velocity Calculator")
    st.latex(r"V = \frac{Q}{A}")

    Q = st.number_input(
        "Discharge (m³/s)",
        min_value=0.0,
        value=1.0
    )
    A = st.number_input(
        "Cross-sectional area (m²)",
        min_value=0.0,
        value=0.5,
        format="%.4f"
    )

    if st.button("Calculate Velocity"):
        if A > 0:
            V = Q / A
            st.success(f"Fluid Velocity = {V:,.4f} m/s")
        else:
            st.error("Area must be greater than zero.")

elif choice == "Discharge":
    st.header("Discharge Calculator")
    st.latex(r"Q = A V")

    A = st.number_input(
        "Cross-sectional area (m²)",
        min_value=0.0,
        value=0.5,
        format="%.4f"
    )
    V = st.number_input(
        "Fluid velocity (m/s)",
        min_value=0.0,
        value=2.0
    )

    if st.button("Calculate Discharge"):
        Q = A * V
        st.success(f"Discharge = {Q:,.4f} m³/s")

elif choice == "Reynolds Number":
    st.header("Reynolds Number Calculator")
    st.latex(r"Re = \frac{\rho V D}{\mu}")

    rho = st.number_input(
        "Fluid density (kg/m³)",
        min_value=0.0,
        value=1000.0
    )
    V = st.number_input(
        "Fluid velocity (m/s)",
        min_value=0.0,
        value=1.0
    )
    D = st.number_input(
        "Pipe diameter (m)",
        min_value=0.0,
        value=0.1
    )
    mu = st.number_input(
        "Dynamic viscosity (Pa·s)",
        min_value=0.0,
        value=0.001,
        format="%.6f"
    )

    if st.button("Calculate Reynolds Number"):
        if mu > 0 and D > 0:
            Re = (rho * V * D) / mu
            st.success(f"Reynolds Number = {Re:,.2f}")

            if Re < 2300:
                st.info("Flow classification: Laminar")
            elif Re < 4000:
                st.info("Flow classification: Transitional")
            else:
                st.info("Flow classification: Turbulent")
        else:
            st.error(
                "Pipe diameter and viscosity must be greater than zero."
            )

elif choice == "Dynamic Pressure":
    st.header("Dynamic Pressure Calculator")
    st.latex(r"P_d = \frac{1}{2}\rho V^2")

    rho = st.number_input(
        "Fluid density (kg/m³)",
        min_value=0.0,
        value=1000.0
    )
    V = st.number_input(
        "Fluid velocity (m/s)",
        min_value=0.0,
        value=2.0
    )

    if st.button("Calculate Dynamic Pressure"):
        Pd = 0.5 * rho * V**2
        st.success(f"Dynamic Pressure = {Pd:,.4f} Pa")

st.divider()
st.caption("Fluid Mechanics Calculator | Built with Streamlit")
```
