from foxscript.CompUtils import Namespace,Function,removeUnnededLinesAndSpaces,extractNamespacesFromText,extractFunctionsFromText,genDatapackFromNamespaces
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
    print("Generating Functions")
    for namespace in namespaces:
        namespace.functions = extractFunctionsFromText(namespace.rawcontent)
        for i in namespace.functions:print(i.name,": ",i.rawcontent,sep="")
    #######################################################################################################################################################
    print("GenDatapack")
    genDatapackFromNamespaces(namespaces)

if __name__=="__main__":
    main()
