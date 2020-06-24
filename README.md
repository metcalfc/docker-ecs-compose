## Compose sample application

### Python/Flask application

```
+--------------------+              +------------------+
|                    |              |                  |
|    Python Flask    |  timestamps  |      Redis       |
|    Application     |------------->|                  |
|                    |              |                  |
+--------------------+              +------------------+
```

Project structure:

```
.
├── docker-compose.yaml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py

```

[_docker-compose.yaml_](docker-compose.yaml)

```
services:
  web:
    build: app
    ports:
      - '5000:5000'
```

## Deploy with docker-compose

```
$ docker-compose up -d
Creating network "flask_default" with the default driver
Building web
Step 1/6 : FROM python:3.7-alpine
...
...
Status: Downloaded newer image for python:3.7-alpine
Creating flask_web_1 ... done

```

## Expected result

Listing containers must show two containers running and the port mapping as below:

```
$ docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                  NAMES
c126411df522        flask_web                    "python3 app.py"         About a minute ago  Up About a minute   0.0.0.0:5000->5000/tcp flask_web_1
```

After the application starts, navigate to `http://localhost:5000` in your web browser or run:

```
$ curl localhost:5000
Hello World!
```

Stop and remove the containers (including resetting the redis data)

```
$ docker-compose down
$ docker-compose rm
```

## Walk through

1. setup creds

```
aws-okta write-to-credentials ${AWS_PROFILE} ~/.aws/credentials
eval $(aws-okta env ${AWS_PROFILE})
```

2. enable plugins

```
export DOCKER_CLI_EXPERIMENTAL=enabled
```

3. create an AWS Docker context and show context

```
docker ecs setup
Enter context name: aws
✔ sandbox.devtools.developer
Enter cluster name:
Enter region: us-west-2
✗ Enter credentials:

docker context ls
NAME                DESCRIPTION                               DOCKER ENDPOINT               KUBERNETES ENDPOINT   ORCHESTRATOR
aws
default *           Current DOCKER_HOST based configuration   unix:///var/run/docker.sock                         swarm
```

4. test locally (note x-aws-pull_credentials )

```
docker context use default
docker-compose up
open http://localhost:5000
```

5. push images to hub for ecs (ecs cannot see your local image cache)

```
make push-images-hub
```

6. switch to ECS context

```
docker context use aws
docker ecs compose up
```

7. walk through the CLI

```
docker ecs compose ps
docker ecs compose logs
```

8. walk through the aws console

- cloud formation
- cloud watch

9. show cloudformation

```
docker ecs

9. compose down to stop the meters

```

docker ecs compose down

```

```
