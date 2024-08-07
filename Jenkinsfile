pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Checking Python Version'
                bat 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                bat 'pytest .\\tests'
            }
        }
    }
}