#!/bin/bash

# Author: Annanda Sousa (annanda.sousa@gmail.com)

curl -X POST \
    http://0.0.0.0:8443/xapi/statements \
    -H "Content-Type: application/json" \
    -H "X-Experience-API-Version: 1.0.3" \
    -u "my_key:my_secret" \
    -d '{
  "actor": {
    "mbox": "mailto:annanda-8443@example.org",
    "name": "Annanda"
  },
  "verb": {
    "id": "http://example.org/verb/did",
    "display": { "en-US": "Did" }
  },
  "object": {
    "id": "http://example.org/activity/activity-2",
    "definition": {
      "name": { "en-US": "Activity 2" },
      "type": "http://example.org/activity-type/generic-activity"
    }
  }
}'