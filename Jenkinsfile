pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                git 'https://github.com/eldadtech/First_Project.git'
            }
        }
        stage ('build') {
            steps{
                bat 'python  main.py'
                
            }
        
        }
    }
}
