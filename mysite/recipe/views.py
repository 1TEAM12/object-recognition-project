from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe

# Create your views here.
@login_required(login_url='user:signin')
def recipe_detail(request, recipe_id):
    if request.method == 'GET':
        context = dict()
        context['recipe'] = get_object_or_404(Recipe, id=recipe_id)
        return render(request, 'recipe/recipe/recipe_detail.html', context=context)
        
@login_required(login_url='user:signin')
def recipe_like_list(request, recipe_id):
    if request.method == 'GET':
        context = dict()
        context['liked_recipes'] = get_list_or_404(Recipe,like_authors=recipe_id)
        return render(request, 'recipe/recipe/recipe_like_list.html', context=context)

@login_required(login_url='user:signin')
def likes(request, recipe_id):
    if request.method == 'POST':
        recipe = Recipe.objects.get(id=recipe_id)
    if recipe.like_authors.filter(id=request.user.id).exists():
        recipe.like_authors.remove(request.user)
    else:
        recipe.like_authors.add(request.user)
    return redirect(request.META['HTTP_REFERER'])
