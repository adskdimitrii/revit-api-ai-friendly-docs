# Postable Command Enumeration

Source: https://www.revitapidocs.com/2026/f6ccdc1b-6ac3-9c49-d0bb-8a7d1877eab0.htm

---

| Postable Command Enumeration |
| --- |

Enumerates all of the built\-in commands which can be posted by an API application. 
**Namespace:** [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm) 
**Assembly:** RevitAPIUI (in RevitAPIUI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum PostableCommand
```

```
Public Enumeration PostableCommand
```

```
public enum class PostableCommand
```

```
type PostableCommand
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| AcquireCoordinates | 33,863 | Determines the coordinates used in a linked project, and uses them for the current project. |
| ActivateControlsAndDimensions | 35,194 | Enable or disable the visibility of pins, constraints, and temporary dimensions when multiple elements are selected. |
| ActivateView | 33,181 | Enables you to modify the selected view without leaving the sheet. |
| AddInsManager | 57,328 | Opens the Add\-Ins Manager dialog, where you can enable and disable add\-ins. |
| AddToSet | 33,908 | Moves selected elements from the main model to one or more design options in a set. |
| AirTerminal | 37,005 | Places a register, grille, or diffuser. |
| Align | 33,218 | Aligns one or more elements with a selected element. |
| AlignedDimension | 48,955 | Places dimensions between parallel references, or between multiple points. |
| AlignedMultiRebarAnnotation | 35,831 | Tags multiple elements with a single annotation that displays aligned dimensions between references as well as parameters from the referenced elements. For example, all rebar in a rebar set can be referenced with a single tag. |
| AlignedToCurrentView | 33,320 | Pastes elements that were cut or copied from another view into the current view. |
| AlignedToPickedLevel | 33,321 | Pastes the selected elements into a elevation view or a section view. |
| AlignedToSamePlace | 33,341 | Pastes the elements to the same place from which they were cut or copied. |
| AlignedToSelectedLevels | 33,328 | Pastes multiple elements from one level to specified levels. |
| AlignedToSelectedViews | 33,332 | Pastes selected elements, including view\-specific elements such as dimensions, into specified views. |
| AlignmentStation | 1,115 | Add an individual alignment station annotation. |
| AlignmentStationLabelTypes | 33,354 | Defines attributes for Alignment Station Labels. |
| AlignmentStationSet | 1,116 | Add a series of alignment station annotations. |
| AllowableBarTypes | 35,599 | Defines the allowable rebar types (diameters) of the shape type. |
| AnalysisDisplayStyles | 32,948 | Specifies a presentation format for visualizing analysis results. |
| AnalyticalLink | 48,756 | Creates an analytical element that connects two separate analytical nodes. |
| AnalyticalMember | 56,298 | Places an analytical member in the project. |
| Anchors | 54,295 | Inserts anchors and the related holes in the selected model elements. |
| AngularDimension | 48,957 | Places a dimension that measures the angle between reference points sharing a common intersection. |
| AngularDimensionTypes | 1,082 | Defines attributes for angular dimensions. |
| ApplyCoping | 46,450 | Adds coping to steel beams and columns. |
| ApplyTemplatePropertiesToCurrentView | 33,651 | Applies properties stored in a view template to the current view. |
| ArchitecturalColumn | 32,918 | Adds architectural columns to the building model. |
| ArchitecturalFloor | 32,914 | Creates a floor for the current level of the building model. |
| ArchitecturalWall | 32,771 | Creates a non\-structural wall in the building model. |
| ArcLengthDimension | 48,959 | Places a dimension that measures the length of a curved wall or other element. |
| ArcWire | 37,106 | Draws arced wire runs. |
| Area | 33,720 | Creates an area defined by walls and boundary lines. |
| AreaAndVolumeComputations | 40,382 | Specifies how areas and volumes are calculated, and creates area schemes. |
| AreaBasedLoadBoundary | 43,647 | Places a boundary line for electrical area based loads. |
| AreaBoundary | 33,719 | Defines boundaries for areas. |
| AreaPlan | 33,638 | Creates an area plan view. |
| AreaReinforcementSymbol | 46,959 | Places a symbol that shows extents and hook types for the selected area reinforcement. |
| AreaTag | 33,718 | Tags the selected area. |
| Array | 33,121 | Creates a linear or radial array of selected elements. |
| Arrowheads | 33,349 | Specifies line weights, fills, and styles for annotation arrowheads. |
| AssemblyCode | 54,096 | Specifies the location of the assembly code file or reloads the assembly code table from the current file. |
| AutomaticBeamSystem | 42,398 | Creates a layout that is used to control the number and spacing of a series of parallel beams. |
| AutomaticCeiling | 33,158 | Creates a ceiling at a specified distance above the level in which it resides. |
| AutomationCustomization | 56,516 | Lets you adjust the Structural Analytical Model Automation settings to suit the specific requirements of your project. |
| BatchPrint | 56,308 | Print a large number of drawings with a batch job. |
| Beam | 34,972 | Adds individual beams, a chain of beams, or beams along grid lines. |
| BeamAnnotations | 35,585 | Places multiple beam tags, annotations, and spot elevations. |
| BeamOrColumnJoins | 49,543 | Adjusts how beams and columns frame into one another. |
| BeamSystemSymbol | 46,567 | Places a beam system span tag. |
| Bolts | 54,293 | Inserts bolts and the related holes in the selected model elements. |
| BottomChord | 3,621 | Draws the bottom chord of the truss family. |
| BoundaryConditions | 35,223 | Defines point, line, and area boundary conditions in an analytical model. |
| BoundaryConditionsSettings | 53,534 | Selects the family symbol and adjusts the spacing for boundary conditions. |
| Brace | 34,973 | Adds diagonal structural members connected to beams and columns. |
| BrowserOrganization | 33,904 | Changes the way that views are listed in the Project Browser. |
| BuildingElevation | 33,255 | Creates an elevation view. |
| BuildingOperatingSchedules | 56,745 | Opens the Building Operation Schedules Editor. |
| BuildingOrSpaceTypeSettings | 37,259 | Opens the Building and Space Type Settings dialog to manage building and space parameters and schedules. |
| CableTray | 37,297 | Draws cable tray runs such as rigid ladder or channel cable tray. |
| CableTrayConnector | 37,291 | Adds a cable tray connector to a component. |
| CableTrayFitting | 37,295 | Places a cable tray fitting. These fittings include elbows, tees, wyes, crosses, and other unions. |
| Callout | 33,298 | Creates a rectangular callout in the view. |
| CalloutTags | 3,167 | Specifies the callout head for callout tags, and the radius of the callout bubble. |
| Camera | 32,956 | Creates a 3D view from the perspective of a camera placed in the view. |
| CanvasTheme | 57,654 | Sets the color theme of the canvas to dark or light. |
| ChamferedWire | 37,260 | Draws chamfered wire runs. |
| CheckCircuits | 37,062 | Verifies all circuits for proper connections to panels and valid system assignments. Errors are reported in a warning dialog. |
| CheckDuctSystems | 37,167 | Verifies all duct systems for properly connected ductwork and valid system assignments. |
| CheckPipeSystems | 37,155 | Verifies all pipe systems for properly connected pipes and valid system assignments. |
| CheckSpelling | 40,986 | Checks the spelling of text notes in a selection or in the current view or sheet. |
| Close | 57,602 | Close Revit. |
| CloseInactiveViews | 33,712 | Closes open views except for the currently active view. The current view remains open in the drawing area. |
| Collaborate | 54,057 | Enables collaboration so team members can work on a model simultaneously. |
| CollaborateInCloud | 54,058 | Enables collaboration in the cloud, which allows team members to work on a model simultaneously. |
| ColorFillLegend | 33,252 | Places a legend in a view to indicate the meanings of color fills for rooms or areas. |
| ColorSchemes | 48,739 | Creates or modifies a color fill scheme for rooms and areas. |
| Communication | 37,278 | Places communication devices such as intercom system components. |
| Conduit | 37,298 | Draws rigid conduit runs. |
| ConduitConnector | 37,292 | Adds a conduit connector to a component. |
| ConduitFitting | 37,296 | Places a conduit fitting. These fittings include elbows, tees, wyes, crosses, and other unions. |
| ConnectionSettings | 996 | Opens the Structural Connections Settings dialog in which you can load and unload add\-in connections into Revit. If no add\-ins are present, no connections are available in the Connections tab. |
| ContourCut | 54,297 | Creates a contour cut on the selected faces of a beam or a plate. |
| Control | 33,034 | Adds a flip arrow to the view. |
| ConvertToFlexDuct | 37,014 | Changes a length of ductwork connected to an air terminal from rigid duct to flexible duct. |
| CoordinationModelAutodeskDocs | 56,560 | Links a coordination model view from Autodesk Docs into the current project. |
| CoordinationModelChanges | 56,713 | Displays the overview of changes between the current version of a linked coordination model from Autodesk Docs and any of its previous versions. |
| CoordinationModelLocal | 56,559 | Links a NWD or NWC file to provide context for the Revit model. |
| CoordinationReviewUseCurrentProject | 35,110 | Displays warnings for monitored elements in the current project. |
| CoordinationSelectLink | 35,111 | Displays warnings for monitored elements between linked projects and the host project. |
| CoordinationSettings | 35,149 | Specifies mapping behavior when copying MEP fixtures from a linked model into the current project. |
| Cope | 55,304 | Creates a parametric cope on intersecting beams and the related connection between the beams. |
| CopeSkewed | 54,286 | Creates a skewed cope at the selected beam end, either at the top or at the bottom. |
| Copy | 33,129 | Copies selected elements and places them in the specified location in the current view. |
| CopyMonitorSelectLink | 35,108 | Copies selected elements from a linked project to the host project, and monitors changes to these elements. |
| CopyMonitorUseCurrentProject | 35,107 | Monitors grids, levels, columns, walls, floors, and openings within the current project. |
| CopyToClipboard | 57,634 | Copies selected elements to the clipboard. |
| CornerCut | 54,288 | Creates a cut on the corner of a selected plate. |
| CreateAnAreaBasedLoad | 43,641 | Creates an area based load from the area defined by the area based load boundaries. |
| CreateAssembly | 53,677 | Creates an assembly from elements you select in the drawing area. |
| CreateEnergyModel | 53,964 | Creates the energy analytical model. |
| CreateFromImport | 56,504 | Creates a solid topographical element. |
| CreateGroup | 33,305 | Creates a group of elements for easy reuse. |
| CreateParts | 35,425 | Creates parts from the layers or subcomponents of a selected element. |
| CreateSimilar | 33,441 | Places an element of the same type as the selected element |
| CreateTemplateFromCurrentView | 33,684 | Creates a view template using the properties of the current view as the basis for the new template. |
| CurtainGrid | 33,199 | Creates a grid line in a curtain wall or curtain system. |
| CurtainSystemByFace | 35,072 | Creates a curtain system on the face of a mass or generic model. |
| CurtainWallMullion | 33,200 | Creates a horizontal or vertical mullion on a curtain grid. |
| CutBy | 55,309 | Creates a cut on a model element along the shape of another intersecting model element and a cut through the intersecting element. The connection between the two elements is also created. |
| CutGeometry | 33,407 | Selects the geometry to cut. |
| CutProfile | 33,709 | Changes the shape of elements that are cut in a view, such as roofs, walls, floors, and the layers of compound structures. |
| CutThrough | 55,308 | Creates a cut through a model element around the contour of another intersecting model element. The weld between the two elements is also created. |
| CutToClipboard | 57,635 | Removes selected elements, and places them on the clipboard. |
| Data | 37,279 | Places data devices such as ethernet and other network connections. |
| DeactivateView | 33,185 | Deactivates the view, so you can no longer change the view from the sheet. |
| DecalTypes | 33,188 | Creates a decal that you can use to place images on surfaces of a building model for rendering. |
| Default3DView | 33,169 | Opens the default orthographic 3D view. |
| Delete | 32,778 | Removes selected elements from the building model. |
| DeleteEnergyModel | 54,224 | Removes the energy analytical model from the Revit project. |
| DemandFactors | 37,068 | Applies demand factors to a panel. |
| Demolish | 33,534 | Marks elements as demolished in the current phase. |
| DesignOptions | 33,907 | Creates and manages design option sets and individual design options for the project. |
| DetailComponent | 33,424 | Adds a view\-specific detail component to a view. |
| DetailLevel | 33,384 | Specifies the detail level (coarse, medium, or fine) that applies to each view scale by default. |
| DetailLine | 33,425 | Creates view\-specific lines. |
| DiameterDimension | 35,778 | Places a dimension that measures the diameter of an arc or circle. |
| DiameterDimensionTypes | 35,779 | Defines attributes for diameter dimensions. |
| DisplaceElements | 54,029 | Creates a view\-specific representation of model elements that can be displaced in the view. |
| Door | 32,772 | Adds doors to the building model. |
| DormerOpening | 35,255 | Cuts a roof to create an opening for a dormer. |
| DraftingView | 33,530 | Creates a view showing details that are not directly associated with the building model. |
| DrawOnFace | 3,096 | Draws lines on existing surfaces. |
| DrawOnWorkPlane | 3,097 | Draws lines on the active work plane. |
| Duct | 37,006 | Draws rigid round, rectangular, or oval ductwork. |
| DuctAccessory | 37,004 | Places a duct accessory. These accessories include dampers, filters and smoke detectors. |
| DuctConnector | 37,218 | Adds a duct connector to a component. |
| DuctFitting | 37,009 | Places a duct fitting. These fittings include elbows, tees, wyes, crosses, and other types of fittings. |
| DuctLegend | 37,027 | Places a legend to indicate the color fills associated with ductwork in duct systems. |
| DuctPlaceholder | 37,427 | Draws placeholder duct without elbow or tee fittings. |
| DuctPressureLossReport | 35,811 | Generates a pressure loss report for one or more duct systems. |
| DuplicateAsDependent | 35,280 | Creates a view that is dependent on the original view. |
| DuplicateView | 33,245 | Creates a view that contains only the model geometry from the current view. |
| DuplicateWithDetailing | 33,858 | Creates a view that includes model geometry and view\-specific elements from the current view. |
| DWFMarkup | 3,401 | Links marked\-up DWF files into a Revit project so you can see the markups on corresponding sheets. |
| Dynamo | 54,157 | Provides access to Dynamo, an open source visual programming platform for designers. |
| DynamoPlayer | 57,282 | Preview, select, and run your Dynamo graphs from a single dialog. |
| DynamoPlayerForSteel | 56,443 | Places steel connections on selected elements using pre\-defined rules. |
| EditATemplate | 37,315 | Modifies a specific panel schedule template. |
| EditingRequests | 33,911 | Displays a list of other users' requests to borrow elements in your worksets, and your pending requests. |
| EditRebarCover | 48,583 | Edits the rebar cover references of an entire rebar host or an individual face. |
| EditSelection | 35,183 | Edits a previously saved selection set. |
| ElectricalAnalyticalLoadTypeSettings | 56,345 | Opens the Electrical Analytical Load Type Settings dialog to define the power requirement for area\-based loads. |
| ElectricalConductorAndCableSettings | 56,831 |  |
| ElectricalConnector | 37,217 | Adds an electrical connector to a component. |
| ElectricalEquipment | 37,060 | Places electrical equipment such as panels and switch gear. |
| ElectricalFixture | 37,061 | Places electrical devices such as receptacles, junction boxes, and other power devices. |
| ElectricalSettings | 37,054 | Opens the Electrical Settings dialog to define distribution systems, wire types, cable tray and conduit sizes, and demand factors. |
| ElementKeynote | 35,158 | Tags a selected element using the keynote specified for the element type. |
| ElevationTags | 3,168 | Defines properties for elevation tags. |
| EnergySettings | 53,612 | Specifies parameters used to create the energy analytical model. |
| EquipmentLoad | 43,648 | Opens the System Browser to define equipment loads, such as a chiller or other specific equipment. |
| ExitRevit | 57,665 | Exit Revit. |
| ExportCADFormatsACIS\_SAT | 3,345 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportCADFormatsDGN | 3,344 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportCADFormatsDWG | 3,342 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportCADFormatsDXF | 3,343 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportCADFormatsOBJ | 3,348 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportCADFormatsSTEP | 3,340 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportCADFormatsSTL | 3,347 | Creates DWG, DXF, DGN, OBJ, SAT, STL or STEP files. |
| ExportDWFOrDWFx | 3,341 | Creates DWF or DWFx files. |
| ExportExportTypes | 3,405 | Exports family types from the current family to a text (.txt) file. |
| ExportFBX | 35,350 | Saves a 3D view as an FBX file. |
| ExportGBXML | 53,615 | Saves the model as a gbXML file. |
| ExportIFC | 3,278 | Creates IFC files. |
| ExportImagesandAnimationsImage | 33,838 | Saves animations or image files. |
| ExportImagesandAnimationsSolarStudy | 12,075 | Saves animations or image files. |
| ExportImagesandAnimationsWalkthrough | 12,059 | Saves animations or image files. |
| ExportODBCDatabase | 33,693 | Saves model data to an ODBC database. |
| ExportOptionsExportSetupsDGN | 33,248 | Sets export options for CAD. |
| ExportOptionsExportSetupsDWGOrDXF | 33,251 | Sets export options for CAD. |
| ExportPDF | 3,346 | Creates PDF files. |
| ExportReportsRoomOrAreaReport | 3,125 | Saves a schedule or Room/Area report. |
| ExportReportsSchedule | 33,710 | Saves a schedule or Room/Area report. |
| FabricationPart | 54,149 | Displays the MEP Fabrication Parts palette. |
| FabricationSettings | 35,839 | Opens the Fabrication Settings dialog. |
| FabricReinforcementSymbol | 35,793 | Located on the Symbol panel of the Annotate tab.Places a symbol that represents the fabric sheet. |
| FamilyCategoryAndParameters | 10,133 | Assigns the properties of a predefined family category to the component you are creating. |
| FamilyTypes | 33,203 | Allows you to enter parameter values for existing family types, add parameters to the family, or create new types within the family. |
| Fascia | 40,601 | Adds fascia to the edge of a roof, soffit, or other fascia, or to model lines. |
| FilledRegion | 33,204 | Creates a 2D, view\-specific graphic with a fill pattern and a boundary line. |
| FillPatterns | 33,163 | Creates or modifies drafting patterns and model patterns. |
| Filters | 33,099 | Creates a filter to modify the visibility and graphics of elements in views based on element parameters. |
| FindOrReplace | 53,591 | Finds and replaces text in an open project file. |
| FireAlarm | 37,280 | Places fire alarm devices such as smoke detectors, manual pull stations, and annunciators. |
| FlexDuct | 37,010 | Draws round and rectangular flexible ductwork. |
| FlexPipe | 37,102 | Draws flexible piping. |
| FloorByFaceFloor | 3,234 | Converts a mass floor into a floor of the building model. |
| FloorPlan | 32,953 | Creates a floor plan view. |
| FormWorkPlaneView | 35,703 | Enables the Workplane Viewer. |
| FramingElevation | 32,814 | Creates a framing elevation to show vertical bracing. |
| GlobalParameters | 54,055 | Specifies parameters that can be added to a project, and used to define values of other parameters. |
| GradedRegion | 33,640 | Modifies topography to indicate changes during the construction process. |
| GraphicalColumnSchedule | 46,139 | Creates a graphical column schedule for the project. |
| GrayInactiveWorksets | 2,765 | Displays elements in inactive worksets as gray to visually distinguish them from elements in active worksets. |
| Grid | 32,770 | Places column grid lines in the building design. |
| GuideGrid | 53,675 | Creates a new guide element in the active sheet to help align elements within and between sheets. |
| Gutter | 40,602 | Adds a gutter to the edge of a roof, soffit, or fascia, or to model lines. |
| HalftoneOrUnderlay | 49,786 | Customizes halftone and underlay elements in view. |
| HideBoundaryOpenEnds | 45,676 | Hides dots that display on the open ends of area based load boundary lines. |
| HideCategory | 3,240 | Hides all elements that belong to a selected category in the current view. |
| HideElements | 35,261 | Hides selected elements in the current view. |
| Holes | 54,294 | Inserts holes on the selected face of model elements. |
| IdsOfSelection | 33,866 | Displays unique identifiers for the selected elements. |
| ImportCAD | 32,959 | Imports data or 3D geometry from other CAD programs to a Revit model or family. |
| ImportGBXML | 3,102 | Imports analysis data from a gbXML file. |
| ImportImage | 33,499 | Imports a raster image into a Revit project to use as a background image or visual aid during the creation or presentation of the model. |
| ImportPDF | 33,503 | Inserts a PDF file into a model view to use as a background image or visual aid. |
| ImportTypes | 3,404 | Imports family types from a text (.txt) file into the current family. |
| InPlaceMass | 42,645 | Creates a mass that is unique to the project. |
| Insert2DElementsFromFile | 42,310 | Copies 2D elements from a detail view (saved in another project) into a detail view in the current project. |
| InsertCoupler | 35,862 | Places a reinforcement coupler element to join rebar in a host. |
| InsertViewsFromFile | 42,309 | Copies specified views (sheets, schedules, or drafting views) from a project file and saves them in the current project. |
| Insulation | 33,432 | Places a batt insulation graphic in a detail view. |
| Isolated | 35,114 | Adds footings or pile caps to the building model. |
| JoinGeometry | 33,729 | Creates clean joins between 2 or more host elements that share a common face, such as walls and floors. |
| JoinOrUnjoinRoof | 33,277 | Connects roofs to other roofs or walls, or reverses a previous join. |
| KeyboardShortcuts | 49,211 | Assigns key sequences to tools. |
| KeynoteLegend | 3,449 | Creates a list of the keynotes used in a project, and their definitions. |
| KeynotingSettings | 3,450 | Specifies the location of the keynote table and the numbering method for keynotes. |
| Label | 33,174 | Creates a label for the annotation symbol. |
| LabelContours | 33,820 | Displays the elevations of contour lines. |
| LaunchAsApp | 56,806 | Open the Content Catalog in a separate window. |
| LaunchInBrowser | 56,807 | Access the Content Catalog in the default browser. |
| LaunchInDockedWindow | 56,808 | Access the Content Catalog in the Revit session from a docked window. |
| Legend | 33,531 | Creates a list of building components and annotations used in a project. |
| LegendComponent | 33,751 | Adds a graphic representation of a selected model element to a legend view. |
| Level | 32,794 | Adds a level to the model. |
| Lighting | 37,281 | Places lighting switches such as daylight sensors, occupancy sensors, and manual switches. |
| LightingFixture | 37,059 | Places lighting fixtures such as ceiling, wall, and recessed lights. |
| LinearDimension | 48,956 | Places horizontal or vertical dimensions that measure the distance between reference points. |
| LinearDimensionTypes | 1,081 | Defines attributes for linear (horizontal and vertical) dimensions. |
| LinearMultiRebarAnnotation | 35,832 | Tags multiple elements with a single annotation that displays linear dimensions between references as well as parameters from the referenced elements. For example, all rebar in a rebar set can be referenced with a single tag. |
| LinePatterns | 33,120 | Creates or modifies line patterns. |
| LineStyles | 33,360 | Creates or modifies line styles. |
| LineWeights | 32,946 | Creates or modifies line weights. |
| Linework | 33,520 | Overrides the line style for a selected line in the active view only. |
| LinkCAD | 32,961 | Links a CAD file to the current Revit project. |
| LinkIFC | 35,853 | Links an IFC file to the current project to reference its information for additional design work. |
| LinkImage | 56,282 | Inserts a link to an image into a model view. |
| LinkPDF | 56,281 | Inserts a link to a PDF into a model view. |
| LinkRevit | 33,836 | Links another Revit model to the current model. |
| LinkTopography | 57,288 | Links existing topography to the current Revit model. |
| LoadAsGroup | 33,695 | Loads a Revit file as a group. |
| LoadAsGroupIntoOpenProjects | 786 | Loads the current project as a group into another open project or family. |
| LoadAutodeskFamily | 32,990 | Load an Autodesk family from the cloud. |
| LoadCasesAndCombinations | 53,532 | Adds and edits load combinations for the analytical model. |
| LoadCasesDisplay | 53,531 | Allows the adjustment of the Category assignment for each load case. |
| LoadClassifications | 37,055 | Assigns and specifies demand factors to a load classification. |
| LoadedTagsAndSymbols | 33,338 | Lists the tags and symbols that will be used for each element category. |
| LoadFamilyIntoProjectAndClose | 54,133 | Loads the family into open projects or family files and closes the family after it loads. |
| LoadIntoProject | 791 | Loads the rebar shape into open projects or family files. |
| LoadRebarShapeIntoProjectAndClose | 54,151 | Loads the rebar shape into open projects or family files and closes the family after it loads. |
| Loads | 56,584 | Defines point, line, and area loads in an analytical model. |
| LoadSelection | 35,180 | Loads a previously saved selection set. |
| LoadShapes | 32,984 | Loads a Revit family into the current file. |
| LoadsScalingDisplay | 53,538 | Overrides the load type graphics scale using the project scale. |
| Location | 33,862 | Specifies the geographic location for the project. |
| MacroManager | 35,602 | Opens the Macro Manager to run, create, or delete a macro. |
| MacroSecurity | 35,603 | Specifies the default security settings for macros in the Revit application. |
| MajorSegment | 35,293 | Identifies one segment of the rebar shape that maintains its general position in rotation and auto\-expansion behaviors. |
| ManageConnectionToARevitServerAccelerator | 53,949 | Specifies the Revit Server Accelerator to use for worksharing, or changes the accelerator to which you are connected. |
| ManageImages | 33,648 | Lists all raster images used in the project. |
| ManageLinks | 33,279 | Provides options to manage linked files and imported data for various file types. |
| ManageTemplates | 37,314 | Manages and applies panel schedule templates to existing schedules in the project. |
| ManageViewTemplates | 33,683 | Displays parameters for view templates in the project. |
| MaskingRegion | 35,287 | Creates a graphic that obscures elements in a project or family. |
| Matchline | 33,905 | Adds matchlines to indicate where a view is split. |
| MatchTypeProperties | 33,513 | Converts one or more elements to match the type of another element in the same view. |
| MaterialAssets | 33,186 | Modifies the assets that define a material. |
| MaterialKeynote | 35,159 | Tags a selected element using the keynote specified for its material. |
| Materials | 33,184 | Specifies the materials and associated properties to apply to model elements or families. |
| MaterialTag | 35,145 | Tags a selected element using the description specified for its material. |
| MaterialTakeoff | 3,388 | Creates a list of the sub\-components or materials of any Revit family category. |
| MeasureAlongAnElement | 48,963 | Measures the length of an element. |
| MeasureBetweenTwoReferences | 48,962 | Measures the distance between two elements or references. |
| MechanicalControlDevice | 45,673 | Places a mechanical control device such as thermostats, CO2 sensors, and humidistats. |
| MechanicalEquipment | 37,008 | Places mechanical equipment such as boilers, furnaces, or fans. |
| MechanicalSettings | 37,168 | Opens the Mechanical Settings dialog. |
| MEPFabricationDuctworkStiffener | 43,659 | Places a stiffener on fabrication ductwork. |
| MirrorDrawAxis | 49,000 | Draws a temporary line to use as an axis for mirroring. |
| MirrorPickAxis | 32,936 | Reverses the position of selected elements, using an existing line or edge as the mirror axis. |
| MirrorProject | 32,919 | Flips the position of a project around a selected axis. |
| Miter | 55,305 | Creates a miter cut vertically or at the bisecting line of two beams and the related connection between the beams. |
| ModelInPlace | 33,544 | Creates a component that is unique to the project. |
| ModelLine | 33,006 | Creates a line that exists in 3D space and is visible in all views of a project. |
| ModelText | 33,660 | Adds 3D text to the building model. |
| Move | 33,127 | Moves selected elements to the specified location in the current view. |
| MultiCategoryTag | 35,203 | Attaches tags to elements of multiple categories, based on a shared parameter. |
| Multiplanar | 50,051 | Toggles the ability to define a rebar shape bent in more than one plane. |
| MultiplePaths | 54,125 | Places multiple paths of travel between two selected points using a specified minimum path separation for each path. |
| MultipleValuesIndication | 54,124 | Specifies the value indicated for a parameter when multiple elements with different parameter values are selected. |
| MultiPointRouting | 37,574 | Automatically build a run of connected MEP fabrication parts by clicking points in the model. |
| NavigationBar | 35,631 | Shows or hides the navigation bar, which provides access to the ViewCube, SteeringWheels, and zoom/pan functions. |
| NewAnnotationSymbol | 33,339 | Creates a tag or symbol to identify elements in the project. |
| NewConceptualMass | 32,986 | Opens a template for creating a conceptual massing model. |
| NewFamily | 32,983 | Creates a set of custom components to use in projects. |
| NewProject | 33,179 | Creates a Revit project file. |
| NewSheet | 32,958 | Creates a page for a document set. |
| NewTitleBlock | 33,140 | Opens a template for creating a Title Block family. |
| NoteBlock | 33,659 | Creates a schedule of annotations added using the Symbol tool. |
| NurseCall | 37,282 | Places nurse call devices such as call stations, code blue stations, and door lights. |
| ObjectStyles | 32,947 | Specifies line weights, colors, and patterns, and materials for model objects, annotation objects, and imported objects. |
| Offset | 33,757 | Copies or moves a selected element (such as a line, wall, or beam) a specified distance perpendicular to its length. |
| OneWayIndicator | 54,126 | Place a one\-way annotation family into the view. |
| OpenCloudModel | 56,379 | Opens a Revit cloud model. |
| OpenFamily | 35,365 | Opens a Revit family. |
| OpenIFC | 3,355 | Opens an IFC file. |
| OpenIFCOptions | 3,409 | Sets options for the IFC template and class mapping. |
| Opening | 33,177 | Creates an opening in a host, such as a wall or ceiling. |
| OpeningByFace | 35,253 | Creates an opening that is perpendicular to the selected face of a roof, floor, or ceiling. |
| OpenProject | 51,800 | Opens a Revit project. |
| OpenRevitFile | 57,601 | Opens any Revit file type. |
| OpenSampleFiles | 35,815 | Opens a Revit sample file. |
| Options | 33,195 | Display Revit Options Dialog. |
| OverrideByCategory | 33,422 | Changes the graphic display settings for all elements that belong to the same category as the selected element in the current view. |
| OverrideByElement | 35,265 | Changes the graphic display settings for selected elements in the current view. |
| OverrideByFilter | 35,266 | Changes the graphic display settings for all elements in the view that meet the criteria specified in a filter. |
| Paint | 33,656 | Applies a material to the face of an element. |
| PAndIDModeler | 35,882 | Create a 3D piping model directly from a 2D P\&ID drawing in the cloud. |
| PAndIDSettings | 35,883 | Manage the mappings between elements, such as services and families, between the P\&ID drawing and the Revit model. |
| PanelByBoundary | 56,448 | Creates a planar analytical panel for the current work plane after a sketch of the contour. |
| PanelByExtrusion | 56,525 | Creates an analytical panel perpendicular to the current work plane after a sketch of the path. |
| PanelSchedules | 37,053 | Generates a panel schedule for a specified panel. |
| ParallelConduits | 37,361 | Creates parallel runs of conduit based on an initial conduit run. |
| ParallelPipes | 37,441 | Creates parallel runs of pipe based on an initial pipe run. |
| ParametersService | 33,870 | Use the Parameters Service to manage shared parameters and import them into a Revit session. |
| ParkingComponent | 33,698 | Adds parking spaces to a topography. |
| PasteFromClipboard | 57,637 | Pastes elements from the clipboard into the current view. |
| PathOfTravel | 54,122 | Creates a path of travel along the shortest distance between 2 selected points. |
| PathReinforcementSymbol | 35,228 | Places a symbol that shows extents and hook types for the selected path reinforcement. |
| PDF | 56,711 | Creates PDF files. |
| PeopleContent | 54,127 | Place a family to indicate a person and a physical distance radius into the view. |
| Phases | 33,472 | Specifies project phases, phase filters, and graphic overrides for phases. |
| PickAPlane | 33,078 | Select a plane in the view to define a new workplane. |
| PickToEdit | 33,910 | Opens a design option for editing by selecting an element contained in the option. |
| Pin | 32,997 | Locks a model element in place. |
| Pipe | 37,100 | Draws rigid piping. |
| PipeAccessory | 37,105 | Places a pipe accessory. These accessories include connectors, valves, and inline water heaters. |
| PipeConnector | 37,219 | Adds a pipe connector to a component. |
| PipeFitting | 37,103 | Places a pipe fitting. These fittings include elbows, tees, wyes, crosses, unions, and other types of fittings. |
| PipeLegend | 37,149 | Places a legend to indicate the color fills associated with piping systems. |
| PipePlaceholder | 37,428 | Draws placeholder pipe without elbow or tee fittings. |
| PipePressureLossReport | 35,812 | Generates a pressure loss report for one or more pipe systems. |
| PlaceAComponent | 33,003 | Places an element in the building model, based on a selected element type. |
| PlaceDecal | 33,789 | Places an image on surfaces of a building model for rendering. |
| PlaceDetailGroup | 33,421 | Places an instance of a detail group in the view. |
| PlaceMass | 42,644 | Places an instance of a mass family in the project. |
| PlaceOnStairOrRamp | 35,807 | Places a railing on a stair or ramp. |
| PlaceView | 33,132 | Adds a view to a sheet. |
| PlanRegion | 33,900 | Creates a plan region within a view. |
| Plate | 54,292 | Creates a structural plate in the building model. |
| PlumbingEquipment | 45,674 | Places plumbing equipment such as hot water heaters, domestic water pumps, and sewage pumps. |
| PlumbingFixture | 37,203 | Places plumbing fixtures. These fixtures include sinks, water closets, tubs, drains, and various appliances. |
| PointCloud | 32,963 | Links a Point Cloud file (\*.rcp or \*.rcs) into the current project. |
| Print | 57,607 | Sends the current drawing area or selected views and sheets to a printer or a printable file. |
| PrintPreview | 57,609 | Displays a preview version of the current view or sheet to print. |
| PrintSetup | 57,606 | Specifies print options. |
| ProjectBrowser | 32,957 | Displays the Project Browser. |
| ProjectInformation | 33,543 | Specifies basic information about the project, including the project status and client information. |
| ProjectParameters | 33,855 | Specifies parameters that can be added to categories of elements in a project, and used in schedules. |
| ProjectUnits | 32,950 | Specifies the display format for units of measure. |
| PropertyLine | 33,480 | Creates a property line in a plan view. |
| PropertyLineData | 56,663 | Define the angle display and units used when creating and labeling property lines. |
| PublishCoordinates | 33,869 | Determines the coordinates used in the current model, and uses them for a linked model. |
| PublishSettings | 54,064 | Selects the views and sheets to publish to the cloud. |
| PurgeUnused | 33,780 | Removes unused families and types from a project. |
| RadialDimension | 48,958 | Places a dimension that measures the radius of an inner curve or fillet. |
| RadialDimensionTypes | 1,199 | Defines attributes for radial dimensions. |
| Railing | 34,969 | Creates a railing by sketching the railing path. |
| Ramp | 33,316 | Adds a ramp to the building model. |
| RebarBendingDetail | 56,523 | Creates realistic or schematic bar bending details for the selected individual rebar or sets. |
| RebarCoverSettings | 35,003 | Adds, removes, or modifies the default rebar cover settings. |
| RebarLine | 33,810 | Defines lines and geometry of the rebar shape. |
| ReCenterReference | 35,901 | Move the reference lines of all of the rooms in the view back to the center of the rooms. |
| ReconcileHosting | 35,708 | Lists tags and elements hosted by the linked model that require review, due to changes in the linked model. |
| Redo | 33,031 | Reverses the effects of the previous UNDO command |
| ReferenceLine | 34,994 | Creates a reference line that you can use when creating a new family, or to create constraints for the family. |
| ReferencePlane | 33,026 | Creates a reference plane using drawing tools. |
| ReflectedCeilingPlan | 33,380 | Creates a reflected ceiling plan view. |
| ReinforcementNumbers | 4,700 | Defines or edits numbering sequences by partition for rebar and fabric sheets. |
| ReinforcementSettings | 35,300 | Customizes reinforcement settings such as rounding parameters, rebar hosting and abbreviations of area/path reinforcement tagging. |
| RelinquishAllMine | 3,363 | Releases ownership of worksets and borrowed elements that have not been changed. |
| ReloadLatest | 1,729 | Loads updates from the central model to your local copy of the project. |
| RelocateProject | 33,856 | Moves the model relative to the shared coordinate system. |
| RemoveCoping | 46,451 | Removes coping from steel beams and columns. |
| RemoveHiddenLinesByElement | 33,673 | Removes hidden lines for model elements and detail elements that are obscured by other elements in the active view only. |
| RemovePaint | 33,657 | Removes paint from selected faces. |
| Render | 1,782 | Creates a photorealistic image of a building model. |
| RenderGallery | 53,962 | Opens your online gallery of completed and in\-progress renderings in a web browser. |
| RenderInCloud | 53,961 | Renders 3D views online to create still images or interactive panoramas. |
| RepairCentralModel | 57,283 | Repairs a corrupt central model. |
| RepeatComponent | 840 | Repeats the selected applied component along a divide path or surface. |
| RepeatingDetailComponent | 42,058 | Repeats a detail component along a path. |
| ReportSharedCoordinates | 33,865 | Displays shared coordinates of a linked model within a host model. |
| ResetSharedCoordinates | 56,335 | Eliminate shared coordinates in the host model. |
| RestoreBackup | 33,690 | Rolls back changes made to a workshared project, or saves a selected backup version to be the current working model. |
| RevealObstacles | 54,111 | Highlights categories that are considered obstacles in the view. |
| RevealWall | 33,654 | Extrudes a profile along a path to create a cutout in a wall. |
| ReviewWarnings | 33,352 | Displays a list of messages that you can ignore or resolve. |
| RevisionCloud | 33,540 | Adds a revision cloud to the current view or sheet to indicate design areas that have changed. |
| RevisionSchedule | 3,154 | Adds a revision schedule to a custom title block. |
| RoofByExtrusion | 1,143 | Creates a roof by extruding a profile that you sketch. |
| RoofByFace | 20 | Creates an element using a non\-vertical face of a mass. |
| RoofByFootprint | 1,142 | Creates a roof using the building footprint to define its boundaries. |
| Room | 33,198 | Creates a room bounded by model elements (such as walls, floors, and ceilings) and separation lines. |
| RoomSeparator | 33,318 | Creates a separation line to bound rooms where no walls or other room\-bounding elements exist. |
| RoomTag | 33,208 | Tags the selected room. |
| Rotate | 32,934 | Rotates selected elements around an axis. |
| RotateProjectNorth | 32,920 | Changes the relationship of elements relative to Project North (the top of the drawing area) in plan views. |
| RotateTrueNorth | 33,857 | Changes the angle for a project relative to True North. |
| RunAnalyticalToPhysicalForBuildings | 56,844 | Generates the structural Physical Model based on the selected analytical elements. |
| RunInterferenceCheck | 3,259 | Locates invalid intersections between elements in a project. |
| RunPhysicalToAnalyticalForBuildings | 56,843 | Generates the structural analytical model for selected structural physical elements. |
| Save | 57,603 | Saves the currently open project file. |
| SaveAsCloudModel | 56,243 | Saves the current Revit model to the cloud. |
| SaveAsFamily | 49,784 | Saves the current family. |
| SaveAsLibraryFamily | 33,923 | Saves a copy of all loaded families, the selected family, group, or view to your library. |
| SaveAsLibraryGroup | 33,696 | Saves a copy of all loaded families, the selected family, group, or view to your library. |
| SaveAsLibraryView | 42,312 | Saves a copy of all loaded families, the selected family, group, or view to your library. |
| SaveAsProject | 57,604 | Saves the current Revit project file. |
| SaveAsTemplate | 49,783 | Saves the current Revit project file as a template. |
| SaveSelection | 35,181 | Saves the currently selected elements as a set. |
| SawCutFlange | 55,306 | Creates a cut on a beam adjusted according to the flange of another intersecting beam and the related connection between the beams. |
| SawCutWeb | 55,307 | Creates a cut on a beam adjusted according to the web of another intersecting beam and the related connection between the beams. |
| Scale | 34,986 | Resizes the selected item. |
| ScheduleOrQuantities | 33,296 | Creates a key schedule or a schedule of building components. |
| ScopeBox | 33,519 | Controls the visibility of datum elements (grids, levels, and reference planes) in specific views. |
| Section | 32,955 | Creates a section view. |
| SectionTags | 3,169 | Specifies the shape of heads and tails for section tags. |
| Security | 37,283 | Places security devices such as door locks, motion sensors, and surveillance cameras. |
| SelectById | 33,867 | Uses an element's unique identifier to locate and select the element in the current view. |
| SelectionBox | 35,857 | Isolates selected elements in the current view (if a 3D isometric view) or the default 3D view. |
| SetWorkPlane | 33,527 | Specifies the work plane for the current view or for a selected work\-plane\-based element. |
| ShaftOpening | 35,257 | Creates a vertical opening that spans multiple levels, cutting through intervening roofs, floors, and ceilings. |
| ShapeStatus | 3,640 | When enabled, this button indicates that the rebar shape is not valid. |
| SharedParameters | 33,748 | Specifies parameters that can be used in multiple families and projects. |
| SharedViews | 56,329 | Opens and closes the Shared Views palette. |
| ShearStuds | 54,296 | Creates shear studs and the related welds on the selected face of model elements. |
| SheetIssuesOrRevisions | 3,153 | Specifies revision information for the project. |
| SheetList | 33,631 | Creates a schedule that lists the drawings in the project. |
| Shorten | 54,264 | Creates a shorten object on the selected beam that can trim or extend the beam. |
| ShowBoundaryOpenEnds | 45,665 | Displays dots on the open ends of area based load boundary lines. |
| ShowDisconnects | 37,444 | Controls the display of graphical disconnect warnings for duct, pipe, conduit, cable tray, electrical circuits, and fabrication hangers. |
| ShowHiddenLinesByElement | 33,671 | Displays hidden lines for individual model elements and detail elements that are obscured by other elements in the current view. |
| ShowHistory | 1,985 | Displays a list of all the times a workshared file (the central model or a local copy of the central model) was saved and who saved it. |
| ShowLastReport | 46,061 | Displays the most recent interference check report. |
| ShowMassByViewSettings | 35,075 | Displays masses based on the settings for the current view. By default, masses are turned off. |
| ShowMassFormAndFloors | 35,060 | Displays mass forms and any mass floors you have specified in all views. |
| ShowMassSurfaceTypes | 35,078 | Displays mass faces, including any glazing and shades that have been specified. |
| ShowMassZonesAndShades | 35,079 | Displays mass zones, glazing, and shades if they have been specified. |
| ShowWarningsInViews | 1,000 | Select to show structural connection warning marks in your project views. Deselect to hide warning marks. |
| ShowWorkPlane | 40,484 | Displays or hides the active work plane in the view. |
| ShowWorksharingMakeEditableControls | 35,195 | Enables/Disables display of "Make Editable" controls when elements are selected. |
| SingleFabricSheetPlacement | 35,823 | Places a single fabric sheet on floors, walls, and foundation slabs. |
| SiteComponent | 40,239 | Adds site\-specific elements, such as trees, parking islands, and fire hydrants. |
| Slab | 35,156 | Adds a foundation slab to the building model. |
| SlabEdgeFloor | 40,603 | Shapes the horizontal edge of a floor slab. |
| Snaps | 32,949 | Specifies snap increments, and enables or disables snap points. |
| Soffit | 493 | Creates a roof soffit in the building model. |
| SolidBlend | 33,278 | Creates a solid 3D shape that changes along its length, blending from a starting shape to an ending shape. |
| SolidExtrusion | 33,002 | Creates a 3D solid by extruding a 2D shape (profile). |
| SolidRevolve | 33,287 | Creates a 3D shape by sweeping a 2D profile around an axis. |
| SolidSweep | 33,300 | Creates a 3D shape by sweeping a 2D profile along a path. |
| SolidSweptBlend | 47,163 | Creates a blend that sweeps along a defined path. |
| Space | 32,784 | Places analytical spaces to account for the entire volume within the model. This includes rooms, plenums and chases. |
| SpaceNaming | 57,269 | Assigns the names and numbers from architectural rooms to MEP spaces used for building performance analysis. |
| SpaceSeparator | 32,786 | Draws a space separation line to divide space. |
| SpaceTag | 32,785 | Labels spaces in a project. |
| SpanDirectionSymbol | 34,980 | Places a span direction symbol on a structural floor. |
| SpatialGrid | 54,128 | Place a square or hexagonal grid in a room element. |
| SpecifyCoordinatesAtPoint | 3,266 | Relocates a model and rotates the model to True North by specifying coordinates for North/South, East/West, and Elevation. |
| SplineWire | 37,261 | Draws splined wire runs. |
| SplitElement | 1,100 | Cuts an element into separate individual elements. |
| SplitFace | 33,689 | Divides the face of an element (such as a wall or floor) into regions for the application of different materials. |
| SplitWithGap | 33,829 | Splits a wall, pipe, duct, cable tray, conduit, structural framing or a column into 2 segments with a defined gap. |
| SpotCoordinate | 1,114 | Displays the North/South and East/West coordinates of points in a project. |
| SpotCoordinateTypes | 33,351 | Defines attributes for spot coordinates. |
| SpotElevation | 1,109 | Displays the elevation of a selected point. |
| SpotElevationTypes | 33,350 | Defines attributes for spot elevations. |
| SpotSlope | 35,259 | Displays the slope at a specific point on a face or an edge of a model element. |
| SpotSlopeTypes | 33,348 | Defines attributes for spot slopes. |
| Sprinkler | 37,206 | Places a sprinkler. |
| Stair | 32,916 | Adds a stair to the building model by creating common run, landing, and support components. |
| StairPath | 33,010 | Annotates the slope direction and walk line of a stair. |
| StairTreadOrRiserNumber | 53,827 | Creates a sequence of tread or riser numbers for a run in plan, elevation, or section views. |
| StartingView | 33,327 | Specifies the view that first displays when you open the model. |
| StatusBar | 59,393 | Displays the status bar at the bottom of the Revit window. |
| StatusBarDesignOptions | 4,610 | Displays the active design option in the status bar. |
| StatusBarWorksets | 4,609 | For a workshared project, displays the active workset and the number of Others' pending Editing Requests in the status bar. |
| StructuralAreaReinforcement | 46,932 | Sketches the boundary of an area to populate with rebar. |
| StructuralColumn | 34,974 | Adds a vertical load\-bearing element to the building model. |
| StructuralConnection | 997 | Adds a structural connection to structural elements. |
| StructuralFabricArea | 35,781 | Located on the Reinforcement panel of the Structure tab (or Modify tab for floors, walls and foundation slabs).Sketches the boundary of a fabric area to populate with fabric sheets. |
| StructuralFloor | 34,985 | Creates a structural floor (slab) for the current level of the building model. |
| StructuralPathReinforcement | 35,225 | Sketches the path of evenly placed reinforcing bars that are created perpendicular to the sketch. |
| StructuralPlan | 32,952 | Creates a structural plan view. |
| StructuralRebar | 35,098 | Places planar, multi\-planar or free form rebar. |
| StructuralSettings | 34,993 | Defines settings for analytical elements and the display of structural framing. |
| StructuralTrusses | 43,213 | Adds a truss to the structure model. |
| StructuralWall | 34,975 | Creates a load\-bearing or shear wall in the building model. |
| SubstitutionSettings | 56,815 | Opens the Twinmotion Substitution Settings dialog. |
| SunSettings | 12,299 | Specifies the location of the sun for solar studies, walkthroughs, and rendered images. |
| SweepWall | 33,655 | Creates a wall sweep by extruding a profile along a path. |
| SwitchJoinOrder | 33,731 | Changes the order in which elements join with one another. |
| Symbol | 33,221 | Places a 2D annotation drawing symbol in the current view. |
| SymbolicLine | 33,700 | Creates lines that are meant for symbolic purposes only, and are not part of the actual geometry of the component or building model. |
| SynchronizeAndModifySettings | 33,542 | Allows you to specify options for the synchronization operation. |
| SynchronizeNow | 42,654 | Updates a local copy of a workshared project using settings from the Synchronize with Central dialog. |
| SystemBrowser | 3,280 | Displays the System Browser. Displays a hierarchical list of all the components in each discipline in a project, either by system or by zone. |
| SystemsAnalysis | 56,254 | Performs a systems analysis and generates a report for whole building energy simulation and analysis. |
| TabViews | 57,650 | Arranges all open views in the drawing area as tabs in a single window. |
| TagAllNotTagged | 33,735 | Adds tags to multiple elements in one step. |
| TagByCategory | 33,329 | Attaches a tag to an element based on the element category. |
| Telephone | 37,284 | Places a telephone jack. |
| TemporaryDimensions | 33,100 | Specifies the placement and component references for temporary dimensions. |
| Text | 33,134 | Adds text annotations (notes) to the current view. |
| ThinLines | 33,834 | Displays all lines on screen as a single width, regardless of zoom level. |
| TileViews | 57,652 | Arranges all open views within the application window, tiled so you can see each one in the drawing area. |
| TitleBlock | 33,806 | Creates a title block element in a sheet view. |
| ToggleHome | 56,242 | Toggle Revit Home. |
| TogglePAndIDModelerBrowser | 35,884 | Toggle P\&ID Modeler browser. |
| TogglePropertiesPalette | 4,534 | Displays or hides a palette where you can view and edit instance properties. |
| ToggleRevealHiddenElementsMode | 35,263 | Toggle reveal hidden elements mode. |
| TopChord | 3,620 | Draws the top chord of the truss family. |
| TopographyCutVoidStability | 56,840 | Enable void cut stability. |
| Toposolid | 56,481 | Creates a solid topographical element. |
| ToposolidByFace | 56,723 | Creates an element using a non\-vertical face of a mass. |
| ToposolidSmoothShading | 56,764 | Display toposolid elements in the model with smoothed surfaces. |
| TransferProjectStandards | 33,699 | Copies selected project settings from another open project to the current project. |
| TrimOrExtendMultipleElements | 48,954 | Trims or extends multiple elements (such as walls, lines, and beams) to a boundary defined by another element. |
| TrimOrExtendSingleElement | 48,953 | Trims or extends one element (such as a wall, line, or beam) to a boundary defined by another element. |
| TrimOrExtendToCorner | 48,952 | Trims or extends elements (such as walls or beams) to form a corner. |
| TypeProperties | 32,790 | Displays properties for the family type to which the selected element belongs. |
| UncutGeometry | 33,408 | Selects which geometry does not get cut when you join geometry. |
| Undo | 33,032 | Reverses the most recent action |
| UnjoinGeometry | 33,730 | Removes a join between 2 or more elements. |
| Unpin | 33,001 | Unlocks a model element so it can move. |
| UserKeynote | 35,160 | Tags an element with a keynote that you select. |
| VerticalOpening | 35,254 | Cuts a vertical opening through a roof, floor, or ceiling. |
| ViewCube | 35,458 | Shows or hides the ViewCube, which allows you to change the orientation of a 3D view. |
| ViewList | 1,075 | Creates a schedule of the views in the project. |
| ViewReference | 33,906 | Adds an annotation indicating the sheet number and detail number for a selected view. |
| VisibilityOrGraphics | 33,175 | Overrides the default visibility and graphic display of model elements and annotations in the current view. |
| VoidBlend | 33,398 | Creates a 3D blend, which is then used to remove part of a solid 3D shape. |
| VoidExtrusion | 33,397 | Creates a 3D shape that is then used to remove part of a solid 3D shape. |
| VoidRevolve | 33,399 | Creates a 3D shape by sweeping a 2D profile around an axis, and uses the 3D shape to remove part of a solid 3D shape. |
| VoidSweep | 33,400 | Creates a 3D shape by sweeping a 2D profile along a path, and uses the resulting 3D shape to remove part of a solid 3D shape. |
| VoidSweptBlend | 47,164 | Creates a blend that sweeps along a defined path, and uses the resulting 3D shape to remove part of a solid 3D shape. |
| Walkthrough | 33,000 | Creates an animated 3D walkthrough of a model. |
| Wall | 35,113 | Creates foundations hosted by walls. |
| WallByFaceWall | 35,074 | Creates walls using faces of a mass or generic model. |
| WallJoins | 33,323 | Changes how walls join together (butt, miter, square off). |
| WallOpening | 35,256 | Cuts a rectangular opening in a straight or curved wall. |
| Web | 3,619 | Draws the web elements between the chords. |
| Welds | 54,290 | Inserts a weld on one of the available edges of the model elements to be connected. |
| Window | 32,773 | Adds windows to the building model. |
| Worksets | 33,460 | Creates worksets and adds elements to them. |
| WorksharingMonitor | 56,309 | Launches Worksharing Monitor to manage a file\-based workshared model. |
| ZoneBySketch | 37,617 | Create a zone by sketching the perimeter. |
| ZoneBySpace | 46,711 | Create a zone by selecting spaces. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)
