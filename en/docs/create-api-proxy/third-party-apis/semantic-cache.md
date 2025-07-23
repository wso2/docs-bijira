# Semantic Caching

AI services frequently involve repetitive queries, leading to unnecessary token usage and increased latency. Bijira’s AI Gateway introduces semantic caching, allowing responses to similar requests to be cached and reused intelligently, minimizing redundant processing, improving response times, and reducing overall costs.


## Configure Semantic Caching Policy

1. In the left navigation menu, click **Develop**, then select **Policy**. 

    ![Semantic Cache Policy](../../assets/img/create-api-proxy/third-party-apis/ai-apis/semantic-cache/semantic-cache-policy.png)  

2. Click Add Resource Level Policy --> Request flow --> Attach mediation policy --> Semantic Caching

    ![Policy List](../../assets/img/create-api-proxy/third-party-apis/ai-apis/semantic-cache/semantic-cache-policy-select.png)  

3. Add the embedding provider and vector store configurations and click **Save**.

     ![Semantic Cache Policy Configs](../../assets/img/create-api-proxy/third-party-apis/ai-apis/semantic-cache/semantic-cache-policy-config.png)  


The configurable fields of the above policy have been described below.

| Field                    | Description                                                        | Example Value                |
| ------------------------ | ------------------------------------------------------------------ | --------------------------- |
| `Embedding Provider`     | AI provider used for generating embeddings (Azure OpenAI or Mistral).| `Azure OpenAI`              |
| `Auth Header Name`       | Header name for authentication <br>(<i>Use the header name ```Authorization``` for Mistral and ```api-key``` for Azure OpenAI.</i>).         | `api-key`             |
| `API Key`                | API key for authenticating with the embedding provider.            | `49fdadxxxxxxxxxxxxxxxxxxxxxxxxxx`       |
| `Embedding Model Name`   | Specific embedding model to use from the provider.                 | `text-embedding-ada-002`    |
| `Embedding Upstream URL` | Endpoint URL of the embedding service.                             | `https://example.openai.azure.com/openai/deployments/xxxxx/embeddings?api-version=2025-07-21` |
| `Vector Store`           | Type of vector database to store embeddings <br><i>(Currently only Redis is supported)</i>.     | `Redis`                     |
| `Host`                   | Host address of the vector database.                               | `redis-xxxxx.us-east.ec2.redis-cloud.com`                 |
| `Port`                   | Network port number of the vector database.                        | `6379`                      |
| `Dimensions`             | Number of dimensions for generated vectors.                        | `1536`                      |
| `Threshold`              | Dissimilarity threshold which is a decimal value for semantic matching that determines the required similarity for cache matches. <br>[<i>**Note**: Lower values (closer to 0) enforce stricter semantic similarity, while higher values allow weaker matches. Typical range: 0.0 (exact) to higher values (e.g., 0.5, 1.2, etc.</i>)]. | `0.1`                       |
| `Username`               | Username for database authentication.                              | `newuser`                     |
| `Password`               | Password for the specified database user.                          | `securepassword123`         |
| `Database`               | Index of the vector database to connect to.                         | `0`             |


> **Note:** The effectiveness of semantic caching can vary based on the selected embedding model and configured similarity threshold. Ensure optimal performance by carefully selecting these parameters according to your specific use case.


## Next Steps

- **Redeploy** to ensure the policy and the configurations are properly applied.  

- **Test the AI API** to ensure it properly cache and serves those cached responses upon receiving semantically similar queries. See [Test REST Endpoints via the OpenAPI Console](../../test-api-proxy/openapi-console.md).  
 

By configuring semantic caching as outlined above, you can efficiently optimize AI service usage within your Bijira environment, significantly reducing latency and operational costs.
  
