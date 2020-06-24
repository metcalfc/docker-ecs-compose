FRONTEND_IMG = metcalfc/timestamper
REGISTRY_ID=175142243308
DOCKER_PUSH_REPOSITORY=dkr.ecr.us-west-2.amazonaws.com

all: build-image 

create-ecr:
	aws ecr create-repository --repository-name ${FRONTEND_IMG}

build-image:
	docker build -t $(REGISTRY_ID).$(DOCKER_PUSH_REPOSITORY)/$(FRONTEND_IMG) ./app
	docker build -t $(FRONTEND_IMG) ./app

push-image-ecr:
	aws ecr get-login-password --region us-west-2 | docker login -u AWS --password-stdin $(REGISTRY_ID).$(DOCKER_PUSH_REPOSITORY)
	docker push $(REGISTRY_ID).$(DOCKER_PUSH_REPOSITORY)/$(FRONTEND_IMG)

push-image-hub:
	docker push $(FRONTEND_IMG)