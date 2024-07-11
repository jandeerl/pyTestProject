pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                PATH = "C:\Users\pc\AppData\Local\Programs\Python\Python310\;$PATH"
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