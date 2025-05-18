import datetime

def format_macro_message(date, macros):
    """
    Formats a clean WhatsApp message with the date and macro summary.
    """
    return (
        f"MyFitnessPal Macros for {date.strftime('%Y-%m-%d')}\n"
        f"Calories: {macros['calories']}\n"
        f"Protein: {macros['protein']}g\n"
        f"Carbs: {macros['carbohydrates']}g\n"
        f"Fat: {macros['fat']}g"
    )

# Placeholder for future AI/ML utilities
def analyze_meal_image(image_path):
    """
    Future feature: Analyze meal images for calorie estimation using AI.
    """
    pass
