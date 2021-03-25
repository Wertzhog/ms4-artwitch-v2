from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IYzBvFN6ZQOpXyoFeBqwjeqMSoCwcNVMhVeKVHK8MkfLCN3Ftg65zfdlr9QxIG4TokVI6gAPspS29ijSXWZl6Zo00Cmv2u7tq',
        'client_secret':'test client secret',
    }

    return render(request, template, context)
