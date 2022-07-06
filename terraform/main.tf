provider "azurerm" {
  tenant_id       = "${var.tenant_id}"
  subscription_id = "${var.subscription_id}"
  client_id       = "${var.client_id}"
  client_secret   = "${var.client_secret}"
  features {}
}

terraform {
  backend "azurerm" {
    storage_account_name = "storage200382"
    container_name       = "container200382"
    access_key           = "4lWhC3b8PzQxjMoQkvtYbg2kg5C5+ujGx8vvu0XDEInW7svi/jXi7QAN+kKbH0X1EcbKEg1V43ow+AStqLcw5A=="
    key                  = "terraform.tfstate"
  }
}

module "network" {
  source               = "./modules/network"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  virtual_network_name = "${var.virtual_network_name}"
  application_type     = "${var.application_type}"
  resource_type        = "NET"
  resource_group       = "${var.resource_group}"
  address_prefix_test  = "${var.address_prefix_test}"
}

module "nsg-test" {
  source           = "./modules/networksecuritygroup"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "NSG"
  resource_group   = "${var.resource_group}"
  subnet_id        = "${module.network.subnet_id_test}"
  address_prefix_test = "${var.address_prefix_test}"
}
module "appservice" {
  source           = "./modules/appservice"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "AppService"
  resource_group   = "${var.resource_group}"
}
module "publicip" {
  source           = "./modules/publicip"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "publicip"
  resource_group   = "${var.resource_group}"
}

module "vm" {
  source               = "./modules/vm"
  name                 = "vm-for-qa"
  location             = "${var.location}"
  application_type     = "${var.application_type}"
  resource_group       = "${var.resource_group}"
  public_ip_address_id = "${module.publicip.public_ip_address_id}"
  subnet_id            = "${module.network.subnet_id_test}"
  admin_username       = "${var.admin_username}"
}