#!/usr/bin/python3

import matplotlib.pyplot as plt 
import numpy as np 
import math as math
import sys as sys
from scipy.integrate import quad

S=100                              # S Factor in MeV-b
M0=7.016929                        # Mass of 7Be in u
M1=2.014102                        # Mass of Deterium in u
Z0=4                               # Atomic Number of 7Be
Z1=1                               # Atomic Number of Deterium
m01=M0*M1/(M0+M1)                  # Reduced Mass

def sigma(E):
    if (E<1.0e-3):
        result=0
    else:
        result= S/E*np.exp(-0.98951013*Z0*Z1*math.sqrt(m01/E))  # Eq. (3.75)
    return result
        
def integrand(E,T9):
    return E*sigma(E)*np.exp(-11.605*E/T9)  # partly Eq. (3.10)

def int_rate(T9):
    result, error = quad(integrand,0,np.inf,args=(T9,),epsabs=0)  # epsabs=0 -> force rel error
    if (abs(error/result)>1.0e-7):
        print("inaccurate integration detected")
        print("T9= %10.2f"% T9)
        print(result,error)
        sys.exit()
    else:
        return 3.7318e10/T9**1.5/np.sqrt(m01)*result  # partly Eq. (3.10)

def calc_rate(T9):
    return 1.07e12/T9**(2/3)*np.exp(-12.428/T9**(1/3))  # formula from BBN code

C1=7.8324e9*(Z0*Z1)**(1/3)/m01**(1/3)*S     # Eq. (3.97)
C2=4.2475*(Z0*Z1)**(2/3)*m01**(1/3)         # Eq. (3.97) not quite consistent with Eq. (3.91)
print("C1= %10.4e   C2= %10.4f"% (C1,C2))
for T9 in [0.001,0.005,0.01,0.05,0.1,0.5,1.0]:
    r_int=int_rate(T9)
    r_calc=calc_rate(T9)
    print("%6.3f %20.10e %20.10e %15.4e"% (T9,r_int,r_calc,r_int/r_calc))
