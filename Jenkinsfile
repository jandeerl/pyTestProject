pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                //checkout scm
                echo 'Building..'
                bat 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}