import pandas as pd
import openai
import os
import random
import pinecone
import time
from dotenv import load_dotenv

load_dotenv()

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment='asia-southeast1-gcp-free')


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']


def insert_embedding():
    """
    Converts the training set into embeddings and inserts
    the embeddings into a vector db
    """
    df = pd.read_csv("./train.csv")
    embeddings = []
    for i in range(len(df)):
        sentence = df.iloc[i]['sentence']
        embeddings.append(get_embedding(sentence, model='text-embedding-ada-002'))
        time.sleep(20)
    df['embedding'] = embeddings
    vectors = list(zip(df.index.astype(str), df.embedding))
    index = pinecone.Index("querysupport")
    index.upsert(vectors)
    print("Done!")


def get_samples(embedding, n_samples, is_random=False, total_sample=40):
    """
    Select examples from the train set to be used within
    the prompts during inference.
    """
    if not is_random:
        index = pinecone.Index("querysupport")
        samples = index.query(
            vector=embedding,
            top_k=n_samples,
            include_values=False
        )
        return [int(sample['id']) for sample in samples['matches']]

    return random.sample(range(0, total_sample), n_samples)
