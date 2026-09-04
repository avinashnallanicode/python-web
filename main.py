import streamlit as st
from functions import readfile, writefile
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = readfile()

def add_todo():
    todo = st.session_state["add"] + "\n"
    todos.append(todo)
    writefile(todos)


st.title("My Todo Application")
st.subheader("This is my todo app")
st.write("Helpful tool to keep track of your day-to-day stuffs")


for index, task in enumerate(todos):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        writefile(todos)
        del st.session_state[task]
        st.rerun()

st.text_input( label="Todo item",
              placeholder="Enter a todo...",
              label_visibility="collapsed",
              on_change=add_todo,
              key="add")
