# Instruction for deploy JmeterAwsConf and JAC_UI under MacOS

1. brew if not installed

		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		
		
2. python3 if not installed

		brew install python3
	
	check version, must be 3.6.0, if not please reinstall python3 with brew
		
		python3 -V

3. virtualenv 

		python3 -m pip install virtualenv
		
	virtualenv must be installed under this python3
	
4. clone remote repo

		git clone git@github.com:1nfo/AWS_TEST.git
		
5. setup

		cd AWS_TEST
		python3 setup.py
		
6. config awscli  

	This step requires:
	1. ~/Jmeter\_test\_key\_pair.pem, 
	2. ~/.aws/config, 
	3. ~/.aws/credentials

6. run flask app

		python main.py
	
		
	