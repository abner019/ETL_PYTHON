pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/abner019/ETL_PYTHON.git', changelog: true)
        sh '''cd /data
ls -l'''
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}