pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/abner019/ETL_PYTHON.git', changelog: true)
        sh 'ls -l'
      }
    }

    stage('deploy_dev') {
      steps {
        echo 'Publicando em QA'
      }
    }

    stage('Aprovado em Dev?') {
      steps {
        input(message: 'AvanÃ§ar', ok: 'Aprovado')
      }
    }

    stage('Deploy_qa') {
      steps {
        echo 'Publicando QA'
      }
    }

    stage('Aprovado QA?') {
      steps {
        input(message: 'Aprovado?', ok: 'Aprovado')
      }
    }

    stage('Liberar Produção?') {
      steps {
        echo 'xx'
      }
    }

    stage('Deploy_Produção') {
      steps {
        echo 'Deploye Prod'
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}