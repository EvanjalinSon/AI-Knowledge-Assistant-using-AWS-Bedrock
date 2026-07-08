# AI Knowledge Assistant using Amazon Bedrock

## Overview
Built a serverless AI Knowledge Assistant using Amazon Bedrock Knowledge Bases and Retrieval-Augmented Generation (RAG). The application retrieves information from company documents stored in Amazon S3 and generates context-aware responses through a web interface.

## Architecture

User
↓
Frontend (HTML/CSS/JavaScript)
↓
API Gateway
↓
AWS Lambda
↓
Amazon Bedrock Knowledge Base
↓
Amazon S3 + Titan Text Embeddings V2 + Amazon S3 Vectors

## AWS Services Used

- Amazon Bedrock
- Bedrock Knowledge Base
- Amazon S3
- Titan Text Embeddings V2
- Amazon S3 Vectors
- AWS Lambda
- Amazon API Gateway
- IAM

## Features

- Retrieval-Augmented Generation (RAG)
- Semantic document search
- Serverless architecture
- REST API
- Web-based chat interface

## Tech Stack

- Python
- HTML
- CSS
- JavaScript
- AWS Lambda
- Amazon Bedrock
- API Gateway
- Amazon S3

## Project Structure

frontend/
lambda/
knowledge-base-documents/
screenshots/
README.md

## Future Improvements

- Amazon Cognito authentication
- Chat history
- Source citations
- Terraform deployment