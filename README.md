# TradingView Signals Translation

## Description

Simple script listening for POST requests from [tradingview](https://www.tradingview.com/support/solutions/43000529348-about-webhooks/) strategies and
translating them to orders in [Binance exchange](https://binance-docs.github.io/apidocs/futures/en/#change-log).

## Tradingview message format

```json
{
    "ticker": "{{ticker}}",
    "position_size": "{{strategy.position_size}}",
    "order.action": "{{strategy.order.action}}",
    "order.contracts": "{{strategy.order.contracts}}",
    "order.price": "{{strategy.order.price}}",
    "order.id": "{{strategy.order.id}}",
    "order.comment": "{{strategy.order.comment}}",
    "order.alert_message": "{{strategy.order.alert_message}}",
    "market_position": "{{strategy.market_position}}",
    "market_position_size": "{{strategy.market_position_size}}",
    "prev_market_position": "{{strategy.prev_market_position}}",
    "prev_market_position_size": "{{strategy.prev_market_position_size}}",
    "timenow": "{{timenow}}",
    "interval": "{{interval}}",
    "strategy_name": "strategy1234",
    "token": "TOKEN"
}
```

## Deploy

Copy files to remote host:
```shell
./deploy.sh
```

Prepare remote host:
```shell
./prepare.sh
```

Run systemd unit:

```shell
sudo vi /lib/systemd/system/app.service
```

```shell
[Unit]
Description=TradingView Translation Signals
After=multi-user.target

[Service]
Type=simple
User=ec2-user
Restart=always
RestartSec=1
ExecStart=/home/ec2-user/venv/bin/python3 -u /home/ec2-user/tradingview-bot/src/main.py --listen 0.0.0.0 --port 8080

[Install]
WantedBy=multi-user.target
```

```shell
sudo systemctl daemon-reload
sudo systemctl enable app.service
sudo systemctl start app.service
```

## Load Balancer

At least 2 instances of the app must be launched behind load balancer. See `./nginx.conf` file.
