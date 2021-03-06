import xml.dom.minidom;
import tools.utils as utils;
import cx_Oracle;
import controller.Mapping as op;

# Iniciar componentes
def init():
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin");


def loadInterface(intefaceFile):
    #montando string do caminho + arquivo
    l_intefaceFile = "./Arquivos/interfaces/" + intefaceFile;
    #parse do documento
    etlDoc = xml.dom.minidom.parse(l_intefaceFile);

    l_eventName = intefaceFile.replace(".xml","");
    #obj
    etlObj = {};
    #list
    etlList = [];
    #buscando tag object (N) vezes
    objectElement = etlDoc.getElementsByTagName("OBJECT");
    # buscando tag object (N) vezes

    for l_object in objectElement:

        l_sourceName = "";
        l_sourceType = "";
        l_sourceCommType = "";
        l_sourceCommand = "";
        l_targetName = "";
        l_targetType = "";
        l_targetCommType = "";
        l_targetCommand = "";

        #buscando atrributo order
        l_order = l_object.getAttribute("order");
        # buscando atrributo step_name
        l_step_name = l_object.getAttribute("step_name");
        #buscando tag SOURCE
        sourceObject = l_object.getElementsByTagName("SOURCE");
        for l_source in sourceObject:
            try:

                ### Buscando Attribute name da Tag SOURCE
                l_sourceName = l_source.getAttribute("name");
                ### Buscando Attribute type da Tag SOURCE
                l_sourceType = l_source.getAttribute("type");
                ### Buscando Tag COMAND
                ComandSourceElement = l_source.getElementsByTagName("COMAND");

                for l_ComandSourceElement in ComandSourceElement:
                    ### Buscando Attribute name da Tag COMAND
                    l_sourceCommName = l_ComandSourceElement.getAttribute("name");
                    ### Buscando Attribute prefix da Tag COMAND
                    l_sourceCommPrefix = l_ComandSourceElement.getAttribute("prefix");
                    ### Buscando Attribute type da Tag COMAND
                    l_sourceCommType = l_ComandSourceElement.getAttribute("type");
                    ### Buscando Conteudo Tag COMAND
                    l_sourceCommand = utils.encode(utils.getText(l_ComandSourceElement.childNodes));
            except IndexError:
                l_sourceName = "";
                l_sourceCommPrefix = "";
                l_sourceType = "";
                l_sourceCommName = ""
                l_sourceCommType = "";
                l_sourceCommand = "";
                pass;

        targetObject = l_object.getElementsByTagName("TARGET");
        for l_target in targetObject:
            try:

                ### Buscando Attribute name da Tag TARGET
                l_targetName = l_target.getAttribute("name");
                ### Buscando Attribute type da Tag TARGET
                l_targetType = l_target.getAttribute("type");
                ### Buscando Tag COMAND
                ComandTargetElement = l_target.getElementsByTagName("COMAND");

                for l_ComandTargetElement in ComandTargetElement:
                    ### Buscando Attribute name da Tag COMAND
                    l_targetCommName = l_ComandTargetElement.getAttribute("name");
                    ### Buscando Attribute name da Tag COMAND
                    l_TargetCommPrefix = l_ComandTargetElement.getAttribute("prefix");
                    ### Buscando Attribute type da Tag COMAND
                    l_targetCommType = l_ComandTargetElement.getAttribute("type");
                    ### Buscando Attribute l_delimiter da Tag COMAND
                    l_TargetDelimiter = l_ComandTargetElement.getAttribute("delimiter");
                    ### Buscando Conteudo Tag COMAND
                    l_targetCommand = utils.encode(utils.getText(l_ComandTargetElement.childNodes));
            except IndexError:
                l_targetName = "";
                l_TargetCommPrefix = "";
                l_targetType = "";
                l_targetCommType = "";
                l_targetCommand = "";
                l_targetCommName = ""
                l_TargetDelimiter = ""

        etlObj = {
            "eventName": l_eventName,
            "order": int(l_order),
            "step_name": l_step_name,
            "source": {
                "name": l_sourceName,
                "type": l_sourceType,
                "comand": {
                    "name": l_sourceCommName,
                    "prefix" : l_sourceCommPrefix,
                    "type": l_sourceCommType,
                    "text": l_sourceCommand
                }
            },
            "target": {
                "name": l_targetName,
                "type": l_targetType,
                "comand": {
                    "name": l_targetCommName,
                    "prefix": l_TargetCommPrefix,
                    "delimiter": l_TargetDelimiter,
                    "type": l_targetCommType,
                    "text": l_targetCommand
                }
            }
        };

        etlList.append(etlObj)

    return etlList;

def ExecuteInterface(obj):
    etlList = utils.getOrderInterfaceProcess(obj);
    l_index = 0;
    for l_list in etlList:
        l_index += 1;
        conv = utils.convJsonToObj(l_list);

        if(conv.source.comand.type == "SQL" and conv.target.comand.type =="SQL"):
            op.SqlToSql(conv);
        elif(conv.source.comand.type == "SQL" and conv.target.comand.type == "FILE") :
            op.SqlToFile(conv);
        else:
            print(conv);
            print("pass");


def endOf():
    pass;

def intefaceMainProcess(name):
    #
    init();
    #
    etlList = loadInterface(name);
    #
    ExecuteInterface(etlList);


