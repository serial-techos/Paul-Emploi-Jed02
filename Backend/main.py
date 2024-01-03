from auth import get_token
import requests
import pandas as pd
#from openai import OpenAI
import json
from jobs import get_jobs
from processing import keep_columns
from dotenv import load_dotenv
import os
from Utils import prompt
from processing import process_job_description

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLIENT_ID= os.getenv("CLIENT_ID")
CLIENT_SECRET= os.getenv("CLIENT_SECRET")
access_token= get_token(CLIENT_ID,CLIENT_SECRET)

jobs_list= get_jobs({'M18','data'}, access_token)
#print(f"My job list is {jobs_list}")

resultats=jobs_list['resultats']
#print(f"My job list is {resultats}")

df_resultats=pd.DataFrame(resultats)
#print(f"My job list in dataframe is {df_resultats}")

colonnes_a_garder= ['id', 'intitule', 'description', 'dateCreation', 'lieuTravail', 'appellationlibelle', 'entreprise', 'typeContrat','experienceLibelle', 'competences','salaire','alternance', 'secteurActiviteLibelle']
df_jobs = keep_columns (df_resultats, colonnes_a_garder)
df_jobs 

df_jobs20=df_jobs.loc[:20]
df_jobs20_list=df_jobs20.T.to_dict().values()

extracted_jobs =process_job_description(df_jobs["description"], debug=True)
extracted_jobs
