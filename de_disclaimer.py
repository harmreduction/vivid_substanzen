
import streamlit as st



def main():

    st.write("Die Informationen auf dieser App sind nicht als Konsumempfehlung gedacht. Sie wurden sorgfältig zusammengestellt, können aber nur einen ersten Anhaltspunkt für eigene Nachforschungen bilden. Konsumerfahrungen und Risiken sind individuell. Sie können von den genannten Informationen abweichen. Sich verstärkende Kombinationen und Mischkonsum generell haben ein höheres Risiko für unerwünschte Nebenwirkungen als der Monokonsum von Substanzen. Eine Verringerung der wahrgenommenen Effekte bei der Kombination von Substanzen ist meistens durch eine Überlagerung und nicht durch eine gegenseitige Aufhebung zu erklären. Die unter gefährlich genannten Kombinationen sind keine abschließende Liste gesundheitsschädlicher Kombinationen.")


    _,footcol, _ = st.columns(3)
    with footcol:
        foot = f' [<img src="https://vivid-hamburg.de/wp-content/uploads/2020/05/logo_lang.jpg" alt="drawing" width="400"/>](https://vivid-hamburg.de/)'
        st.markdown(foot, unsafe_allow_html=True)
