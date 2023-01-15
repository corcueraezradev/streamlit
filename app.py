# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:16:35 2022

@author: machine
"""

import streamlit as st
import os
import math
import random
import smtplib
   
# Google app credentials
USERNAME = "corcueraezradev@gmail.com"
PASSWORD = "xfprffpxmzgsnjtl"

st.title("OTP verification with auto-email")
st.markdown("Author: Ezra Corcuera")
st.markdown("The OTP verification app enables you to authenticate using the one-time password (OTP) that is sent to the registered email address")
emailid = st.text_input("Enter your email", placeholder = "Type here ...", key = "emailid") 

if st.button('Submit', key = "emailid_button"):
    # Generating OTP
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OTP=""
    
    for i in range(2):
        OTP+=str(random.randint(0,9)) + letters[random.randint(0,25)] + str(random.randint(0,9))
    otp = "Enter your code manually to verify.\n Your OTP is: \n" + OTP
    msg= otp
    # Sending email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(USERNAME, PASSWORD)
    s.sendmail('&&&&&&&&&&&', emailid, msg)
    
    if 'key' not in st.session_state:
        st.session_state['key'] = OTP
    else:
        st.session_state['key'] = OTP
    
    
    text = "Check your email. The OTP has been sent to " + emailid
    st.success(text)
    

# Verify OTP
if 'key' in st.session_state: 
    verify_otp = st.text_input("Verify OTP: ", placeholder = "Type here ...", key="verify_otp")

    if st.button('Verify', key = "verify_otp_button"):
        if verify_otp == st.session_state.key:
            st.success("OTP verified, you can login now")        
        else:
            st.error("Please check your OTP again")
