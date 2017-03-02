import os

envName = "jac-env"
envPath = os.getcwd()+"/"+envName

JAC_UI_REPO = "git@github.pydt.lan:szhao/JAC_UI.git"

JmeterAwsConf_REPO = "git@github.pydt.lan:szhao/JmeterAwsConf.git"

os.system("python3 -m virtualenv %s"%envName)
a ='''
alias syn='rm -r %s/lib/python3.6/site-packages/JmeterAwsConf/*;rsync -a --exclude=".*" %s/../JmeterAwsConf/src/ %s/lib/python3.6/site-packages/JmeterAwsConf'
syn
'''%(envPath,envPath,envPath)
os.system("echo \"%s\" >> %s/bin/activate"%(a,envPath))

os.system("mkdir %s/lib/python3.6/site-packages/JmeterAwsConf"%envPath)

os.system("touch %s/lib/python3.6/site-packages/JmeterAwsConf/_"%envPath)

os.system("echo 'alias jacenv=\"source %s/bin/activate\"' >> ~/.profile"%envPath)

os.system("git clone %s"%JAC_UI_REPO)
os.system("git clone %s"%JmeterAwsConf_REPO)

os.system("%s/bin/pip install boto3 paramiko awscli "%envPath)

os.system("%s/bin/pip install flask flask_socketio eventlet"%envPath)

os.system("echo 'please restart termianl, then type jacenv'")
