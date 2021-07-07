from carrito.models import Carrito

def importe_total(request):
    total=0
    carrito = request.session["carrito"]
    if not carrito:
        carrito = {}
    if request.user.is_authenticated:
        for key, value in request.session["carrito"].items():
            total=total+float(value["precio"])
    return {"importe_total": total}
