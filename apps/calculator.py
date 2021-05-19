import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
    options = ["Addition", "Subtraction", "Multiplication", "Division"]
    choice = st.radio("Choose the Operation", options)
    if choice == "Addition":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a+b
        st.text("The result of addition is")
        st.write(c)
    elif choice == "Subtraction":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a - b
        st.text("The result of Subtraction is")
        st.write(c)
    elif choice == "Multiplication":
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a * b
        st.text("The result of Multiplication is")
        st.write(c)
    elif choice == "Division":
        st.warning("Must enter Some value Otherwise You'll get Error!")
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        remainder = a % b
        modulus = a / b
        st.write("Results are : ")
        st.write(" Reminder is ",remainder)
        st.write(" Modulus is ",modulus)


#







