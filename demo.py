import streamlit as st
st.set_page_config(page_title="sparrows")
st.header("Types of sparrows")
col1,col2=st.columns(2)
with col1:
  st.subheader("Song sparrow")
  st.image("https://www.allaboutbirds.org/guide/assets/photo/308771371-480px.jpg")
  st.write("Song sparrows sing well.")
with col2:
  st.subheader("House sparrow")
  st.image("https://wildlifesos.org/wp-content/uploads/2022/03/House-sparrow-female-scaled.jpg")
  st.write("House sparrows are good at adapting to urban environments.")
