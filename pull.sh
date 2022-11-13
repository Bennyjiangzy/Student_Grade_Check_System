docker pull bennyjiang/mysqlsv 
docker pull bennyjiang/auth 
docker pull bennyjiang/analyze 
docker pull bennyjiang/enterdata 
docker pull bennyjiang/showdata 
docker pull bennyjiang/mysql
docker pull bennyjiang/mongodb


docker tag bennyjiang/mysqlsv us.gcr.io/app-368216/cluster-1/mysqlsv
docker tag bennyjiang/auth us.gcr.io/app-368216/cluster-1/auth
docker tag bennyjiang/analyze us.gcr.io/app-368216/cluster-1/analyze
docker tag bennyjiang/enterdata us.gcr.io/app-368216/cluster-1/enterdata
docker tag bennyjiang/showdata us.gcr.io/app-368216/cluster-1/showdata
docker tag bennyjiang/mysql us.gcr.io/app-368216/cluster-1/mysql
docker tag bennyjiang/mongodb us.gcr.io/app-368216/cluster-1/mongodb

docker push us.gcr.io/app-368216/cluster-1/mysqlsv
docker push us.gcr.io/app-368216/cluster-1/auth
docker push us.gcr.io/app-368216/cluster-1/analyze
docker push us.gcr.io/app-368216/cluster-1/enterdata
docker push us.gcr.io/app-368216/cluster-1/showdata
docker push us.gcr.io/app-368216/cluster-1/mysql
docker push us.gcr.io/app-368216/cluster-1/mongodb
