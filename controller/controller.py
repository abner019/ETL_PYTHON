import xml.dom.minidom;
import tools.utils as utils;

def load(intefaceFile):
    #montando string do caminho + arquivo
    l_intefaceFile = "./Arquivos/interfaces/" + intefaceFile;
    #parse do documento
    etlDoc = xml.dom.minidom.parse(l_intefaceFile);
    #buscando tag object (N) vezes
    objectElement = etlDoc.getElementsByTagName("OBJECT");
    # buscando tag object (N) vezes
    for l_object in objectElement:
        print(l_object);
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
                    ### Buscando Attribute type da Tag COMAND
                    l_sourceCommType = l_ComandSourceElement.getAttribute("type");
                    ### Buscando Conteudo Tag COMAND
                    l_sourceCommand = utils.encode(utils.getText(l_ComandSourceElement.childNodes));
            except IndexError:
                l_sourceName = "";
                l_sourceType = "";
                l_sourceCommType = "";
                l_sourceCommand = "";
                pass;
    etlObj = {
        "order": l_order,
        "step_name": l_step_name,
        "source": {
            "name": l_sourceName,
            "type": l_sourceType,
            "comand": {
                "type": l_sourceCommType,
                "text": l_sourceCommand
            }
        }
    };
    print(etlObj);