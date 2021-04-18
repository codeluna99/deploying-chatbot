from django.shortcuts import render

def deployer(request):
    return render(request, 'chatbotDeployment/index.html')
