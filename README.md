# ShortLinkGenerator


<description>

本项目是一个免费的短网址生成工具。该工具仅支持日常生活中的短网址生成，不可以用于违法行为。

</description>

### 准备
> 依赖安装
```bash
pip3 install -r requirements.txt 
```
> 环境变量设置【不配置 OSS 则将使用内存存储】

设置阿里云的 AK、SK，与 OSS endpoint 的 region 与 bucketname。
所需环境变量：
1. ALI_KEY_ID       （AK）
2. ALI_KEY_SECRET   （SK）
3. ALI_OSS_REGION   （例: cn-hangzhou）
4. BUCKET

### 运行
```bash
python3 index.py 
```

通过 127.0.0.1:9000 即可访问