import streamlit as st
import pandas as pd
import numpy as np
st.write("Find the largest among the three")

ValOne = st.number_input("Value One",step=1)

ValTwo = st.number_input('Value Two',step=1)

ValThree = st.number_input('Value Three', step=1)
if (ValOne>ValTwo):
    if (ValOne > ValThree):
        Value = ValOne
    else:
       Value =  ValThree
else:
    if (ValTwo>ValThree):
        Value = ValTwo

    else:
        Value = ValThree

if (st.button("Find the largest value")):
    st.write(Value)

    
    
