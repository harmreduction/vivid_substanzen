import json
import urllib.request
import streamlit_analytics
import streamlit as st
import os
from PIL import Image

interactions_dict = {
    "low risk & synergy": ["LRS.png","These drugs work together to cause an effect greater than the sum of its parts, and they aren't likely to cause an adverse or undesirable reaction when used carefully. Additional research should always be done before combining drugs."
],
    "low risk & no synergy": ["LRNS.png",],
    "low risk & decrease": ["LRD.png","Effects are additive. The combination is unlikely to cause any adverse or undesirable reaction beyond those that might ordinarily be expected from these drugs."
],
    "caution": ["C.png",  "These combinations are not usually physically harmful, but may produce undesirable effects, such as physical discomfort or overstimulation. Extreme use may cause physical health issues. Synergistic effects may be unpredictable. Care should be taken when choosing to use this combination."
],
    "unsafe": ["U.png",  "There is considerable risk of physical harm when taking these combinations, they should be avoided where possible."
],
    "dangerous": ["D.png",  "These combinations are considered extremely harmful and should always be avoided. Reactions to these drugs taken in combination are highly unpredictable and have a potential to cause death."
],
    "serotonin syndrome": ["serotoninsyndrome", "fa-flash"],
    "fallback": ["unknown", "fa-question"]
}


def load_data():
    path_ = "./data"

    pil_path = os.path.join(path_, "PIL")

    # load combo info from tripsit.me
    with urllib.request.urlopen("https://tripsit.me/combo_beta.json") as url:
        combos = json.loads(url.read().decode())

    return pil_path, combos


def main():

    streamlit_analytics.start_tracking()
    pil_path, subs_dict = load_data()
    drug_list = tuple(subs_dict.keys())

    _, coltit, _ = st.columns(3)

    with coltit:

        st.title("TripSit Drug Combinations")
    st.info("#### This is an app version of the [TripSit](https://tripsit.me/) combo chart you can find [here](https://wiki.tripsit.me/wiki/Drug_combinations)")
    st.warning("WARNING! For educational purposes: We do not endorse any of these combinations. This page will always be 'work in progress'. It is extremely important to be safe at all times! See below the graphic for important information regarding specific combinations.")

    st.markdown(
        "## Please select two substances")
    st.markdown('#')
    col1, col2 = st.columns(2)

    with col1:
        substance_a = st.selectbox("Select a substance", drug_list)
    with col2:
        substance_b = st.selectbox("Select a combining substance", subs_dict[substance_a].keys())

    st.markdown('#')
    status = subs_dict[substance_a][substance_b]['status']
    legend = Image.open(os.path.join(pil_path, f"{interactions_dict[status.lower()][0]}"))

    col3, col4 , col5 = st.columns(3)

    with col3:
        st.markdown(f"# {str(substance_a).title()} + {str(substance_b).title()}")

    with col4:
        if "note" in subs_dict[substance_a][substance_b]:

            st.image(legend)
            st.markdown(f"Note: {subs_dict[substance_a][substance_b]['note']}")
        else:
            st.image(legend)

    with col5:
        st.markdown(f"### {interactions_dict[status.lower()][1]}")

    st.markdown('#')
    st.markdown('#')
    st.markdown('#')

    st.markdown("""#### The app, like the combo chart, is meant as a quick reference guide and additional research MUST always be done.
For additional information check out the TripSit [Factsheet](http://drugs.tripsit.me/).
For re-use and attribution info see [here](https://wiki.tripsit.me/wiki/Drug_combinations#Use_.26_Attribution)

Click on the TriPsit Logo to check out the TripSit App 2 with this and more useful information!""")

    _, footcol, _ = st.columns(3)

    with footcol:
        foot = f' [<img src="https://raw.githubusercontent.com/TripSit/combogen/master/resources/img/logo.svg" alt="drawing" width="200"/>](https://play.google.com/store/apps/details?id=me.tripsit.mobile&hl=en_US&gl=US)'
        st.markdown(foot, unsafe_allow_html=True)
    streamlit_analytics.stop_tracking(unsafe_password=st.secrets["analytics"])

