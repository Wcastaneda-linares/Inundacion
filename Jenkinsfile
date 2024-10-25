pipeline {
    agent any

    environment {
        // Puedes definir variables de entorno aquí
        PYTHON_VERSION = '3.8' // Cambia esto según tu versión de Python
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git 'https://github.com/tu_usuario/tu_repositorio.git'
            }
        }
        stage('Setup Python') {
            steps {
                // Configura Python
                sh "pyenv install ${PYTHON_VERSION}"
                sh "pyenv global ${PYTHON_VERSION}"
            }
        }
        stage('Install Dependencies') {
            steps {
                // Instalar dependencias desde requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Ejecutar pruebas
                sh 'pytest'
            }
        }
        stage('Package') {
            steps {
                // Empaquetar la aplicación
                sh 'python setup.py sdist bdist_wheel'
            }
        }
    }

    post {
        success {
            // Acciones a realizar si la construcción es exitosa
            echo 'Construcción exitosa!'
        }
        failure {
            // Acciones a realizar si la construcción falla
            echo 'La construcción falló.'
        }
    }
}

