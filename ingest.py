from src.rag_pipeline import add_document
import os


folder="data"


for file in os.listdir(folder):

    path=os.path.join(folder,file)

    with open(path,"r",encoding="utf-8") as f:

        text=f.read()

    add_document(
        file,
        text
    )

    print("Added:",file)