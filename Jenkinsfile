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
		
		stage('Run Docker Container') {
			steps {
				bat '''
					docker run -d --name docker_calsy_container docker_calsy
					ping 127.0.0.1 -n 6 > nul
					
					echo ===== Container Status =====
					docker ps -a
					
					echo ===== Container Logs =====
					docker logs docker_calsy_container
					
					echo ===== Container Exit Code =====
					docker inspect docker_calsy_container --format "{{.State.ExitCode}}"
					
					echo ===== Checking application exit codee =====
					for /f %%i in ('docker inspect docker_calsy_container --format "{{.State.ExitCode}}"') do set EXIT_CODE=%%i

					echo Application Exit Code: %EXIT_CODE%

						if not "%EXIT_CODE%"=="0" (
						echo ERROR: Application failed inside Docker container!
						exit /b 1
						)

            echo Application completed successfully.
        '''
				}
		}

	}

	post {
		always {
			bat 'docker rm -f docker_calsy_container'
		}
	}

}