# Create a Storage Account

az storage account create --resource-group Azuredevops --name storage200497 --sku Standard_LRS --encryption-services blob

# Create Container

az storage container create --name container200497 --account-name storage200497

# Get Key

az storage account keys list --resource-group Azuredevops --account-name storage200497
