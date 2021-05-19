import streamlit as st
import numpy as np
import math
import csv
from PIL import Image
import pandas as pd
import base64

st.markdown("""
#  Basic Calculator App
""")
# st.markdown("![Alt Text](https://media1.giphy.com/media/ghTPBMNczu5BBGbyX5/200w.webp?"
#             "cid=ecf05e47ywpxdygwxmcsnzwlzuw8h70qzq2ebw11su1jc2gd&rid=200w.webp&ct=g)")
st.text("Use Side Drop Down menu to navigate between our Website's Multipages.")

menu = ["Home", "Calculator", "Advance Calculator"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Home":
    st.subheader("Home")
    st.markdown("![Alt Text](https://media1.giphy.com/media/ghTPBMNczu5BBGbyX5/200w.webp?"
                "cid=ecf05e47ywpxdygwxmcsnzwlzuw8h70qzq2ebw11su1jc2gd&rid=200w.webp&ct=g)")
    st.subheader("Welcome To Our Website")
    st.subheader("Calculator")
    st.write("A calculator is a device that performs arithmetic operations on numbers. "
             "The simplest calculators can do only addition, subtraction, multiplication, "
             "and division. More sophisticated calculators can handle exponent ial operations, "
             "roots, logarithm s, trigonometric functions, and hyperbolic functions")
    image = Image.open('clac9.jpg')
    st.image(image, width=700)

elif choice == "Calculator":
    st.subheader("Simple Calculator")
    image = Image.open('clac7.jpg')
    st.image(image, width=700)
    options = ["Addition", "Subtraction", "Multiplication", "Division"]
    choice = st.selectbox("Options", options)
    # options = ["Addition", "Subtraction", "Multiplication", "Division"]
    # choice = st.radio("Choose the Operation", options)
    if choice == "Addition":
        st.markdown("![Alt Text](https://media3.giphy.com/media/MbFaRTRxoucfCbmLSZ/200."
                    "webp?cid=ecf05e474aznoxblvr7u6oxcwfei5xubdvyoqcv6qmctgj6h&rid=200.webp&ct=g)")
        a = st.number_input("Please input First Number")
        b = st.number_input("Please input Second Number")
        c = a + b
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
        st.write(" Reminder is ", remainder)
        st.write(" Modulus is ", modulus)
elif choice == "Advance Calculator":
    st.subheader("Advance Calculator")
    st.markdown("![Alt Text](https://i.gifer.com/origin/28/282a0194bb9070777e015fdbc12bc7c6_w200.webp)")
    st.subheader("Advance Calculator")
    st.write("By definition, a scientific calculator is a calculator designed to help you"
             " calculate science, engineering, and mathematics problems. It has way more "
             "buttons than your standard calculator that just lets you do your four basic "
             "arithmetic operations of addition, subtraction, multiplication, and division.")
    image = Image.open('clac8.jpg')
    st.image(image, width=600)
    options = ["Factorial", "Exponent", "Square", "Square Root"]
    choice = st.selectbox("Option", options)
    # if choice == "Addition":
    #     a = st.number_input("Please input First Number")
    #     b = st.number_input("Please input Second Number")
    #     c = a+b
    #     st.text("The result of addition is")
    #     st.write(c)
    if choice == "Factorial":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        factorial = 1
        if a < 0:
            st.write("Sorry!!, factorial does not exist for negative numbers")
        elif a == 0:
            st.write("The factorial of 0 is 1")
        else:
            for i in range(1, a + 1):
                factorial = factorial * i
            st.write("The factorial of", a, "is", factorial)
    #
    elif choice == "Exponent":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        b = st.number_input("Enter a Exponential value: ", min_value=0, max_value=100, value=1, step=1)

        result = a ** b
        st.write("Result is : ", result)


    elif choice == "Square":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        square = a * a
        st.write("Sruare of", a, "is", square)
    elif choice == "Square Root":
        a = st.number_input("Enter a Number", min_value=0, max_value=100, value=1, step=1)
        square_root = a ** 0.5
        st.write("Sruare Root of", a, "is", square_root)