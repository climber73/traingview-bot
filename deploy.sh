. ./env.sh

set -x
ssh -i "$KEY_PATH" $HOST "mkdir -p ~/tradingview-bot/src"
ssh -i "$KEY_PATH" $HOST "mkdir -p ~/tradingview-bot/config"
scp -i "$KEY_PATH" ./src/*.py $HOST:~/tradingview-bot/src/
scp -i "$KEY_PATH" ./config/config.yaml $HOST:~/tradingview-bot/config/
scp -i "$KEY_PATH" ./requirements.txt $HOST:~/tradingview-bot
