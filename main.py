# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for model, files, tool windows, actions, and settings.

import xmlProcess;
import model.AdaptadorOracle as oracle;
import controller.controller as ctrl;

if __name__ == '__main__':
    #xmlProcess.main();

#    adapOracle = oracle.AdaptadorOracle();
#    adapOracle.setDataSource(dataSource="XE");
#    conn = adapOracle.createConnect();
#    print(conn);

    ctrl.load("xxab_etl_load_departments.xml");
