#!/bin/bash

curl -X POST \
    http://0.0.0.0:8443/xapi/statements \
    -H "Content-Type: application/json" \
    -H "X-Experience-API-Version: 1.0.3" \
    -u "key:my_key_secret" \
    -d '
        {
            "object": {
                "id": "https://joinclusion.fse.maastrichtuniversity.nl/game",
                "definition": {
                    "name": {
                        "en-US": "Game"
                    }
                }
            },
            "authority": {
                "account": {
                    "homePage": "http://example.org",
                    "name": "0186a2bc-ffb8-8e5f-bb26-d79b9174f441"
                },
                "objectType": "Agent"
            },
            "verb": {
                "id": "http://adlnet.gov/expapi/verbs/registered",
                "display": {
                    "en-US": "registered"
                }
            },
            "id": "83c9e138-8bad-4bb6-bfea-0c4b7bc82e5b",
            "timestamp": "2024-03-12T14:29:31.743000000Z",
            "context": {
                "extensions": {
                    "https://joinclusion.fse.maastrichtuniversity.nl/password": "admin"
                }
            },
            "version": "1.0.0",
            "stored": "2024-03-12T14:29:31.743000000Z",
            "actor": {
                "name": "admin",
                "mbox": "mailto:admin@joinclusion.eu"
            }
        }'


curl -X POST \
    http://0.0.0.0:8443/xapi/statements \
    -H "Content-Type: application/json" \
    -H "X-Experience-API-Version: 1.0.3" \
    -u "key:my_key_secret" \
    -d '
        {
            "object": {
                "id": "https://joinclusion.fse.maastrichtuniversity.nl/game",
                "definition": {
                    "name": {
                        "en-US": "Game"
                    }
                }
            },
            "authority": {
                "account": {
                    "homePage": "http://example.org",
                    "name": "0186a2bc-ffb8-8e5f-bb26-d79b9174f441"
                },
                "objectType": "Agent"
            },
            "verb": {
                "id": "http://adlnet.gov/expapi/verbs/registered",
                "display": {
                    "en-US": "registered"
                }
            },
            "id": "99e1d769-7e7c-42b8-ac3b-7da3c5cd57d5",
            "timestamp": "2023-03-10T09:07:37.343000000Z",
            "context": {
                "extensions": {
                    "https://joinclusion.fse.maastrichtuniversity.nl/password": "admin"
                }
            },
            "version": "1.0.0",
            "stored": "2023-03-10T09:07:37.343000000Z",
            "actor": {
                "name": "admin",
                "mbox": "mailto:admin@joinclusion.eu"
            }
        }'