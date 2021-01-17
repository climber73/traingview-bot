. ./env.sh

set -x
ssh -i "$KEY_PATH" $HOST pwd
ssh -i "$KEY_PATH" $HOST 'python3 --version' # sudo yum install python3
ssh -i "$KEY_PATH" $HOST 'pip3 --version'
ssh -i "$KEY_PATH" $HOST 'git --version' # sudo yum install git
ssh -i "$KEY_PATH" $HOST 'sudo pip3 install --upgrade pip'
ssh -i "$KEY_PATH" $HOST 'pip3 install -r requirements.txt'
ssh -i "$KEY_PATH" $HOST 'pip3 list'
