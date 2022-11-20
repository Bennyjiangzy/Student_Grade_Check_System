kubectl delete service/bk-lb
kubectl delete service/bk-lb-database
kubectl delete pod/frontend-pod
kubectl delete service/ft-lb
kubectl delete pod/mysql-analyze-mongo-pod
kubectl delete deployment auth-sv-backend-dep
kubectl delete pvc mongo-pvc
kubectl delete pvc mysql-pvc
kubectk delete pv mongo-pv
kubectk delete pv mysql-pv