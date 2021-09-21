import random
import streamlit as st

st.title('Rock Paper Scissor')

user= st.radio('Your move, choose wisely',['Rock', 'Paper', 'Scissor'])
option= ['Rock', 'Paper', 'Scissor']
sys= random.choice(option)

if st.button('Play'):
    st.write('System: ', sys)
    if (user == sys):
        st.write("Oh ho! Game Tie")
    elif ('rock' > 'scissor') or ('scissor' > 'paper') or ('paper' > 'rock'):
        st.write('Yay! You Won')
    else:
        st.write('System Won')

