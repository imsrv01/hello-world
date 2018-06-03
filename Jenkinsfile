pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'Building code'
          }
        }
        stage('') {
          steps {
            echo 'Building step'
          }
        }
      }
    }
  }
}