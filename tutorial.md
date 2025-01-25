
#1 install anything LLM & follow instructions to run locally

    - Select an LLM (AnythingLLM : Gemma2)

#2 Create a workspace named "David Lynch" and click on the button to upload files

#3 Drag in JUST the files in rag-film-types folder for now

#4 Select the files and move them to the workspace and then scroll all the way down to save your changes

#5 go to the prefs for the workspace and set the chat type to "query" and click the "update workspace" button

#6 click on the "chat" tab and type in: What was the name of David Lynch's first wife?" 

👍 we have confirmed installation and creation of the RAG database by querying and receiving a response

#1 in ALLM go to settings and developer api and generate and copy an api key - (you will be able to copy it later)

#2 open a terminal into the repo and enter `pip install requests`

#3 run the small test to check if the api is working

`API_KEY="<your-api-key-here" python list_workspaces.py`

#4 your result should be information about David Lynch's acting as well as the contexts the query was relevant to

#5 run the real test to query the rag

`API_KEY="<your-api-key-here" python query_workspace.py`

#6 a few mins later your result should include a list of actors and shows

👍 we have queried the RAG databaase

- general understanding 

#1 join the AnythingLLM discord

    - good link for getting started

        - https://discord.com/channels/1114740394715004990/1327526178403127366/1327863441293180948

