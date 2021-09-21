import random
import streamlit as st

st.title('Rock Paper Scissor')

user= st.radio('Your move, choose wisely',['Rock', 'Paper', 'Scissor'])
option= ['Rock', 'Paper', 'Scissor']
sys= random.choice(option)

if st.button('Play'):
    st.write('System: ', sys)

    def is_win(user, sys):
        if (user == 'Rock' and sys == 'Scissor') or (user == 'Scissor' and sys == 'Paper') or (user == 'Paper' and sys == 'ROck'):
            return True

    if is_win(user, sys):
        st.write('You Won!')
    elif user == sys:
        st.write('Tie')
    else:
        st.write('System Won')
