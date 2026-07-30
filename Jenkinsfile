pipeline {
    agent any

    environment {
        IMAGE_NAME = "oviyamuralidharan/employee-management:latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh 'docker tag employee-management:latest $IMAGE_NAME'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
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