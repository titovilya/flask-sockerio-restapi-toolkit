# Config
env:
	cp .example.env .env

# Builds
# For Linux
build:
	make build-redis \
	&& make build-worker \
	&& make build-flower \
	&& make build-pg \
	&& make build-api \
	&& make build-ap \
	&& make build-nginx \

# For Windows
build-windows:
	make build-redis \
	&& make build-worker \
	&& make build-flower \
	&& make build-pg-windows \
	&& make build-api-windows \
	&& make build-ap-windows \
	&& make build-nginx \
	

build-api:
	python3 -m pip install -r ./services/api/requirements.txt \
	&& docker-compose build api \

build-pg:
	python3 -m pip install -r ./services/main_page/requirements.txt \
	&& docker-compose build main_page \

build-ap:
	python3 -m pip install -r ./services/admin_panel/requirements.txt \
	&& docker-compose build admin_panel \

build-api-windows:
	pip install -r ./services/api/requirements.txt \
	&& docker-compose build api \

build-pg-windows:
	pip install -r ./services/main_page/requirements.txt \
	&& docker-compose build main_page \

build-ap-windows:
	pip install -r ./services/admin_panel/requirements.txt \
	&& docker-compose build admin_panel \

build-nginx:
	docker-compose build nginx

build-redis:
	docker-compose build redis

build-worker:
	docker-compose build worker

build-flower:
	docker-compose build flower

# Run dev apps
dev:
	docker-compose up

# Stop
stop:
	docker-compose down

# Containers
ps:
	docker-compose ps