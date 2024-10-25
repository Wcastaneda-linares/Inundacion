pipeline {
    agent { label 'master' }

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git 'https://github.com/tu_usuario/tu_repositorio.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Instalar dependencias
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecutar pruebas
                sh 'pytest tests/'  // Asumiendo que tus pruebas están en un directorio llamado tests
            }
        }

        stage('Build Application') {
            steps {
                // Aquí puedes agregar comandos para construir tu aplicación, si es necesario
                echo "Construyendo la aplicación..."
            }
        }

        stage('Create Docker Image') {
            steps {
                // Crear una imagen de Docker
                sh 'docker build -t tu_imagen_docker .'
            }
        }
        
        stage('Deploy') {
            steps {
                // Desplegar la aplicación (esto puede variar dependiendo de tu entorno de despliegue)
                echo "Desplegando la aplicación..."
            }
        }
    }
}
