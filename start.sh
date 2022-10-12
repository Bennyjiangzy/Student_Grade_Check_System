docker build -t assign/mysql Mysql/
docker build -t assign/auth Authentication/
docker build -t assign/analyze Analyze/
docker build -t assign/enterdata enterdata/
docker build -t assign/showdata showdata/
docker network create -d bridge assignet
docker-compose up