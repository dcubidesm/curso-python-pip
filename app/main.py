#2.
#__name__, __main__ : Esto permite crear la dualidad entre los diferentes
#módulos(.py) es decir, si se ejecutan por aparte main
#y example DEBE ejecutarse independientemente, siempre y cuando sea desde la terminal.

#Es decir que se puede ejecutar como un script e importandolo desde otro archivo.
import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  '''


if __name__ == '__main__':
  run()
