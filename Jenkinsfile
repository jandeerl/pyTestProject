pipeline {
    agent any
    environment {
         PATH = "C:/Users/pc/AppData/Local/Programs/Python/Python310/;$PATH"
    }

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