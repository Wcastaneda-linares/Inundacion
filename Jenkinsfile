pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Wcastaneda-linares/Inundacion.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Aquí puedes agregar comandos para construir tu proyecto
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Aquí puedes agregar comandos para ejecutar tus pruebas
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Aquí puedes agregar comandos para desplegar tu aplicación
            }
        }
    }
}
