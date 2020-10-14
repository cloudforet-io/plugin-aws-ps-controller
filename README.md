# plugin-aws-power-scheduler-controller

## Using Skaffold
```
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 110365492710.dkr.ecr.ap-northeast-2.amazonaws.com
skaffold dev
# or, to run in background
skaffold run
```
