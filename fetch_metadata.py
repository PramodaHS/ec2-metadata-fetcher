import requests
import sys
import json

def fetch_metadata(version):
    base_url = "http://host.docker.internal:8000/latest/meta-data/"
    
    if version == "v1":
        metadata = {
            "instance-id": requests.get(base_url + "instance-id").text,
            "instance-type": requests.get(base_url + "instance-type").text,
            "placement/availability-zone": requests.get(base_url + "placement/availability-zone").text,
        }
    elif version == "v2":
        headers = {"X-aws-ec2-metadata-token-ttl-seconds": "60"}
        token = requests.put("http://host.docker.internal:8000/latest/api/token", headers=headers).text
        headers["X-aws-ec2-metadata-token"] = token
        metadata = {
            "instance-id": requests.get(base_url + "instance-id", headers=headers).text,
            "instance-type": requests.get(base_url + "instance-type", headers=headers).text,
            "placement/availability-zone": requests.get(base_url + "placement/availability-zone", headers=headers).text,
        }
    
    print(json.dumps(metadata, indent=4))

if __name__ == "__main__":
    fetch_metadata(sys.argv[1])
