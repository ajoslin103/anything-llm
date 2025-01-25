
#1 install anything LLM & follow instructions to run locally -- select an LLM (I used AnythingLLM to download and use Llama3 3B)

#2 create a workspace named "David Lynch" and click on the button to upload files

#3 drag in all the pdf's from the rag-david-lynch folder of this repo

#4 Anything LLM doesn't have great feedback, you'll have to wait a minute and then close the uploader -- you should see the documents with their spinners waiting to complete embedding -- wait it out 

#5 go to the prefs for the workspace and set the chat type to "query" and click the "update workspace" button

#6 click on the "chat" tab and type in: who did david lynch collaborate with?" -- on my m2 this took about 3 minutes and the answer listed several actors and shows

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

- troubleshooting

    - go to your API testing area http://localhost:3001/api/docs
    - and paste in your API Key after clicking a lock somwewhere
        - (strangely, a LOCKED icon means you ARE logged in, while a grey unlocked icon means you are NOT logged in)
      
    - expand any endpoint and click "Try it out" and then "Execute" to see the results after you setup your values