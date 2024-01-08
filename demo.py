import streamlit as st
st.set_page_config(page_title="sparrows")
st.header("Types of sparrows")
col,col2=st.columns(2)
with col1:
  st.subheader("Song sparrow")
  st.image("/.Song sparrow.img",caption="Song sparrow",width=300,use_column_width=True)
  st.write("Song sparrows sing well.")
with col1:
  st.subheader("House sparrow")
  st.image("/.House sparrow.img",caption="Song sparrow",width=300,use_column_width=True)
  st.write("House sparrows are good at adapting to urban environments.")
