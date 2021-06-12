pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/abner019/ETL_PYTHON.git', changelog: true)
        sh 'ls -l'
      }
    }

    stage('') {
      steps {
        input(message: 'QA?', id: '2', submitter: 'XXSYB', submitterParameter: 'SSUB')
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}