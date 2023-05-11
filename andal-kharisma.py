# api.py

from diagrams import Cluster, Diagram
from diagrams.onprem.queue import Kafka
from diagrams.onprem.network import Kong, Nginx, Zookeeper
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Postgresql
from diagrams.onprem.logging import Loki
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.tracing import Jaeger
from diagrams.programming.framework import Angular
from diagrams.programming.language import Nodejs
from diagrams.k8s.compute import Deploy



with Diagram("Andal Karisma Logical Infrastructure", show=False, outformat="png", filename="ak"):
    kafka = Kafka("Kafka")
    kong = Kong("Kong")
    zookeeper = Zookeeper("Zookeeper")

    
    with Cluster("Frontend"):
        aimWeb = Deploy("aim-web")
        akWeb = Deploy("ak-web")
        supportWeb = Deploy("support-web")
    
    with Cluster("Backend"):
        akApi = Deploy("ak-api")
        aimApi = Deploy("aim-api")
        akConsumer = Deploy("ak-consumer")
        aimConsumer = Deploy("aim-consumer")
        leaveApi = Deploy("leave-api")
        leaveConsumer = Deploy("leave-consumer")
        claimApi = Deploy("claim-api")
        claimConsumer = Deploy("claim-consumer")
        akNotifApi = Deploy("ak-notif-api")
        akReport = Deploy("ak-report")
        akTransform = Deploy("ak-transform")
        akTransformKafka = Deploy("ak-transform-kafka")
        andalExecuteJob = Deploy("andal-execute-job")
        andalReminder = Deploy("andal-reminder")
        reportDesigner = Deploy("report-designer")
        staticApi = Deploy("static-api")
        supportApi = Deploy("support-api")

    with Cluster("Database"):
        dbAim = Postgresql("AIM")
        dbAk = Postgresql("Andal Kharisma")
        dbAndalClaim = Postgresql("Andal Claim")
        dbAndalLeave = Postgresql("Andal Leave")
        dbAndalReminder = Postgresql("Andal Reminder")
        dbAndalSupport = Postgresql("Andal Support")
        dbAndalReport = Postgresql("Andal Report")


    akApi >> zookeeper << dbAk
    aimApi >> zookeeper << dbAim
    claimApi >> zookeeper << claimConsumer
    leaveApi >> zookeeper << dbAndalLeave
    reportDesigner >> dbAndalReport
    andalReminder >> zookeeper << dbAndalReminder
    akReport >> zookeeper << dbAndalReport

    zookeeper >> kafka

    kong << akApi
    kong << aimApi
    kong << leaveApi
    kong << claimApi
    kong << akNotifApi
    kong << supportApi
    kong << staticApi
    kong << andalReminder
    kong << akReport

    akConsumer >> zookeeper
    aimConsumer >> zookeeper
    leaveConsumer >> zookeeper
    claimConsumer >> zookeeper

    aimWeb >> kong
    akWeb >> kong 
    supportWeb >> kong

    # lb = ALB("internal load balancer")
    # user = Users("user")

    # with Cluster("EC2 Auto Scaling"):
    #     ec2group = [EC2Instance("backend-1"),
	# 	   EC2Instance("backend-2"),
	# 	   EC2Instance("backend-3")]
    # user >> apigw >> lb >> ec2group
