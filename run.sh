docker run --restart=always --name douyin_download \
-v /root/workspace/DouyinLiveRecorder/config:/app/config \
-v /root/workspace/DouyinLiveRecorder/logs:/app/logs \
-v /root/workspace/DouyinLiveRecorder/backup_config:/app/backup_config \
-v /mnt/data_wd_700/douyin_downloads:/app/downloads \
-e TERM=xterm-256color \
-d douyin_recorder