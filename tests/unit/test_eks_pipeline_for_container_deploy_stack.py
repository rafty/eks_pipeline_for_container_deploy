import aws_cdk as core
import aws_cdk.assertions as assertions

from eks_pipeline_for_container_deploy.eks_pipeline_for_container_deploy_stack import EksPipelineForContainerDeployStack

# example tests. To run these tests, uncomment this file along with the example
# resource in eks_pipeline_for_container_deploy/eks_pipeline_for_container_deploy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = EksPipelineForContainerDeployStack(app, "eks-pipeline-for-container-deploy")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
