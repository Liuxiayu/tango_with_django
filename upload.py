

# html form 表单中需要有一个enctype=muli/formdata
#上传文件实例
# def upload(request):
#     if request.method == "POST":
#         file_obj = request.Files.get("kouge")
#         with open(file_obj.name,"wb") as f:
#             for line in file_obj:
#                 f.write(line)
# #           for chunk in file_obj.chunks():
#                 f.write(chunk)

#     return render(request,"upload.html")