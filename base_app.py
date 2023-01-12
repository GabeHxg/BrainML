import streamlit as st
from streamlit_option_menu import option_menu
from apps import first_page  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

apps = [
    {"func": first_page.app, "title": "first_page", "icon": "people"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Brain MLOps",
        options=titles,
        icons=icons,
        menu_icon="menu-button-fill",
        default_index=default_index,
    )

    st.sidebar.title("Sobre")
    st.sidebar.info(
        """
        Demo foi criada por [Gabriel Hxg](https://gabrielhxg.carrd.co/) 
        como forma de apresentação do potencial de ml em Real Estate Analytics. 

        Dados Fonte: [text](https://google.com)
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break