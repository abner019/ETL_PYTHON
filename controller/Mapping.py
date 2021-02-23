import model.AdaptadorOracle as oracle;
import model.AdaptadorFile as file;
import tools.utils as utils


def SqlToSql(obj):

    g_rs = "";
    #Source
    if ( obj.source.type == "ORACLE"):
        #Pega query que esta em base 64, faz decode
        l_sql = utils.decode(obj.source.comand.text);

       #l_tmp_table = ("TMP" + utils.getUniqueId() + str(obj.order) ).upper();
        #l_sql = "CREATE TABLE " + l_tmp_table + " as  SELECT * FROM (" + l_sql + ") "
        l_dataSource = obj.source.name;
        g_rs =  executeOracleSelectComand(l_dataSource,l_sql);

    if (obj.target.type == "ORACLE"):
        l_sql = utils.decode(obj.target.comand.text);
        l_dataSource = obj.target.name;
        executeOracleBlockComand(l_dataSource, l_sql, g_rs);

def SqlToFile(obj):
    g_rs = "";
    if ( obj.source.type == "ORACLE"):
        #Pega query que esta em base 64, faz decode
        l_sql = utils.decode(obj.source.comand.text);
       #l_tmp_table = ("TMP" + utils.getUniqueId() + str(obj.order) ).upper();
        #l_sql = "CREATE TABLE " + l_tmp_table + " as  SELECT * FROM (" + l_sql + ") "
        l_dataSource = obj.source.name;
        g_rs =  executeOracleSelectComand(l_dataSource,l_sql);
        print(g_rs);

    if (obj.target.type == "FILE"):

        #Pega o data source para saber o local do arquivo parametrizado
        l_dataSource = obj.target.name
        #Nome do arquivo que vai ser gerado no diretorio
        l_fileName = obj.target.comand.name
        #prefixo que o arquivo vai ser gerado
        l_prefix = obj.target.comand.prefix
        #Busca demilitador do arquivo
        l_delimiter = obj.target.comand.delimiter
        #instancia objeto
        fl = file.AdaptadorFile();
        # Cria arquivo
        fl.createFile(l_dataSource, l_fileName,l_prefix, l_delimiter ,  g_rs);



def FileToSql(obj):
    pass;

def FileToFile(pbj):
    pass;








def executeOracleSelectComand(dataSource, command):
    conn = oracle.AdaptadorOracle();
    conn.setDataSource(dataSource);
    connection = conn.createConnect();
    cur = connection.cursor();
    cur.execute(command);
    rs = [];
    for result in cur:
        rs.append(result);
    cur.close();
    connection.commit();
    connection.close();
    return rs;

def executeOracleBlockComand(dataSource, command,dataBinding):
    conn = oracle.AdaptadorOracle();
    conn.setDataSource(dataSource);
    connection = conn.createConnect();
    cur = connection.cursor();
    cur.executemany(command, dataBinding );
    connection.commit();
    connection.close();


