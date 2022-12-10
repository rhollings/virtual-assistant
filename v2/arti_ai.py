# Make AI more conversational <--- 

import sys


sys.path.insert(0, '/Users/rod/Code/Python3/virtual-assistant/funcs')

from wolfram import to_respond

question = "what color is the sky"

print(to_respond(question))