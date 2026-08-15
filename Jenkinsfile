pipeline {
    agent any

    environment {
        IMAGE_NAME = "docker_calsy"
        DOCKER_REPO = "rajpatil479/docker-calsy-jenkins"
    }

    stages {

        stage('Check Environment') {
            steps {
                bat 'where java'
                bat 'where python'
                bat 'where docker'
            }
        }

        stage('Test Calculator') {
            steps {
                bat 'python calsy_for_jenkins_test.py --test'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:build-%BUILD_NUMBER% .'
            }
        }

        stage('Test Docker Image') {
            steps {
                bat 'docker run --rm %IMAGE_NAME%:build-%BUILD_NUMBER% --test'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_TOKEN'
                    )
                ]) {
                    bat 'echo %DOCKER_TOKEN% | docker login -u %DOCKER_USER% --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker tag %IMAGE_NAME%:build-%BUILD_NUMBER% %DOCKER_REPO%:build-%BUILD_NUMBER%'
                bat 'docker tag %IMAGE_NAME%:build-%BUILD_NUMBER% %DOCKER_REPO%:latest'

                bat 'docker push %DOCKER_REPO%:build-%BUILD_NUMBER%'
                bat 'docker push %DOCKER_REPO%:latest'
            }
        }
    }

    post {
        always {
            bat 'docker logout'
        }
    }
}