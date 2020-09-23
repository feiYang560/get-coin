Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker 'python:3.7.6' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
