import streamlit as st
from streamlit_option_menu import option_menu
from apps import data_present  # import your app modules here

st.set_page_config(page_title="Sistema Web de Jurimetria", layout="wide")

apps = [
    {"func": data_present.app, "title": "Apresentação dos dados", "icon": "file-earmark-bar-graph"},
]  # Icons: https://icons.getbootstrap.com/


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
        "Jurimetria",
        options=titles,
        icons=icons,
        menu_icon="menu-button-fill",
        default_index=default_index,
    )

    st.sidebar.title("Sobre")
    st.sidebar.info(
        """
        Sistema Web Jurisprudência e Confecção de Manifestações. 
        Análise de decisões de Tribunais de Contas. 
        """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break