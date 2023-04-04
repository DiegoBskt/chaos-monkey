from kubernetes import client, config
import random

NAMESPACE = "workloads"
POD_PREFIX = "pod-chaos-monkey-"

def main():
    try:
        config.load_kube_config()
        print("load_kube_config")
    except config.config_exception.ConfigException:
        config.load_incluster_config()
        print("load_incluster_config")

    k8s = client.CoreV1Api()

    pods = k8s.list_namespaced_pod(namespace=NAMESPACE)
    pod_names = []

    print("List of pods:")
    for pod in pods.items:
        if not pod.metadata.name.startswith(POD_PREFIX):
            pod_names.append(pod.metadata.name)
            print(f"{pod.metadata.namespace}\t{pod.metadata.name}")

    print(pod_names)

    if not pod_names:
        print("No more pods to delete")
    else:
        random_pod_name = random.choice(pod_names)
        print("Random pod:")
        print(random_pod_name)

        print("Deleting pod...")
        with client.V1DeleteOptions() as delete_options:
            delete_response = k8s.delete_namespaced_pod(namespace=NAMESPACE, name=random_pod_name, body=delete_options)
        print(f"Pod {random_pod_name} deleted!")

if __name__ == "__main__":
    main()
