import streamlit as st
import pandas as pd
import numpy as np
st.write("Find the largest among the three")
ValOne = st.text_input('Value One', '0')

ValTwo = st.text_input('Value Two', '0')

ValThree = st.text_input('Value Three', '0')
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

st.write("Biggest Value is  ", Value)

    
    