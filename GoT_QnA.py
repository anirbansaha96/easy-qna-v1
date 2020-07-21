from haystack import Finder
from haystack.indexing.cleaning import clean_wiki_text
from haystack.indexing.utils import convert_files_to_dicts, fetch_archive_from_http
from haystack.reader.farm import FARMReader
from haystack.reader.transformers import TransformersReader
from haystack.utils import print_answers
from haystack.database.memory import InMemoryDocumentStore
document_store = InMemoryDocumentStore()

#doc_dir = "data/article_txt_got"
#s3_url = "https://s3.eu-central-1.amazonaws.com/deepset.ai-farm-qa/datasets/documents/wiki_gameofthrones_txt.zip"
#fetch_archive_from_http(url=s3_url, output_dir=doc_dir)

#dicts = convert_files_to_dicts(dir_path=doc_dir, clean_func=clean_wiki_text, split_paragraphs=True)
#document_store.write_documents(dicts)

#from haystack.retriever.sparse import TfidfRetriever
#retriever = TfidfRetriever(document_store=document_store)

#reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)

#finder = Finder(reader, retriever)

import streamlit as st

question=st.text_input("Write a Text")

#prediction = finder.get_answers(question=question, top_k_retriever=10, top_k_reader=5)
if question!='':
  prediction='Test Output'

  streamlit.write("You Wrote : ", prediction)
