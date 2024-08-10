import streamlit as st
import pandas as pd 

ccss = """
<style>
    .stApp {
        background: linear-gradient(to right, #b721ff, #21d4fd);
        background-size: cover;
        background-repeat: no-repeat;
    }
</style>
"""
st.markdown(ccss, unsafe_allow_html=True)
st.title("SpeakEasy")
st.header("Welcome to SpeakEasy's TO-DOs")
st.subheader("With SpeakEasy's TO-DOs, you can manage & schedule your day as smooth as it can get!")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

def add_task(task):
    "Add a task to the task list"
    st.session_state.tasks.append(task)

def view_all_tasks():
    "View all tasks in the task list"
    return st.session_state.tasks

def update_task(index, new_task):
    "Update a task in the task list"
    st.session_state.tasks[index] = new_task

def remove_task(index):
    "Remove a task from the task list"
    del st.session_state.tasks[index]

def search_tasks(keyword):
    "Search for tasks containing a specific keyword"
    return [task for task in st.session_state.tasks if keyword.lower() in task.lower()]

def display_total_tasks():
    "Display the total number of tasks"
    return len(st.session_state.tasks)

st.subheader("Add a Task")
with st.form("add_task"):
    task_input = st.text_input("Enter a task")
    if st.form_submit_button("Add Task"):
        add_task(task_input)

st.subheader("View All Tasks")
if st.button("View All Tasks"):
    st.write(view_all_tasks())

st.subheader("Update a Task")
with st.form("update_task"):
    updinx = st.number_input("Enter the task index to update", min_value=0)
    update_task_input = st.text_input("Enter the new task")
    if st.form_submit_button("Update Task"):
        try:
            update_task(int(updinx), update_task_input)
        except IndexError:
            st.error("Invalid task index")

st.subheader("Remove a Task")
with st.form("remove_task"):
    rmvinx = st.number_input("Enter the task index to remove", min_value=0)
    if st.form_submit_button("Remove Task"):
        try:
            remove_task(int(rmvinx))
        except IndexError:
            st.error("Invalid task index")

st.subheader("Search for Tasks")
with st.form("search_tasks"):
    keyword = st.text_input("Enter a keyword to search")
    if st.form_submit_button("Search Tasks"):
        st.write(search_tasks(keyword))

st.subheader("Total Tasks")
st.write("Total tasks:", display_total_tasks())
