kubectl apply -f lb-ft.yml
kubectl apply -f pd-ft.yml
kubectl apply -f autoscale/bk-lb.yml
kubectl apply -f autoscale/database-pv-pvc.yml
kubectl apply -f autoscale/bk-dep-pod.yml
# kubectl apply -f autoscale/bk-hpa.yml