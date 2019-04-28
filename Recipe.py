# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 04:42:48 2019

@author: Anupama Dhir
"""
dict_categories = {}
dict_dessert = {}
list_dessert = []
dict_maincourse = {}
list_maincourse = []
dict_starter = {}
list_starter = []
entering = True

class Recipe:
     def __init__(self, name, category):
        self.name = name    # instance variable unique to each instance
        self.ingredients = []
        self.category = category
        
     def getIngredients(self):
         return ','.join([str(ingredient) for ingredient in self.ingredients])
     
     def getName(self):
         return self.name
     
     def add_ingredient(self, ingredient):
         self.ingredients.append(ingredient)
         
     def get_category(self):
         return self.category

def Menu():
    print ("Menu:")
    print ("1. Enter new recipe")
    print ("2. List all recipes")
    print ("3. List recipes by Category (Starter/ Main Course/ Dessert)")
    print ("4. Quit")
    return (int(input("Enter your choice.")))

while True:
    menu_selection = Menu()
    if menu_selection == 1:
        recipeName = input("Enter recipe name: ")                
        recipe_category = input("Enter recipe category: ") 
        recipe = Recipe(recipeName, recipe_category)  
        print("Enter the ingredients")
        try:
            while True:
                inp = input()
                if inp != "":
                    recipe.add_ingredient(inp)
                else:
                    break
        except EOFError:
            pass
        
        display_ingredients = recipe.getIngredients()
        print ("Ingredients:")
        print(display_ingredients)
        display_category = recipe.get_category()
        print("Category:")
        print(display_category)
        #list_dessert.append(recipeName)
        if display_category.lower() == 'dessert':
            dict_dessert[recipeName] = display_ingredients
            print ("Dessert Details")
            print(dict_dessert)
            list_dessert.append(recipeName)
            dict_categories[display_category] = list_dessert
        elif display_category.lower() == 'main course':
            dict_maincourse[recipeName] = display_ingredients
            print ("Main Course Details")
            print(dict_maincourse)
            list_maincourse.append(recipeName)
            dict_categories[display_category] = list_maincourse
        elif display_category.lower() == 'starter':
            dict_starter[recipeName] = display_ingredients
            print ("Starter Details")
            print(dict_starter)
            list_starter.append(recipeName)
            dict_categories[display_category] = list_starter
        else:
            print ("Category doesn't exist")
        print (dict_categories)
    elif menu_selection == 2:
        for list in list_dessert:
            print (list)
        for list in list_maincourse:
            print (list)
        for list in list_starter:
            print (list)
    elif menu_selection == 3:
        selection_category = input("Enter recipe category to list: ") 
        print ("Selection Category: {}".format (selection_category))
        if selection_category.lower() == 'dessert':
            print (list_dessert)
        elif selection_category.lower() == 'main course':
            print (list_maincourse)
        elif selection_category.lower() == 'starter': 
            print (list_starter)
        else:
            print ("Category doesn't exist")   
    elif menu_selection == 4:
        break
    
#    y_or_n = input("Do you want to enter another recipe? y or n ")
#
#    if y_or_n[0].lower() == 'y':
#
#        entering = True
#
#    else:
#
#        entering = False
#
#        print("No more recipes to add")
#
#        break
