#!/usr/bin/env python3
import argparse
import json
import logging

from google.protobuf.wrappers_pb2 import Int64Value

import doublecloud
from doublecloud.clickhouse.v1.cluster_pb2 import ClusterResources
from doublecloud.clickhouse.v1.cluster_service_pb2 import (
    CreateClusterRequest,
    DeleteClusterRequest,
)
from doublecloud.clickhouse.v1.cluster_service_pb2_grpc import ClusterServiceStub


def create_cluster(sdk, project_id, region_id, name, network_id):
    cluster_service = sdk.client(ClusterServiceStub)
    operation = cluster_service.Create(
        CreateClusterRequest(
            project_id=project_id,
            cloud_type="aws",
            region_id=region_id,
            name=name,
            resources=ClusterResources(
                clickhouse=ClusterResources.Clickhouse(
                    resource_preset_id="s1-c2-m4",
                    disk_size=Int64Value(value=32 * 2**30),
                    replica_count=Int64Value(value=1),
                )
            ),
            network_id=network_id,
        )
    )
    logging.info("Creating initiated")
    return operation


def delete_cluster(sdk, cluster_id):
    cluster_service = sdk.client(ClusterServiceStub)
    return cluster_service.Delete(DeleteClusterRequest(cluster_id=cluster_id))


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    if arguments.token:
        sdk = doublecloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = doublecloud.SDK(service_account_key=json.load(infile))

    cluster_id = None
    try:
        operation = create_cluster(sdk, arguments.project_id, arguments.region, arguments.name, arguments.network_id)
        operation_result = sdk.wait_operation_and_get_result(
            operation,
        )
        cluster_id = operation_result.operation.resource_id

    finally:
        if cluster_id:
            logging.info(f"Deleting cluster {cluster_id}")
            operation = delete_cluster(sdk, cluster_id)
            sdk.wait_operation_and_get_result(
                operation,
            )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    auth = parser.add_mutually_exclusive_group(required=True)
    auth.add_argument(
        "--sa-json-path",
        help="Path to the service account key JSON file.\nThis file can be created using UI:\n"
        "Members -> Service Accounts -> Create and then create authorized keys",
    )
    auth.add_argument("--token", help="IAM token")
    parser.add_argument("--project-id", help="Your project id", required=True)
    parser.add_argument("--region", default="eu-central-1", help="Region to deploy to.")
    parser.add_argument("--name", default="sdk-example", help="New cluster name.")
    parser.add_argument("--network-id", help="Network of the cluster.")

    return parser.parse_args()


if __name__ == "__main__":
    main()
