import flet as ft

import database.DAO



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        distance = self._view._txtIn.value
        self.airports = database.DAO.DAO().getAllNodes()
        self.flights = database.DAO.DAO().getAllFlights()
        dizionario = self._model.buildGraphs(distance)
        for i in dizionario:
            self._view._txt_result.controls.append(
                ft.Text(f"Nodo: {i} Distanza media: {dizionario[i]}"))
            self._view.update_page()