import textwrap

text = "This is a long text that needs to be wrapped to fit within a specific width. The textwrap module is helpful for this purpose."

wrapped_text = textwrap.wrap(text, width=40)

for line in wrapped_text:
    print(line)


