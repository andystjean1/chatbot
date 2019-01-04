import get_transcript as gt
import nltk
import re

script = gt.get_scripts()

sentences = nltk.sent_tokenize(script)

greetings = [s for s in sentences if re.match(r'hey', s)]

print(*greetings, sep="\n")
