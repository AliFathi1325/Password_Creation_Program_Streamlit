import streamlit as st
import random
import string

def create_password(number):
    uppercase = list(string.ascii_uppercase)
    lowercase = list(string.ascii_lowercase)
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '|', '`', '~']
    numbers = [str(i) for i in range(10)]

    all_characters  = [uppercase, lowercase, special, numbers]

    password = ''.join(random.choice(random.choice(all_characters)) for i in range (int(number)))

    return password

st.title('Password Creation Program')

number = st.number_input('How many characters do you have in your password?', min_value=8, max_value=32)

if st.button('Create a password'):
    password = create_password(number)
    st.success(f'''Your password is: {password}''')