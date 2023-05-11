# api.py

from diagrams import Cluster, Diagram
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import EC2Instance
from diagrams.aws.network import ALB
from diagrams.azure.identity import Users
with Diagram("TEST", show=False, outformat="png", filename="api"):
    apigw = APIGateway("api gateway")
    lb = ALB("internal load balancer")
    user = Users("user")

    with Cluster("EC2 Auto Scaling"):
        ec2group = [EC2Instance("backend-1"),
		   EC2Instance("backend-2"),
		   EC2Instance("backend-3")]
    user >> apigw >> lb >> ec2group
