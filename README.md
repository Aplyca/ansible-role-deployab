# Deploy A/B with Ansible

## SSH

* Use your SSH config file (~/.ssh/config) to confgire all the SSH connections, for example the inventory hosts connections.
* Use SSH keys to connect to remote hosts
* Use diferent SSH keys for diffrent environments (development/stage/prod)

## Ansible
* Read how to use the **Ansible** provisioner in README.md of each role.
* To know more about Ansible: http://www.ansible.com

### Dependencies
Install the role dependencies using Ansible Galaxy

```bash
ansible-galaxy install -r dependencies.yml
```

## Releasing code

Release to Stage:

```bash
ansible-playbook -i inventories/local playbook.yml --extra-vars "@tests/custom.yml"
```

Script:

```bash
./deploy.py -ea -v1.0.0
```

Release to Prod:

```bash
ansible-playbook -i inventories/prod playbook.yml --extra-vars "@tests/custom.yml"
```

Script:

```bash
./deploy.py --env a --version 1.0.0
```

### Custom settings
In order to use your own custom settings, use the "settings/custom.yml" file, you can override any variable used in the playbooks and roles.

```bash
ansible-playbook -i inventories/local playbook.yml --extra-vars "@tests/custom.yml"
```

By default the custom.yml file is ignored in git, be mindful to not add to version control your custom files or info.

### Inventory
See the `invetories` folders to know the available inventories
Use the "inventories/custom" to place your custom inventory.

## Tests
```bash
ansible-playbook -i inventories/local tests/playbook.yml
```

## Version control
* Use git to push/push all your changes.
