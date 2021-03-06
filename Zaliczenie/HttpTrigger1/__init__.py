import pyodbc
import azure.functions as func
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    cardCode = req.get_json()
    wartosc = cardCode["cardCode"]
    cardCodestring = str(wartosc)
    # logging.info (type(cardCodestring))
    peopleConString = os.getenv('PeopleConString')
    # logging.info(f'conString {peopleConString}')

    with pyodbc.connect(peopleConString) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cardcode from People")
            row = cursor.fetchone()
            flag = 0
            while row:
                # logging.info (str(row[0]))
                if cardCodestring == row[0]:
                    flag = 1
                row = cursor.fetchone()

    if flag == 0:
        return func.HttpResponse("Zla karta", status_code=403)
    if flag == 1:
        return func.HttpResponse('Dobra karta', status_code=200)