import streamlit as st
st.set_page_config(page_title="sparrows")
st.header("Types of sparrows")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Song sparrow")
  st.image("https://www.allaboutbirds.org/guide/assets/photo/308771371-480px.jpg")
  st.write("Song sparrows sing well.")
with col2:
  st.subheader("House sparrow")
  st.image("https://wildlifesos.org/wp-content/uploads/2022/03/House-sparrow-female-scaled.jpg")
  st.write("House sparrows are good at adapting to urban environments.")
with col3:
  st.subheader("sparrows")
  st.image("https://media1.tenor.com/m/Ni39LJJY6dIAAAAC/sparrows.gif")
  st.write("sparrows playing with water") 
with col1:
  st.video("https://www.youtube.com/watch?v=8WfMUqd4qH8&pp=ygUUdG9tIGFuZCBqZXJyeSB0ZWx1Z3U%3D")
with col2:
  st.image("https://www.gifcen.com/wp-content/uploads/2021/09/tom-and-jerry-gif.gif")
