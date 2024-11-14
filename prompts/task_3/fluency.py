prompts = {
    "1": """\
Your job is to evaluate a summariser chatbot. The chatbot takes articles and summarises their contents into shorter, punchier highlights.

Here is a summary of the original text:

{SUMMARY}

Your task is to list spelling mistake, grammatical error or punctuation error present in the text:

Return them in a list such as:

["wakled", "he was went"]

Otherwise return: NONE
"""
}
