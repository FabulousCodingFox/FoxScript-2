with open("C:/Users/fabif/Desktop/FoxScriptV2/foxscript/config.json") as file: config=eval(file.read())

class Namespace:
    def __init__(self,name) -> None:
        self.name=name
        self.functions=[]
        self.rawcontent=""

class Function:
    def __init__(self,name) -> None:
        self.name=name
        self.rawcontent=""

def removeUnnededLinesAndSpaces(txt):
    instr=False;newtxt=[]
    for chrnum,chr in enumerate(list(txt)):
        if chr=="\"":instr = not instr
        if instr:newtxt.append(chr)
        elif chr!=" " and chr!="\n":newtxt.append(chr)
        elif chr==" " and txt[chrnum-len(config["Keywords"]["class"]):chrnum]==config["Keywords"]["class"]:newtxt.append(chr)
        elif chr==" " and txt[chrnum-len(config["Keywords"]["function"]):chrnum]==config["Keywords"]["function"]:newtxt.append(chr)
    return "".join(newtxt)

def extractNamespacesFromText(txt):
    startindex=0
    stopindex=0
    startintendation=0
    indent=0
    namespaces=[]

    for chrnum,chr in enumerate(list(txt)):

        if txt[chrnum:].startswith(config["Keywords"]["class"]):
            startintendation = indent
            startindex = chrnum

        if chr=="{":indent+=1
        if chr=="}":
            indent-=1
            if indent==startintendation:
                stopindex = chrnum

                cont=txt[startindex:stopindex]
                firstbracketindex=min([charn if char=="{" else 1000 for charn,char in enumerate(list(cont))])

                namespaces.append(Namespace(txt[startindex:stopindex][len(config["Keywords"]["class"])+1:firstbracketindex]))
                namespaces[-1].rawcontent = txt[startindex+firstbracketindex+1:stopindex]
    
    return namespaces



def extractFunctionsFromText(txt):
    startindex=0
    stopindex=0
    startintendation=0
    indent=0
    functions=[]

    for chrnum,chr in enumerate(list(txt)):

        if txt[chrnum:].startswith(config["Keywords"]["function"]):
            startintendation = indent
            startindex = chrnum

        if chr=="{":indent+=1
        if chr=="}":
            indent-=1
            if indent==startintendation:
                stopindex = chrnum

                cont=txt[startindex:stopindex]
                firstbracketindex=min([charn if char=="{" else 1000 for charn,char in enumerate(list(cont))])

                functions.append(Function(txt[startindex:stopindex][len(config["Keywords"]["function"])+1:firstbracketindex]))
                functions[-1].rawcontent = txt[startindex+firstbracketindex+1:stopindex]
    
    return functions

def genDatapackFromNamespaces(namespaces):
    pass
    