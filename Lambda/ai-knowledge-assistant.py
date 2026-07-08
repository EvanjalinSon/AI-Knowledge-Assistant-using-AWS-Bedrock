import json

from config import KNOWLEDGE_BASE_ID, MODEL_ARN
from bedrock_service import ask_knowledge_base


def lambda_handler(event, context):

    try:

        if "body" in event:
            body = json.loads(event["body"])
            question = body.get("question")
        else:
            question = event.get("question")

        if not question:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Question is required."
                })
            }

        response = ask_knowledge_base(
            question,
            KNOWLEDGE_BASE_ID,
            MODEL_ARN
        )
        print(json.dumps(response, indent=2, default=str))

        answer = response["output"]["text"]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "answer": answer
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }