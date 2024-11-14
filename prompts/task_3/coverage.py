prompts = {
    "1": """\
Your job is to evaluate a summariser chatbot. The chatbot takes articles and summarises their contents into shorter, punchier highlights.
    
Here's the original article:
{ARTICLE}

Write a list of the key facts in the text in order:

["1. ....", "2. ....",...,"10: ...."]

Here is a summary of the original text:

{SUMMARY}

Your task is to specify how many of those facts are NOT mentioned directly or indirectly by the summary.

Return the numbers of the key facts that were NOT covered in a list

EXAMPLE OUTPUT: ["1", "9"]\
"""
}
