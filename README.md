```
docker build -t upload_seagate_disk .


```


```
docker run -d -p 80:80 \
  --name upload_seagate_container \
  -v /media/yiyun/seagate/Timeline/:/media/yiyun/seagate/Timeline/ \
  -e FILE_STORAGE_PATH=/media/yiyun/seagate/Timeline/ \
  upload_seagate_disk
```
