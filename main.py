# This is a sample Python script.
import requests

import products
import os


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

path = "https://co2.prom.ua/yandex_market.xml?hash_tag=e82bf7608985d3938a9543608bdd398f&sales_notes=&product_ids=&label_ids=7677794%2C7723458%2C7722434%2C6385601&exclude_fields=description&html_description=0&yandex_cpa=&process_presence_sure=&languages=ru&group_ids="
if __name__ == '__main__':
    print_hi('PyCharm')
    products = products.XmlPromProductService.package_images(path)

    for product in products:

        packageName = "images/" + product.name + "_" + product.id

        os.mkdir(packageName)

        for imageUrl in product.images:
            response = requests.get(imageUrl)
            with open(packageName + imageUrl[imageUrl.rfind("/"):], 'wb') as imgFile:
                imgFile.write(response.content)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
