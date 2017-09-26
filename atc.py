#!/usr/bin/env python


#Max 80 Level
#Define a function named main() that contains your main program
#Create a function named extractData that takes a line of input and uses the split() function you developed in lab 3 to parse it into the five components.
#Create another function named buildTableRow that takes several parameters with the information for one row of the table and creates a properly formed HTML string for the row. Use this function to generate your output table.


def extractData(coords: str) -> (str, float, float, float, float):
    """ takes the input from user and gets it ready to extract.
    preconditons:
    postcondions:
    """
    aircraft_type = coords.split(":", 1)
    x_coord, y_coord, heading, speed = aircraft_type[1].split(",")

    return aircraft_type, float(x_coord), float(y_coord), float(heading), float(speed)


def buildTableRow(aircraft_type: str, x_coord: float, y_coord: float, heading: float, speed: float) -> (str):
    row = "<tr><td>1</td><td>{0}.png</td><td>({1},{2})</td><td>{3}</td><td>{4}</td></tr>".format(
        aircraft_type, str(x_coord), str(y_coord), str(heading), str(speed))
    return row


def createHTMLFile(input):

    tableRows = ""

    for item in input:
        tableRows += buildTableRow(item.get("aircraft"), item.get("x"),
                                   item.get("y"), item.get("heading"), item.get("speed"))

    htmlSource = """
      <html>
      <head>
          <style>
              table, td, th {
                  border: thin solid black;
                  margin: 0px;
                  padding: 10px;
                  border-collapse: collapse;
                  text-align: center;
                  border-color: white;            
              }
              th {   background-color: green;  }
              table {  display: table-inline;  }
              body {
                  font: arial;
                  background: black;
                  color: white;
              }
              h3 {
                  color: green;
              }
          </style>
      </head>
      <body>
          <div align='center'>
          <img src='atclogo.jpg'> 
          <h3>by Stephen Schaub</h3>
          <table>
              <tr>
                  <th>Id</th><th>Type</th><th>Position</th><th>Heading</th>
                  <th>Speed</th>
              </tr>

            {cpivara}
        

          </table>
          <br><br>
          </div>

            <p><i>Tips:
            <ul>
                <li> Right-click this page when viewing it in Chrome or Firefox and choose View Page Source to see the HTML you need to generate.</li>
                <li>Right-click each image and choose <b>"Save image as"</b> to download to your computer.
            </ul>
            </i></p>
            </body>
            </html>""".replace("{cpivara}", tableRows)

    capir = input("Testing!!!")

    return ""


# def test_extractDataInput():
#     assert extractDataInput("duck:100.15,25.2,0,550") == (aircraft_type, x_coord, y_coord, heading, speed)

def main():
    """ the main program"""

    aircraft_types = []

    print("Please enter the following information as specified: aircraft-type:x-coord,y-coord,heading,speed")

    #extractDataInput = input("Please enter the following information as specified: aircraft-type:x-coord,y-coord,heading,speed")
    extractDataInput = "duck:100.15,25.2,0,550"

    while extractDataInput != "":
        aircraft, x, y, heading, speed = extractData(extractDataInput)
        aircraftObj = {"aircraft": aircraft, "x": x,
                       "y": y, "heading": heading, "speed": speed}

        aircraft_types.append(aircraftObj)

        extractDataInput = input("Enter text:")


    print("cpaivara")

    shishi = createHTMLFile(aircraft_types)

    # def buildTableRow():
    #     precondition:
    #     Postcondition:
    return ''


if __name__ == "__main__":
    main()
