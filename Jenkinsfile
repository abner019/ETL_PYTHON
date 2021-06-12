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
          env.TAG_ON_DOCKER_HUB = input message: 'User input required',
              parameters: [choice(name: 'Tag on Docker Hub', choices: 'no\nyes', description: 'Choose "yes" if you want to deploy this build')]
        }
    }

  }
  environment {
    ENV = 'DEV'
  }
}
 
