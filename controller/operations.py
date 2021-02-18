import model.AdaptadorOracle as oracle;
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
        executeOracleBlockComand(l_dataSource, l_sql, g_rs)

def SqlToFile(obj):
    pass;

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
    conn.setDataSource("XE");
    connection = conn.createConnect();
    cur = connection.cursor();
    cur.executemany(command, dataBinding );
    connection.commit();
    connection.close();


