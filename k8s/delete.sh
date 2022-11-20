kubectl delete service/bk-lb
kubectl delete service/bk-lb-database
kubectl delete pod/frontend-pod
kubectl delete service/ft-lb
kubectl delete pod/mysql-analyze-mongo-pod
kubectl delete deployment auth-sv-backend-dep
kubectl delete pvc mongo-pvc
kubectl delete pvc mysql-pvc
kubectl delete pv mongo-pv
kubectl delete pv mysql-pv
kubectl delete horizontalpodautoscaler.autoscaling/auth-sv-backend-dep