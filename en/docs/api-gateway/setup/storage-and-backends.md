# Configuring External Storage and Backends

### PostgreSQL (Gateway Controller)

To use PostgreSQL as the storage backend for the Gateway Controller, update the `config.toml`:

```toml
[controller.storage]
type = "postgres"

[controller.storage.postgres]
host = "postgres.example.com"
port = 5432
database = "gateway"
user = "gateway"
password = "your-postgres-password"
```

For the full list of PostgreSQL configuration options, refer to the [config template](https://github.com/wso2/api-platform/blob/main/gateway/configs/config-template.toml).

### Redis (Gateway Runtime — Distributed Rate Limiting)

To enable distributed rate limiting across multiple Gateway Runtime instances, configure the rate limiting policy to use Redis as the backend in `config.toml`:

```toml
[policy_configurations.ratelimit_v1]
algorithm = "fixed-window"
backend = "redis"

[policy_configurations.ratelimit_v1.redis]
host = "redis.example.com"
port = 6379
password = "your-redis-password"
```

For the full list of Redis configuration options, refer to the [Advanced Rate Limiting documentation](https://wso2.com/api-platform/policy-hub/policies/advanced-ratelimit).
