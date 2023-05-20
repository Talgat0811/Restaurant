from django.shortcuts import render

def index(request):
    return render(request,'restoranDajngo/index.html')

def main(request):
    return  render(request,'restoranDajngo/main.html')

def menu(request):
    return  render(request,'restoranDajngo/menu.html')
def menu2(request):
    return  render(request,'restoranDajngo/menu2.html')
def salads(request):
    return  render(request,'restoranDajngo/salads.html')
def second(request):
    return  render(request,'restoranDajngo/second.html')
def breakfest(request):
    return  render(request,'restoranDajngo/breakfest.html')
def zakuski(request):
    return  render(request,'restoranDajngo/zakuski.html')
def third(request):
    return  render(request,'restoranDajngo/third.html')
def sweets(request):
    return  render(request,'restoranDajngo/sweets.html')
def rezerv(request):
    return  render(request,'restoranDajngo/rezerv.html')