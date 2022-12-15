from django.shortcuts import render,redirect
from AdminApp.models import Category,Product,UserInfo,PaymentMaster
from UserApp.models import MyCart

# Create your views here.
def homepage(request):
    cats = Category.objects.all()
    prods= Product.objects.all()
    return render(request,"homepage.html",{"cats":cats,"prods":prods})

def ShowProduct(request,id):
    #get method returns single object
    catid = Category.objects.get(id=id)
    #filter method returns multiple objects
    prods = Product.objects.filter(cat=catid)
    cats = Category.objects.all()
    return render(request,"homepage.html",{"cats":cats,"prods":prods})

def ViewDetails(request,id):
    prod = Product.objects.get(id=id)
    cats = Category.objects.all()
    return render(request,"ViewDetails.html",{"prod":prod,'cats':cats})

def login(request):
    if(request.method == "GET"):
        cats = Category.objects.all()
        return render(request,"login.html",{'cats':cats})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        try:
            user = UserInfo.objects.get(uname=uname,password=password)
        except:
            return redirect(login)
        else:
            #Create the session
            request.session["uname"]=uname
            return redirect(homepage)

def signup(request):
    if(request.method == "GET"):
        cats = Category.objects.all()
        return render(request,"signup.html",{'cats':cats})
    else:
        uname = request.POST["uname"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = UserInfo(uname,password,email)
        user.save()
        return redirect(homepage)

def signout(request):
    request.session.clear()
    return redirect(homepage)

def addToCart(request):
    if(request.method == "POST"):
        if("uname" in request.session):
            #Add to cart
            #User and Product
            productid = request.POST["prodid"]
            user = request.session["uname"]
            qty = request.POST["qty"]
            product = Product.objects.get(id=productid)
            user = UserInfo.objects.get(uname = user)
            #check for duplicate entry
            try:
                cart = MyCart.objects.get(product=product,user=user)
            except:
                cart = MyCart()
                cart.user = user
                cart.product = product
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)
        else:
            return redirect(login)

def ShowAllCartItems(request):
    uname = request.session["uname"]
    user = UserInfo.objects.get(uname = uname)
    if(request.method == "GET"):
        cats = Category.objects.all()       
        cartitems = MyCart.objects.filter(user=user)
        total = 0
        for item in cartitems:
            total+= item.qty*item.product.price
        request.session["total"] = total
        return render(request,"ShowAllCartItems.html",{"items":cartitems,'cats':cats})
    else:
        action = request.POST["action"]
        id = request.POST["productid"]
        product = Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,product=product)            
        if(action == "remove"):
            item.delete()
        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save() #Update
        return redirect(ShowAllCartItems)

def MakePayment(request):
    if(request.method == "GET"):
        cats = Category.objects.all()
        return render(request,"MakePayment.html",{'cats':cats})
    else:
        cardno = request.POST["cardno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        try:
            buyer = PaymentMaster.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)
        except:
            return redirect(MakePayment)
        else:
            #Its a match
            owner = PaymentMaster.objects.get(cardno='555',cvv='555',expiry='02/2027')
            owner.balance += request.session["total"]
            buyer.balance -=request.session["total"]
            owner.save()
            buyer.save()
            #Delete all items from cart
            
            return render(request,"PaymentSuccess.html")
            

