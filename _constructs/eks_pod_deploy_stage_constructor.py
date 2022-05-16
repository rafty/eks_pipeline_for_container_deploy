import aws_cdk
from constructs import Construct
from aws_cdk import aws_eks
from _stacks.eks_cluster import EksClusterStack


class EksPodDeploymentStage(aws_cdk.Stage):

    def __init__(self,
                 scope: Construct,
                 construct_id: str,
                 eks_cluster: aws_eks.Cluster,
                 env: aws_cdk.Environment,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        

