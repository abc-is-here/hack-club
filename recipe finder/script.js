document.getElementById('search').addEventListener('click', function() {
    const ingredients = document.getElementById('ingredients').value.split(',').map(ing => ing.trim());
    if (ingredients.length > 0) {
        fetchRecipes(ingredients);
    }
});

async function fetchRecipes(ingredients) {
    const apiUrl = 'https://www.themealdb.com/api/json/v1/1/filter.php?i=';
    const requests = ingredients.map(ingredient => fetch(apiUrl + ingredient).then(response => response.json()));

    try {
        const results = await Promise.all(requests);
        const allMeals = results.map(result => result.meals).filter(meals => meals !== null);

        if (allMeals.length === 0) {
            displayRecipes([]);
            return;
        }

        // Find common recipes
        let commonRecipes = allMeals[0];
        for (let i = 1; i < allMeals.length; i++) {
            commonRecipes = commonRecipes.filter(recipe1 => 
                allMeals[i].some(recipe2 => recipe1.idMeal === recipe2.idMeal)
            );
        }

        displayRecipes(commonRecipes);
    } catch (error) {
        console.error('Error fetching recipes:', error);
    }
}

function displayRecipes(recipes) {
    const recipesContainer = document.getElementById('recipes');
    recipesContainer.innerHTML = '';

    if (recipes.length > 0) {
        recipes.forEach(recipe => {
            const recipeElement = document.createElement('div');
            recipeElement.classList.add('recipe');
            recipeElement.innerHTML = `
                <h3>${recipe.strMeal}</h3>
                <img src="${recipe.strMealThumb}" alt="${recipe.strMeal}">
            `;
            recipesContainer.appendChild(recipeElement);
        });
    } else {
        recipesContainer.innerHTML = '<p>No recipes found.</p>';
    }
}
