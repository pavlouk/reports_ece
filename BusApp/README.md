# Bus Company Database Application

## Installation

Download the project, then create and activate virtual environment in the project directory.

In order to create and activate a Python virtual environment in the project directory, use your systems default Python3 environment

```shell
$ python -m venv .venv
$ source .venv/bin/activate # on Linux, or
$ ./venv/Scripts/activate # on Windows
```

After activating the virtual environment it is common for a `(.venv)` prefix to exist in the terminal line.

Next install the dependencies defined in `requirements.txt`

```shell
$ pip install -r requirements.txt
```

This installs the project libraries below

| Name  | Description                                                  | Link                                             |
| ----- | ------------------------------------------------------------ | ------------------------------------------------ |
| Typer | Library for building CLI applications                        | https://typer.tiangolo.com/                      |
| Rich  | Library for writing *rich* text (with color and style) to the terminal | https://rich.readthedocs.io/en/stable/index.html |
| Faker  | Library that generates fake data for you | https://faker.readthedocs.io/en/master/ |

## Utilities

In order to view the CLI commands use the help flag. 

```shell
$ python main.py --help
```

**Side note:** The command above populates the `bus.db` file with fake data generated with the Faker library

The available command utilities

```
company-balance                       Show Total income of the company                       
create-card                           Creates Personal Card                                  
disembark-ticket                      Disembark Bus with Personal Card                       
embark-ticket                         Embark Bus with Personal Card                          
get-card                              Shows Personal Card Info                               
get-itinerary-info                    Shows Selected Itinerary's Info                        
get-stop-bus-arrivals                 Shows Bus Stop Info                                    
get-stop-info                         Shows Bus Stop Info                                    
purchase-balance                      Purchase balance to Personal Card 
```

## Example

This example shows the fake itineraries in the database

```shell
$ python main.py get-itinerary-info
```

```
┃ id ┃ Starting Time    ┃      Ending Time ┃ Direction ┃       Route Name ┃ Bus id ┃ Driver id ┃
│ 1  │ 2024-01-14       │       2024-01-14 │         1 │    ΚΙΛΚΊΣ - ΧΊΟΣ │      1 │         6 │
│    │ 01:47:25.462259  │  02:12:25.462259 │           │                  │        │           │
│ 2  │ 2024-01-14       │       2024-01-14 │         0 │       ΚΟΜΟΤΗΝΉ - │      7 │         3 │
│    │ 01:47:25.470324  │  02:15:25.470324 │           │           ΈΔΕΣΣΑ │        │           │
│ 3  │ 2024-01-14       │       2024-01-14 │         1 │       ΙΩΆΝΝΙΝΑ - │      4 │         4 │
│    │ 01:47:25.477923  │  01:59:25.477923 │           │        ΜΕΣΟΛΌΓΓΙ │        │           │
│ 4  │ 2024-01-14       │       2024-01-14 │         1 │ ΛΙΒΑΔΙΆ - ΚΟΖΆΝΗ │      9 │         3 │
│    │ 01:47:25.486853  │  02:16:25.486853 │           │                  │        │           │
│ 5  │ 2024-01-14       │       2024-01-14 │         1 │ ΧΑΝΙΆ - ΚΑΛΑΜΆΤΑ │     10 │         8 │
│    │ 01:47:25.494468  │  02:05:25.494468 │           │                  │        │           │
│ 6  │ 2024-01-14       │       2024-01-14 │         0 │        ΛΕΥΚΆΔΑ - │      5 │         7 │
│    │ 01:47:25.502630  │  02:08:25.502630 │           │         ΚΑΣΤΟΡΙΆ │        │           │
│ 7  │ 2024-01-14       │       2024-01-14 │         0 │      ΠΟΛΎΓΥΡΟΣ - │      4 │         5 │
│    │ 01:47:25.510155  │  02:10:25.510155 │           │      ΗΓΟΥΜΕΝΊΤΣΑ │        │           │
│ 8  │ 2024-01-14       │       2024-01-14 │         0 │      ΜΕΣΟΛΌΓΓΙ - │     10 │         5 │
│    │ 01:47:25.516923  │  01:57:25.516923 │           │            ΒΌΛΟΣ │        │           │
│ 9  │ 2024-01-14       │       2024-01-14 │         1 │   ΚΑΒΆΛΑ - ΒΌΛΟΣ │      4 │         9 │
│    │ 01:47:25.523843  │  02:00:25.523843 │           │                  │        │           │
│ 10 │ 2024-01-14       │       2024-01-14 │         0 │ ΧΊΟΣ - ΑΡΓΟΣΤΌΛΙ │      9 │         3 │
│    │ 01:47:25.531992  │  02:15:25.531992 │           │                  │        │           │
```

