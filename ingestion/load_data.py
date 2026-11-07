import json
from langchain_core.documents import Document

with open("data/yokai_database.json", "r", encoding="utf-8") as yokai:
  data = json.load(yokai)

docs = []

for yokai in data:
  text = ("Name: " + str(yokai["name"]) + "\nRank: " + str(yokai["rank"]) + "\nTribe: " + str(yokai["tribe"])
  + "\nFavorite Food: " + str(yokai["favorite_food"]) + "\nAbilities: " + str(yokai["abilities"]) + "\nDescription: " + str(yokai["description"]))


  docs.append(Document(
      page_content=text,
      metadata={
        "name": yokai["name"],
        "rank": yokai["rank"],
        "tribe": yokai["tribe"],
        "favorite_food": yokai["favorite_food"],
        "abilities": yokai["abilities"],
        "description": yokai["description"]
      },


    )
  )


for i in range(0, len(docs)):
  print(docs[i].page_content)
  print(docs[i].metadata)

  print()