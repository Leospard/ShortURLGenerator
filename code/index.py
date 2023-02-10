import bottle
import oss2
import re
import os
import json
import random
import urllib.parse
# 获取随机字符串
randomStr = lambda len: "".join(random.sample('abcdefghijklqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 100, len))

AccessKey = {
    "id": os.environ.get("ALI_KEY_ID"),
    "secret": os.environ.get("ALI_KEY_SECRET"),
    # "token": os.environ.get("ALIBABA_CLOUD_SECURITY_TOKEN"),
}
OSSConf = {
    'endPoint': 'oss-' + os.environ.get("region") + '.aliyuncs.com',
    # 'endPoint': 'oss-cn-hongkong.aliyuncs.com',
    'bucketName': os.environ.get("bucket"),
}

# 获取获取/上传文件到OSS的临时地址
auth = oss2.Auth(AccessKey['id'], AccessKey['secret'])
bucket = oss2.Bucket(auth, OSSConf['endPoint'], OSSConf['bucketName'])

print(AccessKey)
print(OSSConf)

# 首页
@bottle.route('/')
def short_index():
    with open('index.html') as f:
        file = f.read()
    return file

@bottle.route("/t/<share:re:.+>")
def to_target(share):
    print(">>>>>>>>>>> to_target")
    random_file = '/tmp/%s' % (randomStr(5))
    try:
        bucket.get_object_to_file(share, random_file)
    except Exception as e:
        print(e)
        return "短网址跳转失败，请确定短网址的正确性"
    with open(random_file) as f:
        target_file = f.read()
    temp_chinese= re.findall('[\u4e00-\u9fa5]', target_file)
    for eve_chinese in temp_chinese:
        target_file = target_file.replace(eve_chinese, urllib.parse.quote(eve_chinese))
    bottle.redirect(target_file)


@bottle.route('/api', method=['GET', 'POST'])
def short_api():
    if bottle.request.method == "POST":
        try:
            body = json.loads(bottle.request.body.read().decode("utf-8"))
            target = body.get("target")
            source = randomStr(5)
            bucket.put_object(source, target)
            return {"status": 1, "url": '/t/' + source}
        except Exception as e:
            print(e)
            return {"status": 0, "msg": '添加失败，异常未知'}


if __name__ == "__main__":
    bottle.run(host='0.0.0.0', debug=False, port=9000)
else:
    app = bottle.default_app()
