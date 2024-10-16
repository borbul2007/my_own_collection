# Ansible Collection for Grafana

This collection (`grafana.grafana`) contains modules and roles to assist in automating the management of resources in 

## Ansible version compatibility

The collection is tested and supported with: `ansible >= 2.10`

## Installing the collection

Before using the Grafana collection, you need to install it using the below command:

```shell
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## Roles included in the collection

This collection includes the following roles to help set up and manage Grafana, Grafana Agent, OpenTelemetry Collector, Loki, Mimir and Promtail:

- **Grafana**: Installs and configures Grafana on your target hosts.
- **Grafana Agent**: Deploys and configures Grafana Agent, allowing for efficient metrics, logs, and trace data shipping to Grafana Cloud or other endpoints.
- **OpenTelemetry Collector**: Sets up and configures the OpenTelemetry Collector, enabling advanced observability features through data collection and transmission.
- **Loki**: Deploy and manage Loki, the log aggregation system.
- **Mimir**: Deploy and manage Mimir, the scalable long-term storage for Prometheus.
- **Promtail**: Deploy and manage Promtail, the agent which ships the contents of local logs to a private Grafana Loki.

## Using this collection

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `grafana.grafana.cloud_stack`:

```yaml
- name: Using grafana collection
  hosts: localhost
  tasks:
    - name: Create a Grafana Cloud stack
      grafana.grafana.cloud_stack:
        name: mystack
        stack_slug: mystack
        org_slug: myorg
        cloud_api_key: "{{ cloud_api_key }}"
        region: eu
        state: present
```

or you can add full namespace and collection name in the `collections` element in your playbook

```yaml
- name: Using grafana collection
  hosts: localhost
  collection:
    - grafana.grafana
  tasks:
    - name: Create a Grafana Cloud stack
      cloud_stack:
        name: mystack
        stack_slug: mystack
        org_slug: myorg
        cloud_api_key: "{{ cloud_api_key }}"
        region: eu
        state: present
```

## License

MIT

