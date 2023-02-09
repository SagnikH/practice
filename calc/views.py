from django.shortcuts import render

# Create your views here.

def calcu(request) :
    return render(request, 'index.html', {'name':'sagnik'})

def res(request) :

    val1 = request.POST["num1"]
    val2 = request.POST["num2"]

    res = int(val1)+int(val2)

    return render(request, 'result.html', {'result':res})

def test(request) :
    return render(request, 'footer.html')