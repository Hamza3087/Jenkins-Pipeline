pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Clone Repository') {
            steps {
                retry(3) {
                    timeout(time: 2, unit: 'MINUTES') {
                        git url: 'https://github.com/Hamza3087/Jenkins-Pipeline.git', branch: 'master'
                    }
                }
            }
        }
        stage('Set Up Python') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv || python -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install pytest
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install --upgrade pip
                            pip install pytest
                        '''
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            python -m unittest discover
                        '''
                    } else {
                        bat '''
                            venv\\Scripts\\activate
                            python -m unittest discover
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up virtual environment'
            script {
                if (isUnix()) {
                    sh 'deactivate || true'
                } else {
                    bat 'venv\\Scripts\\deactivate.bat || exit 0'
                }
            }
        }
        success {
            echo 'Build passed!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}