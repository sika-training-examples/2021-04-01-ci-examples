import json
import random

SERVICES = (
    "foo",
    "bar",
    "baz",
    "aaa",
    "bbb",
    "ccc",
)

def random_sleep():
    return random.randint(0, 20)

def make_service(name):
    return {
        "build-%s" % name: {
            "stage": "build",
            "script":[
                "echo Build %s" % name,
                "sleep %s" % random_sleep(),
            ]
        },
        "deploy-%s" % name: {
            "stage": "deploy",
            "script":[
                "echo Deploy %s" % name,
                "sleep %s" % random_sleep(),
            ]
        }
    }

with open(".gitlab-ci.generated.yml", "w") as f:
    pipeline = {}
    pipeline.update({
        "stages": ["build", "deploy"]
    })
    for service in SERVICES:
        pipeline.update(make_service(service))
    f.write(json.dumps(pipeline))
