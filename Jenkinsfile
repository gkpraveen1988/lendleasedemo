node {
    def app
    def testbed 
    stage('checkout SCM') { 
        echo "CheckoutStage"
        checkout([$class: 'GitSCM', branches: [[name: "master"]],userRemoteConfigs: [[credentialsId: 'gitcred', url: 'https://github.com/gkpraveen1988/lendleasedemo.git']]])
    }

    stage ('Clean up env') {
    sh """
        cnt=\$(docker ps -a | grep mysqlserver | wc -l)
        if [ \$cnt -gt 0 ]
        then
        docker rm -f mysqlserver
        fi

        cnt=\$(docker ps -a | grep mypythonapp | wc -l)
        if [ \$cnt -gt 0 ]
        then
        docker rm -f mypythonapp
        fi

        cnt=\$(docker ps -a | grep mygrafana | wc -l)
        if [ \$cnt -gt 0 ]
        then
        docker rm -f mygrafana
        fi

        cnt=\$(docker ps -a | grep myprometheus | wc -l)
        if [ \$cnt -gt 0 ]
        then
        docker rm -f myprometheus
        fi

    """
    }

    stage('Build image') {         
        app = docker.build("praveen88/personalimages:myappnewtest_latest")    
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockercred') {            
        app.push()        
        }    
    }
    
    stage('Deploy Database') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockercred') {     
            testbed = docker.image('registry.hub.docker.com/praveen88/personalimages:mysqlserver_1.0')
            testbed.pull()
            testbed.run('-p 3306:3306 --name mysqlserver') 
        }    
    }

    stage('Run image') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockercred') {    
            docker.image('registry.hub.docker.com/praveen88/personalimages:myappnewtest_latest').run('-p 5000:5000 --name mypythonapp --link mysqlserver') 
        }    
    }

    stage('Run Grafana') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockercred') {
            def grafanaimg = docker.image('registry.hub.docker.com/praveen88/personalimages:mygrafana_1.0')
            grafanaimg.pull() // make sure
            grafanaimg.run('-p 3000:3000 --name mygrafana --link mysqlserver')
        }
    }    

    stage('Run Prometheus') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockercred') {
            def grafanaimg = docker.image('registry.hub.docker.com/praveen88/personalimages:myprometheus_1.0')
            grafanaimg.pull() // make sure
            grafanaimg.run('-p 9090:9090 --name myprometheus --link mygrafana')
        }
    }
    
     stage ('send notification') {
            slackSend baseUrl: 'https://hooks.slack.com/services/', 
            channel: '#jenkins-notification', 
            color: 'good', 
            message: "Job: ${env.JOB_NAME} with buildnumber ${env.BUILD_NUMBER}; console: ${BUILD_URL}console ",
            teamDomain: 'praveenlearning', 
            tokenCredentialId: 'slacknotification'
    }
}

