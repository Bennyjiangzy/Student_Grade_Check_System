docker build -t bennyjiang/mysqlsv Mysql/
docker build -t bennyjiang/auth Authentication/
docker build -t bennyjiang/analyze Analyze/
docker build -t bennyjiang/enterdata enterdata/
docker build -t bennyjiang/showdata showdata/
docker build -t bennyjiang/mongodb mongodb/
docker build -t bennyjiang/mysql .
# docker network create -d bridge assignet
# docker-compose up

docker push bennyjiang/mysqlsv 
docker push bennyjiang/auth 
docker push bennyjiang/analyze 
docker push bennyjiang/enterdata 
docker push bennyjiang/showdata 
docker push bennyjiang/mysql
docker push bennyjiang/mongodb