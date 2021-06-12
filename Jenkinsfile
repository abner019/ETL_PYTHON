pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/cabral85/udemy-handson-deploy.git', changelog: true)
        sh 'cp . /data'
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}