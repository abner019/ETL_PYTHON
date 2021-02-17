import xml.dom.minidom;
import base64;
import cx_Oracle;
import json
from types import SimpleNamespace

def main():
    cx_Oracle.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin")

    etlDoc = xml.dom.minidom.parse("C:/Users/abner/Desktop/XML_SOURCE_TARGET_PYTHON.xml")
    l_contador = 0;
    l_count = len(etlDoc.getElementsByTagName('OBJECT'));
    #print(etlDoc.toprettyxml());

    eltObjTmp= {
                  "order": "",
                  "source": {
                     "name": "",
                     "type": "",
                     "comand": {
                        "type": "",
                        "text": ""
                     }
                  },
                  "TARGET": {
                     "name": "",
                     "type": "",
                     "COMAND": {
                        "type": "",
                        "text": ""
                     }
                  }
               };
    etlList = [];



    for x in range(l_count):
        etlObj = {};
        ###Recuperando Nó

        ### Buscando Tag OBJECT
        objectElement = etlDoc.getElementsByTagName("OBJECT")[x];

        ### Buscando Attribute order da Tag OBJECT
        l_order = objectElement.getAttribute("order");
        l_step_name = objectElement.getAttribute("step_name");
        try:
            ### Buscando Tag SOURCE
            SourceElement = objectElement.getElementsByTagName("SOURCE")[0];
            ### Buscando Attribute name da Tag SOURCE
            l_sourceName = SourceElement.getAttribute("name");
            ### Buscando Attribute type da Tag SOURCE
            l_sourceType = SourceElement.getAttribute("type");
            ### Buscando Tag COMAND
            ComandSourceElement = SourceElement.getElementsByTagName("COMAND")[0];
            ### Buscando Attribute type da Tag COMAND
            l_sourceCommType = ComandSourceElement.getAttribute("type");
            ### Buscando Conteudo Tag COMAND
            l_sourceCommand = encode(getText(ComandSourceElement.childNodes));
        except IndexError:
            l_sourceName = "";
            l_sourceType = "";
            l_sourceCommType = "";
            l_sourceCommand = "";
            pass;

        try:
            TagetElement = objectElement.getElementsByTagName("TARGET")[0];
            l_TargeName = TagetElement.getAttribute("name");
            l_TargeType = TagetElement.getAttribute("type");
            ### Buscando Tag COMAND
            ComandTargetElement = TagetElement.getElementsByTagName("COMAND")[0];
            ### Buscando Attribute type da Tag COMAND
            l_TargeCommType = ComandTargetElement.getAttribute("type");
            ### Buscando Conteudo Tag COMAND
            l_TargetCommand = encode(getText(ComandTargetElement.childNodes));
        except IndexError:
            pass;

     #   print(SourceElement);
     #   print(TageElement);
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
            },
            "target": {
                "name": l_TargeName,
                "type": l_TargeType,
                "comand": {
                    "type": l_TargeCommType,
                    "text": l_TargetCommand
                }
            }
        };
        etlList.append(etlObj);

    l_procedure = True;
    l_index = 0;
    for l_list in etlList:
        l_index += 1;
        conv = convJsonToObj(l_list);

        try:
            if (conv.source.comand.type == 'SQL' and conv.source.type == 'ORACLE'):
                l_sql = decode(conv.source.comand.text);
                #print(l_sql.replace(",","||'^#^'||"))
                rs = executeOracleSqlComand(l_sql.replace(",","||'^#^'||")  ,  'SOURCE');
                #print(rs);
                if (conv.target.comand.type == 'SQL' and conv.target.type == 'ORACLE'):
                    l1_sql = "begin ";
                    for l_rs in rs:
                        conv_sql = decode(conv.target.comand.text);
                        l1_sql += conv_sql.replace("#VALUES#","('"+ l_rs.replace('^#^',"','").replace(',,',',null,') + "');");
                    l1_sql += "end;";
                    print(l1_sql);
                    executeOracleSqlComand(l1_sql, 'TARGET');
            elif (conv.target.comand.type == 'PLSQL' and conv.target.type == 'ORACLE' and l_procedure == True):

                conv_sql = decode(conv.target.comand.text);
                executeOracleSqlComand(conv_sql, 'TARGET');
            else:
                print("else");
            l_event_name = conv.step_name;
            L_STEP_LOG_ID = l_index;
            sql_erro = " BEGIN INSERT INTO XXAB_ETL_INT_LOG (PROCESS_ID, STEP_LOG_ID , event_name, status, message, creation_date)  VALUES (1,'"+str(L_STEP_LOG_ID) +"' ,'" + l_event_name + "' , 'SUCCESS', '' , SYSDATE);END;"
            executeOracleSqlComand(sql_erro, 'TARGET');

        except Exception as e:
            l_event_name = conv.step_name;
            l_message = str(e);
            sql_erro =" BEGIN INSERT INTO XXAB_ETL_INT_LOG (PROCESS_ID, STEP_LOG_ID , event_name, status, message, creation_date)  VALUES (1,'"+str(L_STEP_LOG_ID) +"' ,'"+ l_event_name+ "' , 'ERRROR', '"+l_message+"' , SYSDATE);END;";
            executeOracleSqlComand(sql_erro, 'TARGET');

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

def executeOracleSqlComand(command,sourceTarget):

    connection = cx_Oracle.connect("TRITLOCAL/TRITLOCAL@localhost:1521/xe");
    if sourceTarget == 'SOURCE':
        cur = connection.cursor();
        print(command);
        cur.execute(command);
        rs = [];
        for result in cur:
            rs.append(result[0]) ;
        cur.close();
        connection.commit();
        connection.close();
        return rs;
    elif sourceTarget == 'TARGET':
        cur = connection.cursor();
        print(command);
        cur.execute(command);
        connection.commit();
        connection.close();

def convJsonToObj(pJson):
    print(pJson);

    data = str(pJson).replace("'",'"');

    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    return x;