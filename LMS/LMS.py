import streamlit as st
import sqlite3 as sql
import datetime as dt

# Create a connection to the SQLite database with better error handling
def create_connection():
    try:
        conn = sql.connect('library_management.db', check_same_thread=False)
        return conn
    except sql.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Initialize connection
conn = create_connection()
if conn is not None:
    c = conn.cursor()

    # Create table with better structure
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 fname TEXT NOT NULL,
                 password TEXT NOT NULL,
                 city TEXT NOT NULL,
                 date TEXT NOT NULL)''')
    conn.commit()

    st.title("Library :red[Management] System")
    st.subheader("Login To Proceed👋")
    logger = st.sidebar.selectbox("Select", options=["Admin", "User"])

    def form_Creation():
        st.write("Please Fill this form without leaving anything undone!")
        with st.form(key="Login"):
            if logger == "User":
                k = dt.datetime.now()
            
                Name = st.text_input("Please Enter Full Name:", placeholder='Full Name')
                Fname = st.text_input("Please Enter Father Name", placeholder='F/Name')
                Password = st.text_input("Please Enter Strong Password!", placeholder='Password', type="password")
                City = st.text_input("Enter Your Current address along with city!", placeholder='Address')
                dated = st.date_input("Enter date", min_value=k.date())
                
                submit = st.form_submit_button()
                
                if submit:
                    if not Name:
                        st.warning("Please Enter Name")
                    elif not Password:
                        st.warning("Not Valid Without Password")
                    elif not City:
                        st.warning("Please Enter Valid Name of City")
                    elif not Fname:
                        st.warning("Please Enter Father Name")
                    elif not dated:
                        st.warning("Please Enter valid Date!")
                    else:
                        try:
                            # Insert user data into the database
                            c.execute("INSERT INTO users (name, fname, password, city, date) VALUES (?, ?, ?, ?, ?)",
                                    (Name, Fname, Password, City, str(dated)))
                            conn.commit()
                            st.success("You have Logged in!")
                            st.page_link('pages/user.py',label='Go to User Dashboard')

                        except sql.Error as e:
                            st.error(f"Error saving to database: {e}")

            elif logger == "Admin":
                Name = st.text_input("Please Enter Full Name:", placeholder='Full Name')
                Password = st.text_input("Please Enter Strong Password!", placeholder='Password', type="password")
                submit = st.form_submit_button()

                if submit:
                    if Name == 'Admin' and Password == 'admin':
                        st.success("You have Logged in!")
                        st.page_link("pages/admin.py",label="Admin Page")
                    else:
                        st.warning("Invalid Username or Password")

    form_Creation()
else:
    st.error("Failed to initialize database connection")