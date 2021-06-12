node{
	stage('Pull'){
		git url: 'https://github.com/abner019/ETL_PYTHON.git'
	}
	stage('Build'){
		sh "/u01/maven/bin/mvn clean package -DskipTests"
	}
	stage('Move'){
		sh "cp -rf target/testeweb.war /data"
	}
	stage('Deploy'){
		sh "/u01/send_curl_deploy.sh"
	}
}
