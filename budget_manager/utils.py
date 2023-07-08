import matplotlib.pyplot as plt


def create_plt(*args):
    """This function creates a bar plot to visualize expenses and revenues.
    It takes arguments for the values and plots them accordingly."""
    try:
        fig = plt.figure(figsize=(8, 5))
        plt.bar(['Wydatki', 'Przychody'], args, color=['red', 'green'], width=0.4)
        plt.xlabel('Rodzaj')
        plt.ylabel('Wartość')
        plt.title('Bilans finansów')
        plt.savefig('budget_manager/static/budget_manager/expense.jpg')
    except TypeError:
        print('Brak danych')
