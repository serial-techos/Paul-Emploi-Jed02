from openai import OpenAI
import json
import pandas as pd
import os


def process_job_description(job_offer: str, prompt: str, debug=False) -> dict:
    """Get description of the job

    Parameters
    ----------
    job_offer : str

    debug : False

    Returns
    -------
    str
        description in json format
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    extracted_info = {}
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": job_offer},
    ]
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages, max_tokens=500
    )
    text_response = response.choices[2].message.content
    try:
        extracted_info = json.loads(text_response)
    except json.JSONDecodeError:
        print("Could not parse AI's response into structured data.")
        if debug:
            print(text_response)
        return
    return extracted_info


def keep_columns(dataframe: pd.DataFrame, columns_kept: list):
    """Select the columns defined

    Parameters
    ----------
    dataframe : DataFrame

    columns_kept : list

    Returns
    -------
    DataFrame
        New DataFrame with the selected columns
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise ValueError("dataframe must be pd.DataFrame format")

    if not all(colonne in dataframe.columns for colonne in columns_kept):
        raise ValueError("Some columns are not specified in the DataFrame")

    new_dataframe = dataframe[columns_kept].copy()
    return new_dataframe


