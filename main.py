#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import streamlit as st
from streamlit_option_menu import option_menu

def Cacher_Hamburger():
    """Fonction permettant de cacher le menu hamburger en haut à droite des apps streamlit."""

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html = True)

st.set_page_config(page_title = "Crêpes", initial_sidebar_state = "collapsed")

Cacher_Hamburger()

Menu = option_menu(None, ["Accueil", "Commandes", "Planning"], default_index = 0, orientation="horizontal")

if Menu == "Accueil":

    st.title("Barbacrêpes")

elif Menu == "Commandes":

    pass

elif Menu == "Planning":
    
    pass
    