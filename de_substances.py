import pandas as pd
import streamlit as st
import os
import json


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

def load_data():
    path_ = "./data"

    with open(os.path.join(path_, "substances.json"), 'r') as fp:
        substance_dic = json.load(fp)

    subs_dict = substance_dic.copy()

    for subs in list(subs_dict.keys()):
        subs_dict[subs]["comment"]=subs_dict[subs]["Dosierung"]["comment"]
        subs_dict[subs]["Dosierung"].pop('comment', None)
        subs_dict[subs]["dose_df"] = pd.DataFrame.from_dict(subs_dict[subs]["Dosierung"])
        subs_dict[subs]["wirkdauer_df"] = pd.DataFrame.from_dict(subs_dict[subs]["Wirkdauer"])
    return subs_dict

subs_dict = load_data()
def main():
    drug_list = tuple(subs_dict.keys())

    st.write("##")


    col1, _, col2 = st.columns(3)



    with col1:
        substance = st.selectbox("Wählt eine Substanz aus", drug_list)
    with col2:
        st.markdown(f"# {subs_dict[substance]['Substanz']}")


    st.info(f"### {subs_dict[substance]['Beschreibung']}")

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(f"### {'Dosierung'}")
        st.dataframe(subs_dict[substance]["dose_df"])

    with col4:

        st.markdown(f"### {'Wirkdauer'}")
        st.dataframe(subs_dict[substance]["wirkdauer_df"])

    st.markdown(f"#### {subs_dict[substance]['comment']}")

    st.markdown("---")
    col5, col6 = st.columns(2)


    var_text = subs_dict[substance]["Konsumform"]

    with col5:
        st.markdown(f"### **Konsumform:**")
        st.markdown(f"#### {var_text.capitalize()}")
    var_text = subs_dict[substance]["Erscheinungsform"]
    with col6:
        st.markdown(f"### **Erscheinungsform:**")
        st.markdown(f"#### {var_text.capitalize()}")
    # st.info(f"##### {var_text}")



    st.markdown("---")
    st.markdown("#### Wirkung")
    col_pos, col_neut, col_neg,  = st.columns(3)

    with col_pos:
        st.markdown(f'#### {subs_dict[substance]["Wirkung"].split(";")[0]}')
    with col_neut:
        st.markdown(f'#### {subs_dict[substance]["Wirkung"].split(";")[1]}')
    with col_neg:
        st.markdown(f'#### {subs_dict[substance]["Wirkung"].split(";")[2]}')

    st.markdown("---")
    st.markdown("#### Kombinationen:")
    st.text("")
    col_pos_, col_neut_, col_neg_,  = st.columns(3)

    with col_pos_:
        st.markdown(f'#### {subs_dict[substance]["Kombinationen"].split(";")[0]}')
    with col_neut_:
        st.markdown(f'#### {subs_dict[substance]["Kombinationen"].split(";")[1]}')
    with col_neg_:
        st.markdown(f'#### {subs_dict[substance]["Kombinationen"].split(";")[2]}')

    st.markdown("---")
    for var in list(subs_dict[substance].keys()):
        if var in ["Toleranz","VIVID Safer-Use Tipps",]:
            var_text = subs_dict[substance][var]

            st.markdown(f"#### {var}:")
            st.markdown(f"##### {var_text}")


    _,footcol, _ = st.columns(3)
    with footcol:
        foot = f' [<img src="https://vivid-hamburg.de/wp-content/uploads/2020/05/logo_lang.jpg" alt="drawing" width="400"/>](https://vivid-hamburg.de/)'
        st.markdown(foot, unsafe_allow_html=True)
