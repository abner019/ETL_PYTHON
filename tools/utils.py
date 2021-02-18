import xml.dom.minidom;
import base64;
import json
from types import SimpleNamespace

def convJsonToObj(pJson):
    print(pJson);

    data = str(pJson).replace("'",'"');

    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    return x;

def encode(string):

    message_bytes = string.encode('utf-8');

    base64_bytes = base64.b64encode(message_bytes);

    return base64_bytes.decode('utf-8');

def decode(string):
    base64_message = string
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    return message ;

def getText(nodelist):
    # Iterate all Nodes aggregate TEXT_NODE
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
        else:
            # Recursive
            rc.append(getText(node.childNodes))
    return ''.join(rc)
#Recupera a chave para ordernar no def getOrderInterfaceProcess
def getOrder(obj):
    return obj['order'];
#Ordena
def getOrderInterfaceProcess(obj):
    my_object = obj;
    my_object.sort(key=getOrder);
    return my_object;
