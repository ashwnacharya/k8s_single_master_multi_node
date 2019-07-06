# k8s_single_master_multi_node
Set up a single master multi node k8s cluster on vagrant VMs.

## To bring up VMs

Run

```
$ vagrant up
```


## To run ansible

Run

```
$ cd ansible
$ ansible-playbook main.yml -i inventories/local
```

# To connect to the cluster using kubectl
Copy the file `/home/vagrant/.kube/config` to your `~/.kube` directory.
Then use kubectl as usual.

