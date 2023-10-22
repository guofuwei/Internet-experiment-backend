import json

from django.http import JsonResponse
from device.models import Device


# Create your views here.
def get_all(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    devices = Device.objects.all()
    data = []
    for device in devices:
        data.append({
            "id": device.id,
            "sn": device.sn,
            "name": device.name,
            "createTime": device.create_time,
            "longitude": device.longitude,
            "latitude": device.latitude,
            "isSpeak": device.is_speak
        })
    return JsonResponse({"code": 200, "msg": "success", "data": data})


def create_new(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    body = request.body
    body = json.loads(body)
    sn = body.get("sn")
    name = body.get("name")
    if not sn or not name:
        return JsonResponse({"code": "400", "msg": "参数错误"})
    device = Device.objects.create(sn=sn, name=name)
    return JsonResponse({"code": 200, "msg": "success"})


# 删除设备
def delete_device(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    body = request.body
    body = json.loads(body)
    device_id = body.get("id")
    if not device_id:
        return JsonResponse({"code": "400", "msg": "参数错误"})
    device = Device.objects.get(id=device_id)
    device.delete()
    return JsonResponse({"code": 200, "msg": "success"})


# 发出声音请求
def speak(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    body = request.body
    body = json.loads(body)
    device_id = body.get("id")
    if not device_id:
        return JsonResponse({"code": "400", "msg": "参数错误"})
    device = Device.objects.get(id=device_id)
    device.is_speak = True
    device.save()
    return JsonResponse({"code": 200, "msg": "success"})


# 停止声音请求
def stop_speak(request):
    if request.method != "POST":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    body = request.body
    body = json.loads(body)
    device_id = body.get("id")
    if not device_id:
        return JsonResponse({"code": "400", "msg": "参数错误"})
    device = Device.objects.get(id=device_id)
    device.is_speak = False
    device.save()
    return JsonResponse({"code": 200, "msg": "success"})


# 获取设备位置
def get_location(request):
    if request.method != "GET":
        return JsonResponse({"code": "400", "msg": "请求方法错误"})
    device_id = request.GET.get("id")
    if not device_id:
        return JsonResponse({"code": "400", "msg": "参数错误"})
    device = Device.objects.get(id=device_id)
    return JsonResponse({"code": 200, "msg": "success", "data": {
        "longitude": device.longitude,
        "latitude": device.latitude
    }})
