import streamlit as st
from utils.config import config_setup
from utils.tab1 import tab1_function
from utils.tab2 import tab2_function
from utils.tab3 import tab3_function

def main():

    config_setup()

    tab1, tab2, tab3 = st.tabs([
    "Step 1 (ROI)", 
    "Step 2 (S1 filtering)", 
    "Step 3 (Download)"])

    with tab1:

        tab1_function()


    with tab2:

        tab2_function()

    
    with tab3:

        tab3_function()


if __name__=='__main__':
    main()