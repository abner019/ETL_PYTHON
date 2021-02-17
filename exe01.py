def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}');  # Press Ctrl+F8 to toggle the breakpoint.


def print_list():

    s = 'abner'

    print(s[::2]);

    for x in s:
     print(x);

def print_letr_n_vezes(vezes,letra):
    x = letra * vezes;
    print(x.upper());
    
def print_split(frase):
    x = frase;
    y = x.split();
    return y;

def print_busca_in(letra,frase):
    x = letra in frase;
    print(x);

def createPerson(nome,sobreNome,idade,Email):
    newPerson = {
        "nome" : nome,
        "sobreNome": sobreNome,
        "idade" : idade,
        "Email" : Email
    };

    newPersonList = [];

    newPersonList.append(newPerson);

    print(newPersonList);


def main():
    disciplina = input("Qual a Disciplina: ");
    prova1 = input("Digite a primeira nota: ");
    prova2 = input("Digite a segunda nota: ");
    media = (prova1 + prova2) / 2
    texto = 'Nota final de' + disciplina + ' = ' + media;
    print(texto);

