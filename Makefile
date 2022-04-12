build:
	docker-compose -f docker-compose.yml build

run:
	docker-compose -f docker-compose.yml up

shell:
	docker-compose -f docker-compose.yml run --service-ports backend-cli bash

# Run within the container
reconcile:
	export DJANGO_SETTINGS_MODULE=musicworks.settings.base && \
	python src/manage.py reconciler $(file)
