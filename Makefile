build:
	docker-compose -f docker-compose.yml build

run:
	docker-compose -f docker-compose.yml up

shell:
	docker-compose -f docker-compose.yml run --service-ports backend bash
