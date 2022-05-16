import aws_cdk
from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_iam
from aws_cdk import aws_eks
from _constructs.vpc_constructor import VpcConstructor


class EksPodDeploymentStack(Stack):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 eks_cluster: aws_eks.Cluster,
                 env: aws_cdk.Environment,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        manifest_directory = './manifests/'
