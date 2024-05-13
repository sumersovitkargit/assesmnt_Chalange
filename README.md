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
![alt text](Image/p.png)

--------------------------------------------------------------------------

# Azure VM Metadata Importer

This script retrieves metadata of a virtual machine (VM) from Azure and allows you to save it in a JSON file. You can also query specific metadata keys.

## Requirements

- Python 3.x
- Azure SDK for Python (`azure-mgmt-compute`)
- Azure Identity library (`azure-identity`)

## Installation

1. Install the required Python packages using pip:

    ```bash
    pip install azure-mgmt-compute azure-identity
    ```

2. Clone or download this repository.

3. Navigate to the directory where you cloned/downloaded the repository.

## Usage

1. Import the `get_vm_metadata`, `save_metadata`, and `query_vm_metadata` functions into your script or use the provided `main.py` script.

2. Update the `subscription_id`, `resource_group_name`, and `vm_name` variables in the `main()` function with your Azure subscription ID, resource group name, and VM name respectively.

3. Run the script:

    ```bash
    python main.py
    ```

4. Follow the prompts to save the VM metadata and query specific keys.

## Example

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def get_vm_metadata(subscription_id, resource_group_name, vm_name):
    # Function definition

def save_metadata(metadata):
    # Function definition

def query_vm_metadata(metadata, key):
    # Function definition

def main():
    # Main function

if __name__ == "__main__":
    main()













