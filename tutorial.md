## Setup and test

#1 install anything LLM & follow instructions to run locally

    - Select an LLM (AnythingLLM : Gemma2)

#2 Create a workspace named "David Lynch"

NOTE: TRY NOT TO USE THE DEFAULT CHAT - IT CAN'T BE DELETED SO IT'S ANSWERS WILL BECOME SHARED DATA (?)

#3 click on the "NEW CHAT" tab and type in: What were the names of any of David Lynch's wives? 

#4 the answer will be inclusive of all his wives, as would be expected with a CHAT

#5 go to the Workspace chat and set type to QUERY - AND set the TEMP to 0 (zero) - save changes at the bottom

#6 paste in: What were the names of any of David Lynch's wives? 

#7 the answer will be "There is no relevant information in this workspace to answer your query" - this is expected with a QUERY

#8 Drag in JUST the "Wikipedia" from the "rag-david-lynch" folder for now

#9 Select the file and move it to the workspace and then scroll all the way down to save your changes

#10 the answer should be: "Jennifer Lynch, Peggy Reavey, Mary Fisk, Isabella Rossellini, Emily Stofle are some of the names of David Lynch’s wives"

#11 ask the same question again, and you should get the same answer

#12 change the TEMP to 0.5 and save

#13 ask the same question again, and you should get a different answer

#14 change the TEMP to 1 and save

#15 ask the same question again, and you should get a fairly bizzare answer

#16 lower the TEMP back to something around 0.25

👍 good - we have confirmed installation and creation of the RAG database by querying and receiving a response, and we have seen how temperature can affect the results

## Now, where is code ??

#### Coooooooode !!

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

