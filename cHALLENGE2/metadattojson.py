import json
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

def get_vm_metadata(subscription_id, resource_group_name, vm_name):
    credentials = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credentials, subscription_id)

    try:
        vm = compute_client.virtual_machines.get(resource_group_name, vm_name)
        return vm.serialize()
    except Exception as e:
        return f"Failed to retrieve VM metadata: {str(e)}"

def save_metadata(metadata):
    try:
        with open('metadata.json', 'w') as file:
            json.dump(metadata, file, indent=4)
        print("VM metadata has been stored in metadata.json")
        return True
    except Exception as e:
        print(f"Failed to save VM metadata: {str(e)}")
        return False

def query_vm_metadata(metadata, key):
    if isinstance(metadata, dict):
        if key in metadata:
            return {key: metadata[key]}
    else:
        return metadata

def main():
    subscription_id = '94e12df9-8810-4706-a83d-06770afb5589'
    resource_group_name = 'Jumpbox_VM_Terraform'
    vm_name = 'Windowsrdpterraform'

    metadata = get_vm_metadata(subscription_id, resource_group_name, vm_name)

    if save_metadata(metadata):
        key_to_query = input("Enter the key you want to query: ")

        result = query_vm_metadata(metadata, key_to_query)
        print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
