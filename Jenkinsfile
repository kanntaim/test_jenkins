pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                retry(3) {
                    bat 'set'
                }
            }
        }
    }
    post{
        always{
            echo 'This will always run'
        }
    }
}
