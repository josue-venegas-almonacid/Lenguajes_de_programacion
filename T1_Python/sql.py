import interpreter as inter
import pyql


def main():
    database = pyql.database()

    while True:
        tokens = inter.parser(inter.tokenizer(input("Query: ")))
        if tokens != None:
            query = pyql.query(tokens)
            database.do_query(query)

if __name__ == '__main__':
    main()
