Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { docker { image 'python3' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}
