# Pod Chaos Monkey Script

This script is a simple Kubernetes controller that randomly deletes a running pod in a given namespace. It can be used as a tool to test the resilience of your Kubernetes setup by ensuring that your applications can handle pod failures gracefully.

## Requirements

- Python 3.x
- Kubernetes Python client library (`kubernetes`)

## Installation

1. Install the required packages:

```
pip install kubernetes
```

2. Clone the repository:

```
git clone https://github.com/example/pod-chaos-monkey.git
```

## Usage

1. Open `pod_chaos_monkey.py` in a text editor.

2. Update the `NAMESPACE` and `POD_PREFIX` variables to match your Kubernetes setup.

3. Save the file.

4. Run the script:

```
python pod_chaos_monkey.py
```

The script will randomly choose a pod that matches the `NAMESPACE` and `POD_PREFIX` criteria, and then delete it using the Kubernetes Python client library.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
