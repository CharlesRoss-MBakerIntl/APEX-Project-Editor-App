import streamlit as st

from agol_restapi_tools import *
from agol_table_pull import *

from local_variables import Links


#Generate Token
token = token_generation("AKDOT_COMMUNICATIONS", "Skisnowbird1")



##################### SET CSS STYLE ######################

tabs_font_css = """
    <style>
    div[class*="stTextArea"] label p {
    font-style: Inter;
    font-size: 18px;
    font-weight: bold
    }

    div[class*="stTextInput"] label p {
    font-style: Inter;
    font-size: 18px;
    font-weight: bold
    }

    div[class*="stNumberInput"] label p {
    font-style: Inter
    font-size: 18px;
    font-weight: bold
    }
    </style>
"""







########################### USER INTERFACE ###############################

#Set Page Configuration Settings
st.set_page_config(page_title="Add Projects", page_icon="📍")

# Call CSS Styles
st.write(tabs_font_css, unsafe_allow_html=True)

#Title
st.markdown("# Add Project")

#Description
st.write(
    """
    Add a new project to the APEX Project Database. Follow the instructions below, when the submit button is selected, wait until all green messages appear.
"""
)

#Spacer
st.write("# ")



########### ADD ATTRIBUTES #############

#Project Name
project_name = st.text_input("Project Name")

#IRIS Number
iris_num = st.text_input("IRIS Number")

#Federal Project Number
fed_num  = st.text_input('Federal Project Number')

#STIP ID
stip_id = st.text_input("STIP ID")

#Route ID
route_id = st.text_input("Route ID")

#Route Name

#Project Description

#Project Purpose

#Project Website

#Project Engineer Email

#Design Engineer

#Construction Engineer

#Contract Value

#Anticipated Start

#Anticipated End

#Project Practice

#Funding Type

#Project Location

#Project Limit

#Project Impact

#Construction Description

#Start Milepost

#End Milepost

#DOT&PF Region

#Borough or Census Area

#State House District

#State Senate District

#Project Priority Area

#Longitude

#Latitude

#Creation Date

#Creator

#Edit Date

#Editor

#Scale_MapSeries



