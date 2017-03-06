import os


envName = "jac-env"
envPath = os.getcwd()+"/"+envName
lib = os.popen("./%s/bin/python -c 'from distutils.sysconfig import get_python_lib as a;print(a())'"%(envName)).read().replace("\n","")

JAC_UI_REPO = "https://github.pydt.lan/szhao/JAC_UI.git"

JmeterAwsConf_REPO = "https://github.pydt.lan/szhao/JmeterAwsConf.git"

os.system("python3 -m virtualenv %s"%envName)

a ='''
alias update='cd %s/JmeterAwsConf/ && git pull; cd %s/JAC_UI/ && git pull;'
alias syn='rm -r %s/JmeterAwsConf/*;rsync -a --exclude=".*" %s/../JmeterAwsConf/src/ %s/JmeterAwsConf ; update'
alias run='cd %s/JAC_UI && python main.py'

syn
echo 'type run to start server'
'''%(os.getcwd(),os.getcwd(),lib,envPath,lib,os.getcwd())

os.system("echo \"%s\" >> %s/bin/activate"%(a,envPath))

os.system("mkdir %s/lib/python3.6/site-packages/JmeterAwsConf"%envPath)

os.system("touch %s/lib/python3.6/site-packages/JmeterAwsConf/_"%envPath)

os.system("awk '!/^alias jacenv=/{print}' ~/.profile > .tmp_profile")

os.system("cat .tmp_profile > ~/.profile")

os.system("echo 'alias jacenv=\"source %s/bin/activate\"' >> ~/.profile"%envPath)

os.system("git clone %s"%JAC_UI_REPO)

os.system("git clone %s"%JmeterAwsConf_REPO)

os.system("%s/bin/pip install boto3 paramiko awscli "%envPath)

os.system("%s/bin/pip install flask flask_socketio eventlet"%envPath)

os.system("source ~/.profile ; echo '' ; echo 'Done. Type jacenv to start virtualenv'")
