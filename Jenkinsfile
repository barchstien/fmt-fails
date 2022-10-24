pipeline {
    agent { label 'gcc-cmake-conan-git' }
    
    stages {
        stage('Prepare') {
            steps {
                echo "node: ${env.NODE_NAME} | workspace: ${env.WORKSPACE}"
                echo "branch_name: ${env.BRANCH_NAME}"
            }
        }
        stage('Build') {
            steps {
                sh "rm -rf build && conan install -if build . && conan build -bf build ."
            }
        }
    }
}

