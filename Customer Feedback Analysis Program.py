import os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import re
import csv
import datetime

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 800))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ExportCSV = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ExportCSV.setGeometry(QtCore.QRect(400, 380, 181, 51))
        self.ExportCSV.setObjectName("ExportCSV")
        self.SentimentText = QtWidgets.QLabel(parent=self.centralwidget)
        self.SentimentText.setGeometry(QtCore.QRect(400, 240, 801, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SentimentText.setFont(font)
        self.SentimentText.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.SentimentText.setWordWrap(True)
        self.SentimentText.setObjectName("SentimentText")
        self.FMTHeader_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.FMTHeader_2.setGeometry(QtCore.QRect(400, 200, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.FMTHeader_2.setFont(font)
        self.FMTHeader_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.FMTHeader_2.setObjectName("FMTHeader_2")
        self.FMTHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.FMTHeader.setGeometry(QtCore.QRect(400, 100, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.FMTHeader.setFont(font)
        self.FMTHeader.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.FMTHeader.setObjectName("FMTHeader")
        self.Topics = QtWidgets.QLabel(parent=self.centralwidget)
        self.Topics.setGeometry(QtCore.QRect(400, 140, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Topics.setFont(font)
        self.Topics.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.Topics.setWordWrap(True)
        self.Topics.setObjectName("Topics")
        self.Analysis = QtWidgets.QLabel(parent=self.centralwidget)
        self.Analysis.setGeometry(QtCore.QRect(400, 40, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Analysis.setFont(font)
        self.Analysis.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.Analysis.setObjectName("Analysis")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(400, 180, 851, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(400, 340, 851, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(400, 80, 851, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.AboutHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.AboutHeader.setGeometry(QtCore.QRect(40, 40, 280, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.AboutHeader.setFont(font)
        self.AboutHeader.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.AboutHeader.setObjectName("AboutHeader")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 80, 280, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.AboutText = QtWidgets.QLabel(parent=self.centralwidget)
        self.AboutText.setGeometry(QtCore.QRect(40, 100, 280, 351))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AboutText.setFont(font)
        self.AboutText.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.AboutText.setWordWrap(True)
        self.AboutText.setObjectName("AboutText")
        self.UploadFileButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.UploadFileButton.setGeometry(QtCore.QRect(40, 481, 280, 51))
        self.UploadFileButton.setObjectName("UploadFileButton")
        self.AnalyseButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.AnalyseButton.setGeometry(QtCore.QRect(40, 540, 280, 51))
        self.AnalyseButton.setObjectName("AnalyseButton")
        self.ErrorMessage = QtWidgets.QLabel(parent=self.centralwidget)
        self.ErrorMessage.setGeometry(QtCore.QRect(40, 600, 280, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ErrorMessage.setFont(font)
        self.ErrorMessage.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.ErrorMessage.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.ErrorMessage.setWordWrap(True)
        self.ErrorMessage.setObjectName("ErrorMessage")
        self.FileStatus = QtWidgets.QLabel(parent=self.centralwidget)
        self.FileStatus.setGeometry(QtCore.QRect(40, 640, 280, 121))
        self.FileStatus.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.FileStatus.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom
            | QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
        )
        self.FileStatus.setWordWrap(True)
        self.FileStatus.setObjectName("FileStatus")
        self.line_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(350, 80, 21, 681))
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(40, 460, 280, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Buttons
        self.UploadFileButton.clicked.connect(self.uploadFileClicked)
        self.AnalyseButton.clicked.connect(self.analyseButtonClicked)
        self.ExportCSV.clicked.connect(self.exportCSVClicked)

        # Variables
        self.SelectedFilePath = None
        self.FileAnalysed = False
        self.ErrorMessageText = ""
        self.Top10Words = ""
        self.CorrectFile = False




    def setFileStatus(self, message, colour=None):
        # Generate HTML Code With The Message And Color For Convenience
        style = f' style="font-weight:600; color:{colour};"' if colour else ' style="font-weight:600;"'
        return f'<html><head/><body><p><span{style}>File:</span><br/>{message}</p></body></html>'

    def setErrorMessage(self, message, colour=None):
        style = f' style="font-weight:600; color:{colour};"' if colour else ' style="font-weight:600;"'
        return f'<html><head/><body><p><span{style}>{message}</span></p></body></html>'




    def FileFormatChecker(self):
        """
        Check If The Selected File Has The Correct Format.

        Steps:
        1. Check If A File Has Been Selected. If Not, Set `self.CorrectFile` To False And Return False.
           ↪ If No File Has Been Selected, There Is No File To Check. Therefore, The Function Returns False.

        2. Read The Selected File And Store Its Contents In The `lines` Variable.

        3. To Check If The File Is Empty, Check If The Number Of Lines Is Zero.
           ↪ If The File Is Empty, Set `self.CorrectFile` To False And Return False.

        4. Iterate Over The Lines With A Step Size Of 2 (To Check Every Other Line). 
           ↪ This Is Because The File Format Is Expected To Have A Review On Ever Odd Line.

           ↪ For Each Line, Strip Any Leading Or Trailing Whitespace And Store It In The `line` Variable.

           ↪ Check If The Line Is Empty Or Does Not Start And End With Double Quotes.
                ↪ If The Line Is Empty Or Does Not Start And End With Double Quotes, Set `self.CorrectFile` To False And Return False.
                ↪ If The Line Is Not Empty And Starts And Ends With Double Quotes, Continue To The Next Step.

        5. If All Lines Pass The Format Check, Set `self.CorrectFile` To True And Return True.
           ↪ The 'self.CorrectFile' Variable Is Used To Check If The File Format Is Correct Withtin The `analyseButtonClicked` Function.
        """
        if not self.SelectedFilePath:
            self.CorrectFile = False
            return False

        with open(self.SelectedFilePath, 'r') as file:
            lines = file.readlines()

        if len(lines) == 0:
            self.CorrectFile = False
            return False

        for i in range(0, len(lines), 2):
            line = lines[i].strip()

            if line == '' or not line.startswith('"') or not line.endswith('"'):
                self.CorrectFile = False
                return False

        self.CorrectFile = True
        return True




    def uploadFileClicked(self):
        """
        This Function Is Called When The Upload File Button Is Clicked.

        Steps:
        1. Open A File Picker And Store The Selected File Path In The `fileName` Variable.
           ↪ If No File Was Selected, Return Nothing.

        2. Check If The Selected File Has A .TXT Extension.
           ↪ If The Selected File Does Not Have A .TXT Extension, Display An Error Message And Return Nothing.
           ↪ If The Selected File Has A .TXT Extension, Continue To The Next Step.

        3. Check If The Selected File Is The Same As The Previously Selected File.
           ↪ If The Selected File Is The Same As The Previously Selected File, Return Nothing.
            # This Is To Prevent The File From Being Re-Read If The Same File Is Selected.
           ↪ If The Selected File Is Not The Same As The Previously Selected File, Reset The Top 10 Words Text.

        4. Set The Selected File Path To The `self.SelectedFilePath` Variable.

        5. Set The File Status Text To The Selected File Name.

        6. Check If The File Format Is Correct Using The `FileFormatChecker` Function.

        7. If The File Format Is Correct, Display A Success Message And Return Nothing.

        8. By Default, Reset The Error Message Text, Sentiment Analysis Text, Top 10 Words Text & Sentiment Analysis Flag.
        """

        fileName, _ = QFileDialog.getOpenFileName(None, "Select File", "", "Text Files (*.txt)")

        FileStatusText = self.setFileStatus('No file selected', colour=None)
        SentimentAnalysisText = '<html><head/><body><p>Positive:</p><p>Negative:</p><p>Neutral:</p></body></html>'

        if fileName:

            if fileName.lower().endswith('.txt'):
                if self.SelectedFilePath != fileName: 
                    self.Top10Words = ''

                self.SelectedFilePath = fileName

                FileStatusText = self.setFileStatus(os.path.basename(fileName))
                ErrorMessageText = self.setErrorMessage('File Uploaded Successfully.<br/>You Can Now Analyze Your File.', colour='#009402')

                if not self.FileFormatChecker():
                    ErrorMessageText = self.setErrorMessage('Error: File is not in the correct format.', colour='#ff0000')

            else:
                ErrorMessageText = self.setErrorMessage('Error: Invalid file type. Must be TXT.', colour='#ff0000')


        else:
            return

        self.FileStatus.setText(FileStatusText)
        self.ErrorMessage.setText(ErrorMessageText)
        self.Topics.setText(self.Top10Words)
        self.SentimentText.setText(SentimentAnalysisText)
        self.FileAnalysed = False




    def analyseButtonClicked(self):
        """
        This Function Is Called When The Analyse Button Is Clicked.

        Stepts:
        1. Check If A File Has Been Selected.
           ↪ If No File Has Been Selected, Display An Error Message And Return Nothing.
              ↪ If A File Has Been Selected, Continue To The Next Step.

        2. Check If The File Format Is Correct.
           ↪ Using The `FileFormatChecker` Function, We Now Know If The File Format Is Correct Due To The `self.CorrectFile` Variable.
           ↪ If The File Format Is Not Correct, Display An Error Message And Return Nothing.
                ↪ If The File Format Is Correct, Continue To The Next Step.

        3. Read The Selected File And Process The Reviews.

        4. Perform Sentiment Analysis On The Processed Reviews.

        5. Extract The Top 10 Words From The Processed Reviews.

        6. Calculate The Sentiment Analysis Percentage For Each Sentiment.

        7. Display The Sentiment Analysis Results And Top 10 Words.

        8. Set The `self.FileAnalysed` Variable To True.
            ↪ This Is Used To Check If The File Has Been Analysed Within The `exportCSVClicked` Function.

        9. Reset The Error Message Text Since The File Has Been Analysed And There Are No Errors.
        """
        if not self.SelectedFilePath:
            error_message = self.setErrorMessage('Error: No file selected.', colour='#ff0000')
            self.ErrorMessage.setText(error_message)
            return

        if not self.CorrectFile:
            error_message = self.setErrorMessage('Error: File is not in the correct format.', colour='#ff0000')
            self.ErrorMessage.setText(error_message)
            return

        with open(self.SelectedFilePath, 'r') as file:  # type: ignore
            FileArray = re.findall(r'"(.*?)"', file.read())

        lemmatizer = WordNetLemmatizer()
        ProcessedReviews = [
            ' '.join([
                lemmatizer.lemmatize(w)
                for w in word_tokenize(review.lower())
                if w.isalpha() and w not in stopwords.words('english')
            ])
            for review in FileArray
        ]

        AllReviews = ' '.join(ProcessedReviews)

        vectorizer = TfidfVectorizer()
        vector = vectorizer.fit_transform([AllReviews])

        if vector.shape[1] > 0:
            TopWords = vectorizer.get_feature_names_out()[
                vector.toarray().flatten().argsort()[-10:]
            ]
            self.Top10Words = ', '.join(TopWords)

        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(AllReviews)

        self.PositivePercentage = sentiment['pos'] * 100
        self.NegativePercentage = sentiment['neg'] * 100
        self.NeutralPercentage = sentiment['neu'] * 100

        SentimentAnalysisText = f"<html><head/><body><p>Positive: {self.PositivePercentage:.2f}%</p><p>Negative: {self.NegativePercentage:.2f}%</p><p>Neutral: {self.NeutralPercentage:.2f}%</p></body></html>"

        self.Topics.setText(self.Top10Words)
        self.SentimentText.setText(SentimentAnalysisText)

        self.FileAnalysed = True
        self.ErrorMessage.setText('')




    def exportCSVClicked(self):
        """
        This Function Is Called When The Export CSV Button Is Clicked.

        Steps:
        1. Check If The File Has Been Analysed.
           ↪ This Is Because We Need To Analyse The File Before We Can Export The CSV.
           ↪ If The File Has Not Been Analysed, Display An Error Message And Return Nothing.
             ↪ If The File Has Been Analysed, Continue To The Next Step.

        2. Get The Current Date And Time And Format It To Be Used As The Default File Name.

        3. Open A File Dialog And Get The File Path.

        4. Check If A File Path Was Selected.
           ↪ If A File Path Was Not Selected, Return Nothing.
             ↪ If A File Path Was Selected, Continue To The Next Step.

        5. Create The CSV File And Write The Data To It.
        """
        if not self.FileAnalysed:
            ErrorMessageText = self.setErrorMessage('Error: File analysis is required before exporting CSV.', colour='#ff0000')
            self.ErrorMessage.setText(ErrorMessageText)
            return

        current_datetime = datetime.datetime.now()
        file_name = current_datetime.strftime("%d-%b-%Y")

        FilePath, _ = QFileDialog.getSaveFileName(None, "Save CSV", file_name, "CSV Files (*.csv)")

        if FilePath:
            headers = ["Top 10 Words", "", "Positive Percentage", "Negative Percentage", "Neutral Percentage"]
            SeparatorRow = ["––––––––––––––", "–––––", "––––––––––––––––", "–––––––––––––––––", "––––––––––––––––"]
            DataRows = []
            for i, word in enumerate(self.Top10Words.split(", ")):
                DataRow = [word, "", "", "", ""]
                if i == 0:
                    DataRow[2] = f"{self.PositivePercentage:.2f}%"
                    DataRow[3] = f"{self.NegativePercentage:.2f}%"
                    DataRow[4] = f"{self.NeutralPercentage:.2f}%"
                DataRows.append(DataRow)

            with open(FilePath, "w", newline="", encoding="utf-8-sig") as csvfile:
                CsvWriter = csv.writer(csvfile)
                CsvWriter.writerow(headers)
                CsvWriter.writerow(SeparatorRow)
                CsvWriter.writerows(DataRows)

            ErrorMessageText = self.setErrorMessage('CSV file has been saved.', colour='#009402')
            self.ErrorMessage.setText(ErrorMessageText)







    # Sets The Text Of The UI Elements By Default When The Program Runs For The First Time
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Customer Feedback Analysis")
        )
        self.ExportCSV.setText(_translate("MainWindow", "Export CSV"))
        self.SentimentText.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Positive:</p><p>Negative:</p><p>Neutral:</p></body></html>",
            )
        )
        self.FMTHeader_2.setText(_translate("MainWindow", "Sentiment Score"))
        self.FMTHeader.setText(_translate("MainWindow", "Frequently Mentioned Topics"))
        self.Topics.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p></p></body></html>",
            )
        )
        self.Analysis.setText(_translate("MainWindow", "Analysis"))
        self.AboutHeader.setText(_translate("MainWindow", "About"))
        self.AboutText.setText(
            _translate(
                "MainWindow",
                "Using this tool is easy and straightforward: \n"
                "\n"
                '1. First, click the "Upload File" button and select the text file with the correct format. \n'
                "\n"
                "2. Once you have uploaded the file, make sure that it is the right one you wanted to analyze. \n"
                "\n"
                '3. Then, click the "Analyze" button and wait for the results to be displayed. \n'
                "\n"
                '4. If you want to export the results to a CSV file, you can do so by clicking the "Export CSV" button.',
            )
        )
        self.UploadFileButton.setText(_translate("MainWindow", "Upload File"))
        self.AnalyseButton.setText(_translate("MainWindow", "Analyze"))
        self.ErrorMessage.setText(_translate("MainWindow", ""))
        self.FileStatus.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-weight:600;">File:</span><br/>No file selected</p></body></html>',
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())