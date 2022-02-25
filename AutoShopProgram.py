import Classes as Cust
import Classes as Car
import Classes as Serv


def main():
    # create instance of the Car Class
    make = "BMW"
    model = "X2"
    year = "2021"

    bmw = Car.Car(make, model, year)
    print("Make:", bmw.get_make())
    print("Model:", bmw.get_model())
    print("Year:", bmw.get_year() + "\n")

    # create instance of the Service Quote Class
    pcharge = 500
    lcharge = 250

    servQuote = Serv.ServiceQuote(pcharge, lcharge)
    print("Parts Charges: $" + format(servQuote.get_parts_charges(), ",.2f"))
    print("Labor Charges: $" + format(servQuote.get_labor_charges(), ",.2f"))
    print("Total Charges: $" + format(servQuote.get_total_charges(), ",.2f"))


main()
