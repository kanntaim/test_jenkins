pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                retry(3) {
                    bat 'python -m pytest C:/Users/n.galeev/PycharmProjects/test_jenkins/pytest_rest_api/test/api_test.py --html=report.html'
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
