import streamlit as st
import random

def task():
    sum0 = random.randint(0, 10)
    sum1 = random.randint(0, 10)
    res = sum0 + sum1
    s = f"# {sum0} + {sum1} = {res}"
    return s, res

def new_task(task_fun):
    s, res = task_fun()
    st.session_state["task"] = s
    st.session_state["result"] = res


if "number_of_smilies" not in st.session_state:
    st.session_state["number_of_smilies"] = 0

smiley_row = st.markdown("# " + ":grinning: "*st.session_state.number_of_smilies)

if "task" not in st.session_state:
    new_task(task)

show_question = st.markdown(st.session_state["task"])


result_entered = st.slider("Ergebnis",0,20,key="result_entered")

if st.button("Überprüfen"):
    if st.session_state.result_entered == st.session_state.result:
        st.success("Richtig!")
        new_task(task)
        show_question.markdown(st.session_state["task"])
        st.session_state.number_of_smilies += 1
        smiley_row.markdown("# " + ":grinning: "*st.session_state.number_of_smilies)
        if st.session_state.number_of_smilies%5 == 0 and st.session_state.number_of_smilies > 0:
            st.balloons()
    else:
        st.error("Leider nicht richtig.")