pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop employee-app || true'
                sh 'docker rm employee-app || true'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name employee-app employee-management'
            }
        }
    }
}
