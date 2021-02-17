# D:\OneDrive\ONEDRIVE_FULL\BACKUP\OneDrive_Fatec\Documentação oficial\TREINAMENTO DSA\PYTHON_FUNDAMENTOS\PythonFundamentos\Cap04\Notebooks\arquivos


def mainProc():
    #abrindo o arquivo
    ar1 = open("C:/Users/abner/Desktop/arquivos/arquivo1.txt",'r');
    #Lendo o conteudo
    print(ar1.read());
    #Contando Caracteres
    print(ar1.tell());
    #Retornar ao inicio do arquivo
    print(ar1.seek(0,0));
    #Ler os 10 primeiro caracteres
    print(ar1.read(10));

