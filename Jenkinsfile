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
        input(message: 'Avan�ar', ok: 'Aprovado')
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}