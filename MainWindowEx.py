import sys
import pandas as pd
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("MainWindow.ui", self)

        self.data = pd.read_csv("emp.csv")
        self.data['Dob'] = pd.to_datetime(self.data['Dob'], format='%d/%m/%Y')

        self.load_data()

        self.pushButton2001.clicked.connect(self.filter_born_2001)
        self.pushButtontop3.clicked.connect(self.export_top_3_oldest)
        self.pushButtonrole.clicked.connect(self.filter_tester_role)
        self.pushButtoncount.clicked.connect(self.count_roles)

    def load_data(self):
        self.display_data(self.data)

    def display_data(self, df):
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(df.iat[row, col])))

    def filter_born_2001(self):
        df_filtered = self.data[self.data['Dob'].dt.year == 2001]
        self.display_data(df_filtered)

    def export_top_3_oldest(self):
        df_sorted = self.data.sort_values(by='Dob').head(3)
        self.display_data(df_sorted)

    def filter_tester_role(self):
        df_filtered = self.data[self.data['Role'] == "Tester"]
        self.display_data(df_filtered)

    def count_roles(self):
        role_counts = self.data['Role'].value_counts().reset_index()
        role_counts.columns = ['Role', 'Count']
        self.display_data(role_counts)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())