# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boris.ui'
#
# Created: Tue Sep 22 10:13:05 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(938, 604)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lbLogoBoris = QtGui.QLabel(self.centralwidget)
        self.lbLogoBoris.setText(_fromUtf8(""))
        self.lbLogoBoris.setScaledContents(False)
        self.lbLogoBoris.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLogoBoris.setObjectName(_fromUtf8("lbLogoBoris"))
        self.verticalLayout_3.addWidget(self.lbLogoBoris)
        self.lbLogoUnito = QtGui.QLabel(self.centralwidget)
        self.lbLogoUnito.setText(_fromUtf8(""))
        self.lbLogoUnito.setTextFormat(QtCore.Qt.AutoText)
        self.lbLogoUnito.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLogoUnito.setWordWrap(True)
        self.lbLogoUnito.setObjectName(_fromUtf8("lbLogoUnito"))
        self.verticalLayout_3.addWidget(self.lbLogoUnito)
        self.lbFocalSubject = QtGui.QLabel(self.centralwidget)
        self.lbFocalSubject.setObjectName(_fromUtf8("lbFocalSubject"))
        self.verticalLayout_3.addWidget(self.lbFocalSubject)
        self.lbCurrentStates = QtGui.QLabel(self.centralwidget)
        self.lbCurrentStates.setObjectName(_fromUtf8("lbCurrentStates"))
        self.verticalLayout_3.addWidget(self.lbCurrentStates)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setEnabled(True)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 352, 412))
        self.page.setObjectName(_fromUtf8("page"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuObservations = QtGui.QMenu(self.menubar)
        self.menuObservations.setObjectName(_fromUtf8("menuObservations"))
        self.menuExport_events = QtGui.QMenu(self.menuObservations)
        self.menuExport_events.setObjectName(_fromUtf8("menuExport_events"))
        self.menuExport_aggregated_events = QtGui.QMenu(self.menuObservations)
        self.menuExport_aggregated_events.setObjectName(_fromUtf8("menuExport_aggregated_events"))
        self.menuAnalyze = QtGui.QMenu(self.menubar)
        self.menuAnalyze.setObjectName(_fromUtf8("menuAnalyze"))
        self.menuPlayback = QtGui.QMenu(self.menubar)
        self.menuPlayback.setObjectName(_fromUtf8("menuPlayback"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setToolTip(_fromUtf8(""))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dwConfiguration = QtGui.QDockWidget(MainWindow)
        self.dwConfiguration.setFloating(False)
        self.dwConfiguration.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dwConfiguration.setObjectName(_fromUtf8("dwConfiguration"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.twConfiguration = QtGui.QTableWidget(self.dockWidgetContents_3)
        self.twConfiguration.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twConfiguration.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twConfiguration.setAlternatingRowColors(True)
        self.twConfiguration.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.twConfiguration.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twConfiguration.setObjectName(_fromUtf8("twConfiguration"))
        self.twConfiguration.setColumnCount(6)
        self.twConfiguration.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.twConfiguration)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.dwConfiguration.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwConfiguration)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dwObservations = QtGui.QDockWidget(MainWindow)
        self.dwObservations.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dwObservations.setFloating(False)
        self.dwObservations.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dwObservations.setObjectName(_fromUtf8("dwObservations"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.twEvents = QtGui.QTableWidget(self.dockWidgetContents_2)
        self.twEvents.setEnabled(True)
        self.twEvents.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twEvents.setAutoScroll(False)
        self.twEvents.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twEvents.setTabKeyNavigation(False)
        self.twEvents.setProperty("showDropIndicator", False)
        self.twEvents.setDragDropOverwriteMode(False)
        self.twEvents.setAlternatingRowColors(True)
        self.twEvents.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twEvents.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twEvents.setObjectName(_fromUtf8("twEvents"))
        self.twEvents.setColumnCount(0)
        self.twEvents.setRowCount(0)
        self.verticalLayout.addWidget(self.twEvents)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.dwObservations.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dwObservations)
        self.dwSubjects = QtGui.QDockWidget(MainWindow)
        self.dwSubjects.setFloating(False)
        self.dwSubjects.setObjectName(_fromUtf8("dwSubjects"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.twSubjects = QtGui.QTableWidget(self.dockWidgetContents)
        self.twSubjects.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twSubjects.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twSubjects.setAlternatingRowColors(True)
        self.twSubjects.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twSubjects.setObjectName(_fromUtf8("twSubjects"))
        self.twSubjects.setColumnCount(4)
        self.twSubjects.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.twSubjects)
        self.dwSubjects.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwSubjects)
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setObjectName(_fromUtf8("actionPause"))
        self.actionPlay = QtGui.QAction(MainWindow)
        self.actionPlay.setObjectName(_fromUtf8("actionPlay"))
        self.actionOpen_video_file = QtGui.QAction(MainWindow)
        self.actionOpen_video_file.setObjectName(_fromUtf8("actionOpen_video_file"))
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.actionFaster = QtGui.QAction(MainWindow)
        self.actionFaster.setEnabled(True)
        self.actionFaster.setObjectName(_fromUtf8("actionFaster"))
        self.actionSlower = QtGui.QAction(MainWindow)
        self.actionSlower.setEnabled(True)
        self.actionSlower.setObjectName(_fromUtf8("actionSlower"))
        self.actionJumpForward = QtGui.QAction(MainWindow)
        self.actionJumpForward.setObjectName(_fromUtf8("actionJumpForward"))
        self.actionLoad_configuration = QtGui.QAction(MainWindow)
        self.actionLoad_configuration.setObjectName(_fromUtf8("actionLoad_configuration"))
        self.actionDelete_selected_observations = QtGui.QAction(MainWindow)
        self.actionDelete_selected_observations.setObjectName(_fromUtf8("actionDelete_selected_observations"))
        self.actionDelete_all_observations = QtGui.QAction(MainWindow)
        self.actionDelete_all_observations.setObjectName(_fromUtf8("actionDelete_all_observations"))
        self.actionSort_observations = QtGui.QAction(MainWindow)
        self.actionSort_observations.setObjectName(_fromUtf8("actionSort_observations"))
        self.actionLoad_observations_file = QtGui.QAction(MainWindow)
        self.actionLoad_observations_file.setObjectName(_fromUtf8("actionLoad_observations_file"))
        self.actionSelect_observations = QtGui.QAction(MainWindow)
        self.actionSelect_observations.setObjectName(_fromUtf8("actionSelect_observations"))
        self.actionConfigure_states_and_events = QtGui.QAction(MainWindow)
        self.actionConfigure_states_and_events.setEnabled(False)
        self.actionConfigure_states_and_events.setObjectName(_fromUtf8("actionConfigure_states_and_events"))
        self.actionEdit_event = QtGui.QAction(MainWindow)
        self.actionEdit_event.setObjectName(_fromUtf8("actionEdit_event"))
        self.actionLoad_configuration_file = QtGui.QAction(MainWindow)
        self.actionLoad_configuration_file.setObjectName(_fromUtf8("actionLoad_configuration_file"))
        self.actionMedia_file_information = QtGui.QAction(MainWindow)
        self.actionMedia_file_information.setObjectName(_fromUtf8("actionMedia_file_information"))
        self.actionStart_live_observation = QtGui.QAction(MainWindow)
        self.actionStart_live_observation.setObjectName(_fromUtf8("actionStart_live_observation"))
        self.actionNew_project = QtGui.QAction(MainWindow)
        self.actionNew_project.setObjectName(_fromUtf8("actionNew_project"))
        self.actionTime_budget = QtGui.QAction(MainWindow)
        self.actionTime_budget.setObjectName(_fromUtf8("actionTime_budget"))
        self.actionSave_project = QtGui.QAction(MainWindow)
        self.actionSave_project.setObjectName(_fromUtf8("actionSave_project"))
        self.actionOpen_project = QtGui.QAction(MainWindow)
        self.actionOpen_project.setObjectName(_fromUtf8("actionOpen_project"))
        self.actionSet_offset = QtGui.QAction(MainWindow)
        self.actionSet_offset.setObjectName(_fromUtf8("actionSet_offset"))
        self.actionEdit_project = QtGui.QAction(MainWindow)
        self.actionEdit_project.setObjectName(_fromUtf8("actionEdit_project"))
        self.actionSave_project_as = QtGui.QAction(MainWindow)
        self.actionSave_project_as.setObjectName(_fromUtf8("actionSave_project_as"))
        self.actionVisualize_data = QtGui.QAction(MainWindow)
        self.actionVisualize_data.setObjectName(_fromUtf8("actionVisualize_data"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionNew_observation = QtGui.QAction(MainWindow)
        self.actionNew_observation.setObjectName(_fromUtf8("actionNew_observation"))
        self.actionSave_observation = QtGui.QAction(MainWindow)
        self.actionSave_observation.setObjectName(_fromUtf8("actionSave_observation"))
        self.actionClose_observation = QtGui.QAction(MainWindow)
        self.actionClose_observation.setObjectName(_fromUtf8("actionClose_observation"))
        self.actionEdit_current_observation = QtGui.QAction(MainWindow)
        self.actionEdit_current_observation.setEnabled(False)
        self.actionEdit_current_observation.setObjectName(_fromUtf8("actionEdit_current_observation"))
        self.actionOpen_observation_2 = QtGui.QAction(MainWindow)
        self.actionOpen_observation_2.setEnabled(False)
        self.actionOpen_observation_2.setVisible(False)
        self.actionOpen_observation_2.setObjectName(_fromUtf8("actionOpen_observation_2"))
        self.actionAdd_event = QtGui.QAction(MainWindow)
        self.actionAdd_event.setObjectName(_fromUtf8("actionAdd_event"))
        self.actionDeselectCurrentSubject = QtGui.QAction(MainWindow)
        self.actionDeselectCurrentSubject.setObjectName(_fromUtf8("actionDeselectCurrentSubject"))
        self.actionNext = QtGui.QAction(MainWindow)
        self.actionNext.setIconVisibleInMenu(False)
        self.actionNext.setObjectName(_fromUtf8("actionNext"))
        self.actionPrevious = QtGui.QAction(MainWindow)
        self.actionPrevious.setObjectName(_fromUtf8("actionPrevious"))
        self.actionJumpTo = QtGui.QAction(MainWindow)
        self.actionJumpTo.setEnabled(True)
        self.actionJumpTo.setObjectName(_fromUtf8("actionJumpTo"))
        self.actionJumpBackward = QtGui.QAction(MainWindow)
        self.actionJumpBackward.setObjectName(_fromUtf8("actionJumpBackward"))
        self.actionEdit_observation = QtGui.QAction(MainWindow)
        self.actionEdit_observation.setEnabled(False)
        self.actionEdit_observation.setVisible(False)
        self.actionEdit_observation.setObjectName(_fromUtf8("actionEdit_observation"))
        self.actionCheckUpdate = QtGui.QAction(MainWindow)
        self.actionCheckUpdate.setObjectName(_fromUtf8("actionCheckUpdate"))
        self.actionExportEventTabular_TSV = QtGui.QAction(MainWindow)
        self.actionExportEventTabular_TSV.setObjectName(_fromUtf8("actionExportEventTabular_TSV"))
        self.actionExportEventString = QtGui.QAction(MainWindow)
        self.actionExportEventString.setObjectName(_fromUtf8("actionExportEventString"))
        self.actionClose_project = QtGui.QAction(MainWindow)
        self.actionClose_project.setObjectName(_fromUtf8("actionClose_project"))
        self.actionObservationsList = QtGui.QAction(MainWindow)
        self.actionObservationsList.setObjectName(_fromUtf8("actionObservationsList"))
        self.actionMapCreator = QtGui.QAction(MainWindow)
        self.actionMapCreator.setObjectName(_fromUtf8("actionMapCreator"))
        self.actionNormalSpeed = QtGui.QAction(MainWindow)
        self.actionNormalSpeed.setObjectName(_fromUtf8("actionNormalSpeed"))
        self.actionSnapshot = QtGui.QAction(MainWindow)
        self.actionSnapshot.setObjectName(_fromUtf8("actionSnapshot"))
        self.actionFrame_by_frame = QtGui.QAction(MainWindow)
        self.actionFrame_by_frame.setCheckable(True)
        self.actionFrame_by_frame.setObjectName(_fromUtf8("actionFrame_by_frame"))
        self.actionExportEventsSQL = QtGui.QAction(MainWindow)
        self.actionExportEventsSQL.setObjectName(_fromUtf8("actionExportEventsSQL"))
        self.actionAggregatedEventsTabularFormat = QtGui.QAction(MainWindow)
        self.actionAggregatedEventsTabularFormat.setObjectName(_fromUtf8("actionAggregatedEventsTabularFormat"))
        self.actionOpen_observation = QtGui.QAction(MainWindow)
        self.actionOpen_observation.setObjectName(_fromUtf8("actionOpen_observation"))
        self.actionExportEventTabular_ODS = QtGui.QAction(MainWindow)
        self.actionExportEventTabular_ODS.setObjectName(_fromUtf8("actionExportEventTabular_ODS"))
        self.actionAaaa = QtGui.QAction(MainWindow)
        self.actionAaaa.setObjectName(_fromUtf8("actionAaaa"))
        self.menuCreate_subtitles_2 = QtGui.QAction(MainWindow)
        self.menuCreate_subtitles_2.setObjectName(_fromUtf8("menuCreate_subtitles_2"))
        self.actionExportEventTabular_XLS = QtGui.QAction(MainWindow)
        self.actionExportEventTabular_XLS.setObjectName(_fromUtf8("actionExportEventTabular_XLS"))
        self.actionUser_guide = QtGui.QAction(MainWindow)
        self.actionUser_guide.setObjectName(_fromUtf8("actionUser_guide"))
        self.menuHelp.addAction(self.actionUser_guide)
        self.menuHelp.addAction(self.actionCheckUpdate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionNew_project)
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionEdit_project)
        self.menuFile.addAction(self.actionSave_project)
        self.menuFile.addAction(self.actionSave_project_as)
        self.menuFile.addAction(self.actionClose_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuExport_events.addAction(self.actionExportEventTabular_TSV)
        self.menuExport_events.addAction(self.actionExportEventTabular_ODS)
        self.menuExport_events.addAction(self.actionExportEventTabular_XLS)
        self.menuExport_events.addSeparator()
        self.menuExport_events.addSeparator()
        self.menuExport_aggregated_events.addAction(self.actionAggregatedEventsTabularFormat)
        self.menuExport_aggregated_events.addAction(self.actionExportEventsSQL)
        self.menuObservations.addAction(self.actionNew_observation)
        self.menuObservations.addAction(self.actionOpen_observation)
        self.menuObservations.addAction(self.actionObservationsList)
        self.menuObservations.addAction(self.actionOpen_observation_2)
        self.menuObservations.addAction(self.actionEdit_observation)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionClose_observation)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionAdd_event)
        self.menuObservations.addAction(self.actionEdit_event)
        self.menuObservations.addAction(self.actionSelect_observations)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionDelete_selected_observations)
        self.menuObservations.addAction(self.actionDelete_all_observations)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionLoad_observations_file)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.menuExport_events.menuAction())
        self.menuObservations.addAction(self.menuExport_aggregated_events.menuAction())
        self.menuObservations.addAction(self.actionExportEventString)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.menuCreate_subtitles_2)
        self.menuObservations.addAction(self.actionMedia_file_information)
        self.menuAnalyze.addAction(self.actionTime_budget)
        self.menuAnalyze.addAction(self.actionVisualize_data)
        self.menuPlayback.addAction(self.actionJumpForward)
        self.menuPlayback.addAction(self.actionJumpBackward)
        self.menuPlayback.addAction(self.actionJumpTo)
        self.menuPlayback.addSeparator()
        self.menuPlayback.addAction(self.actionPlay)
        self.menuPlayback.addAction(self.actionPause)
        self.menuPlayback.addAction(self.actionPrevious)
        self.menuPlayback.addAction(self.actionNext)
        self.menuTools.addAction(self.actionMapCreator)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuObservations.menuAction())
        self.menubar.addAction(self.menuPlayback.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addAction(self.actionJumpBackward)
        self.toolBar.addAction(self.actionJumpForward)
        self.toolBar.addAction(self.actionNormalSpeed)
        self.toolBar.addAction(self.actionFaster)
        self.toolBar.addAction(self.actionSlower)
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addAction(self.actionSnapshot)
        self.toolBar.addAction(self.actionFrame_by_frame)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BORIS", None))
        self.lbFocalSubject.setText(_translate("MainWindow", "lbFocalSubject", None))
        self.lbCurrentStates.setText(_translate("MainWindow", "lbCurrentStates", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuObservations.setTitle(_translate("MainWindow", "Observations", None))
        self.menuExport_events.setTitle(_translate("MainWindow", "Export events", None))
        self.menuExport_aggregated_events.setTitle(_translate("MainWindow", "Export aggregated events", None))
        self.menuAnalyze.setTitle(_translate("MainWindow", "Analyze", None))
        self.menuPlayback.setTitle(_translate("MainWindow", "Playback", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.dwConfiguration.setWindowTitle(_translate("MainWindow", "Ethogram", None))
        item = self.twConfiguration.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key", None))
        item = self.twConfiguration.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Code", None))
        item = self.twConfiguration.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type", None))
        item = self.twConfiguration.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Description", None))
        item = self.twConfiguration.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Modifiers", None))
        item = self.twConfiguration.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Excluded", None))
        self.dwObservations.setWindowTitle(_translate("MainWindow", "Events", None))
        self.dwSubjects.setWindowTitle(_translate("MainWindow", "Subjects", None))
        item = self.twSubjects.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Key", None))
        item = self.twSubjects.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.twSubjects.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Description", None))
        item = self.twSubjects.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Current state(s)", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionPause.setText(_translate("MainWindow", "Pause", None))
        self.actionPause.setToolTip(_translate("MainWindow", "Pause", None))
        self.actionPlay.setText(_translate("MainWindow", "Play", None))
        self.actionOpen_video_file.setText(_translate("MainWindow", "Open media file", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionFaster.setText(_translate("MainWindow", "Faster", None))
        self.actionSlower.setText(_translate("MainWindow", "Slower", None))
        self.actionJumpForward.setText(_translate("MainWindow", "Jump forward", None))
        self.actionLoad_configuration.setText(_translate("MainWindow", "Load configuration", None))
        self.actionDelete_selected_observations.setText(_translate("MainWindow", "Delete selected events", None))
        self.actionDelete_all_observations.setText(_translate("MainWindow", "Delete all events", None))
        self.actionSort_observations.setText(_translate("MainWindow", "Sort events", None))
        self.actionLoad_observations_file.setText(_translate("MainWindow", "Import events", None))
        self.actionSelect_observations.setText(_translate("MainWindow", "Select events from interval", None))
        self.actionConfigure_states_and_events.setText(_translate("MainWindow", "Configure states and events", None))
        self.actionEdit_event.setText(_translate("MainWindow", "Edit event", None))
        self.actionLoad_configuration_file.setText(_translate("MainWindow", "Load state and events configuration file", None))
        self.actionMedia_file_information.setText(_translate("MainWindow", "Media file information", None))
        self.actionStart_live_observation.setText(_translate("MainWindow", "Start observation without media file", None))
        self.actionNew_project.setText(_translate("MainWindow", "New project", None))
        self.actionNew_project.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionTime_budget.setText(_translate("MainWindow", "Time budget", None))
        self.actionSave_project.setText(_translate("MainWindow", "Save project", None))
        self.actionSave_project.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionOpen_project.setText(_translate("MainWindow", "Open project", None))
        self.actionOpen_project.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSet_offset.setText(_translate("MainWindow", "Set time offset", None))
        self.actionEdit_project.setText(_translate("MainWindow", "Edit project", None))
        self.actionSave_project_as.setText(_translate("MainWindow", "Save project as ...", None))
        self.actionVisualize_data.setText(_translate("MainWindow", "Plot events", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))
        self.actionNew_observation.setText(_translate("MainWindow", "New observation", None))
        self.actionSave_observation.setText(_translate("MainWindow", "Save current observation", None))
        self.actionClose_observation.setText(_translate("MainWindow", "Close observation", None))
        self.actionEdit_current_observation.setText(_translate("MainWindow", "Edit current observation", None))
        self.actionOpen_observation_2.setText(_translate("MainWindow", "Open observation", None))
        self.actionAdd_event.setText(_translate("MainWindow", "Add event", None))
        self.actionDeselectCurrentSubject.setText(_translate("MainWindow", "Deselect current subject", None))
        self.actionNext.setText(_translate("MainWindow", "Next", None))
        self.actionNext.setToolTip(_translate("MainWindow", "Next media file", None))
        self.actionPrevious.setText(_translate("MainWindow", "Previous", None))
        self.actionPrevious.setToolTip(_translate("MainWindow", "Previous media file", None))
        self.actionJumpTo.setText(_translate("MainWindow", "Jump to specific time", None))
        self.actionJumpBackward.setText(_translate("MainWindow", "Jump backward", None))
        self.actionJumpBackward.setToolTip(_translate("MainWindow", "Jump backward", None))
        self.actionEdit_observation.setText(_translate("MainWindow", "Edit observation", None))
        self.actionCheckUpdate.setText(_translate("MainWindow", "Check for updates", None))
        self.actionExportEventTabular_TSV.setText(_translate("MainWindow", "Tab Separated Values (tsv)", None))
        self.actionExportEventString.setText(_translate("MainWindow", "Export events as behavioural strings", None))
        self.actionClose_project.setText(_translate("MainWindow", "Close project", None))
        self.actionObservationsList.setText(_translate("MainWindow", "Observations list", None))
        self.actionMapCreator.setText(_translate("MainWindow", "Map creator", None))
        self.actionNormalSpeed.setText(_translate("MainWindow", "Normal speed", None))
        self.actionSnapshot.setText(_translate("MainWindow", "Snapshot", None))
        self.actionFrame_by_frame.setText(_translate("MainWindow", "Frame by frame", None))
        self.actionExportEventsSQL.setText(_translate("MainWindow", "Structured Query Language (SQL)", None))
        self.actionAggregatedEventsTabularFormat.setText(_translate("MainWindow", "Tab Separated Values (tsv)", None))
        self.actionOpen_observation.setText(_translate("MainWindow", "Open observation", None))
        self.actionExportEventTabular_ODS.setText(_translate("MainWindow", "Open Document Spreadsheet (ods)", None))
        self.actionAaaa.setText(_translate("MainWindow", "aaaa", None))
        self.menuCreate_subtitles_2.setText(_translate("MainWindow", "Create subtitles", None))
        self.actionExportEventTabular_XLS.setText(_translate("MainWindow", "Microsoft Excel format (xls)", None))
        self.actionUser_guide.setText(_translate("MainWindow", "User guide", None))

