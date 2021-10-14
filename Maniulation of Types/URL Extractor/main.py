# Fazer um código que auxilie a identificar os itens em uma URL

from URL_extractor import URL_extractor

def main():
    url1 = URL_extractor("www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100", "bytebank", ".com")
    url2 = URL_extractor("www.bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100", "bytebank", ".com")

    
    print(url1 == url2)
    print(len(url1))
    for i in url1:
        print(i)
    
    print(url1.get_parameter_value("moedaDestino"))
    print(url1.find_value_parameter("real"))
    print(url1)

    url1.url = "https://bytebank.com/cambio?moedaOrigem=real"
    print(url1)

if __name__ == "__main__":
    main()