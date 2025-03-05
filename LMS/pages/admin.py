import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('library_management.db')
c = conn.cursor()

# Query to select all records from the user login table
c.execute("SELECT * FROM users")
data = c.fetchall()

# Convert the data to a pandas DataFrame for better readability
df = pd.DataFrame(data, columns=[desc[0] for desc in c.description])

# Display the data in Streamlit
st.title("User Login Data")
st.write("Displaying all user login records:")

# Use st.dataframe to display the data in a table format
st.dataframe(df)

# Close the database connection
conn.close()
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
y = [100,178,213,156,200,145,123,167,198,210,189,200] 
plt.plot(x, y) 
plt.xlabel('Months') 
plt.ylabel('Number of new users') 
plt.title('Newest Users per month in 2024') 
plt.show()
plt.savefig('new_users.png') 
st.image('new_users.png')
st.divider()

conn=sqlite3.connect('user_books.db')
c=conn.cursor()
def formCreation():
    st.subheader('New Book To Database')
    with st.form(key='Registration Form'):
        title = st.text_input('Please Enter The Name of the Book')
        author = st.text_input('Please Enter The Name of The Author:')
        
        submit = st.form_submit_button(label="Submit")
    if submit:
        st.success("Your Request for the New book has been submitted Successfully!")
        info(title, author)

def info(a, b):
    c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            title TEXT(50),
            author TEXT(50)
        )
    """)
    c.execute("INSERT INTO books (title,author) VALUES (?, ?)", (a, b))
    conn.commit()
    conn.close()
    st.success("User has added the values to the Database")

formCreation()