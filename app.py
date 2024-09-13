import streamlit as st
import math as ma

#KNOWN VALUES


col1, col2= st.columns([1,3])


#KNOWN VALUES

def find_values(I_V, A_L, A_S, B_S, B, C, D_L, D_S):
    with col1:

        #Theta 1 
        theta_1 = ma.acos((I_V ** 2 - A_L ** 2 - B_S **  2)/(2 * A_L * B_S))
        theta_1 = ma.degrees(theta_1)
        st.latex(rf' \theta_1  = {round(theta_1, 2)}')
        #Theta 1

        #Alpha 1
        alpha_1 = 90 - theta_1
        st.latex(rf' \alpha_1  = {round(alpha_1, 2)}')
        #Alpha 1

        #B 1
        B_1 = 1.5 * A_S * ma.cos(alpha_1)
        st.latex(rf' B_1  = {round(B_1)}')
        #B 1

        #B 2
        B_2 = B-B_1
        st.latex(rf' B_2  = {round(B_2)}')
        #B 2

        #C 2
        C_2 = ma.sqrt(A_S**2 + B_2 ** 2 - 2 * A_S * B_2 * ma.cos(ma.radians(alpha_1)))
        st.latex(rf' C_2  = {C_2}')
        #C 2

        #C 1
        C_1 = C-C_2
        st.latex(rf' C_1  = {C_1}')
        #C 1

        #Alpha 2 
        alpha_2 = ma.asin(A_S * ma.sin(theta_1) / C_2)
        alpha_2 = ma.degrees(alpha_2)
        st.latex(rf' \alpha_2  = {round(alpha_2, 2)}')
        #Alpha 2 

        #Theta 2 
        theta_2 = ma.asin((B_2*ma.sin(alpha_1) / C_2))
        theta_2 = ma.degrees(theta_2)
        st.latex(rf' \theta_2  = {round(theta_2, 2)}')
        #Theta 2

        #Alpha 3 
        alpha_3 = ma.asin(C_1 * ma.sin(ma.radians(alpha_2)) / D_S)
        alpha_3 = ma.degrees(alpha_3)
        st.latex(rf' \alpha_2  = {round(alpha_3, 2)}')
        #Alpha 3 

        #Theta 3
        theta_3 = ma.asin(B_1 * ma.sin(ma.radians(alpha_2)) / D_S)
        theta_3 = ma.degrees(theta_3)
        st.latex(rf' \alpha_2  = {round(theta_3, 2)}')
        #Theta 3

        #Theta 4
        theta_4 = 270-alpha_3
        st.latex(rf' \theta_4  = {round(theta_4, 2)}')

  
with col2:  
    st.image("Bar_Linkages_Diagram.png", caption="Bar Linkages")

with st.sidebar:
    I_V = st.number_input("Please Enter I_V (mm)", min_value = 0.00)
#

    A_L = st.number_input("Please Enter A_L (mm)", min_value = 0.00)


    A_S = st.number_input("Please Enter A_S (mm)", min_value = 0.00)


    B_S = st.number_input("Please Enter B_S (mm)", min_value = 0.00)


    B = st.number_input("Please Enter B (mm)", min_value = 0.00)


    C = st.number_input("Please Enter C (mm)", min_value = 0.00)


    D_L = st.number_input("Please Enter D_L (mm)", min_value = 0.00)


    D_S = st.number_input("Please Enter D_S (mm)", min_value = 0.00)

    if st.button("Find Values"):
        find_values(I_V, A_L, A_S, B_S, B, C, D_L, D_S)