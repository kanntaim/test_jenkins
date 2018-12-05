pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                retry(3) {
                    python 'C:\Users\n.galeev\PycharmProjects\test_jenkins\pytest_rest_api\api_test.py'
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
