import matplotlib.pyplot as plt

#gráfico de torta
def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,34,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #Para guardar la gráfica en una imagen('nom_image')
    plt.savefig('pie.png')
    plt.close()

generate_pie_chart()