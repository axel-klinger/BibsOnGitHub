import json

html_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="scripts/filter.js"></script>
        <link rel="stylesheet" type="text/css" href="scripts/custom.css">
    </head>
    <body>

        <h2>Libraries on GitHub</h2>
        <p>Type something in the input field to search the table for libraries</p>
        <input id="myInput" type="text" placeholder="Search ...">
        <br><br>

<table>
  <thead>
  <tr>
    <th>Country</th>
    <th>City</th>
    <th>Organisation</th>
    <th>Repositories</th>
  </tr>
  </thead>
  <tbody id="myTable">
  '''
with open("all-libs.json", 'r') as json_file:
    data = json.load(json_file)
    for org in data["organisations"]:
        html_string += "<tr><td>" + org['country'] + "</td><td>" + org['city'] + "</td><td><a href=\"" + org['url'] + "\">" + org['name'] + "</a></td><td>" + str(len(org['repositories'])) + "</td></tr>\n"

html_string += '''
  </tbody>
</table>
</body>
'''
with open('libraries.html', 'w', encoding='utf8') as html_file:
    html_file.write(html_string)
