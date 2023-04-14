# database.py

from diagrams import Diagram
from diagrams.onprem.database import Postgresql
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=False, direction="TB"):
         ELB("lb") >> [Postgresql("database1"),
                       Postgresql("database2"),
                       Postgresql("database3"),
                       Postgresql("database4"),
                       Postgresql("database5")] 
