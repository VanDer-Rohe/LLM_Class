# -*- coding: utf-8 -*-
"""Assigment_zero.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yI77SMulpl4p_A9ORdPizXKoMxue0puh
"""


import streamlit as st
import numpy as np
import numpy.linalg as la
import pickle

"""
This is a starter code for Assignment 0 of the course, "Hands-on Master Class on LLMs and ChatGPT | Autumn 2023"
taught by Dr. Karthik Mohan.

Computes closest category of a given word or sentence input into a search bar.
The search is implemented through streamlit and can be hosted as a "web app" on the cloud through streamlit as well
Example webpage and search demo: searchdemo.streamlit.app
"""


# Compute Cosine Similarity
def cosine_similarity(array_1,array_2):

    x_arr = np.array(array_1)
    y_arr = np.array(array_2)

    cos = np.cos(x_arr, y_arr)

    return cos

def create_pickle_fom_txt(txt_file = "sample_data/glove.6B.50d.txt"):

  embedding_dict = {}
  with open(txt_file, "r") as f:
    for line in f:
      word = line.split(" ")[0]
      embedding = np.array([float(val) for val in line.split(" ")[1:]])
      embedding_dict[word] = embedding
  try:
    file = open("sample_data/embedding_dict.pkl", "wb")
    pickle.dump(embedding_dict, file)
    print("Successfully pickled data")

  except Exception as error:
    print(f"Failed to pickle data, ERROR: {error}")



# Function to Load Glove Embeddings
def load_glove_embeddings(glove_path="sample_data/embedding_dict.pkl"):
    """
    First step: Download the 50d Glove embeddings from here - thttps://www.kaggle.com/datasets/adityajn105/glove6b50d
    Second step: Format the glove embeddings into a dictionary that goes from a word to the 50d embedding.
    Third step: Store the 50d Glove embeddings in a pickle file of a dictionary.
    Now load that pickle file back in this function
    """

    with open(glove_path,"rb") as f:
        embeddings_dict = pickle.load(f)

    print("Successfully un-pickled data")
    return embeddings_dict


# Get Averaged Glove Embedding of a sentence
def averaged_glove_embeddings(sentence, embeddings_dict):
    """
    Simple sentence embedding: Embedding of a sentence is the average of the word embeddings
    """
    words = sentence.split(" ")
    glove_embedding = np.zeros(50)
    count_words = 0

    #add all embeddings together and return sum

    ############################
    ### WRITE YOUR CODE HERE ###
    ############################

    """
    for word in words:

    return
    """


create_pickle_fom_txt()
load_glove_embeddings()

if __name__ == "__main__":
    load_glove_embeddings()
# Load glove embeddings
glove_embeddings = load_glove_embeddings()

# Gold standard words to search from
gold_words = ["flower","mountain","tree","car","building"]

# Text Search
st.title("Search Based Retrieval Demo")
st.subheader("Pass in an input word or even a sentence (e.g. jasmine or mount adams)")
text_search = st.text_input("", value="")


# Find closest word to an input word
if text_search:
    input_embedding = averaged_glove_embeddings(text_search, glove_embeddings)
    cosine_sim = {}
    for index in range(len(gold_words)):
        cosine_sim[index] = cosine_similarity(input_embedding, glove_embeddings[gold_words[index]])

    print(cosine_sim)
    ############################
    ### WRITE YOUR CODE HERE ###
    ############################

    # Sort the cosine similarities
    # sorted_cosine_sim =

    st.write("(My search uses glove embeddings)")
    st.write("Closest word I have between flower, mountain, tree, car and building for your input is: ")
    st.subheader(gold_words[sorted_cosine_sim[0][0]] )
    st.write("")

from google.colab import drive
drive.mount('/content/drive')
