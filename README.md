
# docker build -t webhook-server:latest .
# docker run -p 5000:5000 webhook-server:latest
# docker tag webhook-server:latest <your-dockerhub-username>/webhook-server:latest
# oc new-app <your-dockerhub-username>/webhook-server:latest --name=webhook-server -n webhook-demo


# oc new-app python:3.9~https://github.com/orangeh8/webhook-server.git --name=webhook-server -n webhook-demo
# oc new-app openshift/python:3.11-ubi9~https://github.com/orangeh8/webhook-server.git --name=webhook-server -n webhook-demo
# oc new-app python:3.9-slim~https://github.com/orangeh8/webhook-server.git --name=webhook-server -n webhook-demo
# oc new-app https://github.com/orangeh8/webhook-server.git --name=webhook-server -n webhook-demo
# oc get pods -n webhook-demo
# oc expose svc/webhook-server -n webhook-demo




# apiVersion: monitoring.coreos.com/v1alpha1
# kind: AlertmanagerConfig
# metadata:
#   name: webhook-config
#   namespace: openshift-monitoring
# spec:
#   route:
#     groupBy: ['alertname']
#     receiver: 'webhook-receiver'
#   receivers:
#   - name: 'webhook-receiver'
#     webhookConfigs:
#     - url: 'http://webhook-server-webhook-demo.apps.cluster.example.com/webhook'
#       sendResolved: true