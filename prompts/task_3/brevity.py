prompts = {
    "1": """Your job is to evaluate a summariser chatbot. The chatbot takes articles and summarises their contents into shorter, punchier highlights.

Here is a summary made by the chatbot:

{SUMMARY}

Your job is to assess the brevity and conciseness of the summary using the following categories:

**POOR**
- The summary needlessly uses complicated language
- The summary contains surplus information not needed to summarise the key events
- The summary is long-winded and indirect

**MEDIUM**
- The summary sometimes use complicated language but is largely plain
- The summary only occassionally includes too much information
- The summary is generally direct although slightly off centre at points

**GOOD*
- The summary uses plain and simple language
- The summary contains the minimum amount of information to relay the key events
- THe summary is direct and to the point

RETURN YOUR SCORE IN THE FOLLOWING FORMAT:

{'SCORE' : SCORE GOES HERE}
"""
}
