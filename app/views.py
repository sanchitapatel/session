from django.shortcuts import render

def set(request):
    my_list1={'id':1,'name':'sanchita','city':'bhopal'}
    my_list2={'id':2,'name':'riya','city':'rewa'}
    my_list=[my_list1,my_list2]
    request.session['data']=my_list
    return render(request,'set.html')

def get(request):
    name=request.session.get('data','guest')
    return render(request,'get.html',{'name':name})
def delete(request):
    # if 'name' in request.session:
    #     del request.session['data']
    request.session.flush()
    return render(request,'delete.html')
