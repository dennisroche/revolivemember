import streamlit as st
from datetime import datetime
from pathlib import Path


title = 'REVO Live Member'

def main():
    st.set_page_config(page_title=title, layout='wide')
    with st.sidebar:
        st.image('https://revofitness.com.au/wp-content/uploads/2021/09/revo-master-logo.svg', None, 300)
        st.title(title)

if __name__ == '__main__':
    main()