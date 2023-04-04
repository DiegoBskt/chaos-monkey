
# PodChaosMonkey

[![CodeQL](https://github.com/DiegoBskt/chaos-monkey/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/DiegoBskt/chaos-monkey/actions/workflows/github-code-scanning/codeql)

`PodChaosMonkey` is a program designed to run inside a kubernetes cluster, interact with the kube-apiserver, and delete a random pod in the selected namespace based on a schedule. The purpose of this program is to test the resilience of the system and to ensure that the system can recover from unexpected failures.


## ✈️ QuickStart

Apply the following manifests to prepare the environment and run the PoC.

```bash
$ kubectl apply -f manifests/1-namespace/
```
Create the ServiceAccount with the Role & RoleBinding 

```bash
$ kubectl apply -f manifests/2-serviceaccount/
```

Create the Cronjob with the pods to test it.

```bash
$ kubectl apply -f manifests/3-resources/
```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
