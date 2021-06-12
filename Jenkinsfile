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
      {
        script {

        }
    }

  }
  environment {
    ENV = 'DEV'
  }
}
 
