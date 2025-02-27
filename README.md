
```
curl -X POST -H "Content-Type: application/json" -d '{"status": "firing", "alerts": [{"labels": {"alertname": "TestAlert"}}]}' http://localhost:8080/webhook

# docker build -t webhook-server:latest .
# docker run -p 5000:5000 webhook-server:latest
# docker tag webhook-server:latest <your-dockerhub-username>/webhook-server:latest
# oc new-app <your-dockerhub-username>/webhook-server:latest --name=webhook-server -n webhook-demo


# oc new-app python:3.9-slim~https://github.com/orangeh8/webhook-server.git --name=webhook-server -n webhook-demo
# oc new-app https://github.com/orangeh8/webhook-server.git --name=webhook-server -n webhook-demo
# oc get pods -n webhook-demo
# oc expose svc/webhook-server -n webhook-demo
```

```
apiVersion: monitoring.coreos.com/v1alpha1
kind: AlertmanagerConfig
metadata:
  name: webhook-config
  namespace: openshift-monitoring
spec:
  route:
    groupBy: ['alertname']
    receiver: 'webhook-receiver'
  receivers:
  - name: 'webhook-receiver'
    webhookConfigs:
    - url: 'http://webhook-server-webhook-demo.apps.cluster.example.com/webhook'
      sendResolved: true


global:
  resolve_timeout: 5m
inhibit_rules:
  - equal:
      - namespace
      - alertname
    source_matchers:
      - severity = critical
    target_matchers:
      - severity =~ warning|info
  - equal:
      - namespace
      - alertname
    source_matchers:
      - severity = warning
    target_matchers:
      - severity = info
  - equal:
      - namespace
    source_matchers:
      - alertname = InfoInhibitor
    target_matchers:
      - severity = info
receivers:
  - name: Default
    webhook_configs:
      - url: >-
          http://example-webhook.com/
  - name: Watchdog
  - name: Critical
  - name: 'null'
route:
  group_by:
    - namespace
  group_interval: 5m
  group_wait: 30s
  receiver: Default
  repeat_interval: 12h
  routes:
    - matchers:
        - alertname = Watchdog
      receiver: Watchdog
    - matchers:
        - alertname = InfoInhibitor
      receiver: 'null'
    - matchers:
        - severity = critical
      receiver: Critical

```