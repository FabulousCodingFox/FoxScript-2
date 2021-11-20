from foxscript.CompUtils import Namespace,Function,removeUnnededLinesAndSpaces,extractNamespacesFromText
import os

def main(content):
    with open(os.path.dirname(os.path.abspath(__file__))+"\\config.json","r") as file: config=eval(file.read())
    #######################################################################################################################################################
    print("Deleting newlines and empty spaces")
    content=removeUnnededLinesAndSpaces(content)
    #######################################################################################################################################################
    print("Generating Namespaces")
    namespaces = extractNamespacesFromText(content)
    for i in namespaces:print(i.name,": ",i.rawcontent,sep="")
    #######################################################################################################################################################

if __name__=="__main__":
    main()
