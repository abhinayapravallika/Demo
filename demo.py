import streamlit as st
st.set_page_config(page_title="sparrows")
st.header("Types of sparrows")
col1,col2,col3,col4=st.columns(3)
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
  st.video("https://www.google.com/search?q=mr+bean+giving+food+to+sparrows+videos+&sca_esv=596479318&rlz=1C1ONGR_enIN1050IN1050&biw=1707&bih=811&tbm=vid&sxsrf=AM9HkKkJ-ogiXLpDjCPQi-nKu9SG8zpX6Q%3A1704697075360&ei=85ybZfOeFcOC4-EP-M6WgAk&ved=0ahUKEwiz5IC9m82DAxVDwTgGHXinBZAQ4dUDCA0&uact=5&oq=mr+bean+giving+food+to+sparrows+videos+&gs_lp=Eg1nd3Mtd2l6LXZpZGVvIidtciBiZWFuIGdpdmluZyBmb29kIHRvIHNwYXJyb3dzIHZpZGVvcyAyBRAhGKABMgUQIRigATIFECEYoAEyBRAhGKABSLL3AVDuNVjk6QFwBXgAkAEAmAHxA6AB3keqAQswLjIxLjE2LjMuMrgBA8gBAPgBAagCA8ICBxAjGOoCGCfCAgsQABiABBiKBRiRAsICCxAAGIAEGLEDGIMBwgIFEAAYgATCAg4QABiABBiKBRixAxiDAcICDRAAGIAEGIoFGEMYsQPCAgoQABiABBiKBRhDwgIQEAAYgAQYigUYQxixAxiDAcICCxAAGIAEGIoFGIYDwgIGEAAYFhgewgIHECEYChigAcICBBAhGBXCAggQIRgWGB4YHcICChAhGBYYHhgPGB3CAgkQIRgKGKABGAqIBgE&sclient=gws-wiz-video#")
