BACKUP_DIR="/home/dilshod/PycharmProjects/AdminWebBot/backup/"
FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S`.tar
docker exec -it -u postgres pg_con pg_dump -U postgres -d postgres > $FILE_NAME