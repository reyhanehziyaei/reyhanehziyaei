import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("webjdm-424819-f9fc79386e91.json", scope)
client = gspread.authorize(creds)


sheet = client.open("ContactList").sheet1

def add_contact(name, phone, email):
    sheet.append_row([name, phone, email])

def get_contacts():
    contacts = sheet.get_all_records()
    return pd.DataFrame(contacts)

def update_contact(row, name, phone, email):
    sheet.update_cell(row, 1, name)
    sheet.update_cell(row, 2, phone)
    sheet.update_cell(row, 3, email)

def delete_contact(row):
    sheet.delete_row(row)

st.title("Contact List Manager")

st.header("Add a New Contact")
name = st.text_input("Name")
phone = st.text_input("Phone")
email = st.text_input("Email")

if st.button("Add Contact"):
    add_contact(name, phone, email)
    st.success(f'Contact "{name}" added!')

st.header("Contact List")
contacts_df = get_contacts()

if not contacts_df.empty:
    for index, row in contacts_df.iterrows():
        st.write(f"**Name:** {row['Name']} Phone: {row['Phone']} Email: {row['Email']}")
        if st.button(f"Delete {row['Name']}", key=f"delete_{index}"):
            delete_contact(index + 2)
            st.success(f'Contact "{row["Name"]}" deleted!')
        with st.expander(f"Edit {row['Name']}"):
            new_name = st.text_input("Name", value=row["Name"], key=f"name_{index}")
            new_phone = st.text_input("Phone", value=row["Phone"], key=f"phone_{index}")
            new_email = st.text_input("Email", value=row["Email"], key=f"email_{index}")
            if st.button(f"Update {row['Name']}", key=f"update_{index}"):
                update_contact(index + 2, new_name, new_phone, new_email)
                st.success(f'Contact "{new_name}" updated!')

else:
    st.write("No contacts found.")

st.write("## All Contacts")
st.dataframe(contacts_df)