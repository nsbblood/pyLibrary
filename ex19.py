import textwrap

coolText= """ In summary, for straightforward use cases, dataclass is a good choice. 
For more complex scenarios where customization and control are required,
a regular class is preferable.  """

print("No dedent: ")
print(textwrap.fill(coolText))

print("Dedent")

