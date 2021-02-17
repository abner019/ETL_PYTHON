# ELT-Py
> ELT Python é um software de código aberto para a communidade, desenvolvido em python. Tem comomo objetivo ser uma ferramenta pratica 
> de desenvolver ETL (Extraction, Load, Transformation) e de baixo busto. A fim de freelancers e pequenas utilizarem em seus projetos.

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

 ELT Python é um software de código aberto para a communidade, desenvolvido em python. Tem comomo objetivo ser uma ferramenta pratica 
 de desenvolver ETL (Extraction, Load, Transformation) e de baixo busto. A fim de freelancers e pequenas utilizarem em seus projetos.


![](header.png)

## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```

## Usage example

Projeto atual não existe interface grafica, apenas o processamento logico do Xml, as descrições abaixo descrevem o padrão e a logica do processamento.
```sh
  <ETL/> é a Tag root do arquivo
      #event_name -> Attributo identificador da interface ou job que esta processando
      * <OBJECT/> é Tag filha, responsavel pelo processamento de cada passo no fluxo da execução
          #order -> Attributo que diz a ordem de execução 
          #step_name -> Attributo que identifica o passo que esta em execução 
          * <SOURCE/> é Tag filha do objeto, responsavel em direcionar a conexão da origem de dados
            #name -> Attributo que diz a origem dos dados
            #type -> Attributo que diz qual a tecnologia
            * <COMAND/> é tag filha do source, responsavel por dizer o tipo do comando a ser executado e o codigo do comando
              #type -> Attributo que diz qual o tipo da instrução ou comando 
              @Text@ -> Conteudo da tag é o codigo que será executado.  
          * <TARGET/> é Tag filha do objeto, responsavel em direcionar a conexão da destino de dados
            #name -> Attributo que diz a origem dos dados
            #type -> Attributo que diz qual a tecnologia
            * <COMAND/> é tag filha do TARGET, responsavel por dizer o tipo do comando a ser executado e o codigo do comando
              #type -> Attributo que diz qual o tipo da instrução ou comando 
              @Text@ -> Conteudo da tag é o codigo que será executado.
```

```xml
<ETL event_name = 'xxab.event.name.demo'>
	<OBJECT order="0" step_name = 'SELECT_INSERT_STG_DEPARTMENTS'>
		<SOURCE name='XE_ORIGEM' type="ORACLE">
			<COMAND type='SQL'>SELECT department_id, department_name, manager_id, location_id FROM DEPARTMENTS</COMAND>
		</SOURCE>
		<TARGET name='XE_ORIGEM' type="ORACLE">
			<COMAND type='SQL'>INSERT INTO STG_DEPARTMENTS (department_id, department_name, manager_id, location_id) VALUES #VALUES#</COMAND>
		</TARGET>
	</OBJECT>
</ETL>
```


_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.0.1
    * Criação do adaptador de banco de dados Oracle
    * Criação do Interpretador arquivo XML 
    * Inicio do Projeto
  
## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki