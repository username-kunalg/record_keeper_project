pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Define credentials id
                    def gitCredentialsId = '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'

                    // Checkout the master branch
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/kunal-tnc/record_keeper_project', credentialsId: gitCredentialsId]]])

                    // Checkout the staging branch
                    checkout([$class: 'GitSCM', branches: [[name: '*/staging']], userRemoteConfigs: [[url: 'https://github.com/kunal-tnc/record_keeper_project', credentialsId: gitCredentialsId]]])
                }
            }
        }

        stage('Deploy to Main Server') {
            when {
                branch 'master'
            }
            steps {
                echo 'Deploying to Main Server...'
                sh 'mvn clean package'
            }
        }

        stage('Deploy to Staging Server') {
            when {
                branch 'staging'
            }
            steps {
                echo 'Deploying to Staging Server...'
                sh 'mvn clean package'
            }
        }
    }
}
