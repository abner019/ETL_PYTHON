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
        input(message: 'Avançar', ok: 'Aprovado')
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

    stage('Liberar Produ��o?') {
      steps {
        echo 'xx'
      }
    }

    stage('Deploy_Produ��o') {
      steps {
        echo 'Deploye Prod'
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}