import boto3
import os

ec2 = boto3.client('ec2')

DRY_RUN = os.environ.get('DRY_RUN', 'true').lower() == 'true'

def lambda_handler(event, context):

    print("Cost optimization Lambda triggered")

    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            },
            {
                'Name': 'tag:Environment',
                'Values': ['dev']
            }
        ]
    )

    instances_to_stop = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instances_to_stop.append(instance_id)

    print(f"Instances identified: {instances_to_stop}")

    if not instances_to_stop:
        print("No running instances found")
        return

    if DRY_RUN:
        print("DRY_RUN enabled - no instances will be stopped")
        print(f"Would stop instances: {instances_to_stop}")
    else:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        print(f"Stopped instances: {instances_to_stop}")

    return {
        'statusCode': 200,
        'body': 'Cost optimization workflow executed successfully'
    }
