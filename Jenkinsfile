pipeline{
    agent any 

    environment {
        PYTHON = 'C:\\Python311\\python.exe'
    }

    stages{
        stage ('checkout code'){
           steps {
            checkout scm
           } 
        }

        stage ('show python version'){
            steps {
            bat "${env.PYTHON} --version"
            }
        }

        stage ('run extract.py'){
            steps{
                bat "${env.PYTHON} extract.py"
            }
        }
    }
}