import requests
import argparse
import json

def fetch_metadata(imds_version):
    base_url = "http://localhost:8000/latest/meta-data/"
    headers = {}

    if imds_version == "v2":
        token_url = "http://localhost:8000/latest/api/token"
        token_response = requests.put(token_url, headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"})
        token = token_response.text
        headers["X-aws-ec2-metadata-token"] = token

    metadata = {}
    for item in ["instance-id", "instance-type", "placement/availability-zone"]:
        response = requests.get(base_url + item, headers=headers)
        metadata[item.split("/")[-1]] = response.text

    print(json.dumps(metadata, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch EC2 Metadata using IMDSv1 or IMDSv2")
    parser.add_argument("version", choices=["v1", "v2"], help="Metadata version to use")
    args = parser.parse_args()
    fetch_metadata(args.version)
