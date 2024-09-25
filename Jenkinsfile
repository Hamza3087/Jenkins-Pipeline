pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Set Up Python') {
            steps {
                // Set up Python and install dependencies
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install pytest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Run the unit tests
                sh '''
                source venv/bin/activate
                python -m unittest discover
                '''
            }
        }
    }
    post {
        always {
            // Cleanup
            echo 'Cleaning up virtual environment'
            sh 'deactivate'
        }
        success {
            echo 'Build passed!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

