import streamlit as st
from multiapp import MultiApp
from apps import home, calculator, AdvanceCalculator       # import your app modules here

app = MultiApp()

st.markdown("""
# Simple Calculator
""")

st.text("Use Drop Down menu below to navigate between Homepage and Calculator.")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Calculator", calculator.app)
app.add_app("Advance Calculator", AdvanceCalculator.app)
# The main app
app.run()