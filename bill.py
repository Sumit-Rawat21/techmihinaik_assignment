import random
user_details = {
    "Name": "Sumit Rawat",
    "delivery_address": "INA colony, ND",
    "Email_id": "sumit21cr@gmail.com",
    "Contact_number": 8826743883,
    "Payment_mode": "COD"

}

package_details = {
    "shipping_address": "Maharashtra,India",
    "pincode": 320023,
    "package_ID": 11225,
    "height": 10,
    "width": 15,
    "lenght": 5,
    "weight": 25
}


class ShippeR:

    def __init__(self, package_details):
        self.shipping_address = package_details["shipping_address"]
        self.pincode = package_details["pincode"]
        self.package_ID = package_details["package_ID"]
        self.height = package_details["height"]
        self.width = package_details["width"]
        self.lenght = package_details["lenght"]
        self.weight = package_details["weight"]

    def shipmentBooking(self, weight=25):
        shipment_cost = 10 * weight
        AWB = random.randint(1000000, 9999999)

        return shipment_cost, AWB


def Billing(details):
    print("\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       /   INVOICE   /        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for k in details:
        print("\t\t", k, ":", details[k])

    print("\t\t", "Package ID:", obj1.package_ID)
    print("\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t", "Shipping Cost:", shipment_cost)
    print("\t\t", "Service Cost 3%:", 0.03*shipment_cost)
    print("\t\t", "CGST 2.5%:", 0.025*shipment_cost)
    print("\t\t", "SGST 2.5%:", 0.025*shipment_cost)
    total = shipment_cost+(0.03*shipment_cost)+2*(0.025*shipment_cost)
    print("\t\t", "- - - - - - - - - - - - - - -")
    print("\t\t", "Grand Total:", total)
    print("\t\t", "- - - - - - - - - - - - - - -")


obj1 = ShippeR(package_details)
shipment_cost, AWB = obj1.shipmentBooking()
Billing(user_details)
