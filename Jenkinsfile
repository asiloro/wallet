pipeline {
    agent any
    stages {
        
        stage('Build') {
            
            steps {
                echo 'building the app'
                bat ('docker build -t walletjenkins .')                
            }
        }
        
        stage('test') {
            
            steps {
                echo 'Testing the app'
                bat ('docker run walletjenkins ')
            }
        }    
   }
