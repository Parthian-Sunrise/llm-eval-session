prompts = {
    "1": """\
Your job is to evaluate a summariser chatbot. The chatbot takes articles and summarises their contents into shorter, punchier highlights.
    
Here's the original article:
{ARTICLE}

Write a list of the key facts in the text in order:

Example Output (LIST OF FACTS):
["1. ....", "2. ....",...,"10: ...."]

Here is a summary of the original text:

{SUMMARY}

Your task is to specify how many of those facts are NOT mentioned directly or indirectly by the summary.

Now write a list of the numbers of all the key facts that were not mentioned in the summary.

Example Output (LIST OF THE NUMBERS OF THE FACTS NOT COVERED):
["1", "9"]

Return the following:

{'FACT_LIST' : LIST OF FACTS GOES HERE, 'NOT_COVERED' : LIST OF THE NUMBERS OF THE FACTS NOT COVERED}

"""
}
