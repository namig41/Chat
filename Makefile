DC = docker compose
SERVICE_NAME = main-app
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml
MESSAGING_FILE = docker_compose/messaging.yaml

.PHONY: app
app-start:
	${DC} -f ${APP_FILE} up -d

.PHONY: app-drop
app-drop:
	${DC} -f ${APP_FILE} down

.PHONY: app-rebuild
app-rebuild:
	${DC} -f ${APP_FILE} build --no-cache

.PHONY: app-remove
app-remove:
	${DC} -f ${APP_FILE} down
	${DC} -f ${APP_FILE} rm -f ${SERVICE_NAME}

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up --build -d

.PHONY: storage-drop
storage-drop:
	${DC} -f ${STORAGE_FILE} down

.PHONY: storage-remove
storage-remove:
	${DC} -f ${STORAGE_FILE} rm -f

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f

.PHONY: logs
app-logs:
	${DC} -f ${APP_FILE} logs -f

.PHONY: logs
storage-logs:
	${DC} -f ${STORAGE_FILE} logs -f

.PHONY: shell
shell:
	${DC} -f ${APP_FILE} exec ${SERVICE_NAME} /bin/sh

.PHONY: kafka
kafka-start:
	${DC} -f ${MESSAGING_FILE} up -d

.PHONY: kafka-drop
kafka-drop:
	${DC} -f ${MESSAGING_FILE} down

.PHONY: kafka-logs
kafka-logs:
	${DC} -f ${MESSAGING_FILE} logs -f

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} -f ${MESSAGING_FILE} up --build -d

.PHONY: all-drop
all-drop:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: all-remove
all-remove:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} -f ${MESSAGING_FILE} rm -f
