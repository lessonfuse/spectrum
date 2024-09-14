
```bash
docker run -d \
  --name postgres \
  -e POSTGRES_DB=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=admin \
  -p 5432:5432 \
  postgres:latest
```


```bash
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis:latest
```
