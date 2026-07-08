import boto3
from config import AWS_REGION

client = boto3.client(
    "bedrock-agent-runtime",
    region_name=AWS_REGION
)

def ask_knowledge_base(question, kb_id, model_arn):

    response = client.retrieve_and_generate(
        input={
            "text": question
        },
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": kb_id,
                "modelArn": model_arn
            }
        }
    )

    return response