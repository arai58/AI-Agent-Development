from pathlib import Path
import os


def load_documents():
    documents={}
    folder=Path("knowledge")
    for file in folder.glob("*.txt"):
        documents[file.name]=file.read_text(encoding="utf-8") 
        
    return documents     

#Embedder
def create_embedding(client,selected_model,content):
    response=client.embeddings.create(
            model=selected_model,
            input=content
    )
    return response.data[0].embedding

#Embed List
def embed_contents(client,selected_model,contents):
    embeds={}
    for key in contents.keys():
        embedding=create_embedding(client,selected_model,contents[key])
        embeds[key]=embedding

    return embeds
    