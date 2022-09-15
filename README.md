
# PodChaosMonkey

This program runs inside the cluster, interacts with the kube
apiserver, and deletes one pod at random in the 'workloads' namespace on a schedule. The
program could be known as ‘PodChaosMonkey’.


## ✈️ QuickStart

Apply the following manifests to prepare the environment and run the PoC.

```bash
$ kubectl apply -f manifests/1-namespace/
```
Create the ServiceAccount with the Role & RoleBinding 

```bash
$ kubectl apply -f manifests/2-serviceaccount/
```

Create the Cronjov with the pods to test it.

```bash
$ kubectl apply -f manifests/3-resources/
```


