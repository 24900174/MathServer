from django.shortcuts import render

def powerlamp(request):
    context={}
    context['mathapp'] = ""
    context['I'] = ""
    context['R'] = ""
    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('Intensity','')
        R = request.POST.get('Resistence','')
        print('request=',request)
        print('Intensity=',I)
        print('Resistence=',R)
        power = int(I) * int(I) * int(R)
        context['mathapp'] = power
        context['I'] = I
        context['R'] = R
        print('Power=',context['mathapp'])
    return render(request,'math.html',context)
