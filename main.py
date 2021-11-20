import foxscript.comp
import os
with open(os.path.dirname(os.path.abspath(__file__))+"\\project.fscript","r") as file:content = file.read()
foxscript.comp.main(content)
