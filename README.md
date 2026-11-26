# Meesho App on Kubernetes

Production-style Kubernetes deployment of an e-commerce app (Flask) on Minikube.

## Features
- 3 replicas (Deployment)
- NodePort Service
- Self-healing: pods are recreated when deleted or crashed
- HPA autoscaling on CPU (3 to 8 pods)
- Liveness and readiness probes on /health
- CPU and memory requests/limits
- Rolling updates with zero downtime

## Project structure
- `app/`: Flask app and Dockerfile
- `k8s/`: deployment.yaml, service.yaml, hpa.yaml
- `screenshots/`: proof of each requirement

## Run
    minikube start --driver=docker
    minikube addons enable metrics-server
    minikube image build -t meesho-app:v1 ./app
    kubectl apply -f k8s/
    minikube service meesho-service --url

## Proof (screenshots)
See the `screenshots/` folder for crash recovery, probes and limits, rolling update, rollback and autoscaling.
