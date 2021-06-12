pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/abner019/ETL_PYTHON.git', changelog: true)
        sh 'ls -l'
      }
    }

    stage('SendQA') {
      steps {
        input(message: 'SendTo QA', ok: 'Approve')
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}