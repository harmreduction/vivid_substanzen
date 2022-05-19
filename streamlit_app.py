
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
     page_title="Vivid Substanzen",
     page_icon="https://pbs.twimg.com/profile_images/1396102254487384065/ZjD8GvMw_400x400.png",
     layout="wide", #centered wide
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://vivid-hamburg.de/kontakt/',
         'Report a bug': "https://github.com/ViewsOnDrugs/vivid_substanzen/tree/master",
         'About': "**App Author: [Francisco Arcila](https://twitter.com/franarsal/)** \n\nConcept design: Francisco Arcila."
     }
 )

#app.py
import de_substances, de_disclaimer

PAGES = {
    "Substanzen": de_substances,
    # "MCDA Drugs": en_app,
    "Disclaimer": de_disclaimer,
}



vod_icon='[<img src="https://vivid-hamburg.de/wp-content/uploads/2020/05/logo_lang.jpg"  alt="centered image" class="center" width="300"/>](https://vivid-hamburg.de/)'
st.sidebar.markdown(vod_icon,  unsafe_allow_html=True)
#
title_alignment= ' <div style="text-align: center"> -Know your Drugs- </div>  '
#
st.sidebar.markdown(title_alignment, unsafe_allow_html=True)

with st.sidebar:
    selection = option_menu("", list(PAGES.keys()),
    icons=['file-earmark-text', 'info-circle'], menu_icon="cast", default_index=0,
    styles={
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px"},
        "nav-link-selected": {"background-color": "ffffff"},
    })

# selection = st.sidebar.radio("",list(PAGES.keys()))
page = PAGES[selection]
page.main()
