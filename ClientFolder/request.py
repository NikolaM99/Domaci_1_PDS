
import requests

r = requests.post('http://localhost:8081/users',json={

    "ime":"Nikola",
    "prezime":"Martinovic",
    "username":"nmartinovic",
    "smer":"RI",
    "predmeti": [
                    {"ime":"Racunarske Mreze","espb":8},
                    {"ime":"Bezbednost Mreza","espb":6},
                    {"ime":"Tehnologije komutiranja","espb":6},
                    {"ime":"Tehnologije rutiranja","espb":6},
                ]



    
})