pipeline {
    agent any

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
                bat 'docker build -t docker_calsy .'
            }
        }
		
        stage('Test Docker Image') {
            steps {
                bat 'docker run --rm docker_calsy --test'
            }
        }
	}

}