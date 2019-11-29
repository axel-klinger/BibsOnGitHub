import json

html_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script>
        $(document).ready(function(){
          $("#myInput").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            $("#myTable tr").filter(function() {
              $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
          });
        });
        </script>
        <style>
        table {
          font-family: arial, sans-serif;
          border-collapse: collapse;
          width: 100%;
        }

        td, th {
          border: 1px solid #dddddd;
          text-align: left;
          padding: 8px;
        }

        tr:nth-child(even) {
          background-color: #dddddd;
        }
        </style>
    </head>
    <body>

        <h2>Library Repositories on GitHub</h2>
        <p>Type something in the input field to search the table for projects</p>
        <input id="myInput" type="text" placeholder="Search ...">
        <br><br>

<table>
  <thead>
  <tr>
    <th>Organisation</th>
    <th>Repository</th>
    <th>License</th>
    <th>Stars</th>
    <th>Forks</th>
    <th>Forked</th>
    <th>Last updated</th>
  </tr>
  </thead>
  <tbody id="myTable">
  '''
with open("all-libs.json", 'r') as json_file:
  data = json.load(json_file)
  for org in data["organisations"]:
      for repo in org['repositories']:
          # print(type(repo))
          if type(repo) is dict:
              if str(repo['license']) != "None":
                  license = repo['license']['spdx_id']
              else:
                  license = " "
              html_string += "<tr><td>" + org['name'] + "</td><td><a href=\"" + repo['html_url'] + "\">" + repo['name'] + "</a></td><td>" + license + "</td><td>" + str(repo['stargazers_count']) + "</td><td>" + str(repo['forks_count']) + "</td><td>" + str(repo['fork']) + "</td><td>" + repo['updated_at'] + "</td></tr>\n"

html_string += '''
  </tbody>
</table>
</body>
'''
with open('repositories.html', 'w', encoding='utf8') as html_file:
    html_file.write(html_string)
