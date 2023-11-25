# Skupper - Service Exposure and Gateway Setup using Ansible

This project uses Ansible to deploy services in two namespaces: `dc1` and `dc2`, and sets up a Skupper network between them. It also exposes the AMQP services from the Skupper network to the local machine and retrieves the port mappings for the exposed services.

# Pre-requisites

* Ansible >= 2.9.0
* Skupper (binary)
* OpenShift CLI (oc)
* KUBECONFIG set to a cluster with appropriate permissions to create and remove namespaces

# Running the demo

## Install the required collections

```bash
ansible-galaxy collection install -r requirements.yml
```

## Deploying the demo

  ```bash
  ansible-playbook -i inventory.yml setup.yml
  ```

## Teard  down the demo

  ```bash
  ansible-playbook -i inventory.yml teardown.yml
  ```

## Aditional tasks

In addition to deploying the services and setting up the Skupper network, the Ansible playbook also includes tasks to:

1. Initialize a Skupper gateway of type service.
2. Expose the AMQP services from the Skupper network to the local machine. This is done for both artemis-broker-amqp-0-svc-dc1 and artemis-broker-amqp-0-svc-dc2 services.
3. Retrieve the port mappings for the exposed services using skupper gateway status. The output of this command is stored in the skupper_status variable for potential future use.


These tasks are designed to further integrate the deployed services with the Skupper network and provide local access to the AMQP services.