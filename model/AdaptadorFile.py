import xml.dom.minidom;

class AdaptadorFile:
    def __init__(self):
        self.path = "";



    def setFileDataSource(self,datasource):
        #recuperando arquivo de conexões
        connRepo = xml.dom.minidom.parse("./Arquivos/Adaptadores/conn.xml");
        #recuperando tag oracle do arquivo
        Olement = connRepo.getElementsByTagName("file");
        # fazendo loop na tag oracle
        for l_Olement in Olement:
            # recuperando tag filha datasource
            l_dataSourcet = l_Olement.getElementsByTagName("datasource");
            # fazendo loop na tag dataSource
            for element in l_dataSourcet:
                if element.getAttribute('name') == datasource:
                    self.path = element.getAttribute('path');


    def getPath(self):
        return self.path;