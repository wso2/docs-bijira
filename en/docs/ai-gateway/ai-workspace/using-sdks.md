# Invoke Providers and Proxies via SDKs

Once you have deployed an LLM Provider or LLM Proxy in the AI Workspace, you can invoke it using any supported AI SDK by pointing it at the gateway's Invoke URL and authenticating with your generated API key.

The examples below apply to both providers and proxies — the only difference between the two is the Invoke URL you supply.

## Prerequisites

- An LLM [Provider](llm-providers/configure-provider.md) or [Proxy](llm-proxies/configure-proxy.md) deployed to a gateway
- The **Invoke URL** for the deployed endpoint 
- A generated **API key** 

## Authentication

All requests to the gateway must include your API key in the `X-API-Key` request header. Most SDKs provide a way to set custom or default headers. The code examples below show the correct approach for each SDK.

!!! note "Anthropic SDK"
    The Anthropic SDK automatically sends the `api_key` parameter as the `x-api-key` header, which the gateway uses for authentication. No additional header configuration is needed.

## OpenAI

Uses the [`openai`](https://pypi.org/project/openai/) Python SDK.

!!! info "Invoke URL format"
    The OpenAI provider and proxy expose an OpenAI-compatible API. Append `/v1` to the Invoke URL shown in the console:
    ```
    https://{gateway-host}/{context}/v1
    ```

**Basic chat completion:**

```python
from openai import OpenAI

INVOKE_URL = "https://<gateway-host>/<context>/v1"
API_KEY = "<your-gateway-api-key>"

client = OpenAI(
    api_key=API_KEY,
    base_url=INVOKE_URL,
    default_headers={"X-API-Key": API_KEY},
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is WSO2?"}],
)

print(response.choices[0].message.content)
```

**Streaming:**

```python
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Count from 1 to 5."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
```

## Anthropic

Uses the [`anthropic`](https://pypi.org/project/anthropic/) Python SDK.

**Basic message:**

```python
import anthropic

INVOKE_URL = "https://<gateway-host>/<context>"
API_KEY = "<your-gateway-api-key>"

client = anthropic.Anthropic(
    api_key=API_KEY,
    base_url=INVOKE_URL,
)

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What is WSO2?"}],
)

print(response.content[0].text)
```

**Streaming:**

```python
with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Count from 1 to 5."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

## Gemini

Uses the [`google-genai`](https://pypi.org/project/google-genai/) Python SDK.

!!! note
    The Gemini SDK normally sends its key as the `x-goog-api-key` header, which the gateway does not use for authentication. Pass `api_key="placeholder"` to satisfy the SDK's requirement and supply the gateway API key via the `X-API-Key` header in `HttpOptions` instead.

**Basic content generation:**

```python
from google import genai
from google.genai import types as genai_types

INVOKE_URL = "https://<gateway-host>/<context>"
API_KEY = "<your-gateway-api-key>"

http_options = genai_types.HttpOptions(
    base_url=INVOKE_URL,
    headers={"X-API-Key": API_KEY},
)

client = genai.Client(api_key="placeholder", http_options=http_options)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is WSO2?",
)

print(response.text)
```

**Streaming:**

```python
for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Count from 1 to 5.",
):
    if chunk.text:
        print(chunk.text, end="", flush=True)
```

## Mistral AI

Uses the [`mistralai`](https://pypi.org/project/mistralai/) Python SDK.

!!! note
    The Mistral SDK sends its API key as a `Bearer` token in the `Authorization` header. Since the gateway requires `X-API-Key`, an httpx event hook is used to inject this header on every outgoing request.

**Basic chat completion:**

```python
import httpx
from mistralai import Mistral

INVOKE_URL = "https://<gateway-host>/<context>"
API_KEY = "<your-gateway-api-key>"

def _inject_api_key(request):
    request.headers["X-API-Key"] = API_KEY

http_client = httpx.Client(
    event_hooks={"request": [_inject_api_key]},
)

client = Mistral(
    api_key=API_KEY,
    server_url=INVOKE_URL,
    client=http_client,
)

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "What is WSO2?"}],
)

print(response.choices[0].message.content)
```

**Streaming:**

```python
with client.chat.stream(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Count from 1 to 5."}],
) as stream:
    for event in stream:
        if event.data.choices and event.data.choices[0].delta.content:
            print(event.data.choices[0].delta.content, end="", flush=True)
```

## Azure OpenAI

Uses the [`openai`](https://pypi.org/project/openai/) Python SDK's `AzureOpenAI` client.

!!! note
    The `model` parameter must be your **Azure deployment name**, not the underlying model name (for example, `my-gpt4o-deployment` rather than `gpt-4o`).

**Basic chat completion:**

```python
from openai import AzureOpenAI

INVOKE_URL = "https://<gateway-host>/<context>"
API_KEY = "<your-gateway-api-key>"

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=INVOKE_URL,
    api_version="2024-06-01",
    default_headers={"X-API-Key": API_KEY},
)

response = client.chat.completions.create(
    model="<your-deployment-name>",
    messages=[{"role": "user", "content": "What is WSO2?"}],
)

print(response.choices[0].message.content)
```

**Streaming:**

```python
stream = client.chat.completions.create(
    model="<your-deployment-name>",
    messages=[{"role": "user", "content": "Count from 1 to 5."}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
```
