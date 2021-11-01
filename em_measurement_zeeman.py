#=====================INPUTS=============================================
import math
print("Please provide the following inputs: \n")
N_initial = int(input("\nPlease input the principal quantum number for beginning state: "))
L_initial = int(input("Please input the orbital angular momentum for beginning state: "))
S_initial = int(input("Please input the spin angular momentum for beginning state: "))
J_initial = int(input("Please input the total angular momentum for beginning state: "))
N_final = int(input("\nPlease input the principal quantum number for final state: "))
L_final = int(input("Please input the orbital angular momentum for final state: "))
S_final = int(input("Please input the spin angular momentum for final state: "))
J_final = int(input("Please input the total angular momentum for final state: "))
B_field = float(input("\nPlease input the magnetic field in Tesla: "))
B_field_uncertainty = float(input("Please input the uncertainty of the magnetic field in Tesla: "))
D_m = float(input("Please input the central 1st order ring diameter in mm, Dm: "))
D_m_uncertainty = float(input("Please input the uncertanty of Dm in mm: "))
D_a = float(input("Please input the innermost 2nd order ring diameter in mm, Da: "))
D_a_uncertainty = float(input("Please input the uncertanty of Da in mm: "))
D_b = float(input("Please input the central 2nd order ring diameter in mm, Db: "))
D_b_uncertainty = float(input("Please input the uncertanty of Db in mm: "))
d = int(input("Please input the Fabry-Perot gap in mm: "))
delta_Mg = 0.5
wavelength = 253.7
c = 3*10000000000

#====================G-LANDE FACTOR CALCULATION===========================
#==Calculating Multiplicity==
multiplicity_initial = (2*S_initial) + 1
multiplicity_final = (2*S_final) + 1
print("\nInitial state multiplicity: " + str(multiplicity_initial))
print("Final state multiplicity: " + str(multiplicity_final))

#==Assigning letter to orbital angular momentum for spectroscopic notation==
if L_initial == 0:
    L_initial_letter = "S"
elif L_initial == 1:
    L_initial_letter = "P"
elif L_initial == 2:
    L_initial_letter = "D"
elif L_initial == 3:
    L_initial_letter = "F"
    
if L_final == 0:
    L_final_letter = "S"
elif L_final == 1:
    L_final_letter = "P"
elif L_final == 2:
    L_final_letter = "D"
elif L_final == 3:
    L_final_letter = "F"

#==Spectroscopic Notation of States==
print("\nYour initial state is: " + str(N_initial) + " " + str(multiplicity_initial) + L_initial_letter + str(J_initial))
print("Your final state is: " + str(N_final) + " " + str(multiplicity_final) + L_final_letter + str(J_final))

#==G-lande Calculation====
print("\nCalculating Lande g-factors. . .")
g_initial = 1 + (((J_initial*(J_initial + 1))-(L_initial * (L_initial + 1))+(S_initial * (S_initial + 1)))/(2*J_initial*(J_initial + 1)))
g_final = 1 + (((J_final*(J_final + 1))-(L_final * (L_final + 1))+(S_final * (S_final + 1)))/(2*J_final*(J_final + 1)))
print("\nYour initial G-Lande factor is: " + str(g_initial))
print("Your final G-Lande factor is: " + str(g_final))

#============================WAVELENGTH CALCULATIONS=====================
print("\nCalculating difference in wavelength. . .")
delta_wavelength = ((wavelength*wavelength)/(2*d*0.000001))*((D_b**2-D_a**2)/(D_b**2-D_m**2))
delta_wavelength_nm = delta_wavelength * 0.000000001
print("\nThe difference in wavelength is given by: " + str(delta_wavelength) + " (or " + str(delta_wavelength_nm) + "nm.)"  )

#============================E/M CALCULATIONS============================
print("\nCalculating e/m ratio. . .")
charge_to_mass = ((2*3.14*c)/(delta_Mg*B_field*d))*((D_b**2-D_a**2)/(D_b**2-D_m**2))
print("The charge-to-mass ratio is given by: " + str(charge_to_mass) )

del_D_b =((2*3.14*c)/(delta_Mg*B_field*d))*(1/((D_b**2)-(D_m**2)))*((2*D_b*((D_b**2)-(D_m**2)))-(2*D_b*((D_b**2)-(D_a**2)))/(((D_b**2)-(D_m**2))**2))
del_D_a = ((2*3.14*c)/(delta_Mg*B_field*d))*(1/((D_b**2)-(D_m**2)))*(-2*D_a)
del_D_m = ((2*3.14*c)/(delta_Mg*B_field*d))*((-2*D_m*((D_b**2)-(D_a**2)))/(-1*((D_b**2)-(D_a**2))**2))
del_B_field = ((2*3.14*c)/(delta_Mg*d))*(1/((D_b**2)-(D_m**2)))*((D_b**2)-(D_a**2))*(-1/B_field**2)

charge_to_mass_uncertainty = math.sqrt((del_D_b*D_b_uncertainty)+(del_D_a*D_a_uncertainty)+(del_D_m*D_m_uncertainty)+(del_B_field*B_field_uncertainty))
print("The charge-to-mass ratio uncertainty is given by: " + str(charge_to_mass_uncertainty))

error_percentage = charge_to_mass_uncertainty/charge_to_mass
print("The percentage error is given by: " + str(error_percentage) + "%")

