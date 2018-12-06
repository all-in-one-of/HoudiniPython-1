import hou
import os

from PySide2 import QtWidgets, QtUiTools

class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()

        self.proj = hou.getenv('JOB') + '/'

        #Load UI file
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load('C:/Users/zmfov/Documents/houdini17.0/scripts/python/project_man/project_man.ui')

        # get UI elements
        self.setproj = self.ui.findChild(QtWidgets.QPushButton, "setproj")
        self.projname = self.ui.findChild(QtWidgets.QLabel, "projname")
        self.projpath = self.ui.findChild(QtWidgets.QLabel, "projpath")
        self.scenelist = self.ui.findChild(QtWidgets.QListWidget, "scenelist")

        # create widgets
        # self.btn = QtWidgets.QPushButton("Click Me")
        # self.lblTitle = QtWidgets.QLabel("PRJECT MANAGER")
        # self.label = QtWidgets.QLabel(self.proj)
        #
        # self.listwidget = QtWidgets.QListWidget()

        # create connections
        self.setproj.clicked.connect(self.setproject)



        # layout
        mainLayout = QtWidgets.QVBoxLayout()

        mainLayout.addWidget(self.ui)

        # Add widgets to layout
        # mainLayout.addWidget(self.lblTitle)
        # mainLayout.addWidget(self.label)
        # mainLayout.addWidget(self.listwidget)
        # mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)

    def setproject(self):
        setjob = hou.ui.selectFile(title="Set Project", file_type=hou.fileType.Directory)
        hou.hscript("setenv JOB=" + setjob)

        self.proj = hou.getenv('JOB') + '/'

        projname = setjob.split('/')[-2]
        setjob = os.path.dirname(setjob)
        projpath = os.path.split(setjob)[0]

        self.projname.setText(projname)
        self.projpath.setText(projpath + '/')

        self.createInterface()

    def openScene(self, item):
        print("open hip file")
        hipFile = self.proj + item.data()
        # print hipFile
        # open hip file
        hou.hipFile.load(hipFile)


    def createInterface(self):
        print("creating interface")
        self.scenelist.clear()


        for file in os.listdir(self.proj):
            if file.endswith(".hip"):
                self.scenelist.addItem(file)

        # connect list items to function
        self.scenelist.doubleClicked.connect(self.openScene)

# git test