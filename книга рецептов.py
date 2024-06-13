from tkhtmlview import HTMLLabel
import tkinter as tk

def show_recipe():
    selected_recipe = recipe_listbox.get(tk.ACTIVE)
    if selected_recipe in recipes:
        recipe_text.set_html(recipes[selected_recipe])
    else:
        recipe_text.set_html("<h3>Нет информации о выбранном рецепте</h3>")

recipes = {
    "Первые блюда": "<a href='https://www.russianfood.com/recipes/bytype/?fid=2'>Первые блюда.</a>",
    "Вторые блюда": "<a href='https://www.russianfood.com/recipes/bytype/?fid=3'>Вторые блюда.</a>",
    "Десерты": "<a href='https://www.russianfood.com/recipes/bytype/?fid=45'>Десерты.</a>",
    "Заготовки": "<a href='https://www.russianfood.com/recipes/bytype/?fid=8'>Заготовки.</a>",
    "Закуски": "<a href='https://www.russianfood.com/recipes/bytype/?fid=6'>Закуски.</a>",
    "Изделия из теста": "<a href='https://www.russianfood.com/recipes/bytype/?fid=5'>Изделия из теста.</a>",
    "Маринад": "<a href='https://www.russianfood.com/recipes/bytype/?fid=1535'>Маринад.</a>",
    "Напитки": "<a href='https://www.russianfood.com/recipes/bytype/?fid=4'>Напитки.</a>",
    "Соуса": "<a href='https://www.russianfood.com/recipes/bytype/?fid=9'>Соуса.</a>"
}

root = tk.Tk()
root.title("Справочник рецептов")
root.geometry("900x700")

recipe_listbox = tk.Listbox(root)
recipe_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

recipe_scrollbar = tk.Scrollbar(root)
recipe_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

recipe_listbox.config(yscrollcommand=recipe_scrollbar.set)
recipe_scrollbar.config(command=recipe_listbox.yview)

for recipe in recipes:
    recipe_listbox.insert(tk.END, recipe)

recipe_text = HTMLLabel(root, font=("Arial", 20, "bold", "italic"), width=50, foreground="red")
recipe_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

recipe_listbox.bind("<<ListboxSelect>>", lambda event: show_recipe())

root.mainloop()
