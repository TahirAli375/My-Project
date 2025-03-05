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

conn=sqlite3.connect('books.db')
c=conn.cursor()
def formCreation():
    st.subheader('New Book To Database')
    with st.form(key='Registration Form'):
        Book_Name=st.text_input('Please Enter The Name of the Book')
        Name=st.text_input('Please Enter The Name of The Author:')
        

        submit= st.form_submit_button(label="Submit")
    if submit == True:
        st.success("Your Request for the New book has been submitted Successfully!")
        info(Book_Name,Name)


def info(a,b):
    c.execute(""""
                   
Create Table if not exists Registrations(Name Text(50),FName Text(50),CNIC int(50) )                
 """
    )
    c.execute("Insert info Registration values(?,?,)",(a,b,))
    conn.commit()
    conn.close()
    st.succes("user has added the values to the Database")

formCreation()