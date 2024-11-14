prompts = {
    "1": """\
Here's the text:
{TEXT}

I expect there to be THREE numerical types in this data:

i) Currency amounts
ii) Dates
iii) Numbers

Your task is to look over the text and return a python dictionary of every numerical instance sorted into the appropriate types:

EXAMPLE OUTPUT:

{'currency_amounts' : ["£10.22"],
 'dates' : [18th Nov 2043, 01/02/02],
 'numbers' : [1,300, 1.22]}\
"""
}
