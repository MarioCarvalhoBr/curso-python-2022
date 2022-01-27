import os

os.environ["My Environment"] = "The Best Environment"
myenv = os.environ.get("Path")

print(myenv)