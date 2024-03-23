from audiocraft.models import MusicGen
import streamlit as st 
import os 
import torch 
import torchaudio
import numpy as np
import base64

@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    return model 

st.set_page_config(
    page_icon="",
    page_title="Music Gen"
    
)

def main():
    st,title("Text To Music Generation")

if __name__ == :"__main__":
    main()