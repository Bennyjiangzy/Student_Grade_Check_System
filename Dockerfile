FROM mysql
# Set working directory
ENV MYSQL_ROOT_PASSWORD password
ADD database.sql /docker-entrypoint-initdb.d
EXPOSE 3306