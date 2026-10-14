
# Fluid Mechanics Calculator

# Function to calculate Pressure
def pressure(rho, g, h):
    return rho * g * h


# Function to calculate Fluid Velocity
def velocity(Q, A):
    return Q / A


# Function to calculate Discharge
def discharge(A, V):
    return A * V


# Function to calculate Reynolds Number
def reynolds_number(rho, V, D, mu):
    return (rho * V * D) / mu


# Function to calculate Dynamic Pressure
def dynamic_pressure(rho, V):
    return 0.5 * rho * V ** 2


# Main Menu
while True:
    print("\n===== FLUID MECHANICS CALCULATOR =====")
    print("1. Pressure")
    print("2. Fluid Velocity")
    print("3. Discharge")
    print("4. Reynolds Number")
    print("5. Dynamic Pressure")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rho = float(input("Enter fluid density (kg/m^3): "))
        g = float(input("Enter gravitational acceleration (m/s^2): "))
        h = float(input("Enter height/depth (m): "))

        P = pressure(rho, g, h)
        print("Pressure =", P, "Pa")

    elif choice == 2:
        Q = float(input("Enter discharge (m^3/s): "))
        A = float(input("Enter cross-sectional area (m^2): "))

        V = velocity(Q, A)
        print("Fluid Velocity =", V, "m/s")

    elif choice == 3:
        A = float(input("Enter cross-sectional area (m^2): "))
        V = float(input("Enter fluid velocity (m/s): "))

        Q = discharge(A, V)
        print("Discharge =", Q, "m^3/s")

    elif choice == 4:
        rho = float(input("Enter fluid density (kg/m^3): "))
        V = float(input("Enter fluid velocity (m/s): "))
        D = float(input("Enter pipe diameter (m): "))
        mu = float(input("Enter dynamic viscosity (Pa.s): "))

        Re = reynolds_number(rho, V, D, mu)
        print("Reynolds Number =", Re)

    elif choice == 5:
        rho = float(input("Enter fluid density (kg/m^3): "))
        V = float(input("Enter fluid velocity (m/s): "))

        Pd = dynamic_pressure(rho, V)
        print("Dynamic Pressure =", Pd, "Pa")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
