import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._genere= None

    def fillDDGenre(self):
        #riempi il dropdown con tutti i generi
        generi = self._model.getAllGeneri()
        for g in generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(text=g.Name,
                                                                  data=g,
                                                                  on_click=self.read_genere))
        self._view.update_page()

    def read_genere(self,e):
        if e.control.data == None:
            self._genere = None
        else:
            self._genere=e.control.data

    def handleCreaGrafo(self, e):
        pass

    def handleCreaGrafo(self,e):
        pass

    def handleCammino(self,e):
        pass