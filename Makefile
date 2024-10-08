DC = docker compose
SERVICE_NAME = main-app
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml
MESSAGING_FILE = docker_compose/messaging.yaml

.PHONY: app
app-start:
	${DC} -f ${APP_FILE} up -d

.PHONY: drop-app
drop-app:
	${DC} -f ${APP_FILE} down

.PHONY: rebuild-app
rebuild-app:
	${DC} -f ${APP_FILE} build --no-cache


.PHONY: remove-app
remove-app:
	${DC} -f ${APP_FILE} down
	${DC} -f ${APP_FILE} rm -f ${SERVICE_NAME}

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} -f ${MESSAGING_FILE} up --build -d

.PHONY: drop-all
drop-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: remove-all
remove-all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} -f ${MESSAGING_FILE} rm -f

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up --build -d

.PHONY: drop-storage
drop-storage:
	${DC} -f ${STORAGE_FILE} down

.PHONY: remove-storage
remove-storage:
	${DC} -f ${STORAGE_FILE} rm -f

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f

.PHONY: logs
logs-app:
	${DC} -f ${APP_FILE} logs -f

.PHONY: logs
logs-storage:
	${DC} -f ${STORAGE_FILE} logs -f

.PHONY: shell
shell:
	${DC} -f ${APP_FILE} exec ${SERVICE_NAME} /bin/sh

.PHONY: kafka
kafka-start:
	${DC} -f ${MESSAGING_FILE} up -d

.PHONY: drop-kafka
drop-kafka:
	${DC} -f ${MESSAGING_FILE} down

.PHONY: logs
logs-kafka:
	${DC} -f ${MESSAGING_FILE} logs -f
