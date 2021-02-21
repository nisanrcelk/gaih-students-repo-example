class food():
  def __init__(self,name):
    self.name=name

  def cooking(self):
    print(f"{self.name} cooking...")
      
class soup(food):
 def __init__(self,name):
   super().__init__(name)
   self.ingredients = ["lentil","water","oil","carrot","patoto","onion","garlic"]
   
   self.making="First, wash the lentils thoroughly and set aside to drain.Peel the potatoes, onions and carrots and chop them coarsely.Add the olive oil to the pot.Then add the onion and garlic and fry. Add the carrots and potatoes and fry for a few minutes.Then put the lentils in the pot.Add the water and spices and leave to cook.When the vegetables are soft, pass them through a blender and boil for a few more minutes."
 def make(self):
   print(f" {self.name}'s Ingredients...")
   for i in range(1):
    print(f"1 cup of  {self.ingredients[i]}")
    print(f"2 glasses of {self.ingredients[i+1]}")
    print(f"half a glass of {self.ingredients[i+2]}")
    print(f"1 {self.ingredients[i+3]}")
    print(f"1  {self.ingredients[i+4]}")
    print(f"1 clove of {self.ingredients[i+5]}")

   print(f" {self.name} Making...")  
   print(self.making) 
 
class dessert(food):
 def __init__(self,name):
   super().__init__(name)
   self.ingredients = ["egg","sugar","oil","milk","fame","vanilla","baking powder"]
   self.making="Egg and sugar are whipped thoroughly in a bowl at the high level of the mixer.Then add milk, oil and vanilla and whisk a little more.Add flour and baking powder and beat again.Pour our cake dough into our oiled container and cook it at 180 degrees for 40-45 minutes, first six. Let's cook until."
 def make(self):
   print(f" {self.name}'s Ingredients...")
   for i in range(1):
    print(f"3 {self.ingredients[i]}")
    print(f"2 cups {self.ingredients[i+1]}")
    print(f"half a glass of  {self.ingredients[i+2]}")
    print(f"1 glass of  {self.ingredients[i+3]}")
    print(f"1  {self.ingredients[i+4]}")
    print(f"1  {self.ingredients[i+5]}")
    print(f"1  {self.ingredients[i+6]}")

   print(f" {self.name} Making ...")  
   print(self.making)
  

class vegatable(food):
 def __init__(self,name):
   super().__init__(name)
   self.ingredients = ["beans","onion","oil","tomato","tomato past"]
   self.making="Let's sort and chop the fresh beans after washing them.Let's pour olive oil into the pressure cooker. Let's chop the onions. After the onions are roasted, add the tomato paste, chopped tomatoes, fresh beans and spices. Let's cook it on low heat for 5-6 minutes.Let's add about 3 cups of water and close the pressure cooker lid.Let's cook it for 15 minutes. Bon Appetit."
 def make(self):
   print(f" {self.name}'s Ingredients...")
   for i in range(1):
    print(f"1 kg {self.ingredients[i]}")
    print(f"1 {self.ingredients[i+1]}")
    print(f"a half glass of {self.ingredients[i+2]}")
    print(f"1 {self.ingredients[i+3]}")
    print(f"1 spoon  {self.ingredients[i+4]}")
   print(f" {self.name} Making ...")  
   print(self.making)  

s=soup("Lentil")
s.make()
s.cooking()
print("------------------------------------")   


d=dessert("Cake")
d.make()
d.cooking()
print("------------------------------------")   

v=vegatable("Bean")
v.make()
v.cooking()



