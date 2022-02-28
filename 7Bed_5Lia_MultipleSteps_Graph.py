#!/usr/bin/python3
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

print("Angle Integrated Cross Section vs Energy for 3 separate states.")
#get the energies for 5lia with state 1.5spin,-1 parity, 0.0 excitation energy
energies = np.linspace(1,101,101)  
def generate_specific_rows_energies(filePath, userows = []):
    with open('fort.40') as f:
        for i, line in enumerate(f):
            if i in userows:
                yield line
                
gen_energies = generate_specific_rows_energies('fort.40', userows = energies)
data_energies = np.loadtxt(gen_energies, usecols = 0, unpack = 'true')

#get the integrated cross section for 5lia with
#state 1.5spin,-1 parity, 0.0 excitation energy
state1 = np.linspace(1,101,101)  
def generate_specific_rows_state1(filePath, userows = []):
    with open('fort.40') as f:
        for i, line in enumerate(f):
            if i in userows:
                yield line
                
gen_state1 = generate_specific_rows_state1('fort.40', userows = state1)
data_state1 = np.loadtxt(gen_state1, usecols = 5, unpack = 'true')

#get the integrated cross section for 5lia with
#state 0.5spin,-1 parity, 1.49 excitation energy
state2 = np.linspace(1,101,101)  
def generate_specific_rows_state2(filePath, userows = []):
    with open('fort.40') as f:
        for i, line in enumerate(f):
            if i in userows:
                yield line
                
gen_state2 = generate_specific_rows_state2('fort.40', userows = state2)
data_state2 = np.loadtxt(gen_state2, usecols = 6, unpack = 'true')

#get the integrated cross section for 5lia with
#state 1.5spin,1 parity, 14.5 excitation energy
state3 = np.linspace(1,101,101)  
def generate_specific_rows_state3(filePath, userows = []):
    with open('fort.40') as f:
        for i, line in enumerate(f):
            if i in userows:
                yield line
                
gen_state3 = generate_specific_rows_state3('fort.40', userows = state3)
data_state3 = np.loadtxt(gen_state3, usecols = 7, unpack = 'true')

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.set_size_inches(10,20)
fig.suptitle("7Be+d -> 5Li+a Angle Integrated Cross Section vs Energy for 3 separate states")
ax1.plot(data_energies, data_state1, color='black', lw=2)
ax2.plot(data_energies, data_state2, color='black', lw=2)
ax3.plot(data_energies, data_state3, color='black', lw=2)
ax1.set(xlabel="Energy(MeV)", ylabel="Cross Section(mb/sr)")
ax2.set(xlabel="Energy(MeV)", ylabel="Cross Section(mb/sr)")
ax3.set(xlabel="Energy(MeV)", ylabel="Cross Section(mb/sr)")
ax1.set_title("1.5 Spin, -1 Parity, 0 Excitation Energy")
ax2.set_title("0.5 Spin, -1 Parity, 1.49 Excitation Energy")
ax3.set_title("1.5 Spin, 1 Parity, 14.5 Excitation Energy")
plt.savefig("7bed5liams2")
