import model.AdaptadorOracle;
import tools.utils as utils

def SqlToSql(obj):

    print(obj.source.type);

    #Source
    if ( obj.source.type == "ORACLE"):
        #Pega query que esta em base 64, faz decode
        l_sql = utils.decode(obj.source.comand.text);
        #Troca , por
        #l_sql.replace(",","||'^#^'||") ;

        l_tmp_table = ("TMP" + utils.getUniqueId() + str(obj.order) ).upper();
        l_sql = "CREATE TABLE SELECT * FROM (" + l_sql + ") "

        print(l_tmp_table);

def SqlToFile(obj):
    pass;

def FileToSql(obj):
    pass;

def FileToFile(pbj):
    pass;