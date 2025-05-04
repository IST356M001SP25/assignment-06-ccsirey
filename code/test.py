import streamlit as st
import pandas as pd
import requests
import json 
if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from apicalls import get_google_place_details, get_azure_sentiment, get_azure_named_entity_recognition
else:
    from code.apicalls import get_google_place_details, get_azure_sentiment, get_azure_named_entity_recognition

PLACE_IDS_SOURCE_FILE = "solutions/cache/place_ids.csv"
CACHE_REVIEWS_FILE = "cache/reviews.csv"
CACHE_SENTIMENT_FILE = "cache/reviews_sentiment_by_sentence.csv"
CACHE_ENTITIES_FILE = "cache/reviews_sentiment_by_sentence_with_entities.csv"

def reviews_step(place_ids: str|pd.DataFrame) -> pd.DataFrame:
    '''
      1. place_ids --> reviews_step --> reviews: place_id, name (of place), author_name, rating, text 
    '''

    # if string, then its a filename so load into dataframe
    if isinstance(place_ids, str):
        place_ids_df = pd.read_csv(place_ids)
    else:
        place_ids_df = place_ids

    # TRANSFORMATIONS

    # get google place details for each place_id
    google_places = []
    for index, row in place_ids_df.iterrows():
        place = get_google_place_details(row['Google Place ID'])
        google_places.append(place['result'])

    # construct dataframe at the reviews level, include place_id, name from parent level
    reviews_df = pd.json_normalize(google_places, record_path="reviews", meta=["place_id", 'name'])

    # pair down to the columns we want
    reviews_df = reviews_df[['place_id', 'name',  'author_name', 'rating', 'text']]

    # save to cache, return dataframe
    reviews_df.to_csv(CACHE_REVIEWS_FILE, index=False, header=True)
    return reviews_df

df = reviews_step(PLACE_IDS_SOURCE_FILE)
st.write(df)   