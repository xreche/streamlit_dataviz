import streamlit as st

st.title("Columns Demo")

# --- Container 1 ---
container_1 = st.container(border=True)
container_1.header("Container")
container_1.subheader("Sub header")

container_1_c1, container_1_c2, container_1_c3 = container_1.columns(3)

container_1_c1.button("Colum 1, Container 1")
container_1_c2.button("Colum 2, Container 1")
container_1_c3.button("Colum 3, Container 1")

c1, c2 = st.columns(2)
c1.button("Free Column 1")
c2.button("Free Column 2")

# --- Section 2 ---
container_2 = st.container()
container_2.title("Section 2")
container_2_c1, container_2_c2 = container_2.columns(2)
container_2_c1.button("Colum 1, Container 2")
container_2_c2.button("Colum 2, Container 2")

# --- Section 3 ---
container_3 = st.container()
container_3.title("Section 3")
container_3_c1, container_3_c2, container_3_c3 = container_3.columns(3)
container_3_c1.button("Colum 1, Container 3")
container_3_c2.button("Colum 2, Container 3")
container_3_c3.button("Colum 3, Container 3")
