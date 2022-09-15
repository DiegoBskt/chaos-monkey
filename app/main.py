from kubernetes import client, config
import random
import re

namespace = "workloads"
python_pod_name = "pod-chaos-monkey-"

try:
    config.load_kube_config()
    print("load_kube_config")
except:
    config.load_incluster_config()
    print("load_incluster_config")


v1 = client.CoreV1Api()


ret = v1.list_namespaced_pod(namespace=namespace)
pods_names = []

print("List of pods:")
for i in ret.items:
    if not i.metadata.name.startswith(python_pod_name):
        pods_names.append(i.metadata.name)
        print("%s\t%s" % (i.metadata.namespace, i.metadata.name))

print(pods_names)

if not pods_names:
    print("No more pods to delete")
else:
    random_pod = random.choice(pods_names)
    print("Random pod:")
    print(random_pod)

    print("Deleting pod...")
    ret = v1.delete_namespaced_pod(namespace=namespace,name=random_pod)
    print("Pod " + random_pod + " deleted!") 
