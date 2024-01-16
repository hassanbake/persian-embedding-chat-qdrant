# Running a Qdrant instance on docker in you locall machine

```python
docker run --name qdrant --restart unless-stopped -p 6333:6333 -v D:\Python\rag-qdrant:/qdrant/storage qdrant/qdrant
```
