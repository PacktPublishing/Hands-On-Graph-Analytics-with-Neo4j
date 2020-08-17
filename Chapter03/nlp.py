"""

Requirements:
-------------
spacy

Ussage:
-------

1. Download models:

    python -m spacy download en_core_web_sm

2. Run this script:

    python nlp.py

"""

import spacy

text = "Leonardo DiCaprio was born in Los Angeles."


nlp = spacy.load("en_core_web_sm")

document = nlp(text)

nodes = []
for k, ent in enumerate(document.ents):
    node = f"(n{k}:{ent.label_} {{name: '{ent.text}' }})"
    nodes.append(node)

rel = ""
for token in document:
    if token.pos_ == "VERB":
        rel = f"(n1)-[:{token.text.upper()}]-(n2)"

query = (
    "\n".join(["MATCH " + n for n in nodes])
    + "\nRETURN EXISTS(" + rel + ")"
)
print(query)


# svg = spacy.displacy.render(document, style="dep")
# with open("dep.svg", "w") as f:
#     f.write(svg)
