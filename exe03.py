def somaFunc(p_x,p_y):
    l_soma = p_x + p_y;
    return l_soma;

def subtracao(p_x , p_y):
    l_subtracao = p_x - p_y;
    return l_subtracao;

def divisaoFunc(p_x , p_y):
    l_divisao = p_x / p_y;
    return l_divisao;

def multiplicacaoFunc(p_x , p_y):
    multp = (p_x*p_y);
    return multp;

def mainProc():
    l_resultadoc = 0;
    print("Calculadora 2021");
    print("Informações");
    print("1 - Soma");
    print("2 - Subtracao");
    print("3 - Divisao");
    print("4 - Multiplicacao");
    l_operacao = int(input("Digite a operacao: "));
    l_x = int(input("Digite o primeiro numero: "));
    l_y = int(input("Digite o segundo numero: "));

    if l_operacao == 1:
      l_resultado =  somaFunc(l_x,l_y);
    elif l_operacao == 2 :
        l_resultado = subtracao(l_x,l_y);
    elif l_operacao == 3 :
        l_resultado = divisaoFunc(l_x,l_y);
    elif l_operacao == 4 :
        l_resultado = multiplicacaoFunc(l_x,l_y);
    else:
        print("Operacao invalida!");
    print( int(l_resultado));