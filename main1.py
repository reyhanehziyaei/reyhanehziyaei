
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("reyhameh ziayi")
st.write(" private shared google sheet.")
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet=[ 1, 2, ])

st.dataframe(df)
st.write("Use [FOR command] to show data:")

for row in df.itertuples():
    st.write(f"Name : {row.name} , Famil: {row.famil} , Age: {row.age}, city: {row.city}")





