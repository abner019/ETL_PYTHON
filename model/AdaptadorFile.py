import xml.dom.minidom;
import csv;
import tools.utils as utils

class AdaptadorFile:
    def __init__(self):
        self.path = None;

    def createFile(self,datasource,fileName , prefix , delimiter ,obj):
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
        if self.path != None:
            l_unique_id = utils.getUniqueId();
            with open(self.path + fileName+ str(l_unique_id) +"." + prefix , 'w', newline='') as f:
                writer = csv.writer(f, delimiter=delimiter)
                writer.writerows(obj);