import os

# Import the PyQt and QGIS libraries
from qgis.core import QgsMapLayerRegistry
from qgis.core import QgsProject
from PyQt4.QtGui import *

class Test:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        iface.mapCanvas().setSelectionColor( QColor("red") )

    def initGui(self):
        # Create action that will start plugin configuration
        self.btnredes = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) +
            "/boton1.png" ), "Haz clic en una red", self.iface.mainWindow() )
        # connect the button to the run method
        self.btnredes.triggered.connect( self.run )
        self.btnredes.setCheckable( False )
        # Add toolbar button to the Plugins toolbar
        self.iface.addToolBarIcon(self.btnredes)

        self.btnpostes = QAction( QIcon( os.path.dirname(os.path.realpath(__file__)) +
            "/boton2.png" ), "Haz clic en un poste", self.iface.mainWindow() )
        self.btnpostes.triggered.connect( self.run2 )
        self.btnpostes.setCheckable( False )
        self.iface.addToolBarIcon(self.btnpostes)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu( "&Plugin Inggepro", self.btnredes )
        self.iface.removeToolBarIcon(self.btnredes)

        self.iface.removePluginMenu( "&Plugin Inggepro", self.btnpostes )
        self.iface.removeToolBarIcon(self.btnpostes)

    # run method that performs all the real work
    def run(self, checked):
        caparedes  = QgsMapLayerRegistry.instance().mapLayersByName("redes_coelcha")[0]
        caparedes = self.iface.activeLayer()
        selection = caparedes.selectedFeatures()
        output= []
        i=0
        for feature in selection:
                output.append(feature[30])
                print ("Poste inicio "+str(i)+" es: "+str(feature[30]))
                i+=1
        QMessageBox.question(self.iface.mainWindow(), 'Resultado',
                             'Las redes seleccionadas son: '+str(i)+'\n'+
                             'Posteinicio en cada red es: '+str(output)+'\n')

    def run2(self, checked):
        capapostes  = QgsMapLayerRegistry.instance().mapLayersByName("postes_coelcha")[0]
        capapostes = self.iface.activeLayer()
        selection2 = capapostes.selectedFeatures()
        output2 = []
        j=0
        for feature in selection2:
                output2.append(feature[4])
                print ("Postevnr "+str(j)+" es: "+feature[4])
                j+=1
        QMessageBox.question(self.iface.mainWindow(), 'Resultado',
                             'Los postes seleccionados son: '+str(j)+'\n'+
                             'Postevnr en cada poste es: '+str(output2)+'\n')


