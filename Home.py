##################################################
## Displays the Home page of the developed Streamlit web application.
##################################################
## Author: Matheus Vargas Volpon Berto
## Copyright: Copyright 2022, Discovering Latent Knowledge in medical paper on Acute Myeloid Leukemia
## Email: matheus.berto@estudante.ufscar.br
##################################################

# IMPORTS:
import streamlit as st

# FUNCTIONS:
def set_page_layout():
    '''Define some configs of the Streamlit App page, only front-end settings.'''

    st.set_page_config(
        page_title="WE4LKD AML",
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded",
     )
    
    hide_streamlit_style = """
            <style>           
            footer {
                visibility: hidden;
            }
            
            footer:after {
                content:'Developed by Matheus Vargas Volpon Berto.'; 
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
                top: 2px;
                color: black;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
# MAIN PROGRAM:
if __name__ == '__main__':
    set_page_layout()
    
    st.sidebar.header('GitHub Repository')
    st.sidebar.markdown("[![Foo](https://cdn-icons-png.flaticon.com/32/25/25231.png)](https://github.com/matheusvvb-19/WE4LKD-leukemia_app)")
    
    st.title('Word Embedding For Latent Knowledge Discovery AML')
  
    st.header('1. About this web app')
    st.markdown('This web app contains the models trained during the project and making it possible to users to explore the embeddings, more information about how to use each tool are detailed on the respective page - which can be accessed trough the left sidebar.')
    st.markdown("In the Word2Vec page, you can search for words in the models' vocab and visualize the nearest tokens in the vector space.")
    st.markdown('In the BERT page, you can find similar sentences from our dataset according to an input sentence.')
    
    st.header('Funding')
    st.markdown('This project is fully funded by the Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP, Brazil), identification codes 2021/13054-8 and 2022/07236-9.')
    st.markdown('Undergraduate scholarship student: Matheus Vargas Volpon Berto.')
    st.markdown('Professor and supervisor: Dr. Tiago Almeida.')
    st.markdown('Educational institution: Federal University of São Carlos (UFSCar) - Sorocaba campus.')
    st.markdown("In addition, part of the project was developed in partnership with the Computer Science Department of the University of Sheffield (UK), supervised by Dr. Carolina Scarton.")
