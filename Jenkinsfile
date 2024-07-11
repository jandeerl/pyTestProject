pipeline {
    agent any
    environment {
         PATH = "C:/Users/pc/AppData/Local/Programs/Python/Python310/;C:/Users/pc/AppData/Local/Programs/Python/Python310/Scripts/;$PATH"
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
                bat 'python3 -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}