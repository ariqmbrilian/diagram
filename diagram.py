# diagram.py

from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.aws.network import ELB

with Diagram("Simple Web Service with DB Cluster", show=False, outformat="png", filename="simple-diagram"):
    dns = Route53("dns")
    web = EC2("service")

    with Cluster("DBCluster"):
        db_primary = RDS("primary")
        db_primary - [RDS("replica1"),
                     RDS("replica2")]

        dns >> web >> db_primary
#    ELB("lb") >> EC2("web") >> RDS("userdb")
