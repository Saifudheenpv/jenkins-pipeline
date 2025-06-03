pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                bat 'venv\\Scripts\\activate.bat && flake8 app.py test_app.py'
            }
        }
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\activate.bat && pytest'
            }
        }
    }
    post {
        always {
            bat 'venv\\Scripts\\deactivate.bat || exit 0'
        }
    }
}