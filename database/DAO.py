from database.DB_connect import DBConnect
from model.arco import Arco
from model.genre import Genre


class DAO():
    def __init__(self):
        pass



    #esiste un arco tra due artisti se almeno un cliente ha acquistato brani da entrambi gli artisti
    #con verso da A a B se la popolarità di A è maggiore di B
    #se hanno la stessa popolarità , aggiungere due archi in entrambi i versi
    #popolarità: somma di tutti i brani acquistati di quell'artista
    # Usare le tabelle invoceline e invoce per determinare gli acquisti dei clienti.
    #peso arco tra a e b : somma delle rispettive popolarità



    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []  # lista di generi

        query = """select *
                   from genre g
                             """

        cursor.execute(query, )
        # unpack si può fare quando ti selezioni tutti gli attributi e ti crei l'oggetto intero
        for row in cursor:
            res.append(
                Genre(**row))  # (**row) UNPACK significa:  res.append(ArtObject(object_id=row["object_id], ....)

        cursor.close()
        conn.close()
        return res

    # i vertici sono gli artisti che possiedono almeno un brano Track appartenente al genere selezionato
    @staticmethod
    def getAllNodes(genere_id):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []  # lista di generi

        query = """select a.*
                    from artist a
                    where a.ArtistId in (select ab.ArtistId
                    from track t , album ab
                    where t.AlbumId = ab.AlbumId 
                    and t.GenreId = %s)
                                """

        cursor.execute(query, (genere_id,))
        # unpack si può fare quando ti selezioni tutti gli attributi e ti crei l'oggetto intero
        for row in cursor:
            res.append(
                Genre(**row))  # (**row) UNPACK significa:  res.append(ArtObject(object_id=row["object_id], ....)

        cursor.close()
        conn.close()
        return res

    # esiste un arco tra due artisti se almeno un cliente ha acquistato brani da entrambi gli artisti
    # con verso da A a B se la popolarità di A è maggiore di B
    # se hanno la stessa popolarità , aggiungere due archi in entrambi i versi
    # popolarità: somma di tutti i brani acquistati di quell'artista
    # Usare le tabelle invoceline e invoce per determinare gli acquisti dei clienti.
    # peso arco tra a e b : somma delle rispettive popolarità
    @staticmethod
    def getAllEdges(genere_id):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []  # lista di generi

        query = """select c1.artista as, c2.artista 	 
                    from (select distinct a.ArtistId as artista, i.CustomerId as cliente
                                from album a, track t, invoiceline il, invoice i
                                where a.AlbumId = t.AlbumId  and t.TrackId = il.TrackId and i.InvoiceId = il.InvoiceId
                                and t.GenreId = %s) as c1,
                                (select distinct a.ArtistId as artista, i.CustomerId as cliente
                                from album a, track t, invoiceline il, invoice i
                                where a.AlbumId = t.AlbumId  and t.TrackId = il.TrackId and i.InvoiceId = il.InvoiceId 
                                and t.GenreId=%s) as c2
                    where c1.cliente = c2.cliente and c1.artista < c2.artista
                    order by c1.artista
                                    """

        cursor.execute(query, (genere_id,genere_id))
        # unpack si può fare quando ti selezioni tutti gli attributi e ti crei l'oggetto intero
        for row in cursor:
            res.append(
                Arco(**row))  # (**row) UNPACK significa:  res.append(ArtObject(object_id=row["object_id], ....)

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getPesoEdges(genere_id):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []  # lista di generi

        query = """select count(*) as popolarita, ab.ArtistId as ArtistId
                    from invoice i, invoiceLine il, track t,album ab 
                    where i.InvoiceId = il.InvoiceLineId and t.TrackId = il.trackId  and ab.AlbumId = t.AlbumId 
                    and t.GenreId = 2 
                                                          """

        cursor.execute(query, (genere_id,))

        for row in cursor:
            res.append((row["popolarita"],row["ArtistId"]))   #lista di tuple (popolarotà, artista)

        cursor.close()
        conn.close()
        return res
