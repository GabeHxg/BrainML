# Importing the required libraries
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from gsheetsdb import connect

def app():
    # Present
    st.title("Gdrive ")
    st.markdown("""**Teste | Sistema Web Jurisprudência e Google Drive**""")

    # Reading the dataset
    st.markdown("""Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """)

    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=["https://www.googleapis.com/auth/drive", ],)

    try:
        service = build('drive', 'v3', credentials=credentials)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            st.markdown('No files found.')
            return
        st.markdown('Files:')
        for item in items:
            st.markdown(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        st.markdown(f'An error occurred: {error}')
