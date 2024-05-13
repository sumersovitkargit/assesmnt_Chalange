# 3 Tier Application Setup

This guide outlines the steps to set up a 3-tier application architecture on Kubernetes, consisting of an Application Tier, Logic Tier, and Database Tier.

## 1) Application Tier

- Choose your incoming traffic gateways, such as NodePort, LoadBalancer, or Ingress, to manage traffic flow to the cluster.
- Deploy a frontend application using the Nginx image. 
  - Create a Deployment for the frontend application and deploy it on Kubernetes.

## 2) Logic Tier

- Deploy a backend application using Python, Java, or .Net.
  - Create a Deployment for the backend application and deploy it on Kubernetes.
- Establish connectivity between the backend application and the frontend application via Cluster IP Service.

## 3) Database Tier

- Set up an Azure SQL databae
- Establish connectivity between the server and the backend application using External Name Service.

##  Archetectuer
![Alt Text](/image/p.png)

