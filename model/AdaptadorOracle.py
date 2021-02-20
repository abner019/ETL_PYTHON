import cx_Oracle;
import xml.dom.minidom;



class AdaptadorOracle:

    def __int__(self):
        self.host = None;
        self.port = None;
        self.service = None;
        self.userName = None;
        self.pwd      = None;


    def setDataSource(self, dataSource):
        #recuperando arquivo de conexões
        connRepo = xml.dom.minidom.parse("./Arquivos/Adaptadores/conn.xml");
        #recuperando tag oracle do arquivo
        Olement = connRepo.getElementsByTagName("oracle");
        # fazendo loop na tag oracle
        for l_Olement in Olement:
            # recuperando tag filha datasource
            l_dataSourcet = l_Olement.getElementsByTagName("datasource");
            # fazendo loop na tag dataSource
            for element in l_dataSourcet:

                # Procurando propriedade
                if element.getAttribute('name') == dataSource:
                    self.host = element.getAttribute('host');
                    self.port = element.getAttribute('port');
                    self.service = element.getAttribute('service');
                    self.userName = element.getAttribute('userName');
                    self.pwd = element.getAttribute('pwd');

    def createConnect(self):
        l_connectionString = self.userName + "/" +  self.pwd + "@" + self.host + ":" + self.port + "/" + self.service;

        #connection = cx_Oracle.connect("TRITLOCAL/TRITLOCAL@localhost:1521/xe");
        connection = cx_Oracle.connect(l_connectionString);
        return connection;

    
