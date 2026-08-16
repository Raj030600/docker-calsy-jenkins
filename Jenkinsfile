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

        stage('Test Docker API') {
			steps {
				bat '''
				echo ===== Starting Test API Container =====

				docker rm -f calsy-api-test 2>nul || echo No existing test container

				docker run -d --name calsy-api-test -p 5001:8080 %IMAGE_NAME%:build-%BUILD_NUMBER%

				echo ===== Waiting for Flask API =====
				ping 127.0.0.1 -n 6 >nul

				echo ===== Testing API =====
				curl.exe -f "http://localhost:5001/calculate?a=10&b=2&op=*" 

				echo.
				echo ===== API Test Successful =====

				docker rm -f calsy-api-test
				'''
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
		
		stage('Deploy API') {
			steps {
				bat '''
				echo ===== Deploying Calculator API =====

				docker rm -f calsy-api 2>nul || echo No existing container found

				docker pull %DOCKER_REPO%:latest

				docker run -d --name calsy-api -p 5000:8080 %DOCKER_REPO%:latest

				echo ===== Deployment Started =====
				docker ps
				'''
			}
		}
    }

    post {
        always {
            bat 'docker logout'
        }
    }
}