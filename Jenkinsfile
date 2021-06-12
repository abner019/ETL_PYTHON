pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git(url: 'https://github.com/abner019/ETL_PYTHON', changelog: true)
        sh 'cp . /data'
      }
    }

  }
  environment {
    ENV = 'DEV'
  }
}
