# Instruction for deploy JmeterAwsConf and JAC_UI under MacOS

		
6. First make you have correct credential files in the right directory (which is $HOME directory) of your system

	They are:
	1. $HOME/Jmeter\_test\_key\_pair.pem, 
	2. $HOME/.aws/config, 
	3. $HOME/.aws/credentials

1. install brew if it is not

		/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
		
		
2. python3 if not installed

		brew install python3
	
	check version, must be 3.6.0, if not please reinstall python3 with brew
		
		python3 -V

3. virtualenv 

		python3 -m pip install virtualenv
		
	virtualenv must be installed under this python3
	
4. clone remote repo

		git clone https://github.pydt.lan/szhao/AWS_TEST.git
		
5. setup

		cd AWS_TEST
		python3 setup.py

	
		
	
