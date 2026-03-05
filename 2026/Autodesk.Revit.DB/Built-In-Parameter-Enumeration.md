# Built In Parameter Enumeration

Source: https://www.revitapidocs.com/2026/fb011c91-be7e-f737-28c7-3f1e1917a0e0.htm

---

| Built In Parameter Enumeration |
| --- |

An enumerated type listing all of the built\-in parameter IDs supported by Autodesk
Revit. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum BuiltInParameter
```

```
Public Enumeration BuiltInParameter
```

```
public enum class BuiltInParameter
```

```
type BuiltInParameter
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| ACTUAL\_MAX\_RIDGE\_HEIGHT\_PARAM | \-1,001,705 | "Maximum Ridge Height" |
| ALIGNMENT\_STATION\_LABEL\_DISTANCE | \-1,006,595 | "Distance": Currently not in use |
| ALIGNMENT\_STATION\_LABEL\_INCLUDE\_STATION | \-1,006,597 | "Include Station" |
| ALIGNMENT\_STATION\_LABEL\_IND\_STATION | \-1,006,598 | "Station Indicator" |
| ALIGNMENT\_STATION\_LABEL\_SET\_END\_STATION | \-1,019,203 | "Alignment Label Set End Station" |
| ALIGNMENT\_STATION\_LABEL\_SET\_INTERVAL | \-1,019,201 | "Alignment Station Label Set Interval": The text is not used directly anywhere in the UI,  instead the XAML specifies its own string for the value's label. |
| ALIGNMENT\_STATION\_LABEL\_SET\_OFFSET | \-1,019,200 | "Alignment Station Label Set Offset": The text is not used directly anywhere in the UI,  instead the XAML specifies its own string for the value's label. |
| ALIGNMENT\_STATION\_LABEL\_SET\_START\_STATION | \-1,019,202 | "Alignment Label Set Start Station" |
| ALIGNMENT\_STATION\_LABEL\_STATION\_VALUE | \-1,006,599 | "Station Value" |
| ALIGNMENT\_STATION\_PREFIX | \-1,006,593 | "Station Prefix" |
| ALIGNMENT\_STATION\_SUFFIX | \-1,006,594 | "Station Suffix" |
| ALL\_GRID\_ROTATION\_FOR\_DIVISION\_RULE | \-1,152,349 | "All Grid Rotation" |
| ALL\_MODEL\_COST | \-1,001,205 | "Cost" |
| ALL\_MODEL\_DESCRIPTION | \-1,010,103 | "Description" |
| ALL\_MODEL\_FAMILY\_NAME | \-1,002,002 | "Family Name" |
| ALL\_MODEL\_IMAGE | \-1,152,385 | "Image" |
| ALL\_MODEL\_INSTANCE\_COMMENTS | \-1,010,106 | "Comments" |
| ALL\_MODEL\_MANUFACTURER | \-1,010,108 | "Manufacturer" |
| ALL\_MODEL\_MARK | \-1,001,203 | "Mark" |
| ALL\_MODEL\_MODEL | \-1,010,109 | "Model" |
| ALL\_MODEL\_TYPE\_COMMENTS | \-1,010,105 | "Type Comments" |
| ALL\_MODEL\_TYPE\_IMAGE | \-1,152,384 | "Type Image" |
| ALL\_MODEL\_TYPE\_MARK | \-1,001,405 | "Type Mark" |
| ALL\_MODEL\_TYPE\_NAME | \-1,002,001 | "Type Name" |
| ALL\_MODEL\_URL | \-1,010,104 | "URL" |
| ALLOW\_AUTO\_EMBED | \-1,001,009 | "Automatically Embed" |
| ALLOW\_MULTIPLE\_SELECTION | \-1,612,357 | "Allow Multiple Selection": This is used by the UI to allow selection of multiple elements. |
| ALTERNATE\_UNITS | \-1,006,456 | "Alternate Units" |
| ALTERNATE\_UNITS\_PREFIX | \-1,006,518 | "Alternate Units Prefix" |
| ALTERNATE\_UNITS\_SUFFIX | \-1,006,519 | "Alternate Units Suffix" |
| ALWAYS\_ZERO\_LENGTH | \-1,006,927 | "Base Offset" |
| ANALYTIC\_CONSTRUCTION | \-1,114,830 | "Analytic Construction" |
| ANALYTIC\_CONSTRUCTION\_GBXML\_TYPEID | \-1,005,438 | "Construction Type Id" |
| ANALYTIC\_CONSTRUCTION\_LOOKUP\_TABLE | \-1,005,437 | "Analytic Construction" |
| ANALYTICAL\_ABSORPTANCE | \-1,005,435 | "Absorptance" |
| ANALYTICAL\_ADJACENT\_SPACE | \-1,114,827 | "Adjacent Analytical Space" |
| ANALYTICAL\_DEFINE\_THERMAL\_PROPERTIES\_BY | \-1,005,439 | "Define Thermal Properties by" |
| ANALYTICAL\_ELEMENT\_HAS\_ASSOCIATION | \-1,013,449 | "Has Association": Used for Analytical Member, Analytical Panel, Structural Columns, Structural Framing, Floors, Walls, Structural Foundation |
| ANALYTICAL\_ELEMENT\_PHYSICAL\_ASSET | \-1,013,452 | "Physical Material Asset": Used for Analytical Elements. |
| ANALYTICAL\_ELEMENT\_STRUCTURAL\_ROLE | \-1,013,453 | "Structural Role": Used for Analytical Elements |
| ANALYTICAL\_GEOMETRY\_IS\_VALID | \-1,013,451 | "Analytical Model Correct" |
| ANALYTICAL\_HEAT\_TRANSFER\_COEFFICIENT | \-1,005,430 | "Heat Transfer Coefficient (U)" |
| ANALYTICAL\_LINK\_RELEASE\_ROTATION\_X | \-1,009,528 | "X Rotation" |
| ANALYTICAL\_LINK\_RELEASE\_ROTATION\_Y | \-1,009,529 | "Y Rotation" |
| ANALYTICAL\_LINK\_RELEASE\_ROTATION\_Z | \-1,009,530 | "Z Rotation" |
| ANALYTICAL\_LINK\_RELEASE\_TRANSLATION\_X | \-1,009,525 | "X Translation" |
| ANALYTICAL\_LINK\_RELEASE\_TRANSLATION\_Y | \-1,009,526 | "Y Translation" |
| ANALYTICAL\_LINK\_RELEASE\_TRANSLATION\_Z | \-1,009,527 | "Z Translation" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_ALL\_NON\_ZERO | \-1,060,014 | "All non 0 forces at end" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_FX | \-1,060,006 | "End Fx" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_FY | \-1,060,007 | "End Fy" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_FZ | \-1,060,008 | "End Fz" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_MX | \-1,060,009 | "End Mx" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_MY | \-1,060,010 | "End My" |
| ANALYTICAL\_MEMBER\_FORCE\_END\_MZ | \-1,060,011 | "End Mz" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_ALL\_NON\_ZERO | \-1,060,013 | "All non 0 forces at start" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_FX | \-1,060,000 | "Start Fx" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_FY | \-1,060,001 | "Start Fy" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_FZ | \-1,060,002 | "Start Fz" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_MX | \-1,060,003 | "Start Mx" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_MY | \-1,060,004 | "Start My" |
| ANALYTICAL\_MEMBER\_FORCE\_START\_MZ | \-1,060,005 | "Start Mz" |
| ANALYTICAL\_MEMBER\_ROTATION | \-1,013,456 | "Cross\-Section Rotation": Used for Analytical Member |
| ANALYTICAL\_MEMBER\_SECTION\_TYPE | \-1,009,533 | "Section Type": The id of the type from the structural Family assigned to the analytical member. |
| ANALYTICAL\_MODEL\_AREA | \-1,150,462 | "Area": The Area of Analytical Model |
| ANALYTICAL\_MODEL\_BASE\_ALIGNMENT\_METHOD | \-1,009,506 | "Base Alignment Method" |
| ANALYTICAL\_MODEL\_BASE\_EXTENSION\_METHOD | \-1,009,514 | "Base Extension Method" |
| ANALYTICAL\_MODEL\_BASE\_Y\_PROJECTION | \-1,009,508 | "Base y Projection" |
| ANALYTICAL\_MODEL\_BASE\_Z\_PROJECTION | \-1,009,507 | "Base z Projection" |
| ANALYTICAL\_MODEL\_CODE\_CHECKING | \-1,013,447 | "Code Checking": Used for Analytical wall, Analytical beam, Analytical column, Analytical floor, Analytical wall foundations, Analytical isolated foundations, Analytical foundations slab, Anaytical brace |
| ANALYTICAL\_MODEL\_COLUMN\_BASE\_EXTENSION | \-1,009,515 | "Base x Projection" |
| ANALYTICAL\_MODEL\_COLUMN\_TOP\_EXTENSION | \-1,009,513 | "Top x Projection" |
| ANALYTICAL\_MODEL\_END\_ALIGNMENT\_METHOD | \-1,009,503 | "End Alignment Method" |
| ANALYTICAL\_MODEL\_END\_PROJECTION\_ORTHOGONAL | \-1,009,532 | "End Projection Orthogonal" |
| ANALYTICAL\_MODEL\_END\_Y\_PROJECTION | \-1,009,504 | "End y Projection" |
| ANALYTICAL\_MODEL\_END\_Z\_PROJECTION | \-1,009,505 | "End z Projection" |
| ANALYTICAL\_MODEL\_FLOOR\_ALIGNMENT\_METHOD | \-1,009,516 | "Alignment Method" |
| ANALYTICAL\_MODEL\_FLOOR\_PROJECTION | \-1,009,517 | "z Projection" |
| ANALYTICAL\_MODEL\_FOUNDATIONS\_MARK | \-1,013,445 | "Foundation Number": Used for isolated, wall foundations |
| ANALYTICAL\_MODEL\_HEIGHT\_PARAM | \-1,155,258 | "Height" |
| ANALYTICAL\_MODEL\_LENGTH | \-1,150,461 | "Length": The length of Analytical Model |
| ANALYTICAL\_MODEL\_MANUALLY\_ADJUSTED | \-1,152,343 | "Manually Adjusted" |
| ANALYTICAL\_MODEL\_NODES\_MARK | \-1,013,446 | "Node Number": Used for nodes |
| ANALYTICAL\_MODEL\_PERIMETER | \-1,150,463 | "Perimeter": The Perimeter of Analytical Model |
| ANALYTICAL\_MODEL\_PHYSICAL\_TYPE | \-1,009,524 | "Family Type": the Family Type of the physical element associated with the Analytical Model |
| ANALYTICAL\_MODEL\_ROTATION | \-1,150,501 | "Cross\-Section Rotation": The rotation of Analytical Model |
| ANALYTICAL\_MODEL\_SKETCH\_ALIGNMENT\_METHOD | \-1,009,522 | "Alignment Method" |
| ANALYTICAL\_MODEL\_SKETCH\_PROJECTION | \-1,009,523 | "In\-Plane Projection" |
| ANALYTICAL\_MODEL\_START\_ALIGNMENT\_METHOD | \-1,009,500 | "Start Alignment Method" |
| ANALYTICAL\_MODEL\_START\_PROJECTION\_ORTHOGONAL | \-1,009,531 | "Start Projection Orthogonal" |
| ANALYTICAL\_MODEL\_START\_Y\_PROJECTION | \-1,009,501 | "Start y Projection" |
| ANALYTICAL\_MODEL\_START\_Z\_PROJECTION | \-1,009,502 | "Start z Projection" |
| ANALYTICAL\_MODEL\_STICK\_ELEMENTS\_MARK | \-1,013,443 | "Member Number": Used for beams, braces, columns |
| ANALYTICAL\_MODEL\_SURFACE\_ELEMENTS\_MARK | \-1,013,444 | "Surface Number": Used for floors, slabs, walls |
| ANALYTICAL\_MODEL\_TOP\_ALIGNMENT\_METHOD | \-1,009,509 | "Top Alignment Method" |
| ANALYTICAL\_MODEL\_TOP\_EXTENSION\_METHOD | \-1,009,512 | "Top Extension Method" |
| ANALYTICAL\_MODEL\_TOP\_Y\_PROJECTION | \-1,009,511 | "Top y Projection" |
| ANALYTICAL\_MODEL\_TOP\_Z\_PROJECTION | \-1,009,510 | "Top z Projection" |
| ANALYTICAL\_MODEL\_WALL\_ALIGNMENT\_METHOD | \-1,009,518 | "Alignment Method" |
| ANALYTICAL\_MODEL\_WALL\_BASE\_PROJECTION | \-1,009,521 | "Base y Projection" |
| ANALYTICAL\_MODEL\_WALL\_PROJECTION | \-1,009,519 | "z Projection" |
| ANALYTICAL\_MODEL\_WALL\_TOP\_PROJECTION | \-1,009,520 | "Top y Projection" |
| ANALYTICAL\_NODE\_CAN\_BE\_HOSTED | \-1,180,421 | "Can Be Hosted": Specifies of the Analytical Node can be hosted or not. |
| ANALYTICAL\_NODE\_CONNECTION\_STATUS | \-1,013,457 | "Connection Status" |
| ANALYTICAL\_NODE\_TYPE | \-1,180,420 | "Node Type": Specifies the type of the Analytical Node: hosted or not. |
| ANALYTICAL\_PANEL\_THICKNESS | \-1,013,455 | "Thickness": Used for Analytical Panel |
| ANALYTICAL\_ROUGHNESS | \-1,005,436 | "Roughness" |
| ANALYTICAL\_SOLAR\_HEAT\_GAIN\_COEFFICIENT | \-1,005,432 | "Solar Heat Gain Coefficient" |
| ANALYTICAL\_SPACE | \-1,114,826 | "Analytical Space" |
| ANALYTICAL\_SURFACE | \-1,114,835 | "Analytical Surface" |
| ANALYTICAL\_THERMAL\_MASS | \-1,005,434 | "Thermal Mass" |
| ANALYTICAL\_THERMAL\_RESISTANCE | \-1,005,431 | "Thermal Resistance (R)" |
| ANALYTICAL\_VISUAL\_LIGHT\_TRANSMITTANCE | \-1,005,433 | "Visual Light Transmittance" |
| ANALYTICAL\_ZONE | \-1,114,839 | "Analytical Zone" |
| ANALYTICAL\_ZONE\_NAME | \-1,114,845 | "Name" |
| ANY\_PATTERN\_ID\_PARAM | \-1,002,105 | "Fill Pattern" |
| ANY\_PATTERN\_ID\_PARAM\_NO\_NO | \-1,002,115 | "Fill Pattern" |
| ARC\_CENTER\_MARK | \-1,006,406 | "Center Marks" |
| ARC\_CURVE\_CNTR\_MRK\_VISIBLE | \-1,007,900 | "Center Mark Visible" |
| ARC\_ELEM\_FIX\_KEEP\_CONCENTRIC | \-1,123,512 | "Keep Concentric" |
| ARC\_LEADER\_PARAM | \-1,006,325 | "Arc Leaders" |
| ARC\_WALL\_CNTR\_MRK\_VISIBLE | \-1,007,900 | "Center Mark Visible" |
| AREA\_SCHEME\_ID | \-1,012,704 | "Area Scheme Id" |
| AREA\_SCHEME\_NAME | \-1,012,705 | "Name" |
| AREA\_TYPE | \-1,012,701 | "Area Type" |
| AREA\_TYPE\_TEXT | \-1,012,703 | "Area Type" |
| ARRAY\_ELEMENTS\_APPEND\_TO\_END | \-1,027,550 | "Append To End" |
| ARRAY\_GROUP\_AND\_ASSOCIATE | \-1,027,551 | "Group And Associate" |
| ARRAY\_INSTANCE\_PARAMETER | \-1,027,556 | "Instance" |
| ARRAY\_LABEL | \-1,027,555 | "Label" |
| ARRAY\_MOVE\_TO | \-1,027,553 | "Move To" |
| ARRAY\_NUMBER | \-1,027,552 | "Number" |
| ARRAY\_TYPE\_INDEX | \-1,027,554 | "Array type" |
| ARRAY\_TYPE\_PARAMETER | \-1,027,557 | "Type" |
| ARROW\_CENTERED | \-1,006,524 | "Tick Mark Centered" |
| ARROW\_CLOSED | \-1,006,449 | "Arrow Closed" |
| ARROW\_FILLED | \-1,006,425 | "Fill Tick" |
| ARROW\_SIZE | \-1,006,414 | "Tick Size" |
| ARROW\_TYPE | \-1,006,413 | "Arrow Style" |
| ARROWHEAD\_END\_AT\_RISER | \-1,006,627 | "End at Riser" |
| ARROWHEAD\_TYPE | \-1,006,623 | "Arrowhead Type" |
| ASSEMBLY\_CODE | \-1,002,500 | "Assembly Code" |
| ASSEMBLY\_DESCRIPTION | \-1,002,501 | "Assembly Description" |
| ASSEMBLY\_NAME | \-1,150,420 | "Assembly Name" |
| ASSEMBLY\_NAMING\_CATEGORY | \-1,150,403 | "Naming Category" |
| ASSEMBLY\_PRECAST\_FREEZE | \-1,155,210 | "Disable Precast Updates" |
| ASSIGN\_TEMPLATE\_ON\_VIEW\_CREATION | \-1,008,211 | "New views are dependent on template" |
| ASSOCIATED\_LEVEL | \-1,002,564 | "Associated Level": The level associated with this cell. |
| ASSOCIATED\_LEVEL\_OFFSET | \-1,002,565 | "Associated Level Offset": The offset from the associated level. |
| AUTO\_JOIN\_CONDITION | \-1,007,387 | "Join Condition" |
| AUTO\_JOIN\_CONDITION\_WALL | \-1,007,395 | "Join Condition" |
| AUTO\_MULLION\_BORDER1\_GRID1 | \-1,007,382 | "Border 1 Type" |
| AUTO\_MULLION\_BORDER1\_GRID2 | \-1,007,384 | "Border 1 Type" |
| AUTO\_MULLION\_BORDER1\_HORIZ | \-1,007,393 | "Border 1 Type" |
| AUTO\_MULLION\_BORDER1\_VERT | \-1,007,391 | "Border 1 Type" |
| AUTO\_MULLION\_BORDER2\_GRID1 | \-1,007,383 | "Border 2 Type" |
| AUTO\_MULLION\_BORDER2\_GRID2 | \-1,007,385 | "Border 2 Type" |
| AUTO\_MULLION\_BORDER2\_HORIZ | \-1,007,394 | "Border 2 Type" |
| AUTO\_MULLION\_BORDER2\_VERT | \-1,007,392 | "Border 2 Type" |
| AUTO\_MULLION\_INTERIOR\_GRID1 | \-1,007,380 | "Interior Type" |
| AUTO\_MULLION\_INTERIOR\_GRID2 | \-1,007,381 | "Interior Type" |
| AUTO\_MULLION\_INTERIOR\_HORIZ | \-1,007,390 | "Interior Type" |
| AUTO\_MULLION\_INTERIOR\_VERT | \-1,007,389 | "Interior Type" |
| AUTO\_PANEL | \-1,007,386 | "Curtain Panel" |
| AUTO\_PANEL\_WALL | \-1,007,388 | "Curtain Panel" |
| AZIMUTH | \-1,114,828 | "Azimuth" |
| BACKGROUND\_DRAFT\_PATTERN\_ID\_PARAM | \-1,002,122 | "Background Fill Pattern" |
| BACKGROUND\_PATTERN\_COLOR\_PARAM | \-1,002,124 | "Background Pattern Color" |
| BASELINE\_DIM\_OFFSET | \-1,006,477 | "Baseline Offset" |
| BASEPOINT\_ANGLETON\_PARAM | \-1,150,194 | "Angle to True North" |
| BASEPOINT\_EASTWEST\_PARAM | \-1,150,192 | "E/W" |
| BASEPOINT\_ELEVATION\_PARAM | \-1,150,193 | "Elev" |
| BASEPOINT\_LATITUDE\_PARAM | \-1,154,693 | "Lat" |
| BASEPOINT\_LONGITUDE\_PARAM | \-1,154,692 | "Lon" |
| BASEPOINT\_NORTHSOUTH\_PARAM | \-1,150,191 | "N/S" |
| BEAM\_H\_JUSTIFICATION | \-1,013,414 | "Lateral Justification" |
| BEAM\_SYSTEM\_3D\_PARAM | \-1,013,427 | "Non\-planar" |
| BEAM\_SYSTEM\_TAG\_INST\_PARAM\_ANGLE | \-1,013,418 | "Beam System Tag Direction" |
| BEAM\_SYSTEM\_TAG\_PARAM\_LEFT | \-1,013,416 | "Left" |
| BEAM\_SYSTEM\_TAG\_PARAM\_RIGHT | \-1,013,417 | "Right" |
| BEAM\_V\_JUSTIFICATION | \-1,013,413 | "z\-Direction Justification" |
| BEAM\_V\_JUSTIFICATION\_OTHER\_VALUE | \-1,001,574 | "z\-Direction Offset Value" |
| BENDING\_DETAIL\_ANGULAR\_DIMENSION\_TEXT\_POSITION | \-1,155,312 | "Angle Text Position" |
| BENDING\_DETAIL\_DETAIL\_LEVEL | \-1,155,313 | "Detail Level" |
| BENDING\_DETAIL\_REPRESENTATION\_FOR\_3D\_BARS | \-1,155,308 | "View for 3D Shape" |
| BENDING\_DETAIL\_SEGMENT\_LENGTH\_DIMENSION\_TEXT\_POSITION | \-1,155,311 | "Dimension Text Position" |
| BENDING\_DETAIL\_SEGMENT\_REPRESENTATION | \-1,155,310 | "Representation" |
| BENDING\_DETAIL\_TYPE\_ANGULAR\_DIMENSION\_OFFSET | \-1,155,298 | "Angular Dimension Offset" |
| BENDING\_DETAIL\_TYPE\_ANGULAR\_DIMENSION\_TYPE\_ID | \-1,155,296 | "Angular Dimension Style" |
| BENDING\_DETAIL\_TYPE\_ANGULAR\_DIMENSIONS\_ENABLED | \-1,155,295 | "Angular Dimensions" |
| BENDING\_DETAIL\_TYPE\_ANGULAR\_DIMENSIONS\_FOR\_CRANKS\_ENABLED | \-1,180,442 | "Crank Angles" |
| BENDING\_DETAIL\_TYPE\_ANGULAR\_DIMENSIONS\_FOR\_HOOKS\_ENABLED | \-1,155,306 | "Hook Angles" |
| BENDING\_DETAIL\_TYPE\_ANGULAR\_DIMENSIONS\_MEASUREMENT | \-1,155,307 | "Angle Measurement" |
| BENDING\_DETAIL\_TYPE\_BEND\_DIAMETER\_DIMENSIONS\_ENABLED | \-1,155,299 | "Bend Diameter Dimensions" |
| BENDING\_DETAIL\_TYPE\_BEND\_DIAMETER\_DIMENSIONS\_FOR\_HOOKS\_ENABLED | \-1,155,305 | "Hook Bends" |
| BENDING\_DETAIL\_TYPE\_BEND\_DIAMETER\_DIMENSIONS\_FOR\_SEGMENTS\_ENABLED | \-1,155,304 | "Segment Bends" |
| BENDING\_DETAIL\_TYPE\_DIAMETER\_DIMENSION\_TYPE\_ID | \-1,155,301 | "Diameter Dimension Style" |
| BENDING\_DETAIL\_TYPE\_ORTHOGONAL\_AND\_OVERALL\_DIMESIONS\_ENABLED | \-1,155,294 | "Other Dimensions" |
| BENDING\_DETAIL\_TYPE\_RADIAL\_DIMENSION\_TYPE\_ID | \-1,155,300 | "Radial Dimension Style" |
| BENDING\_DETAIL\_TYPE\_SCHEMATIC\_HEIGHT | \-1,155,318 | "Height" |
| BENDING\_DETAIL\_TYPE\_SCHEMATIC\_WIDTH | \-1,155,317 | "Width" |
| BENDING\_DETAIL\_TYPE\_SEGMENT\_LENGTH\_DIMENSION\_TYPE\_ID | \-1,155,289 | "Linear Dimension Style" |
| BENDING\_DETAIL\_TYPE\_SEGMENT\_LENGTH\_DIMENSIONS\_ENABLED | \-1,155,288 | "Segment Length Dimensions" |
| BENDING\_DETAIL\_TYPE\_SEGMENT\_LENGTH\_DIMENSIONS\_FOR\_HOOKS\_ENABLED | \-1,155,293 | "Hook Lengths" |
| BENDING\_DETAIL\_TYPE\_SEGMENT\_LENGTH\_DIMENSIONS\_OFFSET | \-1,155,292 | "Dimension Offset" |
| BENDING\_DETAIL\_TYPE\_SEGMENT\_LENGTHS\_DISPLAY\_OPTION | \-1,155,291 | "Straight Segment Lengths" |
| BENDING\_DETAIL\_TYPE\_SEGMENT\_LENGTHS\_FOR\_ARCS\_DISPLAY\_OPTION | \-1,155,290 | "Arc Segment Lengths" |
| BENDING\_DETAIL\_TYPE\_SHOW\_ANGULAR\_DIMENSIONS\_FOR | \-1,155,297 | "Show for Angles" |
| BENDING\_DETAIL\_TYPE\_SHOW\_BAR\_BENDING\_USING | \-1,155,302 | "Dimension Type" |
| BENDING\_DETAIL\_TYPE\_TAG\_TYPE\_ID | \-1,155,315 | "Tag Type" |
| BENDING\_DETAIL\_VARYING\_REBAR\_DIMENSION | \-1,155,309 | "Varying Rebar Set Dimensions" |
| BENDINGDETAIL\_POSITION | \-1,180,317 | "Bending Detail Position" |
| BENT\_FABRIC\_PARAM\_BEND\_DIRECTION | \-1,017,729 | "Bend Direction": Direction in which FabricSheet is bent. |
| BENT\_FABRIC\_PARAM\_LONGITUDINAL\_CUT\_LENGTH | \-1,017,734 | "Longitudinal Cut Length": Bent fabric longitudinal cut length. |
| BENT\_FABRIC\_PARAM\_STRAIGHT\_WIRES\_LOCATION | \-1,017,731 | "Straight Wires Location": Location of straight wires in a bent fabric. |
| BLEND\_DEPTH\_PARAM | \-1,155,314 | "Depth" |
| BLEND\_END\_PARAM | \-1,001,805 | "Second End" |
| BLEND\_START\_PARAM | \-1,001,804 | "First End" |
| BOUNDARY\_AREA\_RESTRAINT\_X | \-1,140,518 | "X Spring Modulus" |
| BOUNDARY\_AREA\_RESTRAINT\_Y | \-1,140,519 | "Y Spring Modulus" |
| BOUNDARY\_AREA\_RESTRAINT\_Z | \-1,140,520 | "Z Spring Modulus" |
| BOUNDARY\_BEARING | \-1,012,404 | "Bearing" |
| BOUNDARY\_CONDITIONS\_IS\_EXT | \-1,140,501 | "Is Boundary Conditions External?" |
| BOUNDARY\_CONDITIONS\_TYPE | \-1,140,500 | "Boundary Conditions Type" |
| BOUNDARY\_DIRECTION\_ROT\_X | \-1,140,505 | "X Rotation" |
| BOUNDARY\_DIRECTION\_ROT\_Y | \-1,140,506 | "Y Rotation" |
| BOUNDARY\_DIRECTION\_ROT\_Z | \-1,140,507 | "Z Rotation" |
| BOUNDARY\_DIRECTION\_X | \-1,140,502 | "X Translation" |
| BOUNDARY\_DIRECTION\_Y | \-1,140,503 | "Y Translation" |
| BOUNDARY\_DIRECTION\_Z | \-1,140,504 | "Z Translation" |
| BOUNDARY\_DISTANCE | \-1,012,403 | "Distance" |
| BOUNDARY\_LINEAR\_RESTRAINT\_ROT\_X | \-1,140,517 | "X Spring Modulus" |
| BOUNDARY\_LINEAR\_RESTRAINT\_X | \-1,140,514 | "X Spring Modulus" |
| BOUNDARY\_LINEAR\_RESTRAINT\_Y | \-1,140,515 | "Y Spring Modulus" |
| BOUNDARY\_LINEAR\_RESTRAINT\_Z | \-1,140,516 | "Z Spring Modulus" |
| BOUNDARY\_PARAM\_PRESET | \-1,140,633 | "State" |
| BOUNDARY\_PARAM\_PRESET\_AREA | \-1,140,635 | "State" |
| BOUNDARY\_PARAM\_PRESET\_LINEAR | \-1,140,634 | "State" |
| BOUNDARY\_RADIUS | \-1,012,407 | "Radius" |
| BOUNDARY\_RESTRAINT\_ROT\_X | \-1,140,511 | "X Spring Modulus" |
| BOUNDARY\_RESTRAINT\_ROT\_Y | \-1,140,512 | "Y Spring Modulus" |
| BOUNDARY\_RESTRAINT\_ROT\_Z | \-1,140,513 | "Z Spring Modulus" |
| BOUNDARY\_RESTRAINT\_X | \-1,140,508 | "X Spring Modulus" |
| BOUNDARY\_RESTRAINT\_Y | \-1,140,509 | "Y Spring Modulus" |
| BOUNDARY\_RESTRAINT\_Z | \-1,140,510 | "Z Spring Modulus" |
| BOUNDARY\_X\_ROTATION\_FIXED | \-1,140,521 | "X Rotation \- Fixed" |
| BOUNDARY\_X\_ROTATION\_SPRING | \-1,140,522 | "X Rotation \- Spring" |
| BOUNDARY\_X\_TRANSLATION\_FIXED | \-1,140,523 | "X Translation \- Fixed" |
| BOUNDARY\_X\_TRANSLATION\_SPRING | \-1,140,524 | "X Translation \- Spring" |
| BOUNDARY\_Y\_ROTATION\_FIXED | \-1,140,525 | "Y Rotation \- Fixed" |
| BOUNDARY\_Y\_ROTATION\_SPRING | \-1,140,526 | "Y Rotation \- Spring" |
| BOUNDARY\_Y\_TRANSLATION\_FIXED | \-1,140,527 | "Y Translation \- Fixed" |
| BOUNDARY\_Y\_TRANSLATION\_SPRING | \-1,140,528 | "Y Translation \- Spring" |
| BOUNDARY\_Z\_ROTATION\_FIXED | \-1,140,529 | "Z Rotation \- Fixed" |
| BOUNDARY\_Z\_ROTATION\_SPRING | \-1,140,530 | "Z Rotation \- Spring" |
| BOUNDARY\_Z\_TRANSLATION\_FIXED | \-1,140,531 | "Z Translation \- Fixed" |
| BOUNDARY\_Z\_TRANSLATION\_SPRING | \-1,140,532 | "Z Translation \- Spring" |
| BR\_ORG\_FILTER | \-1,002,007 | "Filter" |
| BR\_ORG\_FOLDERS | \-1,002,006 | "Folders" |
| BUILDING\_CLOSING\_TIME\_PARAM | \-1,114,356 | "Closing Time" |
| BUILDING\_CURVE\_GSTYLE | \-1,006,210 | "Line Style" |
| BUILDING\_CURVE\_GSTYLE\_PLUS\_INVISIBLE | \-1,006,211 | "Subcategory" |
| BUILDING\_OPENING\_TIME\_PARAM | \-1,114,355 | "Opening Time" |
| BUILDING\_UNOCCUPIED\_COOLING\_SET\_POINT\_PARAM | \-1,114,357 | "Unoccupied Cooling Set Point" |
| BUILDINGPAD\_HEIGHTABOVELEVEL\_PARAM | \-1,012,502 | "Height Offset From Level" |
| BUILDINGPAD\_THICKNESS | \-1,012,501 | "Thickness" |
| BUILIDING\_PAD\_STRUCTURE\_ID\_PARAM | \-1,002,119 | "Structure" |
| CABLETRAY\_MINBENDMULTIPLIER\_PARAM | \-1,140,119 | "Bend Radius Multiplier" |
| CALLOUT\_ATTR\_HEAD\_TAG | \-1,008,200 | "Callout Head" |
| CALLOUT\_CORNER\_SHEET\_RADIUS | \-1,008,201 | "Corner Radius" |
| CALLOUT\_SYNCRONIZE\_BOUND\_OFFSET\_FAR | \-1,008,203 | "Far Clip Settings" |
| CALLOUT\_TAG | \-1,008,206 | "Callout Tag" |
| CASEWORK\_CONSTRUCTION\_TYPE | \-1,001,207 | "Construction Type" |
| CASEWORK\_DEPTH | \-1,010,003 | "Depth" |
| CASEWORK\_FINISH | \-1,001,208 | "Finish" |
| CASEWORK\_HEIGHT | \-1,001,300 | "Height" |
| CASEWORK\_WIDTH | \-1,001,301 | "Width" |
| CEILING\_ATTR\_DEFAULT\_HEIGHT\_PARAM | \-1,002,200 | "Default Height above level" |
| CEILING\_ATTR\_PATTERN\_PARAM | \-1,002,201 | "Pattern" |
| CEILING\_ATTR\_SPACING1\_PARAM | \-1,002,202 | "Spacing Axis 1" |
| CEILING\_ATTR\_SPACING2\_PARAM | \-1,002,203 | "Spacing Axis 2" |
| CEILING\_ATTR\_SYSTEMNAME\_PARAM | \-1,002,204 | "System" |
| CEILING\_HAS\_THICKNESS\_PARAM | \-1,002,302 | "Has Thickness" |
| CEILING\_HEIGHTABOVELEVEL\_PARAM | \-1,002,300 | "Height Offset From Level" |
| CEILING\_STRUCTURE\_ID\_PARAM | \-1,002,118 | "Structure" |
| CEILING\_THICKNESS | \-1,002,206 | "Thickness" |
| CEILING\_THICKNESS\_PARAM | \-1,002,301 | "Thickness" |
| CENTER\_MARK\_SIZE | \-1,006,407 | "Center Mark Size" |
| CIRC\_MULLION\_RADIUS | \-1,007,350 | "Radius" |
| CIRCUIT\_LOAD\_CLASSIFICATION\_ABBREVIATION\_PARAM | \-1,140,179 | "Load Classification Abbreviation" |
| CIRCUIT\_LOAD\_CLASSIFICATION\_PARAM | \-1,140,120 | "Load Classification" |
| CIRCUIT\_PHASE\_PARAM | \-1,140,178 | "Phase Label" |
| CIRCUIT\_WAYS\_PARAM | \-1,140,180 | "Ways" |
| CIRCULAR\_FRAMING\_DIAMETER | \-1,155,248 | "Circular Diameter" |
| CLASSIFICATION\_CODE | \-1,002,502 | "Classification Number" |
| CLASSIFICATION\_DESCRIPTION | \-1,002,503 | "Classification Title" |
| CLEAR\_COVER | \-1,013,440 | "Rebar Cover" |
| CLEAR\_COVER\_BOTTOM | \-1,013,439 | "Rebar Cover \- Bottom Face" |
| CLEAR\_COVER\_EXTERIOR | \-1,013,435 | "Rebar Cover \- Exterior Face" |
| CLEAR\_COVER\_INTERIOR | \-1,013,436 | "Rebar Cover \- Interior Face" |
| CLEAR\_COVER\_OTHER | \-1,013,437 | "Rebar Cover \- Other Faces" |
| CLEAR\_COVER\_TOP | \-1,013,438 | "Rebar Cover \- Top Face" |
| CLIENT\_NAME | \-1,006,319 | "Client Name" |
| CLINE\_SUBCATEGORY | \-1,006,220 | "Subcategory" |
| COARSE\_SCALE\_FILL\_PATTERN\_COLOR | \-1,002,110 | "Coarse Scale Fill Color" |
| COARSE\_SCALE\_FILL\_PATTERN\_ID\_PARAM | \-1,002,106 | "Coarse Scale Fill Pattern" |
| COLOR\_FILL\_FILTERED\_PARAM | \-1,007,502 | "Values Displayed" |
| COLOR\_FILL\_SWATCH\_HEIGHT\_PARAM | \-1,007,504 | "Swatch Height" |
| COLOR\_FILL\_SWATCH\_WIDTH\_PARAM | \-1,007,503 | "Swatch Width" |
| COLOR\_SCHEME\_LOCATION | \-1,005,183 | "Color Scheme Location" |
| COLUMN\_BASE\_ATTACH\_CUT\_PARAM | \-1,002,561 | "Base Attachment Cut" |
| COLUMN\_BASE\_ATTACH\_JUSTIFICATION\_PARAM | \-1,002,556 | "Attachment Justification At Base" |
| COLUMN\_BASE\_ATTACHED\_PARAM | \-1,002,560 | "Base is Attached" |
| COLUMN\_BASE\_ATTACHMENT\_OFFSET\_PARAM | \-1,002,558 | "Offset From Attachment At Base" |
| COLUMN\_LOCATION\_MARK | \-1,002,563 | "Column Location Mark" |
| COLUMN\_TOP\_ATTACH\_CUT\_PARAM | \-1,002,562 | "Top Attachment Cut" |
| COLUMN\_TOP\_ATTACH\_JUSTIFICATION\_PARAM | \-1,002,555 | "Attachment Justification At Top" |
| COLUMN\_TOP\_ATTACHED\_PARAM | \-1,002,559 | "Top is Attached" |
| COLUMN\_TOP\_ATTACHMENT\_OFFSET\_PARAM | \-1,002,557 | "Offset From Attachment At Top" |
| CONCEPTUAL\_CONSTRUCTION\_MATERIAL | \-1,012,024 | "Graphical Appearance" |
| CONDUIT\_STANDARD\_TYPE\_PARAM | \-1,140,118 | "Standard" |
| CONNECTOR\_ANGLE | \-1,133,409 | "Angle" |
| CONNECTOR\_ANGLE\_OF\_DEFLECTION | \-1,140,338 | "Angle of Deflection" |
| CONNECTOR\_DIAMETER | \-1,133,415 | "Diameter" |
| CONNECTOR\_ENGAGEMENT\_LENGTH | \-1,140,329 | "Engagement Length" |
| CONNECTOR\_GENDER\_TYPE | \-1,140,172 | "Connector Gender Type" |
| CONNECTOR\_HEIGHT | \-1,133,404 | "Height" |
| CONNECTOR\_INDEX | \-1,133,406 | "Index" |
| CONNECTOR\_INSIDE\_DIAMETER | \-1,133,416 | "Inside Diameter" |
| CONNECTOR\_JOINT\_TYPE | \-1,140,171 | "Connector Joint Type" |
| CONNECTOR\_LENGTH | \-1,140,337 | "Length" |
| CONNECTOR\_PROFILE\_TYPE | \-1,133,400 | "Shape" |
| CONNECTOR\_RADIUS | \-1,133,401 | "Radius" |
| CONNECTOR\_REFERENCE\_INDEX | \-1,133,411 | "Link Connector Index" |
| CONNECTOR\_UTILITY\_PARAM | \-1,150,159 | "Utility" |
| CONNECTOR\_VISIBLE\_SIZE | \-1,133,405 | "Size on screen" |
| CONNECTOR\_WIDTH | \-1,133,403 | "Width" |
| CONSTRUCTION\_IS\_SCHEMATIC | \-1,114,846 | "Schematic" |
| CONSTRUCTION\_NAME | \-1,114,831 | "Name" |
| CONTINUOUS\_FOOTING\_BEARING\_WIDTH | \-1,001,562 | "Width" |
| CONTINUOUS\_FOOTING\_BOTTOM\_HEEL | \-1,001,556 | "Bottom Heel Length" |
| CONTINUOUS\_FOOTING\_BOTTOM\_TOE | \-1,001,554 | "Bottom Toe Length" |
| CONTINUOUS\_FOOTING\_BREAK\_AT\_INSERTS\_DISABLE | \-1,001,592 | "Do Not Break At Inserts" |
| CONTINUOUS\_FOOTING\_DEFAULT\_END\_EXTENSION\_LENGTH | \-1,001,591 | "Default End Extension Length" |
| CONTINUOUS\_FOOTING\_ECCENTRICITY | \-1,001,564 | "Eccentricity" |
| CONTINUOUS\_FOOTING\_LENGTH | \-1,001,567 | "Length" |
| CONTINUOUS\_FOOTING\_STRUCTURAL\_USAGE | \-1,001,563 | "Structural Usage" |
| CONTINUOUS\_FOOTING\_TOP\_HEEL | \-1,001,555 | "Heel Length" |
| CONTINUOUS\_FOOTING\_TOP\_TOE | \-1,001,553 | "Toe Length" |
| CONTINUOUS\_FOOTING\_WIDTH | \-1,001,558 | "Width" |
| CONTINUOUSRAIL\_BEGINNING\_TERMINATION\_ATTACHMENT\_PARAM | \-1,150,347 | "Extension Style" |
| CONTINUOUSRAIL\_BEGINNING\_TERMINATION\_TYPE\_PARAM | \-1,150,345 | "Beginning/Bottom Termination" |
| CONTINUOUSRAIL\_DEFAULT\_JOIN\_TYPE\_PARAM | \-1,150,337 | "Default Join" |
| CONTINUOUSRAIL\_END\_EXTENSION\_LENGTH\_PARAM | \-1,150,350 | "Length" |
| CONTINUOUSRAIL\_END\_TERMINATION\_ATTACHMENT\_PARAM | \-1,150,349 | "Extension Style" |
| CONTINUOUSRAIL\_END\_TERMINATION\_TYPE\_PARAM | \-1,150,346 | "End/Top Termination" |
| CONTINUOUSRAIL\_EXTENSION\_LENGTH\_PARAM | \-1,150,348 | "Length" |
| CONTINUOUSRAIL\_FILLET\_RADIUS\_PARAM | \-1,150,338 | "Fillet Radius" |
| CONTINUOUSRAIL\_JOIN\_TYPE\_PARAM | \-1,150,373 | "Rail Path Join" |
| CONTINUOUSRAIL\_LENGTH\_PARAM | \-1,150,360 | "Length" |
| CONTINUOUSRAIL\_MATERIALS\_PARAM | \-1,150,344 | "Material" |
| CONTINUOUSRAIL\_PLUS\_TREAD\_DEPTH\_PARAM | \-1,150,361 | "Plus Tread Depth" |
| CONTINUOUSRAIL\_PROFILE\_TYPE\_PARAM | \-1,150,339 | "Profile" |
| CONTINUOUSRAIL\_TRANSITION\_TYPE\_PARAM | \-1,150,343 | "Transitions" |
| CONTOUR\_ELEVATION | \-1,012,401 | "Elevation" |
| CONTOUR\_ELEVATION\_STEP | \-1,012,402 | "Increment" |
| CONTOUR\_LABELS\_ELEV\_BASE\_TYPE | \-1,012,621 | "Elevation Base" |
| CONTOUR\_LABELS\_LINEAR\_UNITS | \-1,012,609 | "Units Format" |
| CONTOUR\_LABELS\_PRIMARY\_ONLY | \-1,012,608 | "Label primary contours only" |
| CONTOUR\_LABELS\_RELATIVE\_BASE | \-1,012,622 | "Relative Base" |
| COUPLER\_CODE | \-1,154,638 | "Part Number" |
| COUPLER\_COUPLED\_BAR\_SIZE | \-1,154,640 | "Bar Size 2" |
| COUPLER\_COUPLED\_ENDTREATMENT | \-1,154,653 | "End Treatment 2" |
| COUPLER\_COUPLED\_ENGAGEMENT | \-1,154,646 | "Bar Engagement 2" |
| COUPLER\_LENGTH | \-1,154,644 | "Total Length" |
| COUPLER\_MAIN\_BAR\_SIZE | \-1,154,639 | "Bar Size 1" |
| COUPLER\_MAIN\_ENDTREATMENT | \-1,154,652 | "End Treatment 1" |
| COUPLER\_MAIN\_ENGAGEMENT | \-1,154,645 | "Bar Engagement 1" |
| COUPLER\_MARK | \-1,154,649 | "Schedule Mark" |
| COUPLER\_NUMBER | \-1,154,642 | "Coupler Number" |
| COUPLER\_QUANTITY | \-1,154,641 | "Quantity" |
| COUPLER\_ROTATION\_ANGLE | \-1,155,243 | "Coupler Rotation" |
| COUPLER\_WEIGHT | \-1,154,643 | "Mass" |
| COUPLER\_WIDTH | \-1,154,651 | "External Diameter" |
| COVER\_TYPE\_LENGTH | \-1,013,434 | "Length" |
| COVER\_TYPE\_NAME | \-1,013,433 | "Name" |
| CREATE\_CHAIN | \-1,123,518 | "Chain" |
| CURTAIN\_GRID\_BASE\_ORIENTATION | \-1,007,364 | "Grid Base Orientation" |
| CURTAIN\_VERSION\_PARAM | \-1,013,367 | "Curtain version" |
| CURTAIN\_WALL\_PANEL\_HOST\_ID | \-1,010,303 | "Host Id" |
| CURTAIN\_WALL\_PANELS\_CONSTRUCTION\_TYPE | \-1,001,207 | "Construction Type" |
| CURTAIN\_WALL\_PANELS\_FINISH | \-1,001,208 | "Finish" |
| CURTAIN\_WALL\_PANELS\_HEIGHT | \-1,010,300 | "Height" |
| CURTAIN\_WALL\_PANELS\_WIDTH | \-1,010,301 | "Width" |
| CURTAIN\_WALL\_SYSPANEL\_OFFSET | \-1,010,302 | "Offset" |
| CURTAIN\_WALL\_SYSPANEL\_THICKNESS | \-1,010,304 | "Thickness" |
| CURTAINGRID\_ADJUST\_BORDER\_1 | \-1,013,346 | "Adjust for Mullion Size" |
| CURTAINGRID\_ADJUST\_BORDER\_2 | \-1,013,347 | "Adjust for Mullion Size" |
| CURTAINGRID\_ADJUST\_BORDER\_HORIZ | \-1,013,317 | "Adjust for Mullion Size" |
| CURTAINGRID\_ADJUST\_BORDER\_U | \-1,013,386 | "Adjust for Mullion Size" |
| CURTAINGRID\_ADJUST\_BORDER\_V | \-1,013,387 | "Adjust for Mullion Size" |
| CURTAINGRID\_ADJUST\_BORDER\_VERT | \-1,013,316 | "Adjust for Mullion Size" |
| CURTAINGRID\_ANGLE\_1 | \-1,013,339 | "Angle" |
| CURTAINGRID\_ANGLE\_2 | \-1,013,340 | "Angle" |
| CURTAINGRID\_ANGLE\_HORIZ | \-1,013,310 | "Angle" |
| CURTAINGRID\_ANGLE\_U | \-1,013,379 | "Grid Rotation" |
| CURTAINGRID\_ANGLE\_V | \-1,013,380 | "Grid Rotation" |
| CURTAINGRID\_ANGLE\_VERT | \-1,013,309 | "Angle" |
| CURTAINGRID\_BELT\_1 | \-1,013,344 | "Measurement Line" |
| CURTAINGRID\_BELT\_2 | \-1,013,345 | "Measurement Line" |
| CURTAINGRID\_BELT\_HORIZ | \-1,013,315 | "Measurement Line" |
| CURTAINGRID\_BELT\_RATIO\_1 | \-1,013,368 | "Measurement Line" |
| CURTAINGRID\_BELT\_RATIO\_2 | \-1,013,369 | "Measurement Line" |
| CURTAINGRID\_BELT\_RATIO\_U | \-1,013,390 | "Belt Measurement" |
| CURTAINGRID\_BELT\_RATIO\_V | \-1,013,391 | "Belt Measurement" |
| CURTAINGRID\_BELT\_U | \-1,013,384 | "Belt Measurement" |
| CURTAINGRID\_BELT\_V | \-1,013,385 | "Belt Measurement" |
| CURTAINGRID\_BELT\_VERT | \-1,013,314 | "Measurement Line" |
| CURTAINGRID\_ORIGIN\_1 | \-1,013,342 | "Offset" |
| CURTAINGRID\_ORIGIN\_2 | \-1,013,343 | "Offset" |
| CURTAINGRID\_ORIGIN\_HORIZ | \-1,013,313 | "Offset" |
| CURTAINGRID\_ORIGIN\_U | \-1,013,382 | "Offset" |
| CURTAINGRID\_ORIGIN\_V | \-1,013,383 | "Offset" |
| CURTAINGRID\_ORIGIN\_VERT | \-1,013,312 | "Offset" |
| CURTAINGRID\_USE\_CURVE\_DIST | \-1,013,354 | "Use Curve Distance" |
| CURTAINGRID\_USE\_CURVE\_DIST\_1 | \-1,013,348 | "Use Curve Distance" |
| CURTAINGRID\_USE\_CURVE\_DIST\_2 | \-1,013,349 | "Use Curve Distance" |
| CURTAINGRID\_USE\_CURVE\_DIST\_HORIZ | \-1,013,319 | "Use Curve Distance" |
| CURTAINGRID\_USE\_CURVE\_DIST\_U | \-1,013,388 | "Use Curve Distance" |
| CURTAINGRID\_USE\_CURVE\_DIST\_V | \-1,013,389 | "Use Curve Distance" |
| CURTAINGRID\_USE\_CURVE\_DIST\_VERT | \-1,013,318 | "Use Curve Distance" |
| CURVE\_BASE\_LEVEL | \-1,007,907 | "Bottom Level" |
| CURVE\_BOTTOM\_LEVEL | \-1,007,907 | "Bottom Level" |
| CURVE\_BY\_POINTS\_PROJECTION\_TYPE | \-1,150,212 | "Projection Type" |
| CURVE\_DETERMINES\_ORIENTATION | \-1,004,013 | "Determines Orientation" |
| CURVE\_EDGE\_OFFSET | \-1,013,429 | "Wall offset" |
| CURVE\_ELEM\_ARC\_END\_ANGLE | \-1,004,008 | "Angle 2" |
| CURVE\_ELEM\_ARC\_RADIUS | \-1,004,010 | "Radius" |
| CURVE\_ELEM\_ARC\_RANGE | \-1,004,009 | "Range" |
| CURVE\_ELEM\_ARC\_START\_ANGLE | \-1,004,007 | "Angle 1" |
| CURVE\_ELEM\_DEFINES\_SLOPE | \-1,004,015 | "Defines Beam System Slope" |
| CURVE\_ELEM\_LENGTH | \-1,004,005 | "Length" |
| CURVE\_ELEM\_LINE\_ANGLE | \-1,004,006 | "Angle" |
| CURVE\_HEIGHT\_OFFSET | \-1,006,008 | "Offset From Base" |
| CURVE\_IS\_DETAIL | \-1,004,011 | "Detail Line" |
| CURVE\_IS\_FILLED | \-1,006,310 | "Filled" |
| CURVE\_IS\_MULTILEVEL | \-1,007,908 | "Multilevel Boundary" |
| CURVE\_IS\_REFERENCE\_LINE | \-1,150,147 | "Is Reference Line" |
| CURVE\_IS\_SLOPE\_DEFINING | \-1,006,007 | "Defines Slope" |
| CURVE\_LEVEL | \-1,006,009 | "Level" |
| CURVE\_NUMBER\_OF\_SEGMENTS | \-1,006,013 | "Number of Full Segments" |
| CURVE\_PARAM\_CONCRETE\_CANTILEVER | \-1,006,014 | "Concrete Cantilever" |
| CURVE\_PARAM\_STEEL\_CANTILEVER | \-1,006,015 | "Steel Cantilever" |
| CURVE\_SUPPORT\_OFFSET | \-1,013,412 | "Wall offset" |
| CURVE\_TOP\_LEVEL | \-1,007,906 | "Top Level" |
| CURVE\_VISIBILITY\_PARAM | \-1,001,809 | "Visibility/Graphics Overrides" |
| CURVE\_WALL\_OFFSET | \-1,001,706 | "Wall offset" |
| CURVE\_WALL\_OFFSET\_ROOFS | \-1,001,707 | "Overhang" |
| CUST\_MULLION\_THICK | \-1,007,322 | "Thickness" |
| CUST\_MULLION\_WIDTH1 | \-1,007,320 | "Width on side 1" |
| CUST\_MULLION\_WIDTH2 | \-1,007,321 | "Width on side 2" |
| CUT\_LINE\_ANGLE | \-1,006,619 | "Cut Line Angle" |
| CUT\_LINE\_DISTANCE | \-1,006,617 | "Cut Line Distance" |
| CUT\_LINE\_EXTENSION | \-1,006,618 | "Cut Line Extension" |
| CUT\_LINE\_TYPE | \-1,006,620 | "Cut Line Type" |
| CUT\_MARK\_SYMBOL | \-1,006,616 | "Cut Mark Symbol" |
| CUT\_MARK\_SYMBOL\_SIZE | \-1,006,621 | "Cut Mark Symbol Size" |
| CWP\_ADD\_GRID\_PREFIX | \-1,016,002 | "Add prefix to Grid Name" |
| CWP\_ADD\_GRID\_SUFFIX | \-1,016,003 | "Add suffix to Grid Name" |
| CWP\_ADD\_LEVEL\_PREFIX | \-1,016,004 | "Add prefix to Level Name" |
| CWP\_ADD\_LEVEL\_SUFFIX | \-1,016,005 | "Add suffix to Level Name" |
| CWP\_COPY\_FLOOR\_INSERTS | \-1,016,018 | "Copy openings/inserts" |
| CWP\_COPY\_ROOF\_INSERTS | \-1,016,019 | "Copy openings" |
| CWP\_COPY\_WALL\_INSERTS | \-1,016,017 | "Copy windows/doors/openings" |
| CWP\_LEVEL\_OFFSET | \-1,016,006 | "Offset Level" |
| CWP\_LINKED\_ROOM\_PARAMS | \-1,016,016 | "Parameters" |
| CWP\_LINKED\_ROOM\_PHASES | \-1,016,015 | "Phases" |
| CWP\_REUSE\_EXISTING\_GRIDS | \-1,016,008 | "Reuse matching Grids" |
| CWP\_REUSE\_EXISTING\_LEVELS | \-1,016,007 | "Reuse matching Levels" |
| CWP\_REUSE\_GRIDS\_SAME\_NAME | \-1,016,011 | "Reuse Grids with the same name" |
| CWP\_REUSE\_LEVELS\_SAME\_NAME | \-1,016,010 | "Reuse Levels with the same name" |
| CWP\_SPLIT\_COLUMNS\_AT\_LEVELS | \-1,016,009 | "Split Columns by Levels" |
| DATUM\_BUBBLE\_END\_1 | \-1,008,002 | "Symbol at End 1 Default" |
| DATUM\_BUBBLE\_END\_2 | \-1,008,001 | "Symbol at End 2 Default" |
| DATUM\_BUBBLE\_LOCATION\_IN\_ELEV | \-1,008,003 | "Non\-Plan View Symbols (Default)" |
| DATUM\_PLANE\_DEFINES\_ORIGIN | \-1,004,002 | "Defines Origin" |
| DATUM\_PLANE\_DEFINES\_WALL\_CLOSURE | \-1,004,012 | "Wall Closure" |
| DATUM\_TEXT | \-1,008,000 | "Name" |
| DATUM\_VOLUME\_OF\_INTEREST | \-1,012,201 | "Scope Box" |
| DECAL\_ATTRIBUTES | \-1,012,812 | "Decal Attributes" |
| DECAL\_HEIGHT | \-1,012,815 | "Height" |
| DECAL\_LOCK\_PROPORTIONS | \-1,012,813 | "Lock Proportions" |
| DECAL\_SUBCATEGORY\_ID | \-1,012,818 | "Subcategory" |
| DECAL\_WIDTH | \-1,012,814 | "Width" |
| DEFAULT\_CONSTRUCTION\_EXT\_WALL\_UNDERGROUND | \-1,150,305 | "Mass Exterior Wall \- Underground" |
| DEFAULT\_CONSTRUCTION\_MASS\_EXTERIOR\_WALL | \-1,150,300 | "Mass Exterior Wall" |
| DEFAULT\_CONSTRUCTION\_MASS\_FLOOR | \-1,150,310 | "Mass Floor" |
| DEFAULT\_CONSTRUCTION\_MASS\_GLAZING | \-1,150,306 | "Mass Glazing" |
| DEFAULT\_CONSTRUCTION\_MASS\_INTERIOR\_WALL | \-1,150,301 | "Mass Interior Wall" |
| DEFAULT\_CONSTRUCTION\_MASS\_OPENING | \-1,150,309 | "Mass Opening" |
| DEFAULT\_CONSTRUCTION\_MASS\_ROOF | \-1,150,302 | "Mass Roof" |
| DEFAULT\_CONSTRUCTION\_MASS\_SHADE | \-1,150,303 | "Mass Shade" |
| DEFAULT\_CONSTRUCTION\_MASS\_SKYLIGHT | \-1,150,307 | "Mass Skylight" |
| DEFAULT\_CONSTRUCTION\_MASS\_SLAB | \-1,150,304 | "Mass Slab" |
| DEFAULT\_VIEW\_TEMPLATE | \-1,008,210 | "View Template applied to new views" |
| DEFINES\_CONSTANT\_HEIGHT | \-1,006,006 | "Defines Constant Height" |
| DESIGN\_OPTION\_ID | \-1,013,201 | "Design Option" |
| DESIGN\_OPTION\_PARAM | \-1,013,200 | "Design Option" |
| DIAMETER\_SYMBOL\_LOCATION | \-1,006,998 | "Diameter Symbol Location" |
| DIAMETER\_SYMBOL\_TEXT | \-1,006,999 | "Diameter Symbol Text" |
| DIM\_DISPLAY\_EQ | \-1,004,514 | "Equality Display" |
| DIM\_ISREPORTING | \-1,004,516 | "Is Reporting" |
| DIM\_LABEL | \-1,004,510 | "Label" |
| DIM\_LABEL\_GP\_SHOW | \-1,004,502 | "Show Label in View" |
| DIM\_LABEL\_IS\_INSTANCE | \-1,004,518 | "Is Instance Parameter" |
| DIM\_LABEL\_IS\_TYPE | \-1,004,519 | "Is Type Parameter" |
| DIM\_LEADER | \-1,004,515 | "Leader" |
| DIM\_LEADER\_ARROWHEAD | \-1,006,323 | "Tick Mark" |
| DIM\_LEADER\_DISPLAY\_CONDITION | \-1,006,510 | "Show Leader When Text Moves" |
| DIM\_LEADER\_SHOULDER\_LENGTH | \-1,006,509 | "Shoulder Length" |
| DIM\_LEADER\_TYPE | \-1,006,508 | "Leader Type" |
| DIM\_LINE\_EXTENSION | \-1,006,431 | "Dimension Line Extension" |
| DIM\_NOT\_MODIFIABLE | \-1,004,513 | "Non\-modifiable" |
| DIM\_PREFIX | \-1,006,525 | "Dimension Prefix" |
| DIM\_REFERENCE\_COUNT | \-1,006,520 | "Count" |
| DIM\_STYLE\_ANGULAR\_UNITS | \-1,006,428 | "Units Format" |
| DIM\_STYLE\_ANGULAR\_UNITS\_ALT | \-1,006,460 | "Alternate Units Format" |
| DIM\_STYLE\_CENTERLINE\_PATTERN | \-1,006,434 | "Centerline Pattern" |
| DIM\_STYLE\_CENTERLINE\_SYMBOL | \-1,006,430 | "Centerline Symbol" |
| DIM\_STYLE\_CENTERLINE\_TICK\_MARK | \-1,006,445 | "Centerline Tick Mark" |
| DIM\_STYLE\_DIM\_LINE\_SNAP\_DIST | \-1,006,446 | "Dimension Line Snap Distance" |
| DIM\_STYLE\_FLIPPED\_DIM\_LINE\_EXTENSION | \-1,006,465 | "Flipped Dimension Line Extension" |
| DIM\_STYLE\_INTERIOR\_TICK\_MARK | \-1,006,464 | "Interior Tick Mark" |
| DIM\_STYLE\_LEADER\_TICK\_MARK | \-1,006,514 | "Leader Tick Mark" |
| DIM\_STYLE\_LINEAR\_UNITS | \-1,006,427 | "Units Format" |
| DIM\_STYLE\_LINEAR\_UNITS\_ALT | \-1,006,454 | "Alternate Units Format" |
| DIM\_STYLE\_READ\_CONVENTION | \-1,006,448 | "Read Convention" |
| DIM\_STYLE\_SHOW\_OPENING\_HT | \-1,006,435 | "Show Opening Height" |
| DIM\_STYLE\_SUPPRESS\_SPACES | \-1,006,516 | "Suppress Spaces" |
| DIM\_SUFFIX | \-1,006,526 | "Dimension Suffix" |
| DIM\_TEXT\_BACKGROUND | \-1,006,429 | "Text Background" |
| DIM\_TEXT\_LOCATION\_FOR\_LEADER | \-1,006,511 | "Text Location" |
| DIM\_TO\_INSERT\_TYPE | \-1,006,505 | "Dimension To Opening Type" |
| DIM\_TO\_INSERTS | \-1,006,500 | "Dimension To Openings" |
| DIM\_TO\_INTERSECTING\_GRIDS | \-1,006,507 | "Dimension To Intersecting Grids" |
| DIM\_TO\_INTERSECTING\_WALLS | \-1,006,506 | "Dimension To Intersecting Walls" |
| DIM\_TOTAL\_LENGTH | \-1,006,521 | "Total Length" |
| DIM\_VALUE\_ANGLE | \-1,004,501 | "Value" |
| DIM\_VALUE\_LENGTH | \-1,004,500 | "Value" |
| DIM\_WITNS\_LINE\_CNTRL | \-1,006,432 | "Witness Line Control" |
| DIM\_WITNS\_LINE\_EXTENSION\_BELOW | \-1,006,433 | "Witness Line Length" |
| DIRECTCONTEXT3D\_APPLICATION\_ID | \-1,154,685 | "ApplicationId" |
| DIRECTCONTEXT3D\_LOADED | \-1,154,677 | "Loaded" |
| DIRECTCONTEXT3D\_NAME | \-1,154,675 | "Name" |
| DIRECTCONTEXT3D\_SERVER\_ID | \-1,154,676 | "ServerId" |
| DIRECTCONTEXT3D\_SOURCE\_ID | \-1,154,686 | "Path" |
| DISPLACED\_ELEMENT\_DISPLACEMENT\_X | \-1,141,004 | "X Displacement" |
| DISPLACED\_ELEMENT\_DISPLACEMENT\_Y | \-1,141,005 | "Y Displacement" |
| DISPLACED\_ELEMENT\_DISPLACEMENT\_Z | \-1,141,006 | "Z Displacement" |
| DISPLACEMENT\_PATH\_DEPTH | \-1,141,002 | "Depth" |
| DISPLACEMENT\_PATH\_STYLE | \-1,141,003 | "Style" |
| DISTANCE\_TO\_CUT\_MARK | \-1,006,625 | "Distance to Cut Mark" |
| DIVIDED\_SURFACE\_ALL\_GRID\_ROTATION | \-1,150,068 | "All Grid Rotation" |
| DIVIDED\_SURFACE\_ALL\_POINTS | \-1,150,062 | "Show all points" |
| DIVIDED\_SURFACE\_COMPONENT\_TRIM\_TYPE | \-1,150,083 | "Component Trim" |
| DIVIDED\_SURFACE\_COVER\_FACE\_COMPLETELY | \-1,150,056 | "Cover face completely" |
| DIVIDED\_SURFACE\_DISPLAY\_COMPONENTS | \-1,150,079 | "Components" |
| DIVIDED\_SURFACE\_DISPLAY\_DISCARDEDDIVISIONLINES | \-1,150,084 | "Discarded Division Lines" |
| DIVIDED\_SURFACE\_DISPLAY\_GRIDLINES | \-1,150,073 | "Gridlines" |
| DIVIDED\_SURFACE\_DISPLAY\_NODES | \-1,150,072 | "Nodes" |
| DIVIDED\_SURFACE\_DISPLAY\_ORIGINAL\_SURFACE | \-1,150,070 | "Surface" |
| DIVIDED\_SURFACE\_DISPLAY\_PATTERN\_FILL | \-1,150,077 | "Pattern Fill" |
| DIVIDED\_SURFACE\_DISPLAY\_PATTERN\_LINES | \-1,150,075 | "Pattern Lines" |
| DIVIDED\_SURFACE\_DISPLAY\_SURFACE\_OPTION | \-1,150,069 | "Display Surface Option" |
| DIVIDED\_SURFACE\_EDGE\_NUMBER | \-1,150,053 | "Edge number" |
| DIVIDED\_SURFACE\_FACET\_NUMBER | \-1,150,051 | "Facet number" |
| DIVIDED\_SURFACE\_GRID\_OPTION\_PARAM\_1 | \-1,150,085 | "Option 1" |
| DIVIDED\_SURFACE\_GRID\_OPTION\_PARAM\_2 | \-1,150,086 | "Option 2" |
| DIVIDED\_SURFACE\_GRIDLINES\_STYLE | \-1,150,074 | "Gridlines Style" |
| DIVIDED\_SURFACE\_OFFSET\_FROM\_SURFACE | \-1,150,055 | "Offset from surface" |
| DIVIDED\_SURFACE\_ORIGINAL\_SURFACE\_MATERIAL | \-1,150,071 | "Surface Material" |
| DIVIDED\_SURFACE\_PATTERN | \-1,150,061 | "Tile Pattern" |
| DIVIDED\_SURFACE\_PATTERN\_FILL\_MATERIAL | \-1,150,078 | "Pattern Fill Material" |
| DIVIDED\_SURFACE\_PATTERN\_FLIP | \-1,150,060 | "Component Flip" |
| DIVIDED\_SURFACE\_PATTERN\_INDENT\_1 | \-1,150,057 | "Indent 1" |
| DIVIDED\_SURFACE\_PATTERN\_INDENT\_2 | \-1,150,058 | "Indent 2" |
| DIVIDED\_SURFACE\_PATTERN\_LINES\_STYLE | \-1,150,076 | "Pattern Lines Style" |
| DIVIDED\_SURFACE\_PATTERN\_MIRROR | \-1,150,082 | "Component Mirror" |
| DIVIDED\_SURFACE\_PATTERN\_ROTATION\_ANGLE | \-1,150,059 | "Component Rotation" |
| DIVIDED\_SURFACE\_POINT\_NUMBER | \-1,150,052 | "Point number" |
| DIVIDED\_SURFACE\_RULE\_1\_SUSPENSION | \-1,150,080 | "Is grid 1 suspended?" |
| DIVIDED\_SURFACE\_RULE\_2\_SUSPENSION | \-1,150,081 | "Is grid 2 suspended?" |
| DIVIDED\_SURFACE\_SURFACE\_AREA | \-1,150,050 | "Divided Surface Area" |
| DIVIDED\_SURFACE\_TILE\_BORDER | \-1,150,067 | "Border Tile" |
| DIVIDED\_SURFACE\_TOTAL\_EDGE\_LENGTH | \-1,150,054 | "Total edge length" |
| DIVIDEDPATH\_BEGINNING\_INDENT | \-1,050,428 | "Beginning Indent" |
| DIVIDEDPATH\_DISPLAY\_NODE\_NUMBERS | \-1,050,440 | "Show Node Numbers" |
| DIVIDEDPATH\_DISPLAY\_NODES | \-1,050,437 | "Display Nodes" |
| DIVIDEDPATH\_DISPLAY\_REFERENCE\_CURVES | \-1,050,436 | "Display Path" |
| DIVIDEDPATH\_DISTANCE | \-1,050,427 | "Distance" |
| DIVIDEDPATH\_END\_INDENT | \-1,050,429 | "End Indent" |
| DIVIDEDPATH\_FLIP\_DIRECTION | \-1,050,433 | "Flip Direction" |
| DIVIDEDPATH\_JUSTIFICATION | \-1,050,435 | "Justification" |
| DIVIDEDPATH\_LAYOUT | \-1,050,426 | "Layout" |
| DIVIDEDPATH\_LAYOUT\_FIXED\_NUM\_POINT | \-1,050,434 | "Number" |
| DIVIDEDPATH\_MAX\_DISTANCE | \-1,050,431 | "Maximum Distance" |
| DIVIDEDPATH\_MEASUREMENT\_TYPE | \-1,050,432 | "Measurement Type" |
| DIVIDEDPATH\_MERGED\_POINT\_NUM | \-1,050,439 | "Total Number of Nodes" |
| DIVIDEDPATH\_MIN\_DISTANCE | \-1,050,430 | "Minimum Distance" |
| DIVIDEDPATH\_TOTAL\_PATH\_LENGTH | \-1,050,441 | "Path Length" |
| DIVISION\_PATTERN | \-1,152,346 | "Division Pattern" |
| DIVISION\_PROFILE\_WIDTH | \-1,150,623 | "Width": Width |
| DIVISION\_RULE\_PARAM | \-1,152,351 | "Division Rule" |
| DIVISION\_SKETCH\_CURVE\_DIVISION\_PARAMS\_OVERRIDE\_PARAM | \-1,152,356 | "Profile Override" |
| DIVISION\_SKETCH\_CURVE\_EXTENTD\_TO\_SILH\_PARAM | \-1,152,352 | "Extend to Silhouette" |
| DOOR\_CONSTRUCTION\_TYPE | \-1,001,207 | "Construction Type" |
| DOOR\_COST | \-1,001,205 | "Cost" |
| DOOR\_EVACUATION\_EXIT\_TYPE | \-1,001,212 | "Exit Access" |
| DOOR\_FINISH | \-1,001,208 | "Finish" |
| DOOR\_FIRE\_RATING | \-1,001,206 | "Fire Rating" |
| DOOR\_FRAME\_MATERIAL | \-1,001,210 | "Frame Material" |
| DOOR\_FRAME\_TYPE | \-1,001,209 | "Frame Type" |
| DOOR\_HEIGHT | \-1,001,300 | "Height" |
| DOOR\_NUMBER | \-1,001,203 | "Mark" |
| DOOR\_OPERATION\_TYPE | \-1,001,211 | "Operation" |
| DOOR\_THICKNESS | \-1,001,302 | "Thickness" |
| DOOR\_WIDTH | \-1,001,301 | "Width" |
| DPART\_AREA\_COMPUTED | \-1,001,133 | "Area" |
| DPART\_BASE\_LEVEL | \-1,152,335 | "Base Level" |
| DPART\_BASE\_LEVEL\_BY\_ORIGINAL | \-1,152,336 | "Base Level By Original" |
| DPART\_CAN\_HOST\_REBAR | \-1,017,056 | "Can host rebar" |
| DPART\_EXCLUDED | \-1,152,344 | "Excluded" |
| DPART\_HEIGHT\_COMPUTED | \-1,001,135 | "Height" |
| DPART\_LAYER\_CONSTRUCTION | \-1,001,139 | "Construction" |
| DPART\_LAYER\_FUNCTION | \-1,001,130 | "Layer Function" |
| DPART\_LAYER\_INDEX | \-1,155,219 | "Layer Index" |
| DPART\_LAYER\_WIDTH | \-1,001,134 | "Thickness" |
| DPART\_LENGTH\_COMPUTED | \-1,001,136 | "Length" |
| DPART\_MATERIAL\_BY\_ORIGINAL | \-1,001,128 | "Material By Original" |
| DPART\_MATERIAL\_ID\_PARAM | \-1,001,127 | "Material" |
| DPART\_ORIGINAL\_CATEGORY | \-1,001,125 | "Original Category" |
| DPART\_ORIGINAL\_CATEGORY\_ID | \-1,001,140 | "Original Category" |
| DPART\_ORIGINAL\_FAMILY | \-1,001,126 | "Original Family" |
| DPART\_ORIGINAL\_TYPE | \-1,001,132 | "Original Type" |
| DPART\_PHASE\_CREATED\_BY\_ORIGINAL | \-1,001,137 | "Phase Created By Original" |
| DPART\_PHASE\_DEMOLISHED\_BY\_ORIGINAL | \-1,001,138 | "Phase Demolished By Original" |
| DPART\_SHAPE\_MODIFIED | \-1,152,345 | "Shape is modified" |
| DPART\_VOLUME\_COMPUTED | \-1,001,129 | "Volume" |
| DRAW\_FOR\_EACH\_RUN | \-1,006,628 | "Draw for Each Run" |
| DUCT\_INSULATION\_THICKNESS | \-1,150,436 | "Insulation Thickness" |
| DUCT\_ROUGHNESS | \-1,114,114 | "Roughness" |
| DUCT\_TERMINAL\_ENGAGEMENT\_LENGTH | \-1,133,417 | "Engagement Length" |
| EDGE\_LINEWORK | \-1,006,212 | "Line Style" |
| EDITED\_BY | \-1,002,067 | "Edited by" |
| ELECTICAL\_EQUIP\_VOLTAGE | \-1,010,401 | "Voltage Comments" |
| ELECTICAL\_EQUIP\_WATTAGE | \-1,010,400 | "Wattage Comments" |
| ELEM\_CATEGORY\_PARAM | \-1,140,362 | "Category" |
| ELEM\_CATEGORY\_PARAM\_MT | \-1,140,363 | "Category" |
| ELEM\_DELETABLE\_IN\_FAMILY | \-1,004,004 | "Deletable" |
| ELEM\_FAMILY\_AND\_TYPE\_PARAM | \-1,002,052 | "Family and Type" |
| ELEM\_FAMILY\_PARAM | \-1,002,051 | "Family" |
| ELEM\_IS\_REFERENCE | \-1,004,001 | "Reference" |
| ELEM\_PARTITION\_PARAM | \-1,002,053 | "Workset" |
| ELEM\_REFERENCE\_NAME | \-1,004,003 | "Is Reference" |
| ELEM\_REFERENCE\_NAME\_2D\_XZ | \-1,004,016 | "Is Reference" |
| ELEM\_ROOM\_ID | \-1,002,061 | "Room Id" |
| ELEM\_ROOM\_NAME | \-1,002,060 | "Room Name" |
| ELEM\_ROOM\_NUMBER | \-1,002,059 | "Room Number" |
| ELEM\_TYPE\_LABEL | \-1,002,008 | "Label" |
| ELEM\_TYPE\_PARAM | \-1,002,050 | "Type" |
| ELEMENT\_IS\_CUTTING | \-1,001,807 | "Solid/Void" |
| ELEMENT\_LOCKED\_PARAM | \-1,009,000 | "Locked" |
| ELEV\_ARROW\_ANGLE | \-1,007,602 | "Arrow Angle" |
| ELEV\_ARROW\_FILLED | \-1,007,603 | "Filled" |
| ELEV\_ASSOC\_DATUM | \-1,007,608 | "Associated Datum" |
| ELEV\_REFERENCE\_LABEL\_POS | \-1,007,609 | "Reference Label Position" |
| ELEV\_SHAPE | \-1,007,601 | "Shape" |
| ELEV\_SHOW\_VIEW\_NAME | \-1,007,605 | "Show View Name" |
| ELEV\_SYMBOL\_ID | \-1,007,610 | "Elevation Mark" |
| ELEV\_TEXT\_POS | \-1,007,604 | "Text Position" |
| ELEV\_VIEW\_NAME\_POS | \-1,007,607 | "View Name Position" |
| ELEV\_WIDTH | \-1,007,600 | "Width" |
| ELEVATN\_TAG | \-1,008,207 | "Elevation Tag" |
| ELLIPSE\_FOCUS\_MRK\_VISIBLE | \-1,007,905 | "Focus Marks Visible" |
| ELLIPSE\_MODIFICATION\_KEEPS\_RATIO | \-1,612,354 | "Keep Ratio" |
| ELLIPSE\_X\_PARAM | \-1,010,020 | "X\-Radius Value for Ellipse (for Use with XAML Data Template example)" |
| ELLIPSE\_Y\_PARAM | \-1,010,021 | "Y\-Radius Value for Ellipse (for Use with XAML Data Template example)" |
| END\_EXTENSION | \-1,152,358 | "End Extension" |
| END\_JOIN\_CUTBACK | \-1,152,360 | "End Join Cutback" |
| END\_TREATMENT | \-1,154,654 | "End Treatment" |
| END\_Y\_JUSTIFICATION | \-1,152,370 | "End y Justification" |
| END\_Y\_OFFSET\_VALUE | \-1,152,371 | "End y Offset Value" |
| END\_Z\_JUSTIFICATION | \-1,152,372 | "End z Justification" |
| END\_Z\_OFFSET\_VALUE | \-1,152,373 | "End z Offset Value" |
| ENERGY\_ANALYSIS\_ADVANCED\_OPTIONS | \-1,152,379 | "Other Options" |
| ENERGY\_ANALYSIS\_BUILDING\_OPERATING\_SCHEDULE | \-1,012,047 | "Building Operating Schedule" |
| ENERGY\_ANALYSIS\_CONCEPTUAL\_CONSTRUCTION | \-1,012,056 | "Conceptual Types" |
| ENERGY\_ANALYSIS\_CONSTRUCTION\_JSON | \-1,114,861 | "JSON data for Analytical Constructions" |
| ENERGY\_ANALYSIS\_CREATE\_ANALYTICAL\_MODEL | \-1,012,046 | "Create Energy Model" |
| ENERGY\_ANALYSIS\_CURRENT\_VIEW\_ONLY | \-1,017,750 | "Use Only Elements Visible In Current View" |
| ENERGY\_ANALYSIS\_GLAZING\_IS\_SHADED | \-1,012,053 | "Glazing is Shaded" |
| ENERGY\_ANALYSIS\_HORIZONTAL\_VOID\_THRESHOLD | \-1,150,235 | "Horizontal Void/Chase Area Threshold" |
| ENERGY\_ANALYSIS\_HVAC\_SYSTEM | \-1,012,062 | "HVAC System" |
| ENERGY\_ANALYSIS\_MASS\_ZONING | \-1,012,050 | "Mass Zoning" |
| ENERGY\_ANALYSIS\_MASSZONE\_COREOFFSET | \-1,012,058 | "Perimeter Zone Depth" |
| ENERGY\_ANALYSIS\_MASSZONE\_DIVIDEPERIMETER | \-1,012,059 | "Perimeter Zone Division" |
| ENERGY\_ANALYSIS\_MASSZONE\_USEENERGYDATASETTINGS | \-1,012,060 | "Use Energy Data" |
| ENERGY\_ANALYSIS\_OUTDOOR\_AIR\_INFORMATION\_PARAM | \-1,012,061 | "Outdoor Air Information" |
| ENERGY\_ANALYSIS\_PERCENTAGE\_GLAZING | \-1,012,051 | "Target Percentage Glazing" |
| ENERGY\_ANALYSIS\_PERCENTAGE\_SKYLIGHTS | \-1,012,054 | "Target Percentage Skylights" |
| ENERGY\_ANALYSIS\_PROJECT\_PHASE | \-1,114,822 | "Phase" |
| ENERGY\_ANALYSIS\_SHADE\_DEPTH | \-1,012,057 | "Shade Depth" |
| ENERGY\_ANALYSIS\_SILL\_HEIGHT | \-1,012,052 | "Target Sill Height" |
| ENERGY\_ANALYSIS\_SKYLIGHT\_WIDTH | \-1,012,055 | "Skylight Width \& Depth" |
| ENERGY\_ANALYSIS\_SPACE\_BOUNDING\_PARAM | \-1,150,236 | "Analytical Space Bounding" |
| ENERGY\_ANALYSIS\_SPACE\_JSON | \-1,114,860 | "JSON data for Analytical Spaces" |
| ENERGY\_ANALYSIS\_VERTICAL\_VOID\_THRESHOLD | \-1,150,234 | "Average Vertical Void Height Threshold" |
| ENERGY\_ANALYSIS\_WINDOW\_TYPE\_JSON | \-1,114,862 | "JSON data for Window Types" |
| ENERGY\_ANALYSIS\_ZONE\_DATA\_JSON | \-1,114,863 | "Energy analysis zone data json" |
| EQUALITY\_FORMULA | \-1,006,515 | "Equality Formula" |
| EQUALITY\_TEXT\_FOR\_ANGULAR\_DIM | \-1,006,513 | "Equality Text" |
| EQUALITY\_TEXT\_FOR\_CONTINUOUS\_LINEAR\_DIM | \-1,006,512 | "Equality Text" |
| EQUALITY\_WITNESS\_DISPLAY | \-1,006,517 | "Equality Witness Display" |
| EXCAVATION\_ELEMENT\_FAMILY\_AND\_TYPE | \-1,180,305 | "Element Family and Type" |
| EXCAVATION\_ELEMENT\_ID | \-1,180,304 | "Element Id" |
| EXCAVATION\_VOLUME | \-1,180,306 | "Excavation Volume" |
| EXCAVATION\_VOLUME\_ON\_TOPOSOLID | \-1,180,308 | "Excavation Volume on Toposolid" |
| EXCHANGE\_ENTITY\_ID | \-1,155,401 | "Exchange Entity ID" |
| EXCHANGE\_ID | \-1,155,400 | "Exchange ID" |
| EXTRUSION\_AUTO\_PARAMS | \-1,001,806 | "Auto ends" |
| EXTRUSION\_DEPTH\_PARAM | \-1,001,799 | "Depth" |
| EXTRUSION\_END\_PARAM | \-1,001,801 | "Extrusion End" |
| EXTRUSION\_LENGTH | \-1,001,812 | "Depth" |
| EXTRUSION\_START\_PARAM | \-1,001,800 | "Extrusion Start" |
| FABRIC\_BEND\_DIAMETER | \-1,017,625 | "Bend Diameter": Standard Bend Diameter of Fabric Wire. |
| FABRIC\_NUMBER | \-1,154,617 | "Fabric Number" |
| FABRIC\_PARAM\_COVER\_OFFSET | \-1,017,708 | "Additional Cover Offset": Additional cover offset of the fabric distribution. |
| FABRIC\_PARAM\_CUT\_BY\_HOST | \-1,017,732 | "Cut by Host Cover": Single Fabric Sheet is cut or not cut by the Host Cover. |
| FABRIC\_PARAM\_CUT\_OVERALL\_LENGTH | \-1,017,709 | "Cut Overall Length": Provides a real sheet Length after definition |
| FABRIC\_PARAM\_CUT\_OVERALL\_WIDTH | \-1,017,710 | "Cut Overall Width": Provides a real sheet Width after definition |
| FABRIC\_PARAM\_CUT\_SHEET\_MASS | \-1,017,712 | "Cut Sheet Mass": Calculated cut sheet mass \[Sheet Mass per Unit Area \* (Cut Overall Length \* Cut Overall Width)] |
| FABRIC\_PARAM\_LAPSPLICE\_POSITION | \-1,017,704 | "Lap Splice Position": Fabric lap splice position in the fabric distribution |
| FABRIC\_PARAM\_LOCATION\_GENERIC | \-1,017,705 | "Location": Fabric location in the host. |
| FABRIC\_PARAM\_LOCATION\_SLAB | \-1,017,702 | "Location": Fabric location in the slab |
| FABRIC\_PARAM\_LOCATION\_WALL | \-1,017,703 | "Location": Fabric location in the wall |
| FABRIC\_PARAM\_MAJOR\_LAPSPLICE\_LENGTH | \-1,017,706 | "Major Lap Splice Length": Fabric lap splice length in major direction in the fabric distribution. |
| FABRIC\_PARAM\_MINOR\_LAPSPLICE\_LENGTH | \-1,017,707 | "Minor Lap Splice Length": Fabric lap splice length in minor direction in the fabric distribution. |
| FABRIC\_PARAM\_ROUNDING | \-1,017,028 | "Rounding Overrides" |
| FABRIC\_PARAM\_SHARED\_FAMILY\_KEY | \-1,017,733 | "Shared family key" |
| FABRIC\_PARAM\_SHEET\_TYPE | \-1,017,701 | "Fabric Sheet": List all Fabric Sheet types |
| FABRIC\_PARAM\_SPAN\_SYM\_BOTTOM | \-1,017,721 | "Bottom" |
| FABRIC\_PARAM\_SPAN\_SYM\_D\_BOTTOM | \-1,017,725 | "D\_Bottom" |
| FABRIC\_PARAM\_SPAN\_SYM\_D\_LEFT | \-1,017,726 | "D\_Left" |
| FABRIC\_PARAM\_SPAN\_SYM\_D\_RIGHT | \-1,017,727 | "D\_Right" |
| FABRIC\_PARAM\_SPAN\_SYM\_D\_TOP | \-1,017,724 | "D\_Top" |
| FABRIC\_PARAM\_SPAN\_SYM\_LEFT | \-1,017,722 | "Left" |
| FABRIC\_PARAM\_SPAN\_SYM\_RIGHT | \-1,017,723 | "Right" |
| FABRIC\_PARAM\_SPAN\_SYM\_TOP | \-1,017,720 | "Top" |
| FABRIC\_PARAM\_SPAN\_TAG\_COMPONENT\_REFERENCE | \-1,017,728 | "Tag Component Reference" |
| FABRIC\_PARAM\_TAG\_VIEW | \-1,017,713 | "Tag new members in view": List of all Plan Views and None. |
| FABRIC\_PARAM\_TOTAL\_SHEET\_MASS | \-1,017,711 | "Total Sheet Mass": Calculated all sheet mass: Volume of Wire \* Unit Weight. |
| FABRIC\_PARAM\_WIRES\_AT\_COVER | \-1,017,740 | "Wires at Cover": The distribution of wires that is closest to the cover. |
| FABRIC\_SHEET\_DEFAULT\_MAJOR\_LAPSPLICE\_LENGTH | \-1,017,605 | "Default Major Lap Splice Length": Default Major Lap Splice Length |
| FABRIC\_SHEET\_DEFAULT\_MINOR\_LAPSPLICE\_LENGTH | \-1,017,606 | "Default Minor Lap Splice Length": Default Minor Lap Splice Length |
| FABRIC\_SHEET\_LENGTH | \-1,017,608 | "Length": Length |
| FABRIC\_SHEET\_MAJOR\_DIRECTION\_WIRE\_TYPE | \-1,017,603 | "Major Direction Wire Type": Major Direction Wire Type |
| FABRIC\_SHEET\_MAJOR\_END\_OVERHANG | \-1,017,610 | "Major End Overhang": Major End Overhang |
| FABRIC\_SHEET\_MAJOR\_LAYOUT\_PATTERN | \-1,017,611 | "Major Layout Pattern": Major Layout Pattern |
| FABRIC\_SHEET\_MAJOR\_NUMBER\_OF\_WIRES | \-1,017,612 | "Major Number of Wires": Major Number of Wires |
| FABRIC\_SHEET\_MAJOR\_REINFORCEMENT\_AREA | \-1,017,622 | "Major Reinforcement Area": Major Reinforcement Area |
| FABRIC\_SHEET\_MAJOR\_SPACING | \-1,017,613 | "Major Spacing": Major Spacing |
| FABRIC\_SHEET\_MAJOR\_START\_OVERHANG | \-1,017,609 | "Major Start Overhang": Major Start Overhang |
| FABRIC\_SHEET\_MASS | \-1,017,621 | "Sheet Mass": Sheet Mass |
| FABRIC\_SHEET\_MASSUNIT | \-1,017,624 | "Sheet Mass per Unit Area": Structural Sheet Mass per Unit Area \[Sheet Mass / (Overall Length \* Overall Width)] |
| FABRIC\_SHEET\_MINOR\_DIRECTION\_WIRE\_TYPE | \-1,017,604 | "Minor Direction Wire Type": Minor Direction Wire Type |
| FABRIC\_SHEET\_MINOR\_END\_OVERHANG | \-1,017,617 | "Minor End Overhang": Minor End Overhang |
| FABRIC\_SHEET\_MINOR\_LAYOUT\_PATTERN | \-1,017,618 | "Minor Layout Pattern": Minor Layout Pattern |
| FABRIC\_SHEET\_MINOR\_NUMBER\_OF\_WIRES | \-1,017,619 | "Minor Number of Wires": Minor Number of Wires |
| FABRIC\_SHEET\_MINOR\_REINFORCEMENT\_AREA | \-1,017,623 | "Minor Reinforcement Area": Minor Reinforcement Area |
| FABRIC\_SHEET\_MINOR\_SPACING | \-1,017,620 | "Minor Spacing": Minor Spacing |
| FABRIC\_SHEET\_MINOR\_START\_OVERHANG | \-1,017,616 | "Minor Start Overhang": Minor Start Overhang |
| FABRIC\_SHEET\_OVERALL\_LENGTH | \-1,017,607 | "Overall Length": Overall Length |
| FABRIC\_SHEET\_OVERALL\_WIDTH | \-1,017,614 | "Overall Width": Overall Width |
| FABRIC\_SHEET\_PHYSICAL\_MATERIAL\_ASSET | \-1,017,602 | "Physical Material Asset": Physical Material Asset |
| FABRIC\_SHEET\_WIDTH | \-1,017,615 | "Width": Width |
| FABRIC\_WIRE\_DIAMETER | \-1,017,601 | "Nominal Diameter": Nominal Diameter of Fabric Wire. |
| FABRIC\_WIRE\_DISTANCE | \-1,017,738 | "Wire distance": The distance between wires |
| FABRIC\_WIRE\_LENGTH | \-1,017,737 | "Wire length": The wire length |
| FABRIC\_WIRE\_OFFSET | \-1,017,739 | "Offset along wire direction": Offset along wire direction |
| FABRIC\_WIRE\_TYPE | \-1,017,736 | "Wire type": The wire type assigned |
| FABRICATION\_BOTTOM\_ELEVATION\_INCLUDE\_INSULATION\_OF\_PART | \-1,140,992 | "Bottom Elevation with Insulation" |
| FABRICATION\_BOTTOM\_ELEVATION\_OF\_PART | \-1,140,991 | "Bottom Elevation" |
| FABRICATION\_BOTTOM\_OF\_PART | \-1,140,919 | "Lower End Bottom of Insulation Elevation" |
| FABRICATION\_BRANCH\_SIZE | \-1,141,012 | "Size of Primary Branch End" |
| FABRICATION\_CENTERLINE\_ELEVATION\_OF\_PART | \-1,140,988 | "Spot Centerline Elevation": used for both design and fabrication components |
| FABRICATION\_CHANGE\_SERVICE\_PARAM | \-1,141,009 | "Change Service" |
| FABRICATION\_DOUBLEWALL\_MATERIAL\_ABBREVIATION | \-1,140,998 | "Double Wall Material Abbreviation" |
| FABRICATION\_DUCTWORK\_STIFFENER\_SPEC | \-1,141,017 | "Stiffener Specification" |
| FABRICATION\_END\_OFFSET\_PARAM | \-1,140,925 | "End Middle Elevation" |
| FABRICATION\_END\_SIZE | \-1,141,013 | "Size of Connector End" |
| FABRICATION\_FITTING\_DESCRIPTION | \-1,140,999 | "Fabrication Fitting Description" |
| FABRICATION\_INSULATION\_ABBREVIATION | \-1,140,995 | "Insulation Abbreviation" |
| FABRICATION\_INSULATION\_MATERIAL\_FINISH | \-1,141,007 | "Insulation Material" |
| FABRICATION\_INSULATION\_SPEC | \-1,140,947 | "Insulation Specification" |
| FABRICATION\_INSULATION\_SPECIFICATION\_ABBREVIATION | \-1,140,996 | "Insulation Specification Abbreviation" |
| FABRICATION\_LEVEL\_PARAM | \-1,140,916 | "Reference Level" |
| FABRICATION\_MATERIAL\_ABBREVIATION | \-1,140,997 | "Material Abbreviation" |
| FABRICATION\_MATERIAL\_GAUGE | \-1,141,018 | "Material Gauge" |
| FABRICATION\_OFFSET\_PARAM | \-1,140,917 | "Middle Elevation" |
| FABRICATION\_PART\_ALIAS | \-1,140,968 | "Alias" |
| FABRICATION\_PART\_ANGLE | \-1,140,911 | "Angle" |
| FABRICATION\_PART\_ANGLE\_OPTION | \-1,140,949 | "Angle Option" |
| FABRICATION\_PART\_BOUGHT\_OUT | \-1,140,969 | "Bought Out" |
| FABRICATION\_PART\_CUT\_TYPE | \-1,140,970 | "Cut Type" |
| FABRICATION\_PART\_DEPTH\_IN | \-1,140,930 | "Main Primary Depth" |
| FABRICATION\_PART\_DEPTH\_IN\_OPTION | \-1,140,951 | "Main Primary Depth Option" |
| FABRICATION\_PART\_DEPTH\_OUT | \-1,140,935 | "Main Secondary Depth" |
| FABRICATION\_PART\_DEPTH\_OUT\_OPTION | \-1,140,957 | "Main Secondary Depth Option" |
| FABRICATION\_PART\_DIAMETER\_IN | \-1,140,912 | "Main Primary Diameter" |
| FABRICATION\_PART\_DIAMETER\_IN\_OPTION | \-1,140,952 | "Main Primary Diameter Option" |
| FABRICATION\_PART\_DIAMETER\_OUT | \-1,140,933 | "Main Secondary Diameter" |
| FABRICATION\_PART\_DIAMETER\_OUT\_OPTION | \-1,140,955 | "Main Secondary Diameter Option" |
| FABRICATION\_PART\_DOUBLEWALL\_MATERIAL | \-1,140,971 | "Double Wall Material" |
| FABRICATION\_PART\_DOUBLEWALL\_MATERIAL\_AREA | \-1,140,983 | "Double Wall Material Area" |
| FABRICATION\_PART\_DOUBLEWALL\_MATERIAL\_THICKNESS | \-1,140,972 | "Double Wall Material Thickness" |
| FABRICATION\_PART\_INSULATION\_AREA | \-1,140,974 | "Insulation Area" |
| FABRICATION\_PART\_ITEM\_NUMBER | \-1,140,975 | "Item Number" |
| FABRICATION\_PART\_LENGTH | \-1,140,944 | "Length" |
| FABRICATION\_PART\_LENGTH\_OPTION | \-1,140,948 | "Length Option" |
| FABRICATION\_PART\_LINING\_AREA | \-1,140,976 | "Lining Area" |
| FABRICATION\_PART\_MATERIAL | \-1,140,909 | "Part Material" |
| FABRICATION\_PART\_MATERIAL\_THICKNESS | \-1,140,978 | "Part Material Thickness" |
| FABRICATION\_PART\_NOTES | \-1,140,977 | "Fabrication Notes" |
| FABRICATION\_PART\_PAT\_NO | \-1,141,014 | "Part Pattern Number" |
| FABRICATION\_PART\_SHEETMETAL\_AREA | \-1,140,981 | "Part Sheet Metal Area" |
| FABRICATION\_PART\_TAKEOFF\_DIALOG\_PARAM | \-1,140,965 | "More Parameters" |
| FABRICATION\_PART\_WEIGHT | \-1,140,913 | "Weight" |
| FABRICATION\_PART\_WIDTH\_IN | \-1,140,929 | "Main Primary Width" |
| FABRICATION\_PART\_WIDTH\_IN\_OPTION | \-1,140,950 | "Main Primary Width Option" |
| FABRICATION\_PART\_WIDTH\_OUT | \-1,140,934 | "Main Secondary Width" |
| FABRICATION\_PART\_WIDTH\_OUT\_OPTION | \-1,140,956 | "Main Secondary Width Option" |
| FABRICATION\_PIPE\_INVERT\_ELEVATION | \-1,140,993 | "Pipe Invert Elevation": This parameter is obsolete. It exists only for compatibility. |
| FABRICATION\_PRI\_SIZE | \-1,141,010 | "Size of Primary End" |
| FABRICATION\_PRIMARY\_SIZE | \-1,141,010 | "Size of Primary End" |
| FABRICATION\_PRODUCT\_CODE | \-1,140,966 | "Product Code" |
| FABRICATION\_PRODUCT\_DATA\_FINISH\_DESCRIPTION | \-1,140,900 | "Product Finish Description" |
| FABRICATION\_PRODUCT\_DATA\_INSTALL\_TYPE | \-1,140,910 | "Install Type" |
| FABRICATION\_PRODUCT\_DATA\_ITEM\_DESCRIPTION | \-1,140,906 | "Product Short Description" |
| FABRICATION\_PRODUCT\_DATA\_LONG\_DESCRIPTION | \-1,140,902 | "Product Long Description" |
| FABRICATION\_PRODUCT\_DATA\_MATERIAL\_DESCRIPTION | \-1,140,904 | "Product Material Description" |
| FABRICATION\_PRODUCT\_DATA\_OEM | \-1,140,908 | "OEM" |
| FABRICATION\_PRODUCT\_DATA\_PRODUCT | \-1,140,907 | "Product Name" |
| FABRICATION\_PRODUCT\_DATA\_RANGE | \-1,140,901 | "Product Range" |
| FABRICATION\_PRODUCT\_DATA\_SIZE\_DESCRIPTION | \-1,140,905 | "Product Size Description" |
| FABRICATION\_PRODUCT\_DATA\_SPECIFICATION | \-1,140,903 | "Product Specification Description" |
| FABRICATION\_PRODUCT\_ENTRY | \-1,140,943 | "Product Entry" |
| FABRICATION\_RELATIVE\_FILENAME | \-1,140,921 | "Relative File Name" |
| FABRICATION\_ROUTING\_SOLUTIONS\_UI\_PARAM | \-1,140,967 | "x of XX" |
| FABRICATION\_SEC\_SIZE | \-1,141,011 | "Size of Secondary End" |
| FABRICATION\_SECONDARY\_SIZE | \-1,141,011 | "Size of Secondary End" |
| FABRICATION\_SERVICE\_ABBREVIATION | \-1,140,979 | "Fabrication Service Abbreviation" |
| FABRICATION\_SERVICE\_NAME | \-1,140,973 | "Fabrication Service Name" |
| FABRICATION\_SERVICE\_PARAM | \-1,140,339 | "Fabrication Service" |
| FABRICATION\_SET\_UP\_DOWN\_TAG | \-1,140,982 | "SU/SD from Top" |
| FABRICATION\_SET\_UP\_DOWN\_TAG\_FROM\_BOTTOM | \-1,141,008 | "SU/SD from Bottom" |
| FABRICATION\_SLOPE\_PARAM | \-1,140,923 | "Slope" |
| FABRICATION\_SPECIFICATION | \-1,140,915 | "Specification" |
| FABRICATION\_SPECIFICATION\_ABBREVIATION | \-1,140,994 | "Specification Abbreviation" |
| FABRICATION\_SPOT\_BOTTOM\_ELEVATION\_INCLUDE\_INSULATION\_OF\_PART | \-1,140,987 | "Spot Bottom of Insulation Elevation" |
| FABRICATION\_SPOT\_BOTTOM\_ELEVATION\_OF\_PART | \-1,140,986 | "Spot Bottom Elevation": used for both design and fabrication components |
| FABRICATION\_SPOT\_TOP\_ELEVATION\_INCLUDE\_INSULATION\_OF\_PART | \-1,140,985 | "Spot Top of Insulation Elevation" |
| FABRICATION\_SPOT\_TOP\_ELEVATION\_OF\_PART | \-1,140,984 | "Spot Top Elevation": used for both design and fabrication components |
| FABRICATION\_START\_OFFSET\_PARAM | \-1,140,924 | "Start Middle Elevation" |
| FABRICATION\_TOP\_ELEVATION\_INCLUDE\_INSULATION\_OF\_PART | \-1,140,990 | "Top Elevation with Insulation" |
| FABRICATION\_TOP\_ELEVATION\_OF\_PART | \-1,140,989 | "Top Elevation" |
| FABRICATION\_TOP\_OF\_PART | \-1,140,918 | "Upper End Top of Insulation Elevation" |
| FABRICATION\_VENDOR | \-1,140,920 | "Vendor" |
| FABRICATION\_VENDOR\_CODE | \-1,140,914 | "Vendor Code" |
| FACEROOF\_LEVEL\_PARAM | \-1,001,715 | "Reference Level" |
| FACEROOF\_OFFSET\_PARAM | \-1,001,716 | "Level Offset" |
| FAM\_PROFILE\_DEFINITION | \-1,152,374 | "Profile Definition" |
| FAM\_PROFILE\_USAGE | \-1,001,821 | "Profile Usage" |
| FAMILY\_ALLOW\_CUT\_WITH\_VOIDS | \-1,012,811 | "Cut with Voids When Loaded" |
| FAMILY\_ALWAYS\_VERTICAL | \-1,012,808 | "Always vertical" |
| FAMILY\_AUTOJOIN | \-1,012,832 | "Automatically joins geometry to walls" |
| FAMILY\_BASE\_LEVEL\_OFFSET\_PARAM | \-1,001,357 | "Base Offset" |
| FAMILY\_BASE\_LEVEL\_PARAM | \-1,001,350 | "Base Level" |
| FAMILY\_CAN\_HOST\_REBAR | \-1,013,441 | "Can host rebar" |
| FAMILY\_CATEGORY\_PSEUDO\_PARAM | \-1,001,337 | "Category" |
| FAMILY\_CONTENT\_PART\_TYPE | \-1,114,206 | "Part Type" |
| FAMILY\_CURVE\_ATTACHMENT\_PROPORTION | \-1,150,140 | "Attachment Point" |
| FAMILY\_CURVE\_GSTYLE\_FOR\_2010\_MASS | \-1,006,207 | "Subcategory" |
| FAMILY\_CURVE\_GSTYLE\_PLUS\_INVISIBLE | \-1,006,201 | "Subcategory" |
| FAMILY\_CURVE\_GSTYLE\_PLUS\_INVISIBLE\_MINUS\_ANALYTICAL | \-1,006,203 | "Subcategory" |
| FAMILY\_CURVE\_GSTYLE\_PLUS\_INVISIBLE\_PLUS\_STICK\_SYM | \-1,006,202 | "Subcategory" |
| FAMILY\_CURVE\_GSTYLE\_PLUS\_INVISIBLE\_PLUS\_STICK\_SYM\_MINUS\_ANALYTICAL | \-1,006,204 | "Subcategory" |
| FAMILY\_ELECTRICAL\_MAINTAIN\_ANNOTATION\_ORIENTATION | \-1,114,243 | "Maintain Annotation Orientation" |
| FAMILY\_ELEM\_SUBCATEGORY | \-1,006,200 | "Subcategory" |
| FAMILY\_ENABLE\_CUTTING\_IN\_VIEWS | \-1,013,442 | "Enable Cutting in Views" |
| FAMILY\_EXPORT\_AS\_GEOMETRY | \-1,001,570 | "Always export as geometry" |
| FAMILY\_FREEINST\_DEFAULT\_ELEVATION | \-1,154,647 | "Default Elevation" |
| FAMILY\_HEIGHT\_PARAM | \-1,001,300 | "Height" |
| FAMILY\_HOSTING\_BEHAVIOR | \-1,012,843 | "Host" |
| FAMILY\_IS\_ELEVATION\_MARK\_BODY | \-1,012,842 | "Elevation Mark Use" |
| FAMILY\_IS\_PARAMETRIC | \-1,012,831 | "Is parametric" |
| FAMILY\_KEEP\_TEXT\_READABLE | \-1,012,830 | "Keep text readable" |
| FAMILY\_KEY\_EXT\_PARAM | \-1,012,810 | "Filter Parameter" |
| FAMILY\_KEYWORD\_PROTECTED | \-1,150,602 | "Content protection enabled" |
| FAMILY\_LEVEL\_PARAM | \-1,001,352 | "Level" |
| FAMILY\_LINE\_LENGTH\_PARAM | \-1,001,306 | "Length" |
| FAMILY\_NAME\_PSEUDO\_PARAM | \-1,001,336 | "Family" |
| FAMILY\_NESTING\_BEHAVIOR | \-1,155,320 | "Family Nesting Behavior" |
| FAMILY\_RENDERING\_TYPE | \-1,005,196 | "Render Appearance Source" |
| FAMILY\_RFA\_PATH\_PSEUDO\_PARAM | \-1,001,338 | "File Path" |
| FAMILY\_ROTATE\_TEXT\_WITH\_COMPONENT | \-1,012,706 | "Rotate text with component" |
| FAMILY\_ROTATE\_WITH\_COMPONENT | \-1,012,807 | "Rotate with component" |
| FAMILY\_ROUGH\_HEIGHT\_PARAM | \-1,001,304 | "Rough Height" |
| FAMILY\_ROUGH\_WIDTH\_PARAM | \-1,001,305 | "Rough Width" |
| FAMILY\_ROUNDCONNECTOR\_DIMENSIONTYPE | \-1,152,375 | "Round Connector Dimension" |
| FAMILY\_SELF\_ORIENTING | \-1,155,244 | "Align to View" |
| FAMILY\_SHARED | \-1,012,834 | "Shared" |
| FAMILY\_STRUCT\_FOOTING\_USE\_CAP\_TOP | \-1,001,560 | "Cap" |
| FAMILY\_STRUCT\_MATERIAL\_TYPE | \-1,001,550 | "Material for Model Behavior" |
| FAMILY\_SYMBOLIC\_REP | \-1,005,197 | "Symbolic Representation" |
| FAMILY\_THICKNESS\_PARAM | \-1,001,302 | "Thickness" |
| FAMILY\_TOP\_LEVEL\_OFFSET\_PARAM | \-1,001,358 | "Top Offset" |
| FAMILY\_TOP\_LEVEL\_PARAM | \-1,001,351 | "Top Level" |
| FAMILY\_USAGE\_PSEUDO\_PARAM | \-1,001,335 | "Usage" |
| FAMILY\_USE\_PRECUT\_SHAPE | \-1,012,841 | "Show family pre\-cut in plan views" |
| FAMILY\_USING\_MULTIPLE | \-1,180,200 | "Multiple Join" |
| FAMILY\_WIDTH\_PARAM | \-1,001,301 | "Width" |
| FAMILY\_WINDOW\_INSET\_PARAM | \-1,001,303 | "Inset" |
| FAMILY\_WORK\_PLANE\_BASED | \-1,012,833 | "Work Plane\-Based" |
| FAMILY\_WPB\_DEFAULT\_ELEVATION | \-1,001,320 | "Default Elevation" |
| FASCIA\_DEPTH\_PARAM | \-1,001,711 | "Fascia Depth" |
| FASCIA\_MATERIAL\_PARAM | \-1,012,822 | "Material" |
| FASCIA\_PROFILE\_PARAM | \-1,012,819 | "Profile" |
| FBX\_ASSET\_TYPE | \-1,150,100 | "Light Source" |
| FBX\_LIGHT\_AT\_A\_DISTANCE | \-1,150,133 | "At a distance" |
| FBX\_LIGHT\_BALLAST\_LOSS | \-1,114,218 | "Ballast Loss" |
| FBX\_LIGHT\_COLOR\_FILTER | \-1,150,108 | "Color Filter" |
| FBX\_LIGHT\_DIMMING\_LIGHT\_COLOR | \-1,150,117 | "Dimming Lamp Color Temperature Shift" |
| FBX\_LIGHT\_EFFICACY | \-1,150,104 | "Efficacy" |
| FBX\_LIGHT\_EMIT\_CIRCLE\_DIAMETER | \-1,150,129 | "Emit from Circle Diameter" |
| FBX\_LIGHT\_EMIT\_LINE\_LENGTH | \-1,150,126 | "Emit from Line Length" |
| FBX\_LIGHT\_EMIT\_RECTANGLE\_LENGTH | \-1,150,128 | "Emit from Rectangle Length" |
| FBX\_LIGHT\_EMIT\_RECTANGLE\_WIDTH | \-1,150,127 | "Emit from Rectangle Width" |
| FBX\_LIGHT\_EMIT\_SHAPE\_VISIBLE | \-1,150,118 | "Emit Shape Visible in Rendering" |
| FBX\_LIGHT\_ILLUMINANCE | \-1,150,106 | "Illuminance" |
| FBX\_LIGHT\_INITIAL\_COLOR\_CTRL | \-1,150,138 | "Initial Color" |
| FBX\_LIGHT\_INITIAL\_COLOR\_NAME | \-1,150,134 | "Temperature Color" |
| FBX\_LIGHT\_INITIAL\_COLOR\_TEMPERATURE | \-1,150,107 | "Initial Color Temperature" |
| FBX\_LIGHT\_INITIAL\_INTENSITY | \-1,150,102 | "Initial Intensity" |
| FBX\_LIGHT\_INITIAL\_INTENSITY\_INPUT\_METHOD | \-1,150,132 | "Initial Light Intensity Input Method" |
| FBX\_LIGHT\_LAMP\_LUMEN\_DEPR | \-1,150,114 | "Lamp Lumen Depreciation" |
| FBX\_LIGHT\_LAMP\_TILT\_LOSS | \-1,150,112 | "Lamp Tilt Loss" |
| FBX\_LIGHT\_LIMUNOUS\_FLUX | \-1,010,503 | "Luminous Flux" |
| FBX\_LIGHT\_LIMUNOUS\_INTENSITY | \-1,150,105 | "Luminous Intensity" |
| FBX\_LIGHT\_LOSS\_FACTOR\_CTRL | \-1,150,139 | "Light Loss Factor" |
| FBX\_LIGHT\_LOSS\_FACTOR\_METHOD | \-1,150,137 | "Light Loss Input Method" |
| FBX\_LIGHT\_LUMENAIRE\_DIRT | \-1,150,115 | "Luminaire Dirt Depreciation" |
| FBX\_LIGHT\_PHOTOMETRIC\_FILE | \-1,140,034 | "Photometric Web File" |
| FBX\_LIGHT\_PHOTOMETRIC\_FILE\_CACHE | \-1,150,142 | "None" |
| FBX\_LIGHT\_PHOTOMETRICS | \-1,150,101 | "Light Source Definition" |
| FBX\_LIGHT\_PHOTOMETRICS\_FAM | \-1,150,141 | "Light Source Definition (family)" |
| FBX\_LIGHT\_SOURCE\_DIAMETER | \-1,150,130 | "Light Source Symbol Size" |
| FBX\_LIGHT\_SOURCE\_LENGTH | \-1,150,131 | "Light Source Symbol Length" |
| FBX\_LIGHT\_SPOT\_BEAM\_ANGLE | \-1,010,506 | "Spot Beam Angle" |
| FBX\_LIGHT\_SPOT\_FIELD\_ANGLE | \-1,010,507 | "Spot Field Angle" |
| FBX\_LIGHT\_SPOT\_TILT\_ANGLE | \-1,010,505 | "Tilt Angle" |
| FBX\_LIGHT\_SURFACE\_LOSS | \-1,150,113 | "Surface Depreciation Loss" |
| FBX\_LIGHT\_TEMPERATURE\_LOSS | \-1,150,109 | "Temperature Loss" |
| FBX\_LIGHT\_TOTAL\_LIGHT\_LOSS | \-1,114,217 | "Total Light Loss Factor" |
| FBX\_LIGHT\_VOLTAGE\_LOSS | \-1,150,110 | "Voltage Loss" |
| FBX\_LIGHT\_WATTAGE | \-1,150,103 | "Wattage" |
| FILL\_PATTERN\_ID\_PARAM | \-1,002,101 | "Cut fill pattern" |
| FILL\_PATTERN\_ID\_PARAM\_NO\_NO | \-1,002,114 | "Fill Pattern" |
| FILLED\_REGION\_MASKING | \-1,002,125 | "Masking" |
| FIRE\_RATING | \-1,001,206 | "Fire Rating" |
| FIXED\_ROTATION | \-1,006,504 | "Fixed Rotation" |
| FLEXIBLE\_INSTANCE\_FLIP | \-1,150,321 | "Flip" |
| FLOOR\_ATTR\_DEFAULT\_HEIGHT\_PARAM | \-1,001,903 | "Default Height above level" |
| FLOOR\_ATTR\_DEFAULT\_THICKNESS\_PARAM | \-1,001,902 | "Default Thickness" |
| FLOOR\_ATTR\_THICKNESS\_PARAM | \-1,001,900 | "Thickness" |
| FLOOR\_HEIGHTABOVELEVEL\_PARAM | \-1,001,951 | "Height Offset From Level" |
| FLOOR\_PARAM\_IS\_STRUCTURAL | \-1,001,954 | "Structural" |
| FLOOR\_PARAM\_SPAN\_DIRECTION | \-1,001,955 | "Span Direction" |
| FLOOR\_STRUCTURE\_ID\_PARAM | \-1,002,116 | "Structure" |
| FOLLOW\_SURFACE | \-1,150,211 | "Follow Surface" |
| FOREGROUND\_ANY\_PATTERN\_ID\_PARAM | \-1,002,121 | "Foreground Fill Pattern" |
| FOREGROUND\_DRAFT\_PATTERN\_ID\_PARAM | \-1,002,120 | "Foreground Fill Pattern" |
| FOREGROUND\_PATTERN\_COLOR\_PARAM | \-1,002,123 | "Foreground Pattern Color" |
| FRAMING\_LENGTH\_ROUNDOFF | \-1,150,208 | "Structural Framing Length Roundoff" |
| FRAMING\_SHAPE\_CLASSIFICATION | \-1,155,246 | "Framing Shape" |
| FRICTION\_FACTOR | \-1,140,208 | "Friction Factor" |
| FUNCTION\_PARAM | \-1,001,006 | "Function" |
| FURNITURE\_HEIGHT | \-1,001,300 | "Height" |
| FURNITURE\_THICKNESS | \-1,001,302 | "Thickness" |
| FURNITURE\_WIDTH | \-1,001,301 | "Width" |
| GBXML\_EDIT\_DATA\_PARAM | \-1,114,197 | "Energy Settings" |
| GENERIC\_CONSTRUCTION\_TYPE | \-1,001,207 | "Construction Type" |
| GENERIC\_DEPTH | \-1,010,003 | "Depth" |
| GENERIC\_FINISH | \-1,001,208 | "Finish" |
| GENERIC\_HEIGHT | \-1,001,300 | "Height" |
| GENERIC\_THICKNESS | \-1,001,302 | "Thickness" |
| GENERIC\_WIDTH | \-1,001,301 | "Width" |
| GENERIC\_ZONE\_NAME | \-1,155,116 | "Name" |
| GEO\_LOCATION | \-1,007,720 | "Shared Site" |
| GEOM\_VISIBILITY\_PARAM | \-1,001,808 | "Visibility/Graphics Overrides" |
| GRAPHIC\_DISPLAY\_OPTIONS | \-1,005,173 | "Graphic Display Options" |
| GRAPHIC\_DISPLAY\_OPTIONS\_BACKGROUND | \-1,005,135 | "Background" |
| GRAPHIC\_DISPLAY\_OPTIONS\_FOG | \-1,005,136 | "Depth Cueing" |
| GRAPHIC\_DISPLAY\_OPTIONS\_LIGHTING | \-1,005,133 | "Lighting" |
| GRAPHIC\_DISPLAY\_OPTIONS\_MODEL | \-1,005,131 | "Model Display" |
| GRAPHIC\_DISPLAY\_OPTIONS\_PHOTO\_EXPOSURE | \-1,005,137 | "Photographic Exposure" |
| GRAPHIC\_DISPLAY\_OPTIONS\_SHADOWS | \-1,005,132 | "Shadows" |
| GRAPHIC\_DISPLAY\_OPTIONS\_SKETCHY\_LINES | \-1,154,615 | "Sketchy Lines" |
| GRAPHIC\_DISPLAY\_OPTIONS\_SS\_INTENSITY | \-1,005,134 | "Sun and Shadow Intensity" |
| GRID\_BANK\_COL\_NUM | \-1,114,396 | "Column" |
| GRID\_BANK\_COL\_WIDTH | \-1,114,398 | "Column Distance" |
| GRID\_BANK\_ROW\_HEIGHT | \-1,114,397 | "Row Distance" |
| GRID\_BANK\_ROW\_NUM | \-1,114,395 | "Row" |
| GRID\_BUBBLE\_END\_1 | \-1,008,004 | "Plan View Symbols End 1 (Default)" |
| GRID\_BUBBLE\_END\_2 | \-1,008,005 | "Plan View Symbols End 2 (Default)" |
| GRID\_BUBBLE\_LINE\_PEN | \-1,006,703 | "Bubble Weight Number\\n" |
| GRID\_CENTER\_SEGMENT\_COLOR | \-1,006,706 | "Center Segment Color" |
| GRID\_CENTER\_SEGMENT\_PATTERN | \-1,006,707 | "Center Segment Pattern" |
| GRID\_CENTER\_SEGMENT\_STYLE | \-1,006,704 | "Center Segment" |
| GRID\_CENTER\_SEGMENT\_WEIGHT | \-1,006,705 | "Center Segment Weight" |
| GRID\_END\_SEGMENT\_COLOR | \-1,006,709 | "End Segment Color" |
| GRID\_END\_SEGMENT\_PATTERN | \-1,006,710 | "End Segment Pattern" |
| GRID\_END\_SEGMENT\_WEIGHT | \-1,006,708 | "End Segment Weight" |
| GRID\_END\_SEGMENTS\_LENGTH | \-1,006,711 | "End Segments Length" |
| GRID\_HEAD\_TAG | \-1,006,700 | "Symbol" |
| GRID\_NET\_LOCATION\_MARK | \-1,013,448 | "Location Mark": Provides grid system association information |
| GRIDLINE\_SPEC\_STATUS | \-1,013,308 | "Type Association" |
| GROUP\_ALLOWED\_VIEW\_TYPES | \-1,133,502 | "Allowed View Types" |
| GROUP\_ATTACHED\_PARENT\_NAME | \-1,133,503 | "Attached to" |
| GROUP\_LEVEL | \-1,133,500 | "Reference Level" |
| GROUP\_OFFSET\_FROM\_LEVEL | \-1,133,501 | "Origin Level Offset" |
| GROUPNAME\_PARAM | \-1,010,018 | "Group Name for Ribbon Combo Items (for Use with XAML)" |
| GUIDE\_GRID\_NAME\_PARAM | \-1,013,002 | "Name" |
| GUIDE\_GRID\_SPACING\_PARAM | \-1,013,001 | "Guide Spacing" |
| GUTTER\_MATERIAL\_PARAM | \-1,012,823 | "Material" |
| GUTTER\_PROFILE\_PARAM | \-1,012,836 | "Profile" |
| HANDRAIL\_HAND\_CLEARANCE\_PARAM | \-1,150,342 | "Hand Clearance" |
| HANDRAIL\_HEIGHT\_PARAM | \-1,150,340 | "Height" |
| HANDRAIL\_PROJECTION\_PARAM | \-1,150,341 | "Projection" |
| HANDRAIL\_SUPPORTS\_JUSTIFICATION\_PARAM | \-1,150,355 | "Justification" |
| HANDRAIL\_SUPPORTS\_LAYOUT\_PARAM | \-1,150,352 | "Layout" |
| HANDRAIL\_SUPPORTS\_NUMBER\_PARAM | \-1,150,354 | "Number" |
| HANDRAIL\_SUPPORTS\_SPACING\_PARAM | \-1,150,353 | "Spacing" |
| HANDRAIL\_SUPPORTS\_TYPE\_PARAM | \-1,150,351 | "Family" |
| HEAD\_ON\_PLACEMENT\_METHOD | \-1,006,206 | "Draw in Foreground" |
| HEAVY\_END\_PEN | \-1,006,447 | "Heavy End Pen Weight" |
| HEAVY\_TICK\_MARK\_PEN | \-1,006,420 | "Heavy End Pen Weight" |
| HIGHEST\_ASSOCIATED\_LEVEL | \-1,155,256 | "Highest Associated Level": The highest level associated with this Analytical Element. |
| HOST\_AREA\_COMPUTED | \-1,012,805 | "Area" |
| HOST\_ID\_PARAM | \-1,002,108 | "Host Id" |
| HOST\_PANEL\_SCHEDULE\_AS\_PANEL\_PARAM | \-1,001,124 | "Categorize as" |
| HOST\_PERIMETER\_COMPUTED | \-1,001,953 | "Perimeter" |
| HOST\_SSE\_CURVED\_EDGE\_CONDITION\_PARAM | \-1,001,603 | "Curved Edge Condition" |
| HOST\_VOLUME\_COMPUTED | \-1,012,806 | "Volume" |
| Hosted | \-1,001,121 | "Hosted" |
| ICON\_INDEX\_PARAM | \-1,010,017 | "Index Into Image File Name Array (for Use with XAML)" |
| ID\_PARAM | \-1,002,100 | "Id" |
| IFC\_APPLICATION\_NAME | \-1,019,009 | "IfcApplicationName" |
| IFC\_APPLICATION\_VERSION | \-1,019,010 | "IfcApplicationVersion" |
| IFC\_BUILDING\_GUID | \-1,019,003 | "IfcBuilding GUID" |
| IFC\_EXPORT\_ELEMENT | \-1,019,012 | "Export to IFC" |
| IFC\_EXPORT\_ELEMENT\_AS | \-1,019,014 | "Export to IFC As" |
| IFC\_EXPORT\_ELEMENT\_TYPE | \-1,019,013 | "Export Type to IFC" |
| IFC\_EXPORT\_ELEMENT\_TYPE\_AS | \-1,019,015 | "Export Type to IFC As" |
| IFC\_EXPORT\_PREDEFINEDTYPE | \-1,019,016 | "IFC Predefined Type" |
| IFC\_EXPORT\_PREDEFINEDTYPE\_TYPE | \-1,019,017 | "Type IFC Predefined Type" |
| IFC\_GUID | \-1,019,000 | "IfcGUID" |
| IFC\_IMPORT\_MATERIAL\_NAME | \-1,019,018 | "IFC Material Name" |
| IFC\_ORGANIZATION | \-1,019,011 | "IfcOrganization" |
| IFC\_PROJECT\_GUID | \-1,019,002 | "IfcProject GUID" |
| IFC\_SITE\_GUID | \-1,019,004 | "IfcSite GUID" |
| IFC\_TYPE\_GUID | \-1,019,001 | "Type IfcGUID" |
| IMPORT\_ADT\_COMPONENTS\_DESC | \-1,007,733 | "Component Description" |
| IMPORT\_ADT\_ENTITY\_HEIGHT | \-1,007,734 | "Height" |
| IMPORT\_ADT\_ENTITY\_LENGTH | \-1,007,736 | "Length" |
| IMPORT\_ADT\_ENTITY\_ROLL | \-1,007,738 | "Roll" |
| IMPORT\_ADT\_ENTITY\_STRUCT\_TYPE | \-1,007,731 | "Structural Type Name" |
| IMPORT\_ADT\_ENTITY\_STYLE | \-1,007,732 | "Style Name" |
| IMPORT\_ADT\_ENTITY\_THICKNESS | \-1,007,737 | "Thickness" |
| IMPORT\_ADT\_ENTITY\_TYPE | \-1,007,730 | "Type Name" |
| IMPORT\_ADT\_ENTITY\_WIDTH | \-1,007,735 | "Width" |
| IMPORT\_BACKGROUND | \-1,007,705 | "Draw Layer" |
| IMPORT\_BASE\_LEVEL | \-1,007,702 | "Work Plane" |
| IMPORT\_BASE\_LEVEL\_OFFSET | \-1,007,703 | "Offset from Work Plane" |
| IMPORT\_DISPLAY\_UNITS | \-1,007,704 | "Import Units" |
| IMPORT\_INSTANCE\_CUTTING\_IN\_VIEW | \-1,007,707 | "Enable Cutting in Views" |
| IMPORT\_INSTANCE\_SCALE | \-1,007,706 | "Instance Scale" |
| IMPORT\_SCALE | \-1,007,701 | "Scale Factor" |
| IMPORT\_SYMBOL\_NAME | \-1,007,700 | "Name" |
| INDIVIDUAL\_EXCAVATION\_VOLUME | \-1,180,303 | "Individual Excavation Volume" |
| INFRASTRUCTURE\_ALIGNMENT\_DESCRIPTION | \-1,155,213 | "Description" |
| INFRASTRUCTURE\_ALIGNMENT\_DISPLAYED\_END\_STATION | \-1,155,211 | "Displayed End Station" |
| INFRASTRUCTURE\_ALIGNMENT\_DISPLAYED\_START\_STATION | \-1,155,212 | "Displayed Start Station" |
| INFRASTRUCTURE\_ALIGNMENT\_NAME | \-1,155,214 | "Name" |
| INSERT\_ORIENTATION | \-1,001,834 | "Orientation" |
| INSTANCE\_ELEVATION\_PARAM | \-1,001,360 | "Elevation from Level" |
| INSTANCE\_FREE\_HOST\_OFFSET\_PARAM | \-1,001,364 | "Offset from Host" |
| INSTANCE\_FREE\_HOST\_PARAM | \-1,001,363 | "Host" |
| INSTANCE\_HEAD\_HEIGHT\_PARAM | \-1,001,362 | "Head Height" |
| INSTANCE\_LENGTH\_PARAM | \-1,001,375 | "System Length" |
| INSTANCE\_MOVE\_BASE\_WITH\_GRIDS | \-1,150,173 | "Move Base With Grids" |
| INSTANCE\_MOVE\_TOP\_WITH\_GRIDS | \-1,150,172 | "Move Top With Grids" |
| INSTANCE\_MOVES\_WITH\_GRID\_PARAM | \-1,001,371 | "Moves With Grids" |
| INSTANCE\_OFFSET\_POS\_PARAM | \-1,001,370 | "Moves With Nearby Elements" |
| INSTANCE\_REFERENCE\_LEVEL\_PARAM | \-1,001,383 | "Reference Level" |
| INSTANCE\_SCHEDULE\_ONLY\_LEVEL\_PARAM | \-1,001,365 | "Schedule Level" |
| INSTANCE\_SILL\_HEIGHT\_PARAM | \-1,001,361 | "Sill Height" |
| INSTANCE\_STRUCT\_USAGE\_PARAM | \-1,001,381 | "Structural Usage" |
| INSULATION\_SCALE | \-1,011,101 | "Insulation Bulge to Width Ratio (1/x)" |
| INSULATION\_WIDTH | \-1,011,100 | "Insulation Width" |
| INTERIOR\_TICK\_DISPLAY | \-1,006,523 | "Interior Tick Mark Display" |
| INVALID | \-1 |  |
| IS\_VISIBLE\_PARAM | \-1,006,205 | "Visible" |
| JOIN\_STRENGTH\_ORDER | \-1,012,870 | "Abstract Join Strength Order" |
| JOINT\_GAP\_PARAM | \-1,001,798 | "Joint Gap" |
| JOIST\_SYSTEM\_CLEAR\_SPACING\_PARAM | \-1,013,432 | "Clear Spacing" |
| JOIST\_SYSTEM\_ELEM\_TAG\_NEW\_MEMBERS\_VIEW | \-1,140,757 | "Tag new members in view" |
| JOIST\_SYSTEM\_FIXED\_SPACING\_PARAM | \-1,013,431 | "Fixed Spacing" |
| JOIST\_SYSTEM\_JUSTIFICATION\_PARAM | \-1,013,409 | "Justification" |
| JOIST\_SYSTEM\_LAYOUT\_RULE\_PARAM | \-1,013,410 | "Layout Rule" |
| JOIST\_SYSTEM\_MAXIMUM\_SPACING\_PARAM | \-1,013,430 | "Maximum Spacing" |
| JOIST\_SYSTEM\_NEW\_BEAM\_TYPE\_NO\_FAM\_NAME\_PARAM | \-1,013,419 | "Beam Type (No Family Name)" |
| JOIST\_SYSTEM\_NEW\_BEAM\_TYPE\_PARAM | \-1,013,411 | "Beam Type" |
| JOIST\_SYSTEM\_NUM\_BEAMS\_SAME\_TYPE | \-1,013,415 | "Num. of Beams With Same Type" |
| JOIST\_SYSTEM\_NUMBER\_OF\_LINES\_PARAM | \-1,013,407 | "Number of Lines" |
| JOIST\_SYSTEM\_SPACING\_PARAM | \-1,013,408 | "Centerline Spacing" |
| KEEP\_READABLE | \-1,006,503 | "Keep Readable" |
| KEY\_SOURCE\_PARAM | \-1,140,423 | "Key Source" |
| KEY\_VALUE | \-1,140,418 | "Key Value" |
| KEYNOTE\_NUMBER | \-1,140,421 | "Key Value" |
| KEYNOTE\_PARAM | \-1,140,422 | "Keynote" |
| KEYNOTE\_TEXT | \-1,140,419 | "Keynote Text" |
| LAYER\_ELEM\_AREA\_COMPUTED | \-1,155,234 | "Area" |
| LAYER\_ELEM\_BASE\_CONSTRAINT | \-1,155,229 | "Base Constraint" |
| LAYER\_ELEM\_BASE\_EXTENSION\_DIS | \-1,155,239 | "Base Extension Distance" |
| LAYER\_ELEM\_COMPOUND\_ELEM\_FAMILY | \-1,155,274 | "Compound Element Family" |
| LAYER\_ELEM\_COMPOUND\_ELEM\_TYPE | \-1,155,275 | "Compound Element Type" |
| LAYER\_ELEM\_FUNCTION | \-1,155,237 | "Function": Function |
| LAYER\_ELEM\_IS\_CORE\_LAYER | \-1,155,276 | "Is Core Layer" |
| LAYER\_ELEM\_IS\_STRUCTURAL\_MATERIAL | \-1,155,277 | "Is Structural Material" |
| LAYER\_ELEM\_IS\_VARIABLE | \-1,155,278 | "Is Variable" |
| LAYER\_ELEM\_MATERIALS | \-1,155,236 | "Material": Material |
| LAYER\_ELEM\_OFFSET\_FROM\_HOST | \-1,155,233 | "Offset From Host" |
| LAYER\_ELEM\_SCHEDULE\_FAMILY | \-1,155,279 | "Family" |
| LAYER\_ELEM\_THICKNESS | \-1,155,235 | "Thickness": Thickness |
| LAYER\_ELEM\_TOP\_CONSTRAINT | \-1,155,228 | "Top Constraint" |
| LAYER\_ELEM\_TOP\_EXTENSION\_DIS | \-1,155,238 | "Top Extension Distance" |
| LAYER\_ELEM\_VOLUME\_COMPUTED | \-1,155,232 | "Volume" |
| LAYER\_TYPE\_MATERIALS | \-1,155,231 | "Material": Material |
| LAYER\_TYPE\_THICKNESS | \-1,155,230 | "Thickness": Thickness |
| LAYOUTNODE\_CURVETYPE\_PARAM | \-1,142,000 | "Curve Type Reference" |
| LEADER\_ANGLE | \-1,018,706 | "Angle" |
| LEADER\_ARROW\_WIDTH | \-1,006,426 | "Arrow Width Angle" |
| LEADER\_ARROWHEAD | \-1,006,315 | "Leader Arrowhead" |
| LEADER\_LEFT\_ATTACHMENT | \-1,150,230 | "Left Attachment" |
| LEADER\_LENGTH | \-1,018,705 | "Leader Length" |
| LEADER\_LINE | \-1,006,502 | "Leader Line" |
| LEADER\_OFFSET\_SHEET | \-1,006,501 | "Leader/Border Offset" |
| LEADER\_ORIENTATION | \-1,018,707 | "Orientation" |
| LEADER\_RIGHT\_ATTACHMENT | \-1,150,231 | "Right Attachment" |
| LEGEND\_COMPONENT | \-1,133,750 | "Component Type" |
| LEGEND\_COMPONENT\_DETAIL\_LEVEL | \-1,133,753 | "Detail Level" |
| LEGEND\_COMPONENT\_LENGTH | \-1,133,752 | "Host Length" |
| LEGEND\_COMPONENT\_VIEW | \-1,133,751 | "View Direction" |
| LEVEL\_ATTR\_ROOM\_COMPUTATION\_AUTOMATIC | \-1,006,941 | "Automatic Room Computation Height" |
| LEVEL\_ATTR\_ROOM\_COMPUTATION\_HEIGHT | \-1,006,940 | "Computation Height" |
| LEVEL\_DATA\_FLOOR\_AREA | \-1,012,010 | "Floor Area" |
| LEVEL\_DATA\_FLOOR\_PERIMETER | \-1,012,009 | "Floor Perimeter" |
| LEVEL\_DATA\_MASS\_FAMILY\_AND\_TYPE\_PARAM | \-1,012,017 | "Mass: Family and Type" |
| LEVEL\_DATA\_MASS\_FAMILY\_PARAM | \-1,012,016 | "Mass: Family" |
| LEVEL\_DATA\_MASS\_INSTANCE\_COMMENTS | \-1,012,019 | "Mass: Comments" |
| LEVEL\_DATA\_MASS\_TYPE\_COMMENTS | \-1,012,018 | "Mass: Type Comments" |
| LEVEL\_DATA\_MASS\_TYPE\_DESCRIPTION | \-1,012,020 | "Mass: Description" |
| LEVEL\_DATA\_MASS\_TYPE\_PARAM | \-1,012,013 | "Mass: Type" |
| LEVEL\_DATA\_OWNING\_LEVEL | \-1,012,014 | "Level" |
| LEVEL\_DATA\_SPACE\_USAGE | \-1,012,015 | "Usage" |
| LEVEL\_DATA\_SURFACE\_AREA | \-1,012,011 | "Exterior Surface Area" |
| LEVEL\_DATA\_VOLUME | \-1,012,012 | "Floor Volume" |
| LEVEL\_ELEV | \-1,007,102 | "Elevation" |
| LEVEL\_HEAD\_TAG | \-1,007,100 | "Symbol" |
| LEVEL\_IS\_BUILDING\_STORY | \-1,007,111 | "Building Story" |
| LEVEL\_IS\_GROUND\_PLANE | \-1,150,195 | "Is ground plane" |
| LEVEL\_IS\_STRUCTURAL | \-1,007,112 | "Structural" |
| LEVEL\_NAME | \-1,007,101 | "Level" |
| LEVEL\_PARAM | \-1,001,952 | "Level" |
| LEVEL\_RELATIVE\_BASE\_TYPE | \-1,007,109 | "Elevation Base" |
| LEVEL\_ROOM\_COMPUTATION\_HEIGHT | \-1,006,939 | "Computation Height" |
| LEVEL\_UP\_TO\_LEVEL | \-1,007,110 | "Story Above" |
| LIGHTING\_FIXTURE\_LAMP | \-1,010,501 | "Lamp" |
| LIGHTING\_FIXTURE\_LIGHT\_EMITTER | \-1,010,508 | "Light Emitter" |
| LIGHTING\_FIXTURE\_WATTAGE | \-1,010,500 | "Wattage Comments" |
| LINE\_COLOR | \-1,006,304 | "Color" |
| LINE\_PATTERN | \-1,006,305 | "Line Pattern" |
| LINE\_PEN | \-1,006,303 | "Line Weight" |
| LINE\_SHAPE\_AT\_CORNER | \-1,006,624 | "Line Shape at Landing Corner" |
| LINEAR\_DIM\_TYPE | \-1,006,467 | "Dimension String Type" |
| LINEAR\_FRAMING\_LENGTH | \-1,155,247 | "Length" |
| LOAD\_ALL\_NON\_0\_LOADS | \-1,015,080 | "All non 0 loads" |
| LOAD\_AREA\_AREA | \-1,015,069 | "Area" |
| LOAD\_AREA\_FORCE\_FX1 | \-1,015,060 | "Fx 1" |
| LOAD\_AREA\_FORCE\_FX2 | \-1,015,063 | "Fx 2" |
| LOAD\_AREA\_FORCE\_FX3 | \-1,015,066 | "Fx 3" |
| LOAD\_AREA\_FORCE\_FY1 | \-1,015,061 | "Fy 1" |
| LOAD\_AREA\_FORCE\_FY2 | \-1,015,064 | "Fy 2" |
| LOAD\_AREA\_FORCE\_FY3 | \-1,015,067 | "Fy 3" |
| LOAD\_AREA\_FORCE\_FZ1 | \-1,015,062 | "Fz 1" |
| LOAD\_AREA\_FORCE\_FZ2 | \-1,015,065 | "Fz 2" |
| LOAD\_AREA\_FORCE\_FZ3 | \-1,015,068 | "Fz 3" |
| LOAD\_AREA\_IS\_PROJECTED | \-1,015,070 | "Projected Load" |
| LOAD\_ARROW\_SEPARATION | \-1,015,205 | "Distance between arrows" |
| LOAD\_ATTR\_AREA\_FORCE\_SCALE\_FACTOR | \-1,015,207 | "Area force scale" |
| LOAD\_ATTR\_FORCE\_ARROW\_TYPE | \-1,015,200 | "Force arrowhead" |
| LOAD\_ATTR\_FORCE\_SCALE\_FACTOR | \-1,015,201 | "Force scale" |
| LOAD\_ATTR\_LINEAR\_FORCE\_SCALE\_FACTOR | \-1,015,206 | "Linear force scale" |
| LOAD\_ATTR\_MOMENT\_ARROW\_ARC | \-1,015,202 | "Moment arrowhead" |
| LOAD\_ATTR\_MOMENT\_ARROW\_LINE | \-1,015,203 | "Moment arrowhead (alternate)" |
| LOAD\_ATTR\_MOMENT\_SCALE\_FACTOR | \-1,015,204 | "Moment scale" |
| LOAD\_CASE\_ID | \-1,015,000 | "Load Case" |
| LOAD\_CASE\_NAME | \-1,015,250 | "Name" |
| LOAD\_CASE\_NATURE | \-1,015,252 | "Nature" |
| LOAD\_CASE\_NATURE\_TEXT | \-1,015,082 | "Nature" |
| LOAD\_CASE\_NUMBER | \-1,015,251 | "Case Number" |
| LOAD\_CASE\_SUBCATEGORY | \-1,015,253 | "Category" |
| LOAD\_COMBINATION\_FACTOR | \-1,015,256 | "Factor" |
| LOAD\_COMBINATION\_NAME | \-1,015,255 | "Name" |
| LOAD\_COMMENTS | \-1,015,083 | "Comments" |
| LOAD\_DESCRIPTION | \-1,015,084 | "Description" |
| LOAD\_FORCE\_FX | \-1,015,010 | "Fx" |
| LOAD\_FORCE\_FY | \-1,015,011 | "Fy" |
| LOAD\_FORCE\_FZ | \-1,015,012 | "Fz" |
| LOAD\_IS\_CONSTRAINED\_ON\_HOST | \-1,155,284 | "Is constrained on host" |
| LOAD\_IS\_HOSTED | \-1,015,006 | "Is Hosted" |
| LOAD\_IS\_PROJECTED | \-1,015,042 | "Projected Load" |
| LOAD\_IS\_REACTION | \-1,015,005 | "Is Reaction" |
| LOAD\_IS\_UNIFORM | \-1,015,003 | "Uniform Load" |
| LOAD\_LINEAR\_FORCE\_FX1 | \-1,015,030 | "Fx 1" |
| LOAD\_LINEAR\_FORCE\_FX2 | \-1,015,033 | "Fx 2" |
| LOAD\_LINEAR\_FORCE\_FY1 | \-1,015,031 | "Fy 1" |
| LOAD\_LINEAR\_FORCE\_FY2 | \-1,015,034 | "Fy 2" |
| LOAD\_LINEAR\_FORCE\_FZ1 | \-1,015,032 | "Fz 1" |
| LOAD\_LINEAR\_FORCE\_FZ2 | \-1,015,035 | "Fz 2" |
| LOAD\_LINEAR\_LENGTH | \-1,015,043 | "Length" |
| LOAD\_MOMENT\_MX | \-1,015,013 | "Mx" |
| LOAD\_MOMENT\_MX1 | \-1,015,036 | "Mx 1" |
| LOAD\_MOMENT\_MX2 | \-1,015,039 | "Mx 2" |
| LOAD\_MOMENT\_MY | \-1,015,014 | "My" |
| LOAD\_MOMENT\_MY1 | \-1,015,037 | "My 1" |
| LOAD\_MOMENT\_MY2 | \-1,015,040 | "My 2" |
| LOAD\_MOMENT\_MZ | \-1,015,015 | "Mz" |
| LOAD\_MOMENT\_MZ1 | \-1,015,038 | "Mz 1" |
| LOAD\_MOMENT\_MZ2 | \-1,015,041 | "Mz 2" |
| LOAD\_NATURE\_NAME | \-1,015,254 | "Name" |
| LOAD\_USAGE\_NAME | \-1,015,259 | "Name" |
| LOAD\_USE\_LOCAL\_COORDINATE\_SYSTEM | \-1,015,001 | "Orient to" |
| LOCK\_ALIGNMENT\_UI\_TOGGLE | \-1,155,240 | "Lock": This is used by the UI to allow selection of lock alignment. |
| LOCKED\_BASE\_OFFSET | \-1,150,163 | "Negative Offset" |
| LOCKED\_END\_OFFSET | \-1,150,165 | "Positive Offset" |
| LOCKED\_START\_OFFSET | \-1,150,164 | "Negative Offset" |
| LOCKED\_TOP\_OFFSET | \-1,150,162 | "Positive Offset" |
| LOWEST\_ASSOCIATED\_LEVEL | \-1,155,257 | "Lowest Associated Level": The lowest level associated with this Analytical Element. |
| LV\_MULLION\_LEG1 | \-1,007,354 | "Leg 1" |
| LV\_MULLION\_LEG2 | \-1,007,355 | "Leg 2" |
| MAKE\_SURFACE\_FROM\_CLOSED\_LOOPS | \-1,123,516 | "Make surface from closed loops" |
| MARKUPS\_CREATED | \-1,133,902 | "Created" |
| MARKUPS\_CREATOR | \-1,133,903 | "Creator" |
| MARKUPS\_HISTORY | \-1,133,906 | "History" |
| MARKUPS\_LABEL | \-1,133,904 | "Label" |
| MARKUPS\_MODIFIED | \-1,133,901 | "Modified" |
| MARKUPS\_NOTES | \-1,133,907 | "Notes" |
| MARKUPS\_PRIVATE | \-1,133,908 | "Private" |
| MARKUPS\_STATUS | \-1,133,905 | "Status" |
| MASS\_DATA\_CONCEPTUAL\_CONSTRUCTION | \-1,012,030 | "Conceptual Types" |
| MASS\_DATA\_GLAZING\_IS\_SHADED | \-1,012,040 | "Glazing is Shaded" |
| MASS\_DATA\_MASS\_EXTERIOR\_WALL\_AREA | \-1,012,032 | "Mass Exterior Wall Area" |
| MASS\_DATA\_MASS\_INTERIOR\_WALL\_AREA | \-1,012,033 | "Mass Interior Wall Area" |
| MASS\_DATA\_MASS\_OPENING\_AREA | \-1,012,037 | "Mass Opening Area" |
| MASS\_DATA\_MASS\_ROOF\_AREA | \-1,012,034 | "Mass Roof Area" |
| MASS\_DATA\_MASS\_SKYLIGHT\_AREA | \-1,012,036 | "Mass Skylight Area" |
| MASS\_DATA\_MASS\_WINDOW\_AREA | \-1,012,035 | "Mass Window Area" |
| MASS\_DATA\_PERCENTAGE\_GLAZING | \-1,012,039 | "Target Percentage Glazing" |
| MASS\_DATA\_PERCENTAGE\_SKYLIGHTS | \-1,012,043 | "Target Percentage Skylights" |
| MASS\_DATA\_SHADE\_DEPTH | \-1,012,041 | "Shade Depth" |
| MASS\_DATA\_SILL\_HEIGHT | \-1,012,042 | "Target Sill Height" |
| MASS\_DATA\_SKYLIGHT\_WIDTH | \-1,012,044 | "Skylight Width \& Depth" |
| MASS\_DATA\_SLAB | \-1,012,098 | "Slab" |
| MASS\_DATA\_SUBCATEGORY | \-1,012,031 | "Subcategory" |
| MASS\_DATA\_SURFACE\_DATA\_SOURCE | \-1,012,045 | "Values" |
| MASS\_DATA\_UNDERGROUND | \-1,012,038 | "Underground" |
| MASS\_FLOOR\_AREA\_LEVELS | \-1,012,005 | "Mass Floors" |
| MASS\_GROSS\_AREA | \-1,012,004 | "Gross Floor Area" |
| MASS\_GROSS\_SURFACE\_AREA | \-1,012,006 | "Gross Surface Area" |
| MASS\_GROSS\_VOLUME | \-1,012,007 | "Gross Volume" |
| MASS\_SURFACEDATA\_MATERIAL | \-1,012,023 | "Graphical Appearance" |
| MASS\_ZONE\_CONDITION\_TYPE\_PARAM | \-1,012,027 | "Condition Type" |
| MASS\_ZONE\_FLOOR\_AREA | \-1,012,025 | "Mass Floor Area" |
| MASS\_ZONE\_MATERIAL | \-1,012,022 | "Graphical Appearance" |
| MASS\_ZONE\_SPACE\_TYPE\_PARAM | \-1,012,026 | "Space Type" |
| MASS\_ZONE\_VOLUME | \-1,012,021 | "Mass Zone Volume" |
| MASSING\_INTEGRATION\_LEVEL | \-1,012,000 | "Constrain to Massing" |
| MATCHLINE\_BOTTOM\_OFFSET | \-1,140,752 | "Bottom Offset" |
| MATCHLINE\_BOTTOM\_PLANE | \-1,140,754 | "Bottom Constraint" |
| MATCHLINE\_TOP\_OFFSET | \-1,140,751 | "Top Offset" |
| MATCHLINE\_TOP\_PLANE | \-1,140,753 | "Top Constraint" |
| MATERIAL\_AREA | \-1,140,360 | "Area" |
| MATERIAL\_ASPAINT | \-1,140,359 | "As Paint" |
| MATERIAL\_ASSET\_PARAM\_ASSET\_LIB\_ID | \-1,152,337 | "Asset library id" |
| MATERIAL\_ASSET\_PARAM\_COMMON\_SHARED\_ASSET | \-1,152,338 | "Sharing" |
| MATERIAL\_ASSET\_PARAM\_EXTERNAL\_MATERIAL\_ID | \-1,152,339 | "External Material ID" |
| MATERIAL\_ASSET\_PARAM\_SOURCE | \-1,152,340 | "Source" |
| MATERIAL\_ASSET\_PARAM\_SOURCE\_URL | \-1,152,341 | "Source URL" |
| MATERIAL\_ID\_PARAM | \-1,002,107 | "Material" |
| MATERIAL\_NAME | \-1,140,355 | "Name" |
| MATERIAL\_PARAM\_COLOR | \-1,002,550 | "Color" |
| MATERIAL\_PARAM\_GLOW | \-1,002,552 | "Glow" |
| MATERIAL\_PARAM\_SHININESS | \-1,002,554 | "Shininess" |
| MATERIAL\_PARAM\_SMOOTHNESS | \-1,002,553 | "Smoothness" |
| MATERIAL\_PARAM\_TRANSPARENCY | \-1,002,551 | "Transparency" |
| MATERIAL\_VOLUME | \-1,140,361 | "Volume" |
| MEASURE\_FROM\_STRUCTURE | \-1,001,120 | "Extend into wall (to core)" |
| MECHANICAL\_EQUIPMENT\_SET\_ID\_PARAM | \-1,153,112 | "Mechanical Equipment Set" |
| MECHANICAL\_EQUIPMENT\_SET\_NAME | \-1,153,111 | "Name" |
| MECHANICAL\_EQUIPMENT\_SET\_ON\_DUTY | \-1,153,109 | "On Duty" |
| MECHANICAL\_EQUIPMENT\_SET\_ON\_STANDBY | \-1,153,110 | "On Standby" |
| MEP\_AIRLOOP\_FANTYPE | \-1,153,511 | "Fan" |
| MEP\_AIRLOOP\_HEATEXCHANGER\_TYPE | \-1,153,504 | "Heat Exchanger" |
| MEP\_AIRLOOP\_PREHEAT\_COILTYPE | \-1,153,505 | "Preheat Coil" |
| MEP\_ANALYTICAL\_CRITICALPATH\_PARAM | \-1,153,106 | "Critical Path" |
| MEP\_ANALYTICAL\_CRITICALSEQUENCE | \-1,153,121 | "Critical Sequence" |
| MEP\_ANALYTICAL\_ELEC\_APPARENT\_POWER\_RATING | \-1,153,123 | "Apparent Power Rating" |
| MEP\_ANALYTICAL\_ELEC\_CURRENT | \-1,153,118 | "Current" |
| MEP\_ANALYTICAL\_ELEC\_CURRENT\_RATING | \-1,153,116 | "Current Rating" |
| MEP\_ANALYTICAL\_ELEC\_VOLTAGE | \-1,153,117 | "Voltage" |
| MEP\_ANALYTICAL\_EQUIPMENT\_NAME | \-1,153,518 | "Name" |
| MEP\_ANALYTICAL\_HEADERSEGMENT | \-1,153,120 | "Header" |
| MEP\_ANALYTICAL\_HYDRAULICLOOP | \-1,153,122 | "Hydraulic Loop" |
| MEP\_ANALYTICAL\_LOOP\_BOUNDARY\_PARAM | \-1,153,113 | "Loop Boundary" |
| MEP\_ANALYTICAL\_LOOP\_NAME | \-1,153,500 | "Name" |
| MEP\_ANALYTICAL\_NETWORK | \-1,153,119 | "Network Id" |
| MEP\_ANALYTICAL\_PIPE\_DESIGNFLOW | \-1,153,105 | "Design Flow" |
| MEP\_CHILLED\_WATER\_LOOP | \-1,153,510 | "Chilled Water Loop" |
| MEP\_CONDENSER\_WATER\_LOOP | \-1,153,503 | "Condenser Water Loop" |
| MEP\_COOLING\_COIL\_TYPE | \-1,153,509 | "Cooling Coil" |
| MEP\_ELEC\_ZONE\_EQUIPMENT\_TYPE | \-1,153,529 | "Equipment Type" |
| MEP\_EQUIPMENT\_CALC\_PIPINGFLOW\_PARAM | \-1,153,103 | "Calculated Flow" |
| MEP\_EQUIPMENT\_CALC\_PIPINGPRESSUREDROP\_PARAM | \-1,153,104 | "Calculated Pressure Drop" |
| MEP\_EQUIPMENT\_CLASSIFICATION | \-1,153,100 | "Classification" |
| MEP\_HEATING\_COIL\_TYPE | \-1,153,507 | "Heating Coil" |
| MEP\_HEATING\_HOTWATER\_LOOP | \-1,153,508 | "Heating Hot Water Loop" |
| MEP\_HORIZONTAIL\_OFFSET | \-1,141,034 | "Horizontal Offset" |
| MEP\_IGNORE\_FLOW\_ANALYSIS | \-1,153,114 | "Ignore Flow Analysis" |
| MEP\_LOWER\_BOTTOM\_ELEVATION | \-1,141,025 | "Lower End Bottom Elevation" |
| MEP\_LOWER\_BOTTOM\_ELEVATION\_INCLUDE\_INSULATION | \-1,141,029 | "Lower End Bottom of Insulation Elevation" |
| MEP\_LOWER\_CENTERLINE\_ELEVATION | \-1,141,021 | "Lower End Centerline Elevation" |
| MEP\_LOWER\_TOP\_ELEVATION | \-1,141,024 | "Lower End Top Elevation" |
| MEP\_LOWER\_TOP\_ELEVATION\_INCLUDE\_INSULATION | \-1,141,028 | "Lower End Top of Insulation Elevation" |
| MEP\_PIPE\_LOWER\_INVERT\_ELEVATION | \-1,141,033 | "Lower End Invert Elevation" |
| MEP\_PIPE\_LOWER\_OBVERT\_ELEVATION | \-1,141,031 | "Lower End Obvert Elevation" |
| MEP\_PIPE\_UPPER\_INVERT\_ELEVATION | \-1,141,032 | "Upper End Invert Elevation" |
| MEP\_PIPE\_UPPER\_OBVERT\_ELEVATION | \-1,141,030 | "Upper End Obvert Elevation" |
| MEP\_PREHEAT\_HOTWATER\_LOOP | \-1,153,506 | "Preheat Hot Water Loop" |
| MEP\_PROFILE\_TYPE\_PARAM | \-1,140,259 | "Shape" |
| MEP\_REHEAT\_COIL\_TYPE | \-1,153,514 | "Reheat Coil" |
| MEP\_REHEAT\_HOTWATER\_LOOP | \-1,153,526 | "Reheat Hot Water Loop" |
| MEP\_SEGMENT\_ELEMENT\_TYPENAME | \-1,153,127 | "Type Name" |
| MEP\_SEGMENT\_FAMILYNAME | \-1,153,126 | "Family Name" |
| MEP\_SEGMENT\_FLOW\_CHARACTERISTIC | \-1,153,129 | "Flow Characteristic" |
| MEP\_SEGMENT\_LENGTH | \-1,153,124 | "Analytical Length" |
| MEP\_SEGMENT\_OVERRIDE | \-1,153,128 | "Overrides" |
| MEP\_SEGMENT\_SYSTEMORSERVICE | \-1,153,125 | "System Type/Service Name" |
| MEP\_SPOT\_BOTTOM\_ELEVATION | \-1,140,986 | "Spot Bottom Elevation": used for both design and fabrication components |
| MEP\_SPOT\_BOTTOM\_ELEVATION\_INCLUDE\_INSULATION | \-1,140,987 | "Spot Bottom of Insulation Elevation" |
| MEP\_SPOT\_CENTERLINE\_ELEVATION | \-1,140,988 | "Spot Centerline Elevation": used for both design and fabrication components |
| MEP\_SPOT\_TOP\_ELEVATION | \-1,140,984 | "Spot Top Elevation": used for both design and fabrication components |
| MEP\_SPOT\_TOP\_ELEVATION\_INCLUDE\_INSULATION | \-1,140,985 | "Spot Top of Insulation Elevation" |
| MEP\_SYSTEM\_FILL\_GRAPHICS\_OVERRIDES\_PARAM | \-1,133,418 | "Fill Pattern Graphics Overrides" |
| MEP\_SYSTEM\_LINE\_GRAPHICS\_OVERRIDES\_PARAM | \-1,140,331 | "Graphic Overrides" |
| MEP\_UPPER\_BOTTOM\_ELEVATION | \-1,141,023 | "Upper End Bottom Elevation" |
| MEP\_UPPER\_BOTTOM\_ELEVATION\_INCLUDE\_INSULATION | \-1,141,027 | "Upper End Bottom of Insulation Elevation" |
| MEP\_UPPER\_CENTERLINE\_ELEVATION | \-1,141,020 | "Upper End Centerline Elevation" |
| MEP\_UPPER\_TOP\_ELEVATION | \-1,141,022 | "Upper End Top Elevation" |
| MEP\_UPPER\_TOP\_ELEVATION\_INCLUDE\_INSULATION | \-1,141,026 | "Upper End Top of Insulation Elevation" |
| MEP\_VRF\_LOOP | \-1,153,527 | "Variable Refrigerant Flow Loop" |
| MEP\_WATERLOOP\_CHILLERTYPE | \-1,153,502 | "Chiller Type" |
| MEP\_WATERLOOP\_TYPE | \-1,153,501 | "Loop Type" |
| MEP\_ZONE\_AIR\_LOOP | \-1,153,516 | "Air System" |
| MEP\_ZONE\_EQUIPMENT | \-1,153,519 | "Zone Equipment" |
| MEP\_ZONE\_EQUIPMENT\_BEHAVIOR | \-1,153,513 | "Behavior" |
| MEP\_ZONE\_EQUIPMENT\_DRAW\_VENTILATION | \-1,153,528 | "Draw Ventilation" |
| MEP\_ZONE\_EQUIPMENT\_TYPE | \-1,153,512 | "Equipment Type" |
| MEP\_ZONE\_HOTWATER\_LOOP | \-1,153,517 | "Heating Hot Water Loop" |
| MIRROR\_COPY | \-1,027,004 | "Copy" |
| MODEL\_CATEGORY\_ID\_PARAM | \-1,002,109 | "Subcategory" |
| MODEL\_GRAPHICS\_STYLE | \-1,005,165 | "Visual Style" |
| MODEL\_GRAPHICS\_STYLE\_ANON\_DRAFT | \-1,005,172 | "Visual Style" |
| MODEL\_OR\_SYMBOLIC | \-1,001,818 | "Model or Symbolic" |
| MODEL\_TEXT\_SIZE | \-1,006,336 | "Text Size" |
| MOVE\_CONSTRAIN | \-1,027,001 | "Constrain" |
| MOVE\_DISJOIN | \-1,027,002 | "Disjoin" |
| MOVE\_MULTIPLE | \-1,027,003 | "Multiple" |
| MOVES\_WITH\_GRID\_PARAM | \-1,155,220 | "Moves With Grids": Disable attachment from grids. |
| MULLION\_ANGLE | \-1,007,363 | "Angle" |
| MULLION\_CORNER\_TYPE | \-1,007,353 | "Corner Mullion" |
| MULLION\_DEPTH | \-1,007,356 | "Depth" |
| MULLION\_DEPTH1 | \-1,007,357 | "Depth 1" |
| MULLION\_DEPTH2 | \-1,007,358 | "Depth 2" |
| MULLION\_FAM\_TYPE | \-1,007,352 | "Mullion Family General Shape" |
| MULLION\_OFFSET | \-1,007,351 | "Offset" |
| MULLION\_POSITION | \-1,007,362 | "Position" |
| MULLION\_PROFILE | \-1,007,361 | "Profile" |
| MULTI\_REFERENCE\_ANNOTATION\_DIMENSION\_STYLE | \-1,007,053 | "Dimension Style" |
| MULTI\_REFERENCE\_ANNOTATION\_GROUP\_TAG\_HEADS | \-1,007,052 | "Group Matching Tag Heads" |
| MULTI\_REFERENCE\_ANNOTATION\_REFERENCE\_CATEGORY | \-1,007,050 | "Reference Category" |
| MULTI\_REFERENCE\_ANNOTATION\_SHOW\_DIMENSION\_TEXT | \-1,007,054 | "Show Dimension Text" |
| MULTI\_REFERENCE\_ANNOTATION\_TAG\_TYPE | \-1,007,051 | "Tag Family" |
| MULTIPLE\_ALIGNMENT\_UI\_TOGGLE | \-1,155,241 | "Multiple Alignment": This is used by the UI to allow selection of multiple elements. |
| MULTISTORY\_STAIRS\_ACTUAL\_TREAD\_DEPTH | \-1,154,634 | "Actual Tread Depth" |
| MULTISTORY\_STAIRS\_REF\_LEVEL | \-1,154,630 | "Reference Level": The reference level of stairs |
| NODE\_CONNECTION\_STATUS | \-1,001,597 | "Connection Status" |
| NUMBER\_PARTITION\_PARAM | \-1,154,614 | "Partition" |
| NUMBER\_SYSTEM\_DISPLAY\_RULE | \-1,006,643 | "Display Rule" |
| NUMBER\_SYSTEM\_JUSTIFY | \-1,006,641 | "Justify" |
| NUMBER\_SYSTEM\_JUSTIFY\_OFFSET | \-1,006,637 | "Justify Offset" |
| NUMBER\_SYSTEM\_ORIENTATION | \-1,006,639 | "Orientation" |
| NUMBER\_SYSTEM\_REFERENCE | \-1,006,642 | "Reference" |
| NUMBER\_SYSTEM\_REFERENCE\_OFFSET | \-1,006,638 | "Offset from Reference" |
| NUMBER\_SYSTEM\_TAG\_TYPE | \-1,006,644 | "Tag Type" |
| NUMBER\_SYSTEM\_TEXT\_SIZE | \-1,006,645 | "Number Size" |
| OBJECT\_STYLE\_MATERIAL\_ID\_PARAM | \-1,002,113 | "Object Style Material" |
| OFFSET\_FROM\_REFERENCE\_BASE | \-1,155,252 | "Offset from Reference Base" |
| OFFSETFACES\_SHOW\_SHAPE\_HANDLES | \-1,001,131 | "Show Shape Handles" |
| OPTION\_NAME | \-1,133,602 | "Name" |
| OPTION\_SET\_ID | \-1,133,603 | "Design Option Set Id" |
| OPTION\_SET\_NAME | \-1,133,600 | "Name" |
| ORDINATE\_DIM\_SETTING | \-1,006,468 | "Ordinate Dimension Settings" |
| ORIENT\_BY\_VIEW | \-1,012,200 | "Rotate With Text" |
| ORIGINATING\_ELEMENT\_NAME | \-1,114,833 | "Originating Element" |
| OVAL\_FRAMING\_HEIGHT | \-1,155,250 | "Oval Height" |
| OVAL\_FRAMING\_WIDTH | \-1,155,249 | "Oval Width" |
| PADDING\_LENGTH | \-1,013,366 | "Padding" |
| PANEL\_ID | \-1,140,188 | "Panel" |
| PANEL\_SCHEDULE\_NAME | \-1,140,168 | "Panel Schedule Name" |
| PART\_MAKER\_DIVISION\_PROFILE\_OFFSET | \-1,150,624 | "Profile Offset" |
| PART\_MAKER\_SPLITTER\_PROFILE | \-1,150,603 | "Division Profile" |
| PART\_MAKER\_SPLITTER\_PROFILE\_EDGE\_MATCH | \-1,150,622 | "Edge Match" |
| PART\_MAKER\_SPLITTER\_PROFILE\_FLIP\_ACROSS | \-1,150,604 | "Profile Across Flip" |
| PART\_MAKER\_SPLITTER\_PROFILE\_FLIP\_ALONG | \-1,150,605 | "Profile Along Flip" |
| PARTMAKER\_PARAM\_DIVISION\_GAP | \-1,150,601 | "Gap" |
| PATH\_OF\_TRAVEL\_FROM\_ROOM | \-1,155,202 | "From Room" |
| PATH\_OF\_TRAVEL\_LEVEL\_NAME | \-1,155,093 | "Level" |
| PATH\_OF\_TRAVEL\_SPEED | \-1,155,123 | "Speed" |
| PATH\_OF\_TRAVEL\_TIME | \-1,155,090 | "Time" |
| PATH\_OF\_TRAVEL\_TO\_ROOM | \-1,155,201 | "To Room" |
| PATH\_OF\_TRAVEL\_VIEW\_NAME | \-1,155,094 | "View Name" |
| PATH\_REIN\_ADDL\_OFFSET | \-1,018,322 | "Additional Offset" |
| PATH\_REIN\_ALT\_OFFSET | \-1,018,321 | "Alternating Bar \- Offset" |
| PATH\_REIN\_ALTERNATING | \-1,018,304 | "Alternating Bars" |
| PATH\_REIN\_END\_HOOK\_ORIENT\_1\_SLAB | \-1,018,317 | "Primary Bar \- End Hook Orientation" |
| PATH\_REIN\_END\_HOOK\_ORIENT\_1\_WALL | \-1,018,319 | "Primary Bar \- End Hook Orientation" |
| PATH\_REIN\_END\_HOOK\_ORIENT\_2\_SLAB | \-1,018,318 | "Alternating Bar \- End Hook Orientation" |
| PATH\_REIN\_END\_HOOK\_ORIENT\_2\_WALL | \-1,018,320 | "Alternating Bar \- End Hook Orientation" |
| PATH\_REIN\_END\_HOOK\_TYPE\_1 | \-1,018,315 | "Primary Bar \- End Hook Type" |
| PATH\_REIN\_END\_HOOK\_TYPE\_2 | \-1,018,316 | "Alternating Bar \- End Hook Type" |
| PATH\_REIN\_END\_SPANHOOK\_ALT | \-1,018,356 | "End Hook Angle Alternating" |
| PATH\_REIN\_END\_SPANHOOK\_PRIM | \-1,018,355 | "End Hook Angle Primary" |
| PATH\_REIN\_FACE\_SLAB | \-1,018,300 | "Face" |
| PATH\_REIN\_FACE\_WALL | \-1,018,301 | "Face" |
| PATH\_REIN\_HOOK\_ORIENT\_1\_SLAB | \-1,018,311 | "Primary Bar \- Hook Orientation" |
| PATH\_REIN\_HOOK\_ORIENT\_1\_WALL | \-1,018,313 | "Primary Bar \- Hook Orientation" |
| PATH\_REIN\_HOOK\_ORIENT\_2\_SLAB | \-1,018,312 | "Alternating Bar \- Hook Orientation" |
| PATH\_REIN\_HOOK\_ORIENT\_2\_WALL | \-1,018,314 | "Alternating Bar \- Hook Orientation" |
| PATH\_REIN\_HOOK\_TYPE\_1 | \-1,018,309 | "Primary Bar \- Start Hook Type" |
| PATH\_REIN\_HOOK\_TYPE\_2 | \-1,018,310 | "Alternating Bar \- Start Hook Type" |
| PATH\_REIN\_LENGTH\_1 | \-1,018,307 | "Primary Bar \- Length" |
| PATH\_REIN\_LENGTH\_2 | \-1,018,308 | "Alternating Bar \- Length" |
| PATH\_REIN\_NUMBER\_OF\_BARS | \-1,018,303 | "Number Of Bars" |
| PATH\_REIN\_SHAPE\_1 | \-1,018,361 | "Primary Bar \- Shape" |
| PATH\_REIN\_SHAPE\_2 | \-1,018,362 | "Alternating Bar \- Shape" |
| PATH\_REIN\_SPACING | \-1,018,302 | "Bar Spacing" |
| PATH\_REIN\_SPANHOOK\_ALT | \-1,018,351 | "Start Hook Angle Alternating" |
| PATH\_REIN\_SPANHOOK\_PRIM | \-1,018,350 | "Start Hook Angle Primary" |
| PATH\_REIN\_SPANLENGTH\_ALT\_OFFSET | \-1,018,360 | "Offset" |
| PATH\_REIN\_SPANLENGTH\_BARLENGTH\_ALT | \-1,018,359 | "Length (Alternating Bar)" |
| PATH\_REIN\_SPANLENGTH\_BARLENGTH\_PRIM | \-1,018,358 | "Length (Primary Bar)" |
| PATH\_REIN\_SPANLENGTH\_BOTTOM\_ALT | \-1,018,353 | "Bottom (Alternating Bar)" |
| PATH\_REIN\_SPANLENGTH\_BOTTOM\_PRIM | \-1,018,352 | "Bottom (Primary Bar)" |
| PATH\_REIN\_SPANLENGTH\_TOP\_ALT | \-1,018,357 | "Top (Alternating Bar)" |
| PATH\_REIN\_SUMMARY | \-1,018,354 | "Summary" |
| PATH\_REIN\_TYPE\_1 | \-1,018,305 | "Primary Bar \- Type" |
| PATH\_REIN\_TYPE\_2 | \-1,018,306 | "Alternating Bar \- Type" |
| PATTERN\_INDENT\_1\_FOR\_DIVISION\_RULE | \-1,152,347 | "Indent 1" |
| PATTERN\_INDENT\_2\_FOR\_DIVISION\_RULE | \-1,152,348 | "Indent 2" |
| PATTERN\_MIRROR\_FOR\_DIVISION\_RULE | \-1,152,350 | "Mirror" |
| PEAK\_AIRFLOW\_PARAM | \-1,114,818 | "Peak Airflow" |
| PEAK\_COOLING\_LOAD\_PARAM | \-1,114,801 | "Peak Cooling Load" |
| PEAK\_HEATING\_LOAD\_PARAM | \-1,114,800 | "Peak Heating Load" |
| PEAK\_LATENT\_COOLING\_LOAD | \-1,114,819 | "Peak Latent Cooling Load" |
| PHASE\_CREATED | \-1,012,100 | "Phase Created" |
| PHASE\_DEMOLISHED | \-1,012,101 | "Phase Demolished" |
| PHASE\_NAME | \-1,012,110 | "Name" |
| PHASE\_SEQUENCE\_NUMBER | \-1,012,111 | "Sequence Number" |
| PHY\_MATERIAL\_PARAM\_AVERAGE\_MODULUS | \-1,152,317 | "Average Modulus" |
| PHY\_MATERIAL\_PARAM\_BEHAVIOR | \-1,140,322 | "Behavior" |
| PHY\_MATERIAL\_PARAM\_BENDING | \-1,140,414 | "Bending" |
| PHY\_MATERIAL\_PARAM\_BENDING\_REINFORCEMENT | \-1,140,315 | "Bending reinforcement" |
| PHY\_MATERIAL\_PARAM\_CLASS | \-1,150,464 | "Class" |
| PHY\_MATERIAL\_PARAM\_COMPRESSION\_PARALLEL | \-1,140,407 | "Compression parallel to grain" |
| PHY\_MATERIAL\_PARAM\_COMPRESSION\_PERPENDICULAR | \-1,140,408 | "Compression perpendicular to grain" |
| PHY\_MATERIAL\_PARAM\_CONCRETE\_COMPRESSION | \-1,140,314 | "Concrete compression" |
| PHY\_MATERIAL\_PARAM\_EXP\_COEFF | \-1,140,415 | "Thermal expansion coefficient" |
| PHY\_MATERIAL\_PARAM\_EXP\_COEFF\_1 | \-1,152,306 | "Thermal Expansion Coefficient 1" |
| PHY\_MATERIAL\_PARAM\_EXP\_COEFF\_2 | \-1,152,307 | "Thermal Expansion Coefficient 2" |
| PHY\_MATERIAL\_PARAM\_EXP\_COEFF1 | \-1,140,310 | "Thermal expansion coefficient X" |
| PHY\_MATERIAL\_PARAM\_EXP\_COEFF2 | \-1,140,311 | "Thermal expansion coefficient Y" |
| PHY\_MATERIAL\_PARAM\_EXP\_COEFF3 | \-1,140,312 | "Thermal expansion coefficient Z" |
| PHY\_MATERIAL\_PARAM\_FIVEPERCENT\_MODULUS\_OF\_ELACTICITY | \-1,152,318 | "5% Modulus of Elasticity" |
| PHY\_MATERIAL\_PARAM\_GRADE | \-1,140,417 | "Grade" |
| PHY\_MATERIAL\_PARAM\_LIGHT\_WEIGHT | \-1,140,323 | "Lightweight" |
| PHY\_MATERIAL\_PARAM\_MINIMUM\_TENSILE\_STRENGTH | \-1,140,319 | "Minimum tensile strength" |
| PHY\_MATERIAL\_PARAM\_MINIMUM\_YIELD\_STRESS | \-1,140,318 | "Minimum yield stress" |
| PHY\_MATERIAL\_PARAM\_POISSON\_MOD | \-1,140,412 | "Poisson ratio" |
| PHY\_MATERIAL\_PARAM\_POISSON\_MOD\_12 | \-1,152,303 | "Poisson Ratio 12" |
| PHY\_MATERIAL\_PARAM\_POISSON\_MOD\_23 | \-1,152,304 | "Poisson Ratio 23" |
| PHY\_MATERIAL\_PARAM\_POISSON\_MOD1 | \-1,140,303 | "Poisson ratio X" |
| PHY\_MATERIAL\_PARAM\_POISSON\_MOD2 | \-1,140,304 | "Poisson ratio Y" |
| PHY\_MATERIAL\_PARAM\_POISSON\_MOD3 | \-1,140,305 | "Poisson ratio Z" |
| PHY\_MATERIAL\_PARAM\_REDUCTION\_FACTOR | \-1,140,320 | "Reduction factor for shear" |
| PHY\_MATERIAL\_PARAM\_RESISTANCE\_CALC\_STRENGTH | \-1,140,321 | "Resistance calculation strength" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_MOD | \-1,140,413 | "Shear modulus" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_MOD\_12 | \-1,152,305 | "Shear Modulus 12" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_MOD1 | \-1,140,306 | "Shear modulus X" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_MOD2 | \-1,140,307 | "Shear modulus Y" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_MOD3 | \-1,140,308 | "Shear modulus Z" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_PARALLEL | \-1,140,409 | "Shear parallel to grain" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_PERPENDICULAR | \-1,140,410 | "Shear perpendicular to grain" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_REINFORCEMENT | \-1,140,316 | "Shear reinforcement yield stress" |
| PHY\_MATERIAL\_PARAM\_SHEAR\_STRENGTH\_REDUCTION | \-1,140,317 | "Shear strength modification" |
| PHY\_MATERIAL\_PARAM\_SPECIES | \-1,140,416 | "Species" |
| PHY\_MATERIAL\_PARAM\_STRUCTURAL\_DENSITY | \-1,152,313 | "Density" |
| PHY\_MATERIAL\_PARAM\_STRUCTURAL\_SPECIFIC\_HEAT | \-1,152,312 | "Specific Heat" |
| PHY\_MATERIAL\_PARAM\_STRUCTURAL\_THERMAL\_TREATED | \-1,152,314 | "Thermally Treated" |
| PHY\_MATERIAL\_PARAM\_SUBCLASS | \-1,150,465 | "Subclass" |
| PHY\_MATERIAL\_PARAM\_TENSION\_PARALLEL | \-1,152,315 | "Tension Parallel to Grain" |
| PHY\_MATERIAL\_PARAM\_TENSION\_PERPENDICULAR | \-1,152,316 | "Tension Perpendicular to Grain" |
| PHY\_MATERIAL\_PARAM\_THERMAL\_CONDUCTIVITY | \-1,152,308 | "Thermal Conductivity" |
| PHY\_MATERIAL\_PARAM\_THERMAL\_CONDUCTIVITY\_X | \-1,152,309 | "Thermal Conductivity X" |
| PHY\_MATERIAL\_PARAM\_THERMAL\_CONDUCTIVITY\_Y | \-1,152,310 | "Thermal Conductivity Y" |
| PHY\_MATERIAL\_PARAM\_THERMAL\_CONDUCTIVITY\_Z | \-1,152,311 | "Thermal Conductivity Z" |
| PHY\_MATERIAL\_PARAM\_TYPE | \-1,140,400 | "Material Type" |
| PHY\_MATERIAL\_PARAM\_UNIT\_WEIGHT | \-1,140,309 | "Unit weight" |
| PHY\_MATERIAL\_PARAM\_WOOD\_CONSTRUCTION | \-1,152,319 | "Construction" |
| PHY\_MATERIAL\_PARAM\_YOUNG\_MOD | \-1,140,401 | "Young modulus" |
| PHY\_MATERIAL\_PARAM\_YOUNG\_MOD\_1 | \-1,152,301 | "Young's Modulus 1" |
| PHY\_MATERIAL\_PARAM\_YOUNG\_MOD\_2 | \-1,152,302 | "Young's Modulus 2" |
| PHY\_MATERIAL\_PARAM\_YOUNG\_MOD1 | \-1,140,300 | "Young modulus X" |
| PHY\_MATERIAL\_PARAM\_YOUNG\_MOD2 | \-1,140,301 | "Young modulus Y" |
| PHY\_MATERIAL\_PARAM\_YOUNG\_MOD3 | \-1,140,302 | "Young modulus Z" |
| PHY\_MATERIAL\_PROPERTIES | \-1,150,467 | "Properties" |
| PIPE\_INSULATION\_THICKNESS | \-1,150,437 | "Insulation Thickness" |
| PIPE\_ROUGHNESS | \-1,140,204 | "Roughness" |
| PIPE\_VELOCITY\_PRESSURE | \-1,140,285 | "Velocity Pressure" |
| PIPING\_CONNECTION\_TYPE | \-1,115,973 | "Connection Type" |
| PIPING\_GENDER\_TYPE | \-1,115,974 | "Gender Type" |
| PLACEMENT\_BOTTOM | \-1,166,004 | "Bottom" |
| PLACEMENT\_CENTER\_X | \-1,166,001 | "Center X" |
| PLACEMENT\_CENTER\_Y | \-1,166,002 | "Center Y" |
| PLACEMENT\_LEFT | \-1,166,003 | "Left" |
| PLACEMENT\_PARAMS\_SHOW | \-1,166,000 | "Enable Position Parameters" |
| PLACEMENT\_RIGHT | \-1,166,005 | "Right" |
| PLACEMENT\_TOP | \-1,166,006 | "Top" |
| PLAN\_REGION\_VIEW\_RANGE | \-1,013,103 | "View Range" |
| PLAN\_VIEW\_CUT\_PLANE\_HEIGHT | \-1,005,155 | "Cut Plane Height" |
| PLAN\_VIEW\_LEVEL | \-1,005,166 | "Associated Level" |
| PLAN\_VIEW\_NORTH | \-1,005,168 | "Orientation" |
| PLAN\_VIEW\_RANGE | \-1,005,162 | "View Range" |
| PLAN\_VIEW\_TOP\_CLIP\_HEIGHT | \-1,005,159 | "Top Clip Height" |
| PLAN\_VIEW\_VIEW\_DIR | \-1,008,209 | "View Direction" |
| PLANE\_SELECTION\_PARAM | \-1,123,515 | "Host" |
| PLANE\_SHOW\_PARAM | \-1,123,514 | "Show Host" |
| PLUMBING\_FIXTURES\_CW\_CONNECTION | \-1,010,705 | "CW Connection" |
| PLUMBING\_FIXTURES\_DRAIN | \-1,010,702 | "Drain" |
| PLUMBING\_FIXTURES\_HW\_CONNECTION | \-1,010,704 | "HW Connection" |
| PLUMBING\_FIXTURES\_SUPPLY\_FITTING | \-1,010,700 | "Supply Fitting" |
| PLUMBING\_FIXTURES\_SUPPLY\_PIPE | \-1,010,701 | "Supply Pipe" |
| PLUMBING\_FIXTURES\_TRAP | \-1,010,703 | "Trap" |
| PLUMBING\_FIXTURES\_VENT\_CONNECTION | \-1,010,707 | "Vent Connection" |
| PLUMBING\_FIXTURES\_WASTE\_CONNECTION | \-1,010,706 | "Waste Connection" |
| POCHE\_MAT\_ID | \-1,008,208 | "Coarse Poche Material" |
| POINT\_ADAPTIVE\_CONSTRAINED | \-1,152,332 | "Constrained" |
| POINT\_ADAPTIVE\_NUM\_PARAM | \-1,152,334 | "Number" |
| POINT\_ADAPTIVE\_ORIENTATION\_TYPE | \-1,152,331 | "Orients to" |
| POINT\_ADAPTIVE\_SHOW\_NUMBER | \-1,152,333 | "Show Placement Number" |
| POINT\_ADAPTIVE\_TYPE\_PARAM | \-1,150,155 | "Point" |
| POINT\_ELEMENT\_ANGLE | \-1,150,226 | "Angle" |
| POINT\_ELEMENT\_CHORD\_LENGTH | \-1,150,225 | "Chord Length" |
| POINT\_ELEMENT\_DRIVEN | \-1,150,145 | "Driven by Host" |
| POINT\_ELEMENT\_DRIVING | \-1,150,153 | "Driving Curve(s)" |
| POINT\_ELEMENT\_HOSTED\_ON\_FACE\_U\_PARAM | \-1,150,166 | "Hosted U Parameter" |
| POINT\_ELEMENT\_HOSTED\_ON\_FACE\_V\_PARAM | \-1,150,167 | "Hosted V Parameter" |
| POINT\_ELEMENT\_HOSTED\_PARAM | \-1,150,146 | "Hosted Parameter" |
| POINT\_ELEMENT\_MEASURE\_FROM | \-1,150,227 | "Measure From" |
| POINT\_ELEMENT\_MEASUREMENT\_TYPE | \-1,150,220 | "Measurement Type" |
| POINT\_ELEMENT\_MIRRORED | \-1,150,169 | "Mirrored" |
| POINT\_ELEMENT\_NON\_NORMALIZED\_CURVE\_PARAMATER | \-1,150,221 | "Non\-Normalized Curve Parameter" |
| POINT\_ELEMENT\_NORMALIZED\_CURVE\_PARAMATER | \-1,150,222 | "Normalized Curve Parameter" |
| POINT\_ELEMENT\_NORMALIZED\_SEGMENT\_LENGTH | \-1,150,224 | "Normalized Segment Length" |
| POINT\_ELEMENT\_OFFSET | \-1,150,144 | "Offset" |
| POINT\_ELEMENT\_ROTATION\_ANGLE | \-1,150,322 | "Rotation Angle" |
| POINT\_ELEMENT\_SEGMENT\_LENGTH | \-1,150,223 | "Segment Length" |
| POINT\_ELEMENT\_SHOW\_NORMAL\_PLANE\_ONLY | \-1,150,197 | "Show Normal Reference Plane Only" |
| POINT\_ELEMENT\_SHOW\_PLANES | \-1,150,148 | "Show Reference Planes" |
| POINT\_ELEMENT\_ZFLIPPED | \-1,150,168 | "Flipped" |
| POINT\_ELEVATION | \-1,012,400 | "Elevation" |
| POINT\_FLEXIBLE\_CONSTRAINED | \-1,150,157 | "Constrained" |
| POINT\_FLEXIBLE\_NUM\_PARAM | \-1,150,209 | "Number" |
| POINT\_FLEXIBLE\_ORIENTATION\_TYPE | \-1,150,320 | "Orientation" |
| POINT\_FLEXIBLE\_SHOW\_NUMBER | \-1,150,158 | "Show Placement Number" |
| POINT\_NAME\_PARAM | \-1,150,156 | "Name" |
| POINT\_VISIBILITY\_PARAM | \-1,150,149 | "Visibility/Graphics Overrides" |
| POINTCLOUDINSTANCE\_NAME | \-1,150,600 | "Name": The name of the instance as it will show in the Property Palette |
| POINTCLOUDTYPE\_SCALE | \-1,150,500 | "Scale": The scale for this instance |
| PREFER\_DIM\_SIDE\_UI\_FILTER | \-1,155,242 | "Prefer:": This is used by the UI to allow select prefer dimension side. |
| PREFER\_PATTERN\_ALIGN\_UI\_FILTER | \-1,155,263 | "Pattern:": This is used by the UI to allow to select the preferred preference of aligning pattern. |
| PRIMARY\_OPTION\_ID | \-1,133,601 | "Primary Option Id" |
| PROFILE\_ANGLE | \-1,001,817 | "Angle" |
| PROFILE\_FAM\_TYPE | \-1,001,816 | "Profile" |
| PROFILE\_FAM\_TYPE\_PLUS\_NONE | \-1,001,832 | "Profile" |
| PROFILE\_FLIPPED\_HOR | \-1,001,815 | "Profile Is Flipped" |
| PROFILE\_OFFSET\_X | \-1,001,813 | "Horizontal Profile Offset" |
| PROFILE\_OFFSET\_Y | \-1,001,814 | "Vertical Profile Offset" |
| PROFILE\_PARAM\_ALONG\_PATH | \-1,001,833 | "Parameter along path" |
| PROFILE1\_ANGLE | \-1,001,826 | "Angle" |
| PROFILE1\_FAM\_TYPE | \-1,001,825 | "Profile" |
| PROFILE1\_FLIPPED\_HOR | \-1,001,824 | "Profile Is Flipped" |
| PROFILE1\_OFFSET\_X | \-1,001,822 | "Horizontal Profile Offset" |
| PROFILE1\_OFFSET\_Y | \-1,001,823 | "Vertical Profile Offset" |
| PROFILE2\_ANGLE | \-1,001,831 | "Angle" |
| PROFILE2\_FAM\_TYPE | \-1,001,830 | "Profile" |
| PROFILE2\_FLIPPED\_HOR | \-1,001,829 | "Profile Is Flipped" |
| PROFILE2\_OFFSET\_X | \-1,001,827 | "Horizontal Profile Offset" |
| PROFILE2\_OFFSET\_Y | \-1,001,828 | "Vertical Profile Offset" |
| PROJECT\_ADDRESS | \-1,006,318 | "Project Address" |
| PROJECT\_AUTHOR | \-1,019,005 | "Author" |
| PROJECT\_BUILDING\_NAME | \-1,019,006 | "Building Name" |
| PROJECT\_BUILDING\_TYPE | \-1,114,168 | "Building Type" |
| PROJECT\_ISSUE\_DATE | \-1,006,321 | "Project Issue Date" |
| PROJECT\_NAME | \-1,006,317 | "Project Name" |
| PROJECT\_NUMBER | \-1,006,316 | "Project Number" |
| PROJECT\_ORGANIZATION\_DESCRIPTION | \-1,019,007 | "Organization Description" |
| PROJECT\_ORGANIZATION\_NAME | \-1,019,008 | "Organization Name" |
| PROJECT\_POSTAL\_CODE | \-1,114,169 | "Postal Code" |
| PROJECT\_REVISION\_ENUMERATION | \-1,011,956 | "Numbering" |
| PROJECT\_REVISION\_REVISION\_DATE | \-1,011,953 | "Revision Date" |
| PROJECT\_REVISION\_REVISION\_DESCRIPTION | \-1,011,952 | "Revision Description" |
| PROJECT\_REVISION\_REVISION\_ISSUED | \-1,011,957 | "Issued" |
| PROJECT\_REVISION\_REVISION\_ISSUED\_BY | \-1,011,955 | "Issued by" |
| PROJECT\_REVISION\_REVISION\_ISSUED\_TO | \-1,011,954 | "Issued to" |
| PROJECT\_REVISION\_REVISION\_NUM | \-1,011,951 | "Revision Number" |
| PROJECT\_REVISION\_SEQUENCE\_NUM | \-1,011,950 | "Revision Sequence": read\_only Make this read\-only again when NewSchedules\_DisplayTags is cleaned up |
| PROJECT\_STATUS | \-1,006,320 | "Project Status" |
| PROJECTED\_SURFACE\_AREA | \-1,012,610 | "Projected Area" |
| PROJECTION\_TYPE | \-1,523,514 | "Projection Type" |
| PROPERTY\_AREA | \-1,012,600 | "Area" |
| PROPERTY\_AREA\_OPEN | \-1,012,606 | "Area" |
| PROPERTY\_AREA\_UNITS | \-1,012,612 | "Area Units, Format" |
| PROPERTY\_LENGTH\_UNITS | \-1,012,613 | "Units Format" |
| PROPERTY\_SEGMENT\_BEARING | \-1,012,616 | "Bearing" |
| PROPERTY\_SEGMENT\_DISTANCE | \-1,012,614 | "Distance" |
| PROPERTY\_SEGMENT\_E\_W | \-1,012,617 | "E/W" |
| PROPERTY\_SEGMENT\_L\_R | \-1,012,619 | "L/R" |
| PROPERTY\_SEGMENT\_N\_S | \-1,012,615 | "N/S" |
| PROPERTY\_SEGMENT\_RADIUS | \-1,012,618 | "Radius" |
| PROPERTY\_SEGMENT\_SUBCATEGORY\_ID | \-1,012,620 | "Subcategory" |
| PROPERTY\_SET\_DESCRIPTION | \-1,150,481 | "Description" |
| PROPERTY\_SET\_KEYWORDS | \-1,152,342 | "Keywords" |
| PROPERTY\_SET\_MATERIAL\_ASPECT | \-1,150,480 | "Material aspect" |
| PROPERTY\_SET\_NAME | \-1,150,466 | "Property Set Name" |
| PROPERTY\_SUBCATEGORY\_ID | \-1,012,607 | "Subcategory" |
| RADIAL\_ARRAY\_ARC\_RADIUS | \-1,004,014 | "Radius" |
| RADIUS\_SYMBOL\_LOCATION | \-1,006,408 | "Radius Symbol Location" |
| RADIUS\_SYMBOL\_TEXT | \-1,006,997 | "Radius Symbol Text" |
| RAILING\_SYSTEM\_HANDRAILS\_HEIGHT\_PARAM | \-1,150,331 | "Height" |
| RAILING\_SYSTEM\_HANDRAILS\_LATTERAL\_OFFSET | \-1,150,332 | "Lateral Offset" |
| RAILING\_SYSTEM\_HANDRAILS\_POSITION\_PARAM | \-1,150,330 | "Position" |
| RAILING\_SYSTEM\_HANDRAILS\_TYPES\_PARAM | \-1,150,329 | "Type" |
| RAILING\_SYSTEM\_HAS\_TOP\_RAIL | \-1,150,380 | "Use Top Rail": Whether railing has top rail |
| RAILING\_SYSTEM\_SECONDARY\_HANDRAILS\_HEIGHT\_PARAM | \-1,150,335 | "Height" |
| RAILING\_SYSTEM\_SECONDARY\_HANDRAILS\_LATTERAL\_OFFSET | \-1,150,336 | "Lateral Offset" |
| RAILING\_SYSTEM\_SECONDARY\_HANDRAILS\_POSITION\_PARAM | \-1,150,334 | "Position" |
| RAILING\_SYSTEM\_SECONDARY\_HANDRAILS\_TYPES\_PARAM | \-1,150,333 | "Type" |
| RAILING\_SYSTEM\_TOP\_RAIL\_HEIGHT\_PARAM | \-1,150,328 | "Height" |
| RAILING\_SYSTEM\_TOP\_RAIL\_TYPES\_PARAM | \-1,150,327 | "Type" |
| RAMP\_ATTR\_LEFT\_BALUSTER\_ATTACH\_PT | \-1,008,306 | "Left Baluster Location" |
| RAMP\_ATTR\_MATERIAL | \-1,008,308 | "Ramp Material" |
| RAMP\_ATTR\_MIN\_INV\_SLOPE | \-1,008,301 | "Ramp Max Slope (1/x)" |
| RAMP\_ATTR\_RIGHT\_BALUSTER\_ATTACH\_PT | \-1,008,307 | "Right Baluster Location" |
| RAMP\_ATTR\_SHAPE | \-1,008,305 | "Shape" |
| RAMP\_ATTR\_TEXT\_FONT | \-1,008,309 | "Text Font" |
| RAMP\_ATTR\_TEXT\_SIZE | \-1,008,310 | "Text Size" |
| RAMP\_ATTR\_THICKNESS | \-1,008,304 | "Thickness" |
| RAMP\_MAX\_RUN\_LENGTH | \-1,008,303 | "Maximum Incline Length" |
| RASTER\_ENABLE\_SNAPS | \-1,007,770 | "Enable Snaps" |
| RASTER\_HORIZONTAL\_SCALE | \-1,007,768 | "Horizontal Scale" |
| RASTER\_LOCK\_PROPORTIONS | \-1,007,752 | "Lock Proportions" |
| RASTER\_SHEETHEIGHT | \-1,007,751 | "Height" |
| RASTER\_SHEETWIDTH | \-1,007,750 | "Width" |
| RASTER\_SYMBOL\_FILENAME | \-1,007,763 | "Loaded from file" |
| RASTER\_SYMBOL\_HEIGHT | \-1,007,766 | "Height" |
| RASTER\_SYMBOL\_LINKLOAD\_STATUS | \-1,007,771 | "Link Status" |
| RASTER\_SYMBOL\_PAGENUMBER | \-1,007,769 | "Page Number" |
| RASTER\_SYMBOL\_PIXELHEIGHT | \-1,007,761 | "Height (pixels)" |
| RASTER\_SYMBOL\_PIXELWIDTH | \-1,007,760 | "Width (pixels)" |
| RASTER\_SYMBOL\_RESOLUTION | \-1,007,764 | "Resolution (dpi)" |
| RASTER\_SYMBOL\_VIEWNAME | \-1,007,762 | "View Name" |
| RASTER\_SYMBOL\_WIDTH | \-1,007,765 | "Width" |
| RASTER\_VERTICAL\_SCALE | \-1,007,767 | "Vertical Scale" |
| RBS\_ADDITIONAL\_FLOW | \-1,114,166 | "Additional Flow" |
| RBS\_ADJUSTABLE\_CONNECTOR | \-1,140,223 | "Allow Slope Adjustments" |
| RBS\_AREA\_BASED\_LOAD\_TYPE | \-1,153,533 | "Area Based Load Type" |
| RBS\_BUILDING\_CONSTRUCTIONCLASS | \-1,150,160 | "Building Infiltration Class" |
| RBS\_BUILDING\_USELOADCREDITS | \-1,150,203 | "Use Load Credits" |
| RBS\_CABLETRAY\_BENDRADIUS | \-1,140,115 | "Bend Radius" |
| RBS\_CABLETRAY\_HEIGHT\_PARAM | \-1,140,121 | "Height" |
| RBS\_CABLETRAY\_RUNGHEIGHT | \-1,140,114 | "Rung Height" |
| RBS\_CABLETRAY\_RUNGSPACE | \-1,140,112 | "Rung Space" |
| RBS\_CABLETRAY\_RUNGWIDTH | \-1,140,113 | "Rung Width" |
| RBS\_CABLETRAY\_SHAPETYPE | \-1,140,130 | "Shape" |
| RBS\_CABLETRAY\_THICKNESS | \-1,140,111 | "Thickness" |
| RBS\_CABLETRAY\_WIDTH\_PARAM | \-1,140,122 | "Width" |
| RBS\_CABLETRAYCONDUIT\_BENDORFITTING | \-1,140,129 | "Bend or Fitting" |
| RBS\_CABLETRAYCONDUIT\_CONNECTORELEM\_TYPE | \-1,133,414 | "Connector Type" |
| RBS\_CABLETRAYCONDUIT\_SYSTEM\_TYPE | \-1,133,413 | "System Type" |
| RBS\_CABLETRAYCONDUITRUN\_LENGTH\_PARAM | \-1,140,132 | "Length" |
| RBS\_CABLETRAYRUN\_HEIGHT\_PARAM | \-1,140,133 | "Height" |
| RBS\_CABLETRAYRUN\_WIDTH\_PARAM | \-1,140,134 | "Width" |
| RBS\_CALCULATED\_SIZE | \-1,114,240 | "Size" |
| RBS\_COMPONENT\_CLASSIFICATION\_PARAM | \-1,150,412 | "Component Classification" |
| RBS\_CONDUIT\_BENDRADIUS | \-1,140,116 | "Bend Radius" |
| RBS\_CONDUIT\_DIAMETER\_PARAM | \-1,140,123 | "Diameter(Trade Size)" |
| RBS\_CONDUIT\_INNER\_DIAM\_PARAM | \-1,140,126 | "Inside Diameter" |
| RBS\_CONDUIT\_OUTER\_DIAM\_PARAM | \-1,140,127 | "Outside Diameter" |
| RBS\_CONDUIT\_TRADESIZE | \-1,140,117 | "Conduit Size Lookup" |
| RBS\_CONDUITRUN\_DIAMETER\_PARAM | \-1,140,135 | "Diameter(Trade Size)" |
| RBS\_CONDUITRUN\_INNER\_DIAM\_PARAM | \-1,140,136 | "Inside Diameter" |
| RBS\_CONDUITRUN\_OUTER\_DIAM\_PARAM | \-1,140,137 | "Outside Diameter" |
| RBS\_CONNECTOR\_DESCRIPTION | \-1,140,000 | "Connector Description" |
| RBS\_CONNECTOR\_ISPRIMARY | \-1,133,412 | "Primary Connector" |
| RBS\_CONNECTOR\_OFFSET\_OBSOLETE | \-1,114,237 | "Connector Offset" |
| RBS\_CONSTRUCTION\_SET\_PARAM | \-1,114,249 | "Schematic Types" |
| RBS\_CONSTRUCTION\_TYPE\_SHADINGFACTOR\_PARAM | \-1,114,295 | "Internal Shading Factor" |
| RBS\_CTC\_BOTTOM\_ELEVATION | \-1,140,125 | "Lower End Bottom Elevation" |
| RBS\_CTC\_SERVICE\_TYPE | \-1,140,128 | "Service Type" |
| RBS\_CTC\_TOP\_ELEVATION | \-1,140,124 | "Upper End Top Elevation" |
| RBS\_CURVE\_DIAMETER\_PARAM | \-1,114,103 | "Diameter" |
| RBS\_CURVE\_HEIGHT\_PARAM | \-1,114,102 | "Height" |
| RBS\_CURVE\_HOR\_OFFSET\_PARAM | \-1,114,105 | "Horizontal Justification" |
| RBS\_CURVE\_SLOPE | \-1,140,224 | "Slope Percentage (%)" |
| RBS\_CURVE\_SURFACE\_AREA | \-1,114,120 | "Area" |
| RBS\_CURVE\_UTSLOPE | \-1,140,254 | "Slope" |
| RBS\_CURVE\_VERT\_OFFSET\_PARAM | \-1,114,106 | "Vertical Justification" |
| RBS\_CURVE\_WIDTH\_PARAM | \-1,114,101 | "Width" |
| RBS\_CURVETYPE\_DEFAULT\_BEND\_PARAM | \-1,114,394 | "Bend" |
| RBS\_CURVETYPE\_DEFAULT\_CAP\_PARAM | \-1,114,148 | "Cap" |
| RBS\_CURVETYPE\_DEFAULT\_CROSS\_PARAM | \-1,114,112 | "Cross" |
| RBS\_CURVETYPE\_DEFAULT\_ELBOW\_PARAM | \-1,114,110 | "Elbow" |
| RBS\_CURVETYPE\_DEFAULT\_ELBOWDOWN\_PARAM | \-1,114,388 | "Vertical Outside Bend" |
| RBS\_CURVETYPE\_DEFAULT\_ELBOWUP\_PARAM | \-1,114,387 | "Vertical Inside Bend" |
| RBS\_CURVETYPE\_DEFAULT\_HORIZONTAL\_BEND\_PARAM | \-1,114,393 | "Horizontal Bend" |
| RBS\_CURVETYPE\_DEFAULT\_MECHJOINT\_PARAM | \-1,114,145 | "Flange" |
| RBS\_CURVETYPE\_DEFAULT\_TAKEOFF\_PARAM | \-1,114,133 | "Tap" |
| RBS\_CURVETYPE\_DEFAULT\_TEE\_PARAM | \-1,114,111 | "Tee" |
| RBS\_CURVETYPE\_DEFAULT\_TEEDOWN\_PARAM | \-1,114,390 | "Tee Down" |
| RBS\_CURVETYPE\_DEFAULT\_TEEUP\_PARAM | \-1,114,389 | "Tee Up" |
| RBS\_CURVETYPE\_DEFAULT\_TRANSITION\_PARAM | \-1,114,113 | "Transition" |
| RBS\_CURVETYPE\_DEFAULT\_UNION\_PARAM | \-1,114,131 | "Union" |
| RBS\_CURVETYPE\_MAX\_HEIGHT\_PARAM | \-1,114,119 | "Max Height" |
| RBS\_CURVETYPE\_MAX\_WIDTH\_PARAM | \-1,114,165 | "Max Width" |
| RBS\_CURVETYPE\_MULTISHAPE\_TRANSITION\_OVALROUND\_PARAM | \-1,114,392 | "Multi Shape Transition Oval to Round" |
| RBS\_CURVETYPE\_MULTISHAPE\_TRANSITION\_PARAM | \-1,114,126 | "Multi Shape Transition Rect to Round" |
| RBS\_CURVETYPE\_MULTISHAPE\_TRANSITION\_RECTOVAL\_PARAM | \-1,114,391 | "Multi Shape Transition Rect to Oval" |
| RBS\_CURVETYPE\_PREFERRED\_BRANCH\_PARAM | \-1,114,134 | "Preferred Junction Type" |
| RBS\_DISTRIBUTIONSYS\_CONFIG\_PARAM | \-1,140,060 | "Configuration" |
| RBS\_DISTRIBUTIONSYS\_HL\_PHASE\_PARAM | \-1,141,050 | "High\-leg Phase" |
| RBS\_DISTRIBUTIONSYS\_NUMWIRES\_PARAM | \-1,140,059 | "Wires" |
| RBS\_DISTRIBUTIONSYS\_PHASE\_PARAM | \-1,140,061 | "Phase" |
| RBS\_DISTRIBUTIONSYS\_VLG\_PARAM | \-1,140,062 | "Line to Ground Voltage" |
| RBS\_DISTRIBUTIONSYS\_VLL\_PARAM | \-1,140,063 | "Line to Line Voltage" |
| RBS\_DUCT\_BOTTOM\_ELEVATION | \-1,140,240 | "Lower End Bottom Elevation" |
| RBS\_DUCT\_CALCULATED\_SIZE | \-1,150,426 | "Duct Size" |
| RBS\_DUCT\_CONNECTOR\_SYSTEM\_CLASSIFICATION\_PARAM | \-1,133,408 | "System Classification" |
| RBS\_DUCT\_FITTING\_LOSS\_METHOD\_PARAM | \-1,114,136 | "Loss Method" |
| RBS\_DUCT\_FITTING\_LOSS\_METHOD\_SERVER\_PARAM | \-1,114,146 | "Loss Method" |
| RBS\_DUCT\_FITTING\_LOSS\_METHOD\_SETTINGS | \-1,114,149 | "Loss Method Settings" |
| RBS\_DUCT\_FITTING\_LOSS\_TABLE\_PARAM | \-1,114,137 | "ASHRAE Table" |
| RBS\_DUCT\_FLOW\_CONFIGURATION\_PARAM | \-1,140,221 | "Flow Configuration" |
| RBS\_DUCT\_FLOW\_DIRECTION\_PARAM | \-1,140,219 | "Flow Direction" |
| RBS\_DUCT\_FLOW\_PARAM | \-1,013,405 | "Flow" |
| RBS\_DUCT\_PIPE\_SYSTEM\_ABBREVIATION\_PARAM | \-1,150,468 | "System Abbreviation" |
| RBS\_DUCT\_PRESSURE\_DROP | \-1,140,282 | "Pressure Drop" |
| RBS\_DUCT\_ROUTING\_PREFERENCE\_PARAM | \-1,140,280 | "Routing Preferences" |
| RBS\_DUCT\_SIZE\_FORMATTED\_PARAM | \-1,114,143 | "Size" |
| RBS\_DUCT\_SLOPE | \-1,140,255 | "Slope" |
| RBS\_DUCT\_STATIC\_PRESSURE | \-1,114,142 | "Static Pressure" |
| RBS\_DUCT\_SYSTEM\_CALCULATION\_PARAM | \-1,140,336 | "Calculations" |
| RBS\_DUCT\_SYSTEM\_TYPE\_PARAM | \-1,140,333 | "System Type" |
| RBS\_DUCT\_TOP\_ELEVATION | \-1,140,239 | "Upper End Top Elevation" |
| RBS\_DUCT\_TYPE\_PARAM | \-1,114,138 | "Duct Type" |
| RBS\_ELEC\_AMBIENT\_TEMPERATURE | \-1,140,020 | "Ambient Temperature" |
| RBS\_ELEC\_ANALYTICAL\_AREA | \-1,153,551 | "Area" |
| RBS\_ELEC\_ANALYTICAL\_CONNECTED\_PHASE | \-1,153,553 | "Connected Phases" |
| RBS\_ELEC\_ANALYTICAL\_DOWNSTREAM\_CONNECTED\_PHASES | \-1,153,556 | "Downstream Connected Phases" |
| RBS\_ELEC\_ANALYTICAL\_FEEDER\_LENGTH | \-1,153,545 | "Length" |
| RBS\_ELEC\_ANALYTICAL\_HIGH\_LEG\_PHASE | \-1,153,554 | "High\-leg Phase" |
| RBS\_ELEC\_ANALYTICAL\_LEVEL\_ID | \-1,153,544 | "Level" |
| RBS\_ELEC\_ANALYTICAL\_LOAD\_DENSITY | \-1,153,532 | "Power Density" |
| RBS\_ELEC\_ANALYTICAL\_LOAD\_NAME\_PARAM | \-1,153,537 | "Name" |
| RBS\_ELEC\_ANALYTICAL\_LOAD\_SET\_ON\_DUTY | \-1,153,548 | "Quantity of Prime" |
| RBS\_ELEC\_ANALYTICAL\_LOAD\_SET\_ON\_STANDBY | \-1,153,549 | "Quantity on Standby" |
| RBS\_ELEC\_ANALYTICAL\_LOAD\_SET\_ON\_TOTAL | \-1,153,538 | "Total Quantity" |
| RBS\_ELEC\_ANALYTICAL\_LOAD\_TYPE\_PARAM | \-1,153,535 | "Load Type" |
| RBS\_ELEC\_ANALYTICAL\_LOADS\_IN\_SET | \-1,153,550 | "Loads in Set" |
| RBS\_ELEC\_ANALYTICAL\_NUMPHASES | \-1,153,552 | "Number of Phases" |
| RBS\_ELEC\_ANALYTICAL\_SECONDARY\_HIGH\_LEG\_PHASE | \-1,153,555 | "Secondary High\-leg Phase" |
| RBS\_ELEC\_ANALYTICAL\_TOTAL\_COINCIDENT\_LOAD | \-1,155,151 | "Total Coincident Loads" |
| RBS\_ELEC\_APPARENT\_CURRENT\_PARAM | \-1,140,045 | "Apparent Current" |
| RBS\_ELEC\_APPARENT\_CURRENT\_PHASEA\_PARAM | \-1,140,044 | "Apparent Current Phase A" |
| RBS\_ELEC\_APPARENT\_CURRENT\_PHASEB\_PARAM | \-1,140,043 | "Apparent Current Phase B" |
| RBS\_ELEC\_APPARENT\_CURRENT\_PHASEC\_PARAM | \-1,140,042 | "Apparent Current Phase C" |
| RBS\_ELEC\_APPARENT\_LOAD | \-1,140,004 | "Apparent Power" |
| RBS\_ELEC\_APPARENT\_LOAD\_PHASE1 | \-1,140,005 | "Apparent Power Phase 1" |
| RBS\_ELEC\_APPARENT\_LOAD\_PHASE2 | \-1,140,006 | "Apparent Power Phase 2" |
| RBS\_ELEC\_APPARENT\_LOAD\_PHASE3 | \-1,140,007 | "Apparent Power Phase 3" |
| RBS\_ELEC\_APPARENT\_LOAD\_PHASEA | \-1,140,053 | "Apparent Power Phase A" |
| RBS\_ELEC\_APPARENT\_LOAD\_PHASEB | \-1,140,054 | "Apparent Power Phase B" |
| RBS\_ELEC\_APPARENT\_LOAD\_PHASEC | \-1,140,055 | "Apparent Power Phase C" |
| RBS\_ELEC\_APPARENT\_POWER\_DENSITY | \-1,153,543 | "Apparent Power Density" |
| RBS\_ELEC\_BALANCED\_LOAD | \-1,140,003 | "Balanced Load" |
| RBS\_ELEC\_CALC\_COEFFICIENT\_UTILIZATION | \-1,140,040 | "Calculate Coefficient of Utilization" |
| RBS\_ELEC\_CIRCUIT\_CABLE\_SIZE\_PARAM | \-1,141,052 | "Cable Size" |
| RBS\_ELEC\_CIRCUIT\_CABLE\_TYPE\_PARAM | \-1,141,051 | "Cable Type" |
| RBS\_ELEC\_CIRCUIT\_CONNECTION\_TYPE\_PARAM | \-1,140,176 | "Connection Type" |
| RBS\_ELEC\_CIRCUIT\_CORE\_TYPE\_PARAM | \-1,141,057 | "Core Type" |
| RBS\_ELEC\_CIRCUIT\_FRAME\_PARAM | \-1,140,154 | "Frame" |
| RBS\_ELEC\_CIRCUIT\_GROUND\_CONDUCTOR\_SIZE\_PARAM | \-1,141,055 | "Size of Ground Conductor" |
| RBS\_ELEC\_CIRCUIT\_HOT\_CONDUCTOR\_SIZE\_PARAM | \-1,141,053 | "Size of Hot Conductor" |
| RBS\_ELEC\_CIRCUIT\_LENGTH\_PARAM | \-1,140,039 | "Length" |
| RBS\_ELEC\_CIRCUIT\_NAME | \-1,140,089 | "Load Name" |
| RBS\_ELEC\_CIRCUIT\_NAMING | \-1,140,087 | "Circuit Naming" |
| RBS\_ELEC\_CIRCUIT\_NAMING\_INDEX | \-1,140,177 | "Circuit Naming Index" |
| RBS\_ELEC\_CIRCUIT\_NEUTRAL\_CONDUCTOR\_SIZE\_PARAM | \-1,141,054 | "Size of Neutral Conductor" |
| RBS\_ELEC\_CIRCUIT\_NOTES\_PARAM | \-1,140,156 | "Schedule Circuit Notes" |
| RBS\_ELEC\_CIRCUIT\_NUMBER | \-1,140,103 | "Circuit Number" |
| RBS\_ELEC\_CIRCUIT\_NUMBER\_OF\_ELEMENTS\_PARAM | \-1,140,155 | "Number of Elements" |
| RBS\_ELEC\_CIRCUIT\_NUMBERING\_TYPE | \-1,155,099 | "Circuit Numbering Option" |
| RBS\_ELEC\_CIRCUIT\_OTHER\_CONDUCTOR\_SIZE\_PARAM | \-1,141,056 | "Size of Other Conductor" |
| RBS\_ELEC\_CIRCUIT\_PANEL\_PARAM | \-1,140,104 | "Panel" |
| RBS\_ELEC\_CIRCUIT\_PATH\_MODE\_PARAM | \-1,140,174 | "Path Mode" |
| RBS\_ELEC\_CIRCUIT\_PATH\_OFFSET\_PARAM | \-1,140,175 | "Offset" |
| RBS\_ELEC\_CIRCUIT\_PREFIX | \-1,140,085 | "Circuit Prefix" |
| RBS\_ELEC\_CIRCUIT\_PREFIX\_SEPARATOR | \-1,140,086 | "Circuit Prefix Separator" |
| RBS\_ELEC\_CIRCUIT\_RATING\_PARAM | \-1,140,038 | "Rating" |
| RBS\_ELEC\_CIRCUIT\_SLOT\_INDEX | \-1,140,181 | "Slot Index" |
| RBS\_ELEC\_CIRCUIT\_START\_SLOT | \-1,140,173 | "Start Slot" |
| RBS\_ELEC\_CIRCUIT\_STATE | \-1,140,189 | "Circuit State" |
| RBS\_ELEC\_CIRCUIT\_TYPE | \-1,140,018 | "System Type" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_NUM\_GROUNDS\_PARAM | \-1,140,098 | "\# of Ground Conductors" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_NUM\_HOTS\_PARAM | \-1,140,100 | "\# of Hot Conductors" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_NUM\_NEUTRALS\_PARAM | \-1,140,099 | "\# of Neutral Conductors" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_NUM\_OTHERS\_PARAM | \-1,140,190 | "\# of Other Conductors" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_NUM\_RUNS\_PARAM | \-1,140,101 | "\# of Runs" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_SIZE\_PARAM | \-1,140,037 | "Wire Size" |
| RBS\_ELEC\_CIRCUIT\_WIRE\_TYPE\_PARAM | \-1,140,036 | "Wire Type" |
| RBS\_ELEC\_DEMAND\_CURRENT\_PHASEA | \-1,140,185 | "Demand Current Phase A" |
| RBS\_ELEC\_DEMAND\_CURRENT\_PHASEB | \-1,140,186 | "Demand Current Phase B" |
| RBS\_ELEC\_DEMAND\_CURRENT\_PHASEC | \-1,140,187 | "Demand Current Phase C" |
| RBS\_ELEC\_DEMAND\_LOAD\_PHASEA | \-1,140,182 | "Demand Apparent Power Phase A" |
| RBS\_ELEC\_DEMAND\_LOAD\_PHASEB | \-1,140,183 | "Demand Apparent Power Phase B" |
| RBS\_ELEC\_DEMAND\_LOAD\_PHASEC | \-1,140,184 | "Demand Apparent Power Phase C" |
| RBS\_ELEC\_DEMANDFACTOR\_DEMANDLOAD\_PARAM | \-1,140,065 | "Demand Apparent Power" |
| RBS\_ELEC\_DEMANDFACTOR\_LOAD\_PARAM | \-1,140,066 | "Connected Apparent Power" |
| RBS\_ELEC\_DEMANDFACTOR\_LOADCLASSIFICATION\_PARAM | \-1,140,067 | "Load Classification" |
| RBS\_ELEC\_DISTRIBUTION\_NODE\_LOAD\_SET | \-1,153,547 | "Load Set" |
| RBS\_ELEC\_DISTRIBUTION\_NODE\_SUPPLY\_FROM | \-1,153,541 | "Supply From" |
| RBS\_ELEC\_DISTRIBUTION\_NODE\_SUPPLY\_FROM1 | \-1,153,539 | "Supply From 1" |
| RBS\_ELEC\_DISTRIBUTION\_NODE\_SUPPLY\_FROM2 | \-1,153,542 | "Supply From 2" |
| RBS\_ELEC\_DISTRIBUTION\_NODE\_SUPPLY\_TO | \-1,153,546 | "Supply To" |
| RBS\_ELEC\_EDIT\_CIRCUIT\_NAMING\_SETTINGS\_PARAM | \-1,155,145 | "Circuit Naming Settings" |
| RBS\_ELEC\_ENCLOSURE | \-1,140,083 | "Enclosure" |
| RBS\_ELEC\_LOAD\_CLASSIFICATION | \-1,140,014 | "Load Classification" |
| RBS\_ELEC\_LOADSUMMARY\_CONNECTED\_CURRENT\_PARAM | \-1,140,161 | "Connected Current" |
| RBS\_ELEC\_LOADSUMMARY\_CONNECTED\_LOAD\_PARAM | \-1,140,158 | "Connected Apparent Power" |
| RBS\_ELEC\_LOADSUMMARY\_DEMAND\_CURRENT\_PARAM | \-1,140,162 | "Estimated Demand Current" |
| RBS\_ELEC\_LOADSUMMARY\_DEMAND\_FACTOR\_PARAM | \-1,140,159 | "Demand Factor" |
| RBS\_ELEC\_LOADSUMMARY\_DEMAND\_FACTOR\_RULE\_PARAM | \-1,140,163 | "Description" |
| RBS\_ELEC\_LOADSUMMARY\_DEMAND\_LOAD\_PARAM | \-1,140,160 | "Demand Apparent Power" |
| RBS\_ELEC\_LOADSUMMARY\_LOADCLASSIFICATION\_PARAM | \-1,140,157 | "Load Classification" |
| RBS\_ELEC\_MAINS | \-1,140,082 | "Mains" |
| RBS\_ELEC\_MAX\_CIRCUITS\_DATA\_PANEL | \-1,155,152 | "Maximum Amount of Circuits" |
| RBS\_ELEC\_MAX\_POLE\_BREAKERS | \-1,140,079 | "Max Number of Single Pole Breakers" |
| RBS\_ELEC\_MODIFICATIONS | \-1,140,084 | "Modifications" |
| RBS\_ELEC\_MOUNTING | \-1,140,081 | "Mounting" |
| RBS\_ELEC\_NUMBER\_OF\_CIRCUITS | \-1,155,150 | "Max Number of Circuits" |
| RBS\_ELEC\_NUMBER\_OF\_POLES | \-1,140,001 | "Number of Poles" |
| RBS\_ELEC\_PANEL\_BRANCH\_CIRCUIT\_APPARENT\_LOAD\_PHASEA | \-1,155,102 | "Branch Circuit Apparent Power Phase A" |
| RBS\_ELEC\_PANEL\_BRANCH\_CIRCUIT\_APPARENT\_LOAD\_PHASEB | \-1,155,103 | "Branch Circuit Apparent Power Phase B" |
| RBS\_ELEC\_PANEL\_BRANCH\_CIRCUIT\_APPARENT\_LOAD\_PHASEC | \-1,155,104 | "Branch Circuit Apparent Power Phase C" |
| RBS\_ELEC\_PANEL\_BRANCH\_CIRCUIT\_CURRENT\_PHASEA | \-1,155,105 | "Branch Circuit Current Phase A" |
| RBS\_ELEC\_PANEL\_BRANCH\_CIRCUIT\_CURRENT\_PHASEB | \-1,155,106 | "Branch Circuit Current Phase B" |
| RBS\_ELEC\_PANEL\_BRANCH\_CIRCUIT\_CURRENT\_PHASEC | \-1,155,107 | "Branch Circuit Current Phase C" |
| RBS\_ELEC\_PANEL\_BUSSING\_PARAM | \-1,140,143 | "Bussing" |
| RBS\_ELEC\_PANEL\_CONFIGURATION\_PARAM | \-1,140,170 | "Panel Configuration" |
| RBS\_ELEC\_PANEL\_CURRENT\_PHASEA\_PARAM | \-1,140,164 | "Current Phase A" |
| RBS\_ELEC\_PANEL\_CURRENT\_PHASEB\_PARAM | \-1,140,165 | "Current Phase B" |
| RBS\_ELEC\_PANEL\_CURRENT\_PHASEC\_PARAM | \-1,140,166 | "Current Phase C" |
| RBS\_ELEC\_PANEL\_FEED\_PARAM | \-1,140,138 | "Feed" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_APPARENT\_LOAD\_PHASEA | \-1,155,108 | "Feed Through Lugs Apparent Power Phase A" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_APPARENT\_LOAD\_PHASEB | \-1,155,109 | "Feed Through Lugs Apparent Power Phase B" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_APPARENT\_LOAD\_PHASEC | \-1,155,110 | "Feed Through Lugs Apparent Power Phase C" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_CURRENT\_PHASEA | \-1,155,111 | "Feed Through Lugs Current Phase A" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_CURRENT\_PHASEB | \-1,155,112 | "Feed Through Lugs Current Phase B" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_CURRENT\_PHASEC | \-1,155,113 | "Feed Through Lugs Current Phase C" |
| RBS\_ELEC\_PANEL\_FEED\_THRU\_LUGS\_PARAM | \-1,155,100 | "Feed Through Lugs" |
| RBS\_ELEC\_PANEL\_GROUND\_BUS\_PARAM | \-1,140,144 | "Ground Bus" |
| RBS\_ELEC\_PANEL\_LOCATION\_PARAM | \-1,140,169 | "Location" |
| RBS\_ELEC\_PANEL\_MAINSTYPE\_PARAM | \-1,140,139 | "Mains Type" |
| RBS\_ELEC\_PANEL\_MCB\_RATING\_PARAM | \-1,140,140 | "MCB Rating" |
| RBS\_ELEC\_PANEL\_NAME | \-1,140,078 | "Panel Name" |
| RBS\_ELEC\_PANEL\_NEUTRAL\_BUS\_PARAM | \-1,140,145 | "Neutral Bus" |
| RBS\_ELEC\_PANEL\_NEUTRAL\_RATING\_PARAM | \-1,140,146 | "Neutral Rating" |
| RBS\_ELEC\_PANEL\_NUMPHASES\_PARAM | \-1,140,147 | "Number of Phases" |
| RBS\_ELEC\_PANEL\_NUMWIRES\_PARAM | \-1,140,148 | "Number of Wires" |
| RBS\_ELEC\_PANEL\_SCHEDULE\_FOOTER\_NOTES\_PARAM | \-1,140,150 | "Schedule Footer Notes" |
| RBS\_ELEC\_PANEL\_SCHEDULE\_HEADER\_NOTES\_PARAM | \-1,140,149 | "Schedule Header Notes" |
| RBS\_ELEC\_PANEL\_SUBFEED\_LUGS\_PARAM | \-1,140,142 | "SubFeed Lugs" |
| RBS\_ELEC\_PANEL\_SUPPLY\_FROM\_PARAM | \-1,140,141 | "Supply From" |
| RBS\_ELEC\_PANEL\_TOTAL\_CONNECTED\_CURRENT\_PARAM | \-1,140,152 | "Total Connected Current" |
| RBS\_ELEC\_PANEL\_TOTAL\_DEMAND\_CURRENT\_PARAM | \-1,140,153 | "Total Estimated Demand Current" |
| RBS\_ELEC\_PANEL\_TOTAL\_DEMAND\_FACTOR\_PARAM | \-1,140,151 | "Total Demand Factor" |
| RBS\_ELEC\_PANEL\_TOTALESTLOAD\_HVAC\_PARAM | \-1,140,077 | "HVAC Total Demand Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALESTLOAD\_LIGHT\_PARAM | \-1,140,075 | "Lighting Total Demand Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALESTLOAD\_OTHER\_PARAM | \-1,140,071 | "Other Total Demand Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALESTLOAD\_PARAM | \-1,140,069 | "Total Demand Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALESTLOAD\_POWER\_PARAM | \-1,140,073 | "Power Total Demand Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALLOAD\_HVAC\_PARAM | \-1,140,076 | "HVAC Total Connected Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALLOAD\_LIGHT\_PARAM | \-1,140,074 | "Lighting Total Connected Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALLOAD\_OTHER\_PARAM | \-1,140,070 | "Other Total Connected Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALLOAD\_PARAM | \-1,140,068 | "Total Connected Apparent Power" |
| RBS\_ELEC\_PANEL\_TOTALLOAD\_POWER\_PARAM | \-1,140,072 | "Power Total Connected Apparent Power" |
| RBS\_ELEC\_POWER\_FACTOR | \-1,140,008 | "Power Factor" |
| RBS\_ELEC\_POWER\_FACTOR\_STATE | \-1,140,009 | "Power Factor State" |
| RBS\_ELEC\_ROOM\_AVERAGE\_ILLUMINATION | \-1,140,033 | "Average Estimated Illumination" |
| RBS\_ELEC\_ROOM\_CAVITY\_RATIO | \-1,140,035 | "Room Cavity Ratio" |
| RBS\_ELEC\_ROOM\_LIGHTING\_CALC\_LUMINAIREPLANE | \-1,144,331 | "Lighting Calculation Luminaire Plane" |
| RBS\_ELEC\_ROOM\_LIGHTING\_CALC\_WORKPLANE | \-1,140,029 | "Lighting Calculation Workplane" |
| RBS\_ELEC\_ROOM\_REFLECTIVITY\_CEILING | \-1,140,030 | "Ceiling Reflectance" |
| RBS\_ELEC\_ROOM\_REFLECTIVITY\_FLOOR | \-1,140,032 | "Floor Reflectance" |
| RBS\_ELEC\_ROOM\_REFLECTIVITY\_WALLS | \-1,140,031 | "Wall Reflectance" |
| RBS\_ELEC\_SHORT\_CIRCUIT\_RATING | \-1,140,080 | "Short Circuit Rating Comments" |
| RBS\_ELEC\_SWITCH\_ID\_PARAM | \-1,140,110 | "Switch ID" |
| RBS\_ELEC\_TRUE\_CURRENT\_PARAM | \-1,140,049 | "True Current" |
| RBS\_ELEC\_TRUE\_CURRENT\_PHASEA\_PARAM | \-1,140,048 | "True Current Phase A" |
| RBS\_ELEC\_TRUE\_CURRENT\_PHASEB\_PARAM | \-1,140,047 | "True Current Phase B" |
| RBS\_ELEC\_TRUE\_CURRENT\_PHASEC\_PARAM | \-1,140,046 | "True Current Phase C" |
| RBS\_ELEC\_TRUE\_LOAD | \-1,140,010 | "True Power" |
| RBS\_ELEC\_TRUE\_LOAD\_PHASE1 | \-1,140,011 | "True Power Phase 1" |
| RBS\_ELEC\_TRUE\_LOAD\_PHASE2 | \-1,140,012 | "True Power Phase 2" |
| RBS\_ELEC\_TRUE\_LOAD\_PHASE3 | \-1,140,013 | "True Power Phase 3" |
| RBS\_ELEC\_TRUE\_LOAD\_PHASEA | \-1,140,050 | "True Power Phase A" |
| RBS\_ELEC\_TRUE\_LOAD\_PHASEB | \-1,140,051 | "True Power Phase B" |
| RBS\_ELEC\_TRUE\_LOAD\_PHASEC | \-1,140,052 | "True Power Phase C" |
| RBS\_ELEC\_VOLTAGE | \-1,140,002 | "Voltage" |
| RBS\_ELEC\_VOLTAGE\_DROP\_PARAM | \-1,140,041 | "Voltage Drop" |
| RBS\_ELEC\_WIRE\_CIRCUITS | \-1,140,102 | "Circuits" |
| RBS\_ELEC\_WIRE\_ELEVATION | \-1,140,096 | "Elevation" |
| RBS\_ELEC\_WIRE\_GROUND\_ADJUSTMENT | \-1,140,092 | "Ground Conductors" |
| RBS\_ELEC\_WIRE\_HOT\_ADJUSTMENT | \-1,140,094 | "Hot Conductors" |
| RBS\_ELEC\_WIRE\_NEUTRAL\_ADJUSTMENT | \-1,140,093 | "Neutral Conductors" |
| RBS\_ELEC\_WIRE\_SHARE\_GROUND | \-1,140,090 | "Share Ground Conductor" |
| RBS\_ELEC\_WIRE\_SHARE\_NEUTRAL | \-1,140,091 | "Share Neutral Conductor" |
| RBS\_ELEC\_WIRE\_TICKMARK\_STATE | \-1,140,106 | "Tick Marks" |
| RBS\_ELEC\_WIRE\_TYPE | \-1,140,097 | "Type" |
| RBS\_ELECTRICAL\_DATA | \-1,114,241 | "Electrical Data" |
| RBS\_END\_LEVEL\_PARAM | \-1,114,001 | "End Level" |
| RBS\_END\_OFFSET\_PARAM | \-1,114,003 | "End Middle Elevation" |
| RBS\_ENERGY\_ANALYSIS\_BUILDING\_ENVELOPE\_ANALYTICAL\_GRID\_CELL\_SIZE | \-1,150,233 | "Analytical Grid Cell Size" |
| RBS\_ENERGY\_ANALYSIS\_BUILDING\_ENVELOPE\_ANALYTICAL\_SPACE\_IDENTIFICATION\_RESOLUTION | \-1,152,376 | "Analytical Space Resolution" |
| RBS\_ENERGY\_ANALYSIS\_BUILDING\_ENVELOPE\_ANALYTICAL\_SURFACE\_IDENTIFICATION\_RESOLUTION | \-1,152,377 | "Analytical Surface Resolution" |
| RBS\_ENERGY\_ANALYSIS\_BUILDING\_ENVELOPE\_DETERMINATION\_PARAM | \-1,150,232 | "Building Envelope" |
| RBS\_ENERGY\_ANALYSIS\_EXPORT\_CATEGORY\_PARAM | \-1,114,386 | "Export Category" |
| RBS\_ENERGY\_ANALYSIS\_EXPORT\_COMPLEXITY\_PARAM | \-1,114,385 | "Export Complexity" |
| RBS\_ENERGY\_ANALYSIS\_EXPORT\_GBXML\_DEFAULTS\_PARAM | \-1,114,383 | "Export Default Values" |
| RBS\_ENERGY\_ANALYSIS\_GROUND\_PLANE\_PARAM | \-1,114,293 | "Ground Plane" |
| RBS\_ENERGY\_ANALYSIS\_INCLUDE\_THERMAL\_PROPERTIES | \-1,150,210 | "Detailed Elements" |
| RBS\_ENERGY\_ANALYSIS\_MODE | \-1,152,378 | "Mode" |
| RBS\_ENERGY\_ANALYSIS\_PROJECT\_PHASE\_PARAM | \-1,114,324 | "Project Phase" |
| RBS\_ENERGY\_ANALYSIS\_SLIVER\_SPACE\_TOLERANCE | \-1,114,333 | "Sliver Space Tolerance" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_ADJACENT\_SPACE\_ID1 | \-1,114,285 | "Adjacent Space Id (1\)" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_ADJACENT\_SPACE\_ID2 | \-1,114,286 | "Adjacent Space Id (2\)" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_AZIMUTH | \-1,114,289 | "Azimuth" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_CADOBJECTID | \-1,114,287 | "CADObjectID" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_ORIGIN\_X | \-1,114,290 | "Origin (X)" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_ORIGIN\_Y | \-1,114,291 | "Origin (Y)" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_ORIGIN\_Z | \-1,114,292 | "Origin (Z)" |
| RBS\_ENERGY\_ANALYSIS\_SURFACE\_TILT | \-1,114,288 | "Tilt" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_BUILDING\_SHELL\_MODE | \-1,114,361 | "Show Analytical Building Shell" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_COORD\_AXIS\_MODE | \-1,114,368 | "Show a Coordinate System Symbol for each Surface" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_INNER\_SHELL\_MODE | \-1,114,363 | "Show Inner Space Shells" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_OUTER\_SHELL\_MODE | \-1,114,362 | "Show Analytical Space Shells" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_RBE\_MODE | \-1,114,367 | "Show Room Bounding Elements Dimmed and Underlay" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_SHADING\_SURFACES\_MODE | \-1,114,366 | "Show Shading Surfaces" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_SURFACES\_MODE | \-1,114,364 | "Show Surfaces" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_TRANSPARENT\_MODE | \-1,114,365 | "Show Surfaces Transparent" |
| RBS\_ENERGY\_ANALYSIS\_VIEW\_UPDATE\_SURFACES | \-1,114,299 | "Update Surfaces" |
| RBS\_EQ\_DIAMETER\_PARAM | \-1,114,127 | "Equivalent Diameter" |
| RBS\_FAMILY\_CONTENT\_ANNOTATION\_DISPLAY | \-1,114,242 | "Use Annotation Scale" |
| RBS\_FAMILY\_CONTENT\_DISTRIBUTION\_SYSTEM | \-1,140,064 | "Distribution System" |
| RBS\_FAMILY\_CONTENT\_OFFSET\_HEIGHT | \-1,114,212 | "OffsetHeight" |
| RBS\_FAMILY\_CONTENT\_OFFSET\_WIDTH | \-1,114,211 | "OffsetWidth" |
| RBS\_FAMILY\_CONTENT\_SECONDARY\_DISTRIBSYS | \-1,140,088 | "Secondary Distribution System" |
| RBS\_FAMILY\_CONTENT\_TAKEOFF\_FIXED\_LENGTH | \-1,114,215 | "Takeoff Fixed Length" |
| RBS\_FAMILY\_CONTENT\_TAKEOFF\_LENGTH | \-1,114,213 | "Takeoff Length" |
| RBS\_FAMILY\_CONTENT\_TAKEOFF\_PROJLENGTH | \-1,114,214 | "Takeoff Length Projection" |
| RBS\_FLEX\_DUCT\_TYPE\_PARAM | \-1,114,139 | "Flex Duct Type" |
| RBS\_FLEX\_PATTERN\_PARAM | \-1,114,005 | "Flex Pattern" |
| RBS\_FLEX\_PIPE\_TYPE\_PARAM | \-1,114,141 | "Flex Pipe" |
| RBS\_FLEXDUCT\_ROUNDTYPE\_PARAM | \-1,114,135 | "Flex Duct Type" |
| RBS\_FLOW\_FACTOR\_PARAM | \-1,140,222 | "Flow Factor" |
| RBS\_FLOW\_OBSOLETE | \-1,114,104 | "Flow" |
| RBS\_FP\_SPRINKLER\_COVERAGE\_PARAM | \-1,140,261 | "Coverage" |
| RBS\_FP\_SPRINKLER\_K\_FACTOR\_PARAM | \-1,140,264 | "K\-Factor" |
| RBS\_FP\_SPRINKLER\_ORIFICE\_PARAM | \-1,140,262 | "Orifice" |
| RBS\_FP\_SPRINKLER\_ORIFICE\_SIZE\_PARAM | \-1,140,266 | "Orifice Size" |
| RBS\_FP\_SPRINKLER\_PRESSURE\_CLASS\_PARAM | \-1,140,263 | "Pressure Class" |
| RBS\_FP\_SPRINKLER\_RESPONSE\_PARAM | \-1,140,260 | "Response" |
| RBS\_FP\_SPRINKLER\_TEMPERATURE\_RATING\_PARAM | \-1,140,265 | "Temperature Rating" |
| RBS\_FRICTION | \-1,114,116 | "Friction" |
| RBS\_GBXML\_OPENING\_TYPE | \-1,114,400 | "Opening Type" |
| RBS\_GBXML\_SURFACE\_AREA | \-1,114,247 | "Area" |
| RBS\_GBXML\_SURFACE\_NAME | \-1,114,245 | "Surface Name" |
| RBS\_GBXML\_SURFACE\_TYPE | \-1,114,246 | "Surface Type" |
| RBS\_HVACLOAD\_DOOR\_AREA\_PARAM | \-1,114,372 | "Door Area" |
| RBS\_HVACLOAD\_DOOR\_COOLING\_LOAD\_PARAM | \-1,114,379 | "Door Cooling Load" |
| RBS\_HVACLOAD\_FLOOR\_AREA\_PARAM | \-1,114,373 | "Floor Area" |
| RBS\_HVACLOAD\_PARTITION\_AREA\_PARAM | \-1,114,374 | "Partition Area" |
| RBS\_HVACLOAD\_PARTITION\_COOLING\_LOAD\_PARAM | \-1,114,380 | "Partition Cooling Load" |
| RBS\_HVACLOAD\_PLENUM\_COOLING\_LOAD\_PARAM | \-1,114,382 | "Plenum Cooling Load" |
| RBS\_HVACLOAD\_ROOF\_AREA\_PARAM | \-1,114,369 | "Roof Area" |
| RBS\_HVACLOAD\_ROOF\_COOLING\_LOAD\_PARAM | \-1,114,376 | "Roof Cooling Load" |
| RBS\_HVACLOAD\_SKYLIGHT\_AREA\_PARAM | \-1,114,375 | "Skylight Area" |
| RBS\_HVACLOAD\_SKYLIGHT\_COOLING\_LOAD\_PARAM | \-1,114,381 | "Skylight Cooling Load" |
| RBS\_HVACLOAD\_WALL\_AREA\_PARAM | \-1,114,370 | "Wall Area" |
| RBS\_HVACLOAD\_WALL\_COOLING\_LOAD\_PARAM | \-1,114,377 | "Wall Cooling Load" |
| RBS\_HVACLOAD\_WINDOW\_AREA\_PARAM | \-1,114,371 | "Window Area" |
| RBS\_HVACLOAD\_WINDOW\_COOLING\_LOAD\_PARAM | \-1,114,378 | "Window Cooling Load" |
| RBS\_HYDRAULIC\_DIAMETER\_PARAM | \-1,114,129 | "Hydraulic Diameter" |
| RBS\_INSULATION\_LINING\_VOLUME | \-1,150,425 | "Volume" |
| RBS\_INSULATION\_THICKNESS | \-1,114,117 | "Insulation Thickness" |
| RBS\_INSULATION\_THICKNESS\_FOR\_DUCT | \-1,114,358 | "Insulation Thickness" |
| RBS\_INSULATION\_THICKNESS\_FOR\_PIPE | \-1,114,359 | "Insulation Thickness" |
| RBS\_IS\_CUSTOM\_FITTING | \-1,114,238 | "IsCustom" |
| RBS\_LINING\_THICKNESS | \-1,114,118 | "Lining Thickness" |
| RBS\_LINING\_THICKNESS\_FOR\_DUCT | \-1,114,360 | "Lining Thickness" |
| RBS\_LOAD\_SUB\_CLASSIFICATION\_MOTOR | \-1,140,131 | "Load Sub\-Classification Motor" |
| RBS\_LOOKUP\_TABLE\_NAME | \-1,114,236 | "Lookup Table Name" |
| RBS\_LOSS\_COEFFICIENT | \-1,114,124 | "Loss Coefficient" |
| RBS\_MAX\_FLOW | \-1,114,123 | "Max Flow" |
| RBS\_MIN\_FLOW | \-1,114,122 | "Min Flow" |
| RBS\_OFFSET\_PARAM | \-1,114,132 | "Middle Elevation" |
| RBS\_PANEL\_SCHEDULE\_SHEET\_APPEARANCE\_INST\_PARAM | \-1,007,808 | "Appearance" |
| RBS\_PANEL\_SCHEDULE\_SHEET\_APPEARANCE\_PARAM | \-1,007,807 | "Appearance On Sheet" |
| RBS\_PARALLELCONDUITS\_HORIZONTAL\_NUMBER | \-1,140,268 | "Horizontal Number for parallel conduits" |
| RBS\_PARALLELCONDUITS\_HORIZONTAL\_OFFSET\_VALUE | \-1,140,270 | "Horizontal Offset value for parallel conduits" |
| RBS\_PARALLELCONDUITS\_VERTICAL\_NUMBER | \-1,140,269 | "Vertical Number for parallel conduits" |
| RBS\_PARALLELCONDUITS\_VERTICAL\_OFFSET\_VALUE | \-1,140,271 | "Vertical Offset value for parallel conduits" |
| RBS\_PARALLELPIPES\_HORIZONTAL\_NUMBER | \-1,140,272 | "Horizontal Number for parallel pipes" |
| RBS\_PARALLELPIPES\_HORIZONTAL\_OFFSET\_VALUE | \-1,140,274 | "Horizontal Offset value for parallel pipes" |
| RBS\_PARALLELPIPES\_VERTICAL\_NUMBER | \-1,140,273 | "Vertical Number for parallel pipes" |
| RBS\_PARALLELPIPES\_VERTICAL\_OFFSET\_VALUE | \-1,140,275 | "Vertical Offset value for parallel pipes" |
| RBS\_PART\_TYPE | \-1,115,958 | "Part Type" |
| RBS\_PIPE\_ADDITIONAL\_FLOW\_PARAM | \-1,140,226 | "Additional Flow" |
| RBS\_PIPE\_BOTTOM\_ELEVATION | \-1,155,115 | "Lower End Bottom Elevation" |
| RBS\_PIPE\_CALCULATED\_SIZE | \-1,150,427 | "Pipe Size" |
| RBS\_PIPE\_CLASS\_PARAM | \-1,140,200 | "Schedule/Type" |
| RBS\_PIPE\_CONNECTIONTYPE\_PARAM | \-1,140,201 | "Connection Type" |
| RBS\_PIPE\_CONNECTOR\_SYSTEM\_CLASSIFICATION\_PARAM | \-1,133,410 | "System Classification" |
| RBS\_PIPE\_CWFU\_PARAM | \-1,140,250 | "CWFU" |
| RBS\_PIPE\_DIAMETER\_PARAM | \-1,140,225 | "Diameter" |
| RBS\_PIPE\_FITTING\_LOSS\_KFACTOR\_PARAM | \-1,140,228 | "K Coefficient" |
| RBS\_PIPE\_FITTING\_LOSS\_METHOD\_PARAM | \-1,140,230 | "Loss Method" |
| RBS\_PIPE\_FITTING\_LOSS\_METHOD\_SERVER\_PARAM | \-1,114,147 | "Loss Method" |
| RBS\_PIPE\_FITTING\_LOSS\_METHOD\_SETTINGS | \-1,114,150 | "Loss Method Settings" |
| RBS\_PIPE\_FITTING\_LOSS\_TABLE\_PARAM | \-1,140,229 | "K Coefficient Table" |
| RBS\_PIPE\_FIXTURE\_UNITS\_PARAM | \-1,140,246 | "Fixture Units" |
| RBS\_PIPE\_FLOW\_CONFIGURATION\_PARAM | \-1,140,249 | "Flow Configuration" |
| RBS\_PIPE\_FLOW\_DIRECTION\_PARAM | \-1,140,248 | "Flow Direction" |
| RBS\_PIPE\_FLOW\_PARAM | \-1,140,213 | "Flow" |
| RBS\_PIPE\_FLOW\_STATE\_PARAM | \-1,140,209 | "Flow State" |
| RBS\_PIPE\_FLUID\_DENSITY\_PARAM | \-1,140,214 | "Fluid Density" |
| RBS\_PIPE\_FLUID\_TEMPERATURE\_PARAM | \-1,140,217 | "Fluid Temperature" |
| RBS\_PIPE\_FLUID\_TYPE\_PARAM | \-1,140,218 | "Fluid Type" |
| RBS\_PIPE\_FLUID\_VISCOSITY\_PARAM | \-1,140,215 | "Fluid Dynamic Viscosity" |
| RBS\_PIPE\_FRICTION\_PARAM | \-1,140,206 | "Friction" |
| RBS\_PIPE\_HWFU\_PARAM | \-1,140,251 | "HWFU" |
| RBS\_PIPE\_INNER\_DIAM\_PARAM | \-1,140,212 | "Inside Diameter" |
| RBS\_PIPE\_INSULATION\_THICKNESS | \-1,140,241 | "Insulation Thickness" |
| RBS\_PIPE\_INVERT\_ELEVATION | \-1,140,237 | "Invert Elevation": This parameter is obsolete. It exists only for compatibility. |
| RBS\_PIPE\_JOINTTYPE\_PARAM | \-1,140,278 | "Connection Type" |
| RBS\_PIPE\_MATERIAL\_PARAM | \-1,140,202 | "Material" |
| RBS\_PIPE\_OUTER\_DIAMETER | \-1,140,238 | "Outside Diameter" |
| RBS\_PIPE\_PRESSUREDROP\_PARAM | \-1,140,205 | "Pressure Drop" |
| RBS\_PIPE\_REYNOLDS\_NUMBER\_PARAM | \-1,140,211 | "Reynolds Number" |
| RBS\_PIPE\_SEGMENT\_PARAM | \-1,140,277 | "Pipe Segment" |
| RBS\_PIPE\_SIZE\_FORMATTED\_PARAM | \-1,114,144 | "Size" |
| RBS\_PIPE\_SIZE\_MAXIMUM | \-1,140,284 | "Maximum Size" |
| RBS\_PIPE\_SIZE\_MINIMUM | \-1,140,283 | "Minimum Size" |
| RBS\_PIPE\_SLOPE | \-1,140,256 | "Slope" |
| RBS\_PIPE\_SLOPE\_DEF\_PARAM | \-1,140,330 | "Pipe Slope Definitions" |
| RBS\_PIPE\_SLOPE\_OPTIONS\_DEF\_PARAM | \-1,140,340 | "Pipe Slope Options" |
| RBS\_PIPE\_STATIC\_PRESSURE | \-1,140,242 | "Static Pressure" |
| RBS\_PIPE\_SYSTEM\_CALCULATION\_PARAM | \-1,140,335 | "Calculations" |
| RBS\_PIPE\_SYSTEM\_FIXTURE\_UNIT\_PARAM | \-1,140,257 | "Fixture Units" |
| RBS\_PIPE\_TOP\_ELEVATION | \-1,155,114 | "Upper End Top Elevation" |
| RBS\_PIPE\_TYPE\_FITTING\_LOSS\_KFACTOR\_PARAM | \-1,140,232 | "K Coefficient" |
| RBS\_PIPE\_TYPE\_FITTING\_LOSS\_METHOD\_PARAM | \-1,140,234 | "Loss Method" |
| RBS\_PIPE\_TYPE\_FITTING\_LOSS\_TABLE\_PARAM | \-1,140,233 | "K Coefficient Table" |
| RBS\_PIPE\_TYPE\_PARAM | \-1,114,140 | "Pipe Type" |
| RBS\_PIPE\_TYPE\_VALVE\_LOSS\_CVFACTOR\_PARAM | \-1,140,231 | "Cv Coefficient" |
| RBS\_PIPE\_VALVE\_LOSS\_CVFACTOR\_PARAM | \-1,140,227 | "Cv Coefficient" |
| RBS\_PIPE\_VELOCITY\_PARAM | \-1,140,207 | "Velocity" |
| RBS\_PIPE\_VOLUME\_PARAM | \-1,140,253 | "Volume" |
| RBS\_PIPE\_WALL\_THICKNESS | \-1,141,040 | "Wall Thickness" |
| RBS\_PIPE\_WFU\_PARAM | \-1,140,252 | "WFU" |
| RBS\_PIPING\_SYSTEM\_TYPE\_PARAM | \-1,140,334 | "System Type" |
| RBS\_PRESSURE\_DROP | \-1,114,108 | "Pressure Drop" |
| RBS\_PROJECT\_CONSTRUCTION\_TYPE\_SHADINGFACTOR\_PARAM | \-1,114,296 | "Internal Shading Factor" |
| RBS\_PROJECT\_LOCATION\_PARAM | \-1,114,282 | "Location" |
| RBS\_PROJECT\_REPORTTYPE\_PARAM | \-1,150,161 | "Report Type" |
| RBS\_REFERENCE\_FREESIZE | \-1,150,435 | "Free Size" |
| RBS\_REFERENCE\_INSULATION\_THICKNESS | \-1,150,431 | "Insulation Thickness": This parameter is obsolete. Use DUCT\_INSULATION\_THICKNESS and PIPE\_INSULATION\_THICKNESS. |
| RBS\_REFERENCE\_INSULATION\_TYPE | \-1,150,430 | "Insulation Type" |
| RBS\_REFERENCE\_LINING\_THICKNESS | \-1,150,433 | "Lining Thickness" |
| RBS\_REFERENCE\_LINING\_TYPE | \-1,150,432 | "Lining Type" |
| RBS\_REFERENCE\_OVERALLSIZE | \-1,150,434 | "Overall Size" |
| RBS\_REYNOLDSNUMBER\_PARAM | \-1,114,128 | "Reynolds number" |
| RBS\_ROOM\_COEFFICIENT\_UTILIZATION | \-1,114,216 | "Coefficient of Utilization" |
| RBS\_ROUTING\_PREFERENCE\_PARAM | \-1,140,276 | "Routing Preferences" |
| RBS\_SECTION | \-1,114,125 | "Section" |
| RBS\_SEGMENT\_DESCRIPTION\_PARAM | \-1,140,279 | "Segment Description" |
| RBS\_SERVICE\_TYPE\_PARAM | \-1,114,248 | "Building Service" |
| RBS\_SHOW\_PROFILE\_TYPE | \-1,140,258 | "Show Round" |
| RBS\_SIZE\_LOCK | \-1,114,167 | "Size Lock" |
| RBS\_START\_LEVEL\_PARAM | \-1,114,000 | "Reference Level" |
| RBS\_START\_OFFSET\_PARAM | \-1,114,002 | "Start Middle Elevation" |
| RBS\_SYSTEM\_ABBREVIATION\_PARAM | \-1,140,332 | "Abbreviation" |
| RBS\_SYSTEM\_BASE\_ELEMENT\_PARAM | \-1,140,326 | "System Equipment" |
| RBS\_SYSTEM\_CLASSIFICATION\_PARAM | \-1,140,325 | "System Classification" |
| RBS\_SYSTEM\_FLOW\_CONVERSION\_METHOD\_PARAM | \-1,140,328 | "Flow Conversion Method" |
| RBS\_SYSTEM\_NAME\_PARAM | \-1,140,324 | "System Name" |
| RBS\_SYSTEM\_NUM\_ELEMENTS\_PARAM | \-1,140,327 | "Number of Elements" |
| RBS\_SYSTEM\_RISEDROP\_1LINEDROPSYMBOL\_PARAM | \-1,150,408 | "Single Line Drop Symbol" |
| RBS\_SYSTEM\_RISEDROP\_1LINERISESYMBOL\_PARAM | \-1,150,407 | "Single Line Rise Symbol" |
| RBS\_SYSTEM\_RISEDROP\_1LINETEEDOWNSYMBOL\_PARAM | \-1,150,405 | "Single Line Tee Down Symbol" |
| RBS\_SYSTEM\_RISEDROP\_1LINETEEUPSYMBOL\_PARAM | \-1,150,406 | "Single Line Tee Up Symbol" |
| RBS\_SYSTEM\_RISEDROP\_2LINEDROPSYMBOL\_PARAM | \-1,150,410 | "Two Line Drop Symbol" |
| RBS\_SYSTEM\_RISEDROP\_2LINERISESYMBOL\_PARAM | \-1,150,409 | "Two Line Rise Symbol" |
| RBS\_SYSTEM\_RISEDROP\_PARAM | \-1,150,411 | "Rise / Drop Symbol" |
| RBS\_VELOCITY | \-1,114,107 | "Velocity" |
| RBS\_VELOCITY\_PRESSURE | \-1,114,121 | "Velocity Pressure" |
| RBS\_VOLTAGETYPE\_MAXVOLTAGE\_PARAM | \-1,140,056 | "Maximum Voltage" |
| RBS\_VOLTAGETYPE\_MINVOLTAGE\_PARAM | \-1,140,057 | "Minimum Voltage" |
| RBS\_VOLTAGETYPE\_VOLTAGE\_PARAM | \-1,140,058 | "Actual Voltage" |
| RBS\_WIRE\_CIRCUIT\_DESCRIPTION | \-1,140,109 | "Circuit Description" |
| RBS\_WIRE\_CIRCUIT\_LOAD\_NAME | \-1,140,108 | "Circuit Load Name" |
| RBS\_WIRE\_CONDUIT\_TYPE\_PARAM | \-1,140,021 | "Conduit Type" |
| RBS\_WIRE\_INSULATION\_PARAM | \-1,140,026 | "Insulation" |
| RBS\_WIRE\_MATERIAL\_PARAM | \-1,140,028 | "Material" |
| RBS\_WIRE\_MAX\_CONDUCTOR\_SIZE\_PARAM | \-1,140,025 | "Max Size" |
| RBS\_WIRE\_NEUTRAL\_INCLUDED\_IN\_BALANCED\_LOAD\_PARAM | \-1,140,023 | "Neutral Included in Balanced Load" |
| RBS\_WIRE\_NEUTRAL\_MODE\_PARAM | \-1,140,022 | "Neutral Size" |
| RBS\_WIRE\_NEUTRAL\_MULTIPLIER\_PARAM | \-1,140,024 | "Neutral Multiplier" |
| RBS\_WIRE\_NUM\_CONDUCTORS\_PARAM | \-1,140,107 | "Number of Conductors" |
| RBS\_WIRE\_TEMPERATURE\_RATING\_PARAM | \-1,140,027 | "Temperature Rating" |
| REBAR\_ALIGNMENT\_OPTIONS | \-1,155,283 | "Bar Alignment" |
| REBAR\_BAR\_ALLOWED\_BAR\_TYPES | \-1,017,021 | "Allowable Rebar Bar Types" |
| REBAR\_BAR\_CRANK\_LENGTHS | \-1,018,275 | "Crank Lengths" |
| REBAR\_BAR\_DEFORMATION\_TYPE | \-1,018,274 | "Deformation" |
| REBAR\_BAR\_DIAMETER | \-1,017,000 | "Bar Diameter" |
| REBAR\_BAR\_HOOK\_LENGTHS | \-1,017,018 | "Hook Lengths" |
| REBAR\_BAR\_MAXIMUM\_BEND\_RADIUS | \-1,017,020 | "Maximum Bend Radius" |
| REBAR\_BAR\_SPLICE\_LENGTHS | \-1,180,309 | "Splice Lengths" |
| REBAR\_BAR\_STIRRUP\_BEND\_DIAMETER | \-1,017,019 | "Stirrup/Tie Bend Diameter" |
| REBAR\_BAR\_STYLE | \-1,017,002 | "Subcategory" |
| REBAR\_CONSTRAINTS\_STATUS | \-1,180,301 | "Rebar Constraint Status" |
| REBAR\_CONTAINER\_BAR\_TYPE | \-1,018,505 | "Bar Type" |
| REBAR\_CRANK\_AT\_END\_TYPE | \-1,180,433 | "Crank at End" |
| REBAR\_CRANK\_AT\_START\_TYPE | \-1,180,432 | "Crank at Start" |
| REBAR\_CRANK\_LENGTH\_MULTIPLIER | \-1,180,416 | "Length Multiplier" |
| REBAR\_CRANK\_LENGTH\_OVERRIDE | \-1,180,438 | "Override Crank Lengths" |
| REBAR\_CRANK\_OFFSET\_MULTIPLIER | \-1,180,417 | "Crank Offset Multiplier" |
| REBAR\_CRANK\_RATIO | \-1,180,418 | "Crank Slope 1:" |
| REBAR\_DISTRIBUTION\_TYPE | \-1,017,057 | "Distribution Type" |
| REBAR\_ELEM\_BAR\_SPACING | \-1,017,013 | "Spacing" |
| REBAR\_ELEM\_ENDTREATMENT\_END | \-1,154,656 | "End Treatment At End" |
| REBAR\_ELEM\_ENDTREATMENT\_START | \-1,154,655 | "End Treatment At Start" |
| REBAR\_ELEM\_HOOK\_END\_TYPE | \-1,017,008 | "Hook At End" |
| REBAR\_ELEM\_HOOK\_START\_TYPE | \-1,017,006 | "Hook At Start" |
| REBAR\_ELEM\_HOOK\_STYLE | \-1,017,026 | "Style" |
| REBAR\_ELEM\_HOST\_MARK | \-1,154,619 | "Host Mark" |
| REBAR\_ELEM\_LAYOUT\_RULE | \-1,017,011 | "Layout Rule" |
| REBAR\_ELEM\_LENGTH | \-1,017,016 | "Bar Length" |
| REBAR\_ELEM\_QUANTITY\_OF\_BARS | \-1,017,012 | "Quantity" |
| REBAR\_ELEM\_SCHEDULE\_MARK | \-1,017,032 | "Schedule Mark" |
| REBAR\_ELEM\_TERMINATION\_END\_ORIENT | \-1,017,009 | "Orientation At End" |
| REBAR\_ELEM\_TERMINATION\_START\_ORIENT | \-1,017,007 | "Orientation At Start" |
| REBAR\_ELEM\_TOTAL\_LENGTH | \-1,017,005 | "Total Bar Length" |
| REBAR\_ELEMENT\_ROUNDING | \-1,017,027 | "Rounding Overrides" |
| REBAR\_ELEMENT\_VISIBILITY | \-1,017,014 | "View Visibility States" |
| REBAR\_GEOMETRY\_TYPE | \-1,154,694 | "Geometry" |
| REBAR\_HOOK\_ANGLE | \-1,017,003 | "Hook Angle" |
| REBAR\_HOOK\_LENGTH\_OVERRIDE | \-1,155,215 | "Override Hook Lengths" |
| REBAR\_HOOK\_LINE\_LEN\_FACTOR | \-1,017,004 | "Extension Multiplier" |
| REBAR\_HOOK\_STYLE | \-1,017,017 | "Style" |
| REBAR\_HOST\_CATEGORY | \-1,017,055 | "Host Category" |
| REBAR\_INCLUDE\_FIRST\_BAR | \-1,017,039 | "Include First Bar" |
| REBAR\_INCLUDE\_LAST\_BAR | \-1,017,040 | "Include Last Bar" |
| REBAR\_INSTANCE\_BAR\_DIAMETER | \-1,017,037 | "Bar Diameter" |
| REBAR\_INSTANCE\_BAR\_MODEL\_DIAMETER | \-1,155,224 | "Model Bar Diameter" |
| REBAR\_INSTANCE\_BEND\_DIAMETER | \-1,017,038 | "Bend Diameter" |
| REBAR\_INSTANCE\_STIRRUP\_TIE\_ATTACHMENT | \-1,017,047 | "Stirrup/Tie Attachment" |
| REBAR\_INTERNAL\_MULTIPLANAR | \-1,017,049 | "INTERNAL: Multiplanar" |
| REBAR\_INTERNAL\_MULTIPLANAR\_ARC\_CONNECTOR | \-1,154,659 | "INTERNAL: Multiplanar Arc Connector" |
| REBAR\_INTERNAL\_MULTIPLANAR\_DUPLICATE | \-1,017,050 | "INTERNAL: Multiplanar Duplicate" |
| REBAR\_INTERNAL\_MULTIPLANAR\_END\_CONNECTOR | \-1,017,052 | "INTERNAL: Multiplanar End Connector" |
| REBAR\_INTERNAL\_MULTIPLANAR\_START\_CONNECTOR | \-1,017,051 | "INTERNAL: Multiplanar Start Connector" |
| REBAR\_MAX\_LENGTH | \-1,017,063 | "Maximum Bar Length" |
| REBAR\_MAXIM\_SUFFIX | \-1,017,062 | "Maximum Suffix" |
| REBAR\_MAXIMUM\_NUMBER | \-1,180,414 | "Maximum Rebar Number" |
| REBAR\_MIN\_LENGTH | \-1,017,064 | "Minimum Bar Length" |
| REBAR\_MINIM\_SUFFIX | \-1,017,061 | "Minimum Suffix" |
| REBAR\_MINIMUM\_NUMBER | \-1,180,413 | "Minimum Rebar Number" |
| REBAR\_MODEL\_BAR\_DIAMETER | \-1,155,223 | "Model Bar Diameter" |
| REBAR\_MODIFIED\_SET | \-1,155,221 | "Modified Rebar Set" |
| REBAR\_NUMBER | \-1,154,616 | "Rebar Number" |
| REBAR\_NUMBER\_SUFFIX | \-1,017,060 | "Rebar Number Suffix" |
| REBAR\_QUANITY\_BY\_DISTRIB | \-1,017,065 | "Quantity By Rebar Set" |
| REBAR\_SHAPE | \-1,017,015 | "Shape" |
| REBAR\_SHAPE\_ALLOWED\_BAR\_TYPES | \-1,017,021 | "Allowable Rebar Bar Types" |
| REBAR\_SHAPE\_CRANK\_END\_ANGLED\_LENGTH | \-1,180,430 | "End Crank Angled Length" |
| REBAR\_SHAPE\_CRANK\_END\_LENGTH | \-1,180,431 | "End Crank Length" |
| REBAR\_SHAPE\_CRANK\_END\_OFFSET | \-1,180,428 | "End Crank Offset" |
| REBAR\_SHAPE\_CRANK\_END\_RATIO | \-1,180,440 | "End Crank Slope 1:" |
| REBAR\_SHAPE\_CRANK\_END\_STRAIGHT\_LENGTH | \-1,180,429 | "End Crank Straight Length" |
| REBAR\_SHAPE\_CRANK\_START\_ANGLED\_LENGTH | \-1,180,425 | "Start Crank Angled Length" |
| REBAR\_SHAPE\_CRANK\_START\_LENGTH | \-1,180,426 | "Start Crank Length" |
| REBAR\_SHAPE\_CRANK\_START\_OFFSET | \-1,180,423 | "Start Crank Offset" |
| REBAR\_SHAPE\_CRANK\_START\_RATIO | \-1,180,439 | "Start Crank Slope 1:" |
| REBAR\_SHAPE\_CRANK\_START\_STRAIGHT\_LENGTH | \-1,180,424 | "Start Crank Straight Length" |
| REBAR\_SHAPE\_END\_HOOK\_LENGTH | \-1,017,035 | "End Hook Length" |
| REBAR\_SHAPE\_END\_HOOK\_OFFSET | \-1,017,036 | "End Hook Offset Length" |
| REBAR\_SHAPE\_HOOK\_STYLE | \-1,017,022 | "Style" |
| REBAR\_SHAPE\_IMAGE | \-1,154,618 | "Shape Image" |
| REBAR\_SHAPE\_NAME | \-1,180,441 | "Shape Name" |
| REBAR\_SHAPE\_OUT\_OF\_PLANE\_BEND\_DIAMETER | \-1,017,048 | "Out of Plane Bend Diameter" |
| REBAR\_SHAPE\_PARAM\_END\_HOOK\_TAN\_LEN | \-1,017,054 | "End Tangent Hook Length" |
| REBAR\_SHAPE\_PARAM\_START\_HOOK\_TAN\_LEN | \-1,017,053 | "Start Tangent Hook Length" |
| REBAR\_SHAPE\_SPIRAL\_BASE\_FINISHING\_TURNS | \-1,017,045 | "Base Finishing Turns" |
| REBAR\_SHAPE\_SPIRAL\_HEIGHT | \-1,017,043 | "Height" |
| REBAR\_SHAPE\_SPIRAL\_PITCH | \-1,017,042 | "Pitch" |
| REBAR\_SHAPE\_SPIRAL\_TOP\_FINISHING\_TURNS | \-1,017,044 | "Top Finishing Turns" |
| REBAR\_SHAPE\_START\_HOOK\_LENGTH | \-1,017,033 | "Start Hook Length" |
| REBAR\_SHAPE\_START\_HOOK\_OFFSET | \-1,017,034 | "Start Hook Offset Length" |
| REBAR\_SHAPE\_STIRRUP\_TIE\_ATTACHMENT | \-1,017,046 | "Stirrup/Tie Attachment" |
| REBAR\_SHAPE\_TERMINATION\_ROTATION\_AT\_END | \-1,155,204 | "Rotation At End" |
| REBAR\_SHAPE\_TERMINATION\_ROTATION\_AT\_START | \-1,155,203 | "Rotation At Start" |
| REBAR\_SHAPE\_TYPE\_AT\_END | \-1,180,435 | "Type At End" |
| REBAR\_SHAPE\_TYPE\_AT\_START | \-1,180,434 | "Type At Start" |
| REBAR\_SPLICE\_LAP\_LENGTH\_MULTIPLIER | \-1,180,400 | "Lap Length Multiplier" |
| REBAR\_SPLICE\_SHIFT\_BARS | \-1,180,412 | "Shift Bars" |
| REBAR\_SPLICE\_SPLICE\_LINE\_POSITION | \-1,180,401 | "Splice Position" |
| REBAR\_SPLICE\_STAGGER\_LENGTH\_MULTIPLIER | \-1,180,411 | "Stagger Length Multiplier" |
| REBAR\_STAGGER\_OFFSET\_AT\_END | \-1,180,410 | "Offset At End" |
| REBAR\_STAGGER\_OFFSET\_AT\_START | \-1,180,409 | "Offset At Start" |
| REBAR\_STAGGERED\_SET | \-1,180,415 | "Staggered Set" |
| REBAR\_STANDARD\_BEND\_DIAMETER | \-1,017,010 | "Standard Bend Diameter" |
| REBAR\_STANDARD\_HOOK\_BEND\_DIAMETER | \-1,017,041 | "Standard Hook Bend Diameter" |
| REBAR\_SYSTEM\_ACTIVE\_BACK\_DIR\_1 | \-1,018,204 | "Interior Major Direction" |
| REBAR\_SYSTEM\_ACTIVE\_BACK\_DIR\_2 | \-1,018,205 | "Interior Minor Direction" |
| REBAR\_SYSTEM\_ACTIVE\_BOTTOM\_DIR\_1 | \-1,018,103 | "Bottom Major Direction" |
| REBAR\_SYSTEM\_ACTIVE\_BOTTOM\_DIR\_1\_GENERIC | \-1,018,252 | "Bottom/Interior Major Direction" |
| REBAR\_SYSTEM\_ACTIVE\_BOTTOM\_DIR\_2 | \-1,018,104 | "Bottom Minor Direction" |
| REBAR\_SYSTEM\_ACTIVE\_BOTTOM\_DIR\_2\_GENERIC | \-1,018,253 | "Bottom/Interior Minor Direction" |
| REBAR\_SYSTEM\_ACTIVE\_FRONT\_DIR\_1 | \-1,018,200 | "Exterior Major Direction" |
| REBAR\_SYSTEM\_ACTIVE\_FRONT\_DIR\_2 | \-1,018,203 | "Exterior Minor Direction" |
| REBAR\_SYSTEM\_ACTIVE\_TOP\_DIR\_1 | \-1,018,100 | "Top Major Direction" |
| REBAR\_SYSTEM\_ACTIVE\_TOP\_DIR\_1\_GENERIC | \-1,018,250 | "Top/Exterior Major Direction" |
| REBAR\_SYSTEM\_ACTIVE\_TOP\_DIR\_2 | \-1,018,102 | "Top Minor Direction" |
| REBAR\_SYSTEM\_ACTIVE\_TOP\_DIR\_2\_GENERIC | \-1,018,251 | "Top/Exterior Minor Direction" |
| REBAR\_SYSTEM\_ADDL\_BOTTOM\_OFFSET | \-1,018,025 | "Additional Bottom Cover Offset" |
| REBAR\_SYSTEM\_ADDL\_EXTERIOR\_OFFSET | \-1,018,026 | "Additional Exterior Cover Offset" |
| REBAR\_SYSTEM\_ADDL\_INTERIOR\_OFFSET | \-1,018,027 | "Additional Interior Cover Offset" |
| REBAR\_SYSTEM\_ADDL\_TOP\_OFFSET | \-1,018,024 | "Additional Top Cover Offset" |
| REBAR\_SYSTEM\_BAR\_TYPE\_BACK\_DIR\_1 | \-1,018,208 | "Interior Major Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_BACK\_DIR\_2 | \-1,018,209 | "Interior Minor Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_BOTTOM\_DIR\_1 | \-1,018,107 | "Bottom Major Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_BOTTOM\_DIR\_1\_GENERIC | \-1,018,256 | "Bottom/Interior Major Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_BOTTOM\_DIR\_2 | \-1,018,108 | "Bottom Minor Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_BOTTOM\_DIR\_2\_GENERIC | \-1,018,257 | "Bottom/Interior Minor Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_FRONT\_DIR\_1 | \-1,018,206 | "Exterior Major Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_FRONT\_DIR\_2 | \-1,018,207 | "Exterior Minor Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_TOP\_DIR\_1 | \-1,018,105 | "Top Major Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_TOP\_DIR\_1\_GENERIC | \-1,018,254 | "Top/Exterior Major Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_TOP\_DIR\_2 | \-1,018,106 | "Top Minor Bar Type" |
| REBAR\_SYSTEM\_BAR\_TYPE\_TOP\_DIR\_2\_GENERIC | \-1,018,255 | "Top/Exterior Minor Bar Type" |
| REBAR\_SYSTEM\_BOTTOM\_MAJOR\_MATCHES\_BOTTOM\_MINOR | \-1,018,021 | "Bottom Major and Minor Layers Match" |
| REBAR\_SYSTEM\_COVER\_BOTTOM | \-1,018,007 | "Rebar Cover Bottom/Interior" |
| REBAR\_SYSTEM\_COVER\_SIDE | \-1,018,000 | "Rebar Cover Side/Edge" |
| REBAR\_SYSTEM\_COVER\_TOP | \-1,018,006 | "Rebar Cover Top/Exterior" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_BACK\_DIR\_1 | \-1,018,212 | "Interior Major Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_BACK\_DIR\_2 | \-1,018,213 | "Interior Minor Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_BOTTOM\_DIR\_1 | \-1,018,111 | "Bottom Major Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_BOTTOM\_DIR\_2 | \-1,018,112 | "Bottom Minor Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_FRONT\_DIR\_1 | \-1,018,210 | "Exterior Major Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_FRONT\_DIR\_2 | \-1,018,211 | "Exterior Minor Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_TOP\_DIR\_1 | \-1,018,109 | "Top Major Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_ORIENT\_TOP\_DIR\_2 | \-1,018,110 | "Top Minor Hook Orientation" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_BACK\_DIR\_1 | \-1,018,216 | "Interior Major Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_BACK\_DIR\_2 | \-1,018,217 | "Interior Minor Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_BOTTOM\_DIR\_1 | \-1,018,115 | "Bottom Major Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_BOTTOM\_DIR\_2 | \-1,018,116 | "Bottom Minor Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_FRONT\_DIR\_1 | \-1,018,214 | "Exterior Major Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_FRONT\_DIR\_2 | \-1,018,215 | "Exterior Minor Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_TOP\_DIR\_1 | \-1,018,113 | "Top Major Hook Type" |
| REBAR\_SYSTEM\_HOOK\_TYPE\_TOP\_DIR\_2 | \-1,018,114 | "Top Minor Hook Type" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_BOTTOM\_DIR\_1\_NO\_SPACING | \-1,018,013 | "Bottom/Interior Major (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_BOTTOM\_DIR\_1\_WITH\_SPACING | \-1,018,012 | "Bottom/Interior Major" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_BOTTOM\_DIR\_2\_NO\_SPACING | \-1,018,015 | "Bottom/Interior Minor (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_BOTTOM\_DIR\_2\_WITH\_SPACING | \-1,018,014 | "Bottom/Interior Minor" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_DIR\_1\_NO\_SPACING | \-1,018,017 | "Major, Both Faces (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_DIR\_1\_WITH\_SPACING | \-1,018,016 | "Major, Both Faces" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_DIR\_2\_NO\_SPACING | \-1,018,019 | "Minor, Both Faces (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_DIR\_2\_WITH\_SPACING | \-1,018,018 | "Minor, Both Faces" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_NO\_SPACING | \-1,018,003 | "Layer Summary (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_TOP\_DIR\_1\_NO\_SPACING | \-1,018,009 | "Top/Exterior Major (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_TOP\_DIR\_1\_WITH\_SPACING | \-1,018,008 | "Top/Exterior Major" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_TOP\_DIR\_2\_NO\_SPACING | \-1,018,011 | "Top/Exterior Minor (Brief)" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_TOP\_DIR\_2\_WITH\_SPACING | \-1,018,010 | "Top/Exterior Minor" |
| REBAR\_SYSTEM\_LAYER\_SUMMARY\_WITH\_SPACING | \-1,018,002 | "Layer Summary" |
| REBAR\_SYSTEM\_LAYOUT\_RULE | \-1,018,001 | "Layout Rule" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_BACK\_DIR\_1 | \-1,018,220 | "Interior Major Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_BACK\_DIR\_2 | \-1,018,221 | "Interior Minor Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_BOTTOM\_DIR\_1 | \-1,018,119 | "Bottom Major Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_BOTTOM\_DIR\_1\_GENERIC | \-1,018,268 | "Bottom/Interior Major Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_BOTTOM\_DIR\_2 | \-1,018,120 | "Bottom Minor Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_BOTTOM\_DIR\_2\_GENERIC | \-1,018,269 | "Bottom/Interior Minor Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_FRONT\_DIR\_1 | \-1,018,218 | "Exterior Major Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_FRONT\_DIR\_2 | \-1,018,219 | "Exterior Minor Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_TOP\_DIR\_1 | \-1,018,117 | "Top Major Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_TOP\_DIR\_1\_GENERIC | \-1,018,266 | "Top/Exterior Major Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_TOP\_DIR\_2 | \-1,018,118 | "Top Minor Number Of Lines" |
| REBAR\_SYSTEM\_NUMBER\_OF\_LINES\_TOP\_DIR\_2\_GENERIC | \-1,018,267 | "Top/Exterior Minor Number Of Lines" |
| REBAR\_SYSTEM\_OVERRIDE | \-1,018,005 | "Override Area Reinforcement Settings" |
| REBAR\_SYSTEM\_SPACING\_BACK\_DIR\_1 | \-1,018,224 | "Interior Major Spacing" |
| REBAR\_SYSTEM\_SPACING\_BACK\_DIR\_2 | \-1,018,225 | "Interior Minor Spacing" |
| REBAR\_SYSTEM\_SPACING\_BOTTOM\_DIR\_1 | \-1,018,123 | "Bottom Major Spacing" |
| REBAR\_SYSTEM\_SPACING\_BOTTOM\_DIR\_1\_GENERIC | \-1,018,272 | "Bottom/Interior Major Spacing" |
| REBAR\_SYSTEM\_SPACING\_BOTTOM\_DIR\_2 | \-1,018,124 | "Bottom Minor Spacing" |
| REBAR\_SYSTEM\_SPACING\_BOTTOM\_DIR\_2\_GENERIC | \-1,018,273 | "Bottom/Interior Minor Spacing" |
| REBAR\_SYSTEM\_SPACING\_FRONT\_DIR\_1 | \-1,018,222 | "Exterior Major Spacing" |
| REBAR\_SYSTEM\_SPACING\_FRONT\_DIR\_2 | \-1,018,223 | "Exterior Minor Spacing" |
| REBAR\_SYSTEM\_SPACING\_TOP\_DIR\_1 | \-1,018,121 | "Top Major Spacing" |
| REBAR\_SYSTEM\_SPACING\_TOP\_DIR\_1\_GENERIC | \-1,018,270 | "Top/Exterior Major Spacing" |
| REBAR\_SYSTEM\_SPACING\_TOP\_DIR\_2 | \-1,018,122 | "Top Minor Spacing" |
| REBAR\_SYSTEM\_SPACING\_TOP\_DIR\_2\_GENERIC | \-1,018,271 | "Top/Exterior Minor Spacing" |
| REBAR\_SYSTEM\_SPANACTIVE\_DIR\_1 | \-1,018,050 | "Bars In Major Direction" |
| REBAR\_SYSTEM\_SPANACTIVE\_DIR\_2 | \-1,018,051 | "Bars In Minor Direction" |
| REBAR\_SYSTEM\_SPANHOOK\_BOTTOM\_DIR\_2 | \-1,018,054 | "Hook Angle Bottom" |
| REBAR\_SYSTEM\_SPANHOOK\_LEFT\_DIR\_1 | \-1,018,052 | "Hook Angle Left" |
| REBAR\_SYSTEM\_SPANHOOK\_RIGHT\_DIR\_1 | \-1,018,053 | "Hook Angle Right" |
| REBAR\_SYSTEM\_SPANHOOK\_TOP\_DIR\_2 | \-1,018,055 | "Hook Angle Top" |
| REBAR\_SYSTEM\_TOP\_MAJOR\_MATCHES\_BOTTOM\_MAJOR | \-1,018,022 | "Top and Bottom Major Layers Match" |
| REBAR\_SYSTEM\_TOP\_MAJOR\_MATCHES\_TOP\_MINOR | \-1,018,020 | "Top Major and Minor Layers Match" |
| REBAR\_SYSTEM\_TOP\_MINOR\_MATCHES\_BOTTOM\_MINOR | \-1,018,023 | "Top and Bottom Minor Layers Match" |
| REBAR\_TERMINATION\_ROTATION\_AT\_END | \-1,155,206 | "Rotation At End" |
| REBAR\_TERMINATION\_ROTATION\_AT\_END\_SCHEDULES\_TAGS\_FILTERS | \-1,155,217 | "Rotation At End" |
| REBAR\_TERMINATION\_ROTATION\_AT\_START | \-1,155,205 | "Rotation At Start" |
| REBAR\_TERMINATION\_ROTATION\_AT\_START\_SCHEDULES\_TAGS\_FILTERS | \-1,155,216 | "Rotation At Start" |
| REBAR\_TYPE\_AT\_END | \-1,180,437 | "End of Bar" |
| REBAR\_TYPE\_AT\_START | \-1,180,436 | "Start of Bar" |
| REBAR\_WORKSHOP\_INSTRUCTIONS | \-1,154,695 | "Workshop Instructions" |
| RECT\_MULLION\_THICK | \-1,007,304 | "Thickness" |
| RECT\_MULLION\_WIDTH1 | \-1,007,300 | "Width on side 1" |
| RECT\_MULLION\_WIDTH2 | \-1,007,301 | "Width on side 2" |
| REF\_TABLE\_ELEM\_NAME | \-1,007,850 | "Key Name" |
| REF\_TABLE\_PARAM\_NAME | \-1,007,851 | "Parameter Name" |
| REFERENCE\_BASE\_ON\_HOST | \-1,155,251 | "Reference Base on Host" |
| REFERENCE\_LINE\_SUBCATEGORY | \-1,006,221 | "Subcategory" |
| REFERENCE\_OTHER\_VIEW\_UI\_REF\_VIEW | \-1,140,759 | "Reference View": This is used by the UI to allow selection of view reference. |
| REFERENCE\_OTHER\_VIEW\_UI\_TOGGLE | \-1,140,758 | "Reference Other View": This is used to determine whether reference other view is enable or not. |
| REFERENCE\_VIEWER\_ATTR\_TAG | \-1,140,756 | "View Reference Tag" |
| REFERENCE\_VIEWER\_TARGET\_VIEW | \-1,140,755 | "Target view" |
| REFERENCE\_VIEWER\_UI\_TARGET\_FILTER | \-1,141,000 | "Filter": This is used by the UI to filter the list of target views. |
| REFERENCE\_VIEWER\_UI\_TARGET\_VIEW | \-1,141,001 | "Target view": This is used by the UI to allow selection of target view.  It allows the UI to set a filter that is incompatible  with the current target view (REFERENCE\_VIEWER\_TARGET\_VIEW). |
| REFERENCED\_VIEW | \-1,152,380 | "Referenced View": The view referenced by a section or callout. |
| REIN\_EST\_BAR\_LENGTH | \-1,018,501 | "Estimated Total Bar Length" |
| REIN\_EST\_BAR\_VOLUME | \-1,018,502 | "Estimated Reinforcement Volume" |
| REIN\_EST\_NUMBER\_OF\_BARS | \-1,018,500 | "Estimated Number of Bars" |
| REINFORCEMENT\_VOLUME | \-1,018,503 | "Reinforcement Volume" |
| RELATED\_TO\_MASS | \-1,001,713 | "Related to Mass" |
| RELATIVE\_ROUGHNESS | \-1,140,210 | "Relative Roughness" |
| RENDER\_PLANT\_HEIGHT | \-1,005,193 | "Height" |
| RENDER\_PLANT\_NAME | \-1,005,192 | "Plant Name" |
| RENDER\_PLANT\_TRIM\_HEIGHT | \-1,005,194 | "Plant Trim Height" |
| RENDER\_RPC\_FILENAME | \-1,005,195 | "Render Appearance" |
| RENDER\_RPC\_PROPERTIES | \-1,005,198 | "Render Appearance Properties" |
| REPEATING\_DETAIL\_ELEMENT | \-1,011,106 | "Detail" |
| REPEATING\_DETAIL\_INSIDE | \-1,011,107 | "Inside" |
| REPEATING\_DETAIL\_LAYOUT | \-1,011,105 | "Layout" |
| REPEATING\_DETAIL\_NUMBER | \-1,011,103 | "Number" |
| REPEATING\_DETAIL\_ROTATION | \-1,011,109 | "Detail Rotation" |
| REPEATING\_DETAIL\_SPACING | \-1,011,104 | "Spacing" |
| REVEAL\_PROFILE\_PARAM | \-1,012,835 | "Profile" |
| REVISION\_CLOUD\_REVISION | \-1,011,900 | "Revision" |
| REVISION\_CLOUD\_REVISION\_DATE | \-1,011,903 | "Revision Date" |
| REVISION\_CLOUD\_REVISION\_DESCRIPTION | \-1,011,902 | "Revision Description" |
| REVISION\_CLOUD\_REVISION\_ISSUED\_BY | \-1,011,906 | "Issued by" |
| REVISION\_CLOUD\_REVISION\_ISSUED\_TO | \-1,011,904 | "Issued to" |
| REVISION\_CLOUD\_REVISION\_NUM | \-1,011,901 | "Revision Number" |
| REVOLUTION\_END\_ANGLE | \-1,001,803 | "End Angle" |
| REVOLUTION\_START\_ANGLE | \-1,001,802 | "Start Angle" |
| RGB\_B\_PARAM | \-1,010,024 | "Blue value for RGB color spec. (for Use with XAML Data Template example)" |
| RGB\_G\_PARAM | \-1,010,023 | "Green value for RGB color spec. (for Use with XAML Data Template example)" |
| RGB\_R\_PARAM | \-1,010,022 | "Red value for RGB color spec. (for Use with XAML Data Template example)" |
| ROOF\_ATTR\_DEFAULT\_THICKNESS\_PARAM | \-1,001,600 | "Default Thickness" |
| ROOF\_ATTR\_THICKNESS\_PARAM | \-1,001,601 | "Thickness" |
| ROOF\_BASE\_LEVEL\_PARAM | \-1,001,708 | "Base Level" |
| ROOF\_CONSTRAINT\_LEVEL\_PARAM | \-1,001,651 | "Reference Level" |
| ROOF\_CONSTRAINT\_OFFSET\_PARAM | \-1,001,652 | "Level Offset" |
| ROOF\_CURVE\_HEIGHT\_AT\_WALL | \-1,006,005 | "Plate Offset From Base" |
| ROOF\_CURVE\_HEIGHT\_OFFSET | \-1,006,001 | "Offset From Roof Base" |
| ROOF\_CURVE\_IS\_SLOPE\_DEFINING | \-1,006,000 | "Defines Roof Slope" |
| ROOF\_EAVE\_CUT\_PARAM | \-1,001,710 | "Rafter Cut" |
| ROOF\_FACES\_LOCATION | \-1,001,714 | "Picked Faces Location" |
| ROOF\_LEVEL\_OFFSET\_PARAM | \-1,001,701 | "Base Offset From Level" |
| ROOF\_RAFTER\_OR\_TRUSS\_PARAM | \-1,001,709 | "Rafter or Truss" |
| ROOF\_SLOPE | \-1,006,016 | "Slope" |
| ROOF\_STRUCTURE\_ID\_PARAM | \-1,002,117 | "Structure" |
| ROOF\_UPTO\_LEVEL\_OFFSET\_PARAM | \-1,001,703 | "Cutoff Offset" |
| ROOF\_UPTO\_LEVEL\_PARAM | \-1,001,702 | "Cutoff Level" |
| ROOM\_ACTUAL\_EXHAUST\_AIRFLOW\_PARAM | \-1,114,196 | "Actual Exhaust Airflow" |
| ROOM\_ACTUAL\_LIGHTING\_LOAD\_PARAM | \-1,114,226 | "Actual Lighting Load" |
| ROOM\_ACTUAL\_LIGHTING\_LOAD\_PER\_AREA\_PARAM | \-1,114,261 | "Actual Lighting Load per area" |
| ROOM\_ACTUAL\_POWER\_LOAD\_PARAM | \-1,114,225 | "Actual Power Load" |
| ROOM\_ACTUAL\_POWER\_LOAD\_PER\_AREA\_PARAM | \-1,114,260 | "Actual Power Load per area" |
| ROOM\_ACTUAL\_RETURN\_AIRFLOW\_PARAM | \-1,114,195 | "Actual Return Airflow" |
| ROOM\_ACTUAL\_SUPPLY\_AIRFLOW\_PARAM | \-1,114,194 | "Actual Supply Airflow" |
| ROOM\_AIR\_CHANGES\_PER\_HOUR\_PARAM | \-1,154,671 | "Air Changes per Hour" |
| ROOM\_AREA | \-1,006,902 | "Area" |
| ROOM\_AREA\_PER\_PERSON\_PARAM | \-1,114,175 | "Area per Person" |
| ROOM\_BASE\_HEAT\_LOAD\_ON\_PARAM | \-1,114,259 | "Heat Load Values" |
| ROOM\_BASE\_LIGHTING\_LOAD\_ON\_PARAM | \-1,114,224 | "Base Lighting Load on" |
| ROOM\_BASE\_POWER\_LOAD\_ON\_PARAM | \-1,114,223 | "Base Power Load on" |
| ROOM\_BASE\_RETURN\_AIRFLOW\_ON\_PARAM | \-1,114,252 | "Return Airflow" |
| ROOM\_CALCULATED\_COOLING\_LOAD\_PARAM | \-1,114,255 | "Calculated Cooling Load" |
| ROOM\_CALCULATED\_COOLING\_LOAD\_PER\_AREA\_PARAM | \-1,114,322 | "Calculated Cooling Load per area" |
| ROOM\_CALCULATED\_HEATING\_LOAD\_PARAM | \-1,114,253 | "Calculated Heating Load" |
| ROOM\_CALCULATED\_HEATING\_LOAD\_PER\_AREA\_PARAM | \-1,114,321 | "Calculated Heating Load per area" |
| ROOM\_CALCULATED\_SUPPLY\_AIRFLOW\_PARAM | \-1,114,180 | "Calculated Supply Airflow" |
| ROOM\_CALCULATED\_SUPPLY\_AIRFLOW\_PER\_AREA\_PARAM | \-1,114,323 | "Calculated Supply Airflow per area" |
| ROOM\_CALCULATION\_POINT | \-1,114,399 | "Room Calculation Point" |
| ROOM\_COMPUTATION\_HEIGHT | \-1,006,928 | "Computation Height" |
| ROOM\_COMPUTATION\_METHOD | \-1,006,926 | "Computation" |
| ROOM\_CONDITION\_TYPE\_PARAM | \-1,114,171 | "Condition Type" |
| ROOM\_CONSTRUCTION\_SET\_PARAM | \-1,114,251 | "Construction Type" |
| ROOM\_DEPARTMENT | \-1,006,907 | "Department" |
| ROOM\_DESIGN\_COOLING\_LOAD\_PARAM | \-1,114,256 | "Design Cooling Load" |
| ROOM\_DESIGN\_EXHAUST\_AIRFLOW\_PARAM | \-1,114,178 | "Specified Exhaust Airflow" |
| ROOM\_DESIGN\_HEATING\_LOAD\_PARAM | \-1,114,254 | "Design Heating Load" |
| ROOM\_DESIGN\_LIGHTING\_LOAD\_PARAM | \-1,114,230 | "Specified Lighting Load" |
| ROOM\_DESIGN\_LIGHTING\_LOAD\_PER\_AREA\_PARAM | \-1,114,220 | "Specified Lighting Load per area" |
| ROOM\_DESIGN\_MECHANICAL\_LOAD\_PER\_AREA\_PARAM | \-1,114,221 | "Design HVAC Load per area" |
| ROOM\_DESIGN\_OTHER\_LOAD\_PER\_AREA\_PARAM | \-1,114,222 | "Design Other Load per area" |
| ROOM\_DESIGN\_POWER\_LOAD\_PARAM | \-1,114,229 | "Specified Power Load" |
| ROOM\_DESIGN\_POWER\_LOAD\_PER\_AREA\_PARAM | \-1,114,219 | "Specified Power Load per area" |
| ROOM\_DESIGN\_RETURN\_AIRFLOW\_PARAM | \-1,114,177 | "Specified Return Airflow" |
| ROOM\_DESIGN\_SUPPLY\_AIRFLOW\_PARAM | \-1,114,176 | "Specified Supply Airflow" |
| ROOM\_EDIT\_ELECTRICAL\_LOADS\_PARAM | \-1,114,284 | "Electrical Loads" |
| ROOM\_EDIT\_PEOPLE\_LOADS\_PARAM | \-1,114,283 | "People" |
| ROOM\_FINISH\_BASE | \-1,006,906 | "Base Finish" |
| ROOM\_FINISH\_CEILING | \-1,006,905 | "Ceiling Finish" |
| ROOM\_FINISH\_FLOOR | \-1,006,903 | "Floor Finish" |
| ROOM\_FINISH\_WALL | \-1,006,904 | "Wall Finish" |
| ROOM\_HEIGHT | \-1,006,920 | "Unbounded Height" |
| ROOM\_LEVEL\_ID | \-1,006,916 | "Level" |
| ROOM\_LIGHTING\_LOAD\_UNITS\_PARAM | \-1,114,258 | "Lighting Load Units" |
| ROOM\_LOWER\_OFFSET | \-1,006,925 | "Base Offset" |
| ROOM\_NAME | \-1,006,900 | "Name" |
| ROOM\_NUMBER | \-1,006,901 | "Number" |
| ROOM\_NUMBER\_OF\_PEOPLE\_PARAM | \-1,114,174 | "Number of People" |
| ROOM\_OCCUPANCY | \-1,006,909 | "Occupancy" |
| ROOM\_OCCUPANCY\_UNIT\_PARAM | \-1,114,173 | "Occupancy Unit" |
| ROOM\_OUTDOOR\_AIR\_INFO\_PARAM | \-1,154,662 | "Outdoor Air Information" |
| ROOM\_OUTDOOR\_AIR\_PER\_AREA\_PARAM | \-1,154,668 | "Outdoor Air per Area" |
| ROOM\_OUTDOOR\_AIR\_PER\_PERSON\_PARAM | \-1,154,665 | "Outdoor Air per Person" |
| ROOM\_OUTDOOR\_AIRFLOW\_PARAM | \-1,154,689 | "Outdoor Airflow" |
| ROOM\_OUTDOOR\_AIRFLOW\_STANDARD\_PARAM | \-1,154,687 | "Outdoor Air Method" |
| ROOM\_PEOPLE\_LATENT\_HEAT\_GAIN\_PER\_PERSON\_PARAM | \-1,114,189 | "Latent Heat Gain per person" |
| ROOM\_PEOPLE\_SENSIBLE\_HEAT\_GAIN\_PER\_PERSON\_PARAM | \-1,114,239 | "Sensible Heat Gain per person" |
| ROOM\_PEOPLE\_TOTAL\_HEAT\_GAIN\_PER\_PERSON\_PARAM | \-1,114,188 | "Total Heat Gain per person" |
| ROOM\_PERIMETER | \-1,006,917 | "Perimeter" |
| ROOM\_PHASE | \-1,012,113 | "Phase" |
| ROOM\_PHASE\_ID | \-1,012,112 | "Phase Id" |
| ROOM\_PLENUM\_LIGHTING\_PARAM | \-1,150,188 | "Plenum Lighting Contribution" |
| ROOM\_POWER\_LOAD\_UNITS\_PARAM | \-1,114,257 | "Power Load Units" |
| ROOM\_SPACE\_TYPE\_PARAM | \-1,114,172 | "Space Type" |
| ROOM\_TAG\_ORIENTATION\_PARAM | \-1,007,004 | "Orientation" |
| ROOM\_UPPER\_LEVEL | \-1,006,922 | "Upper Limit" |
| ROOM\_UPPER\_OFFSET | \-1,006,924 | "Limit Offset" |
| ROOM\_VOLUME | \-1,006,921 | "Volume" |
| ROTATE\_ANGLE | \-1,027,502 | "Rotation Angle" |
| ROTATE\_COPY | \-1,027,501 | "Copy" |
| ROTATE\_DISJOIN | \-1,027,500 | "Disjoin" |
| ROUTE\_ANALYSIS\_SETTINGS\_PARAM | \-1,155,095 | "Route Analysis Settings" |
| ROUTING\_PREFERENCE\_PARAM | \-1,140,281 | "Routing Preference" |
| RVT\_HOST\_LEVEL | \-1,007,724 | "Map Levels..." |
| RVT\_LEVEL\_OFFSET | \-1,007,725 | "Map Levels..." |
| RVT\_LINK\_FILE\_NAME\_WITHOUT\_EXT | \-1,007,726 | "File Name" |
| RVT\_LINK\_INSTANCE\_NAME | \-1,007,721 | "Name" |
| RVT\_LINK\_INSTANCE\_PROJECT\_INFORMATION | \-1,007,729 | "Project Information" |
| RVT\_LINK\_PHASE\_MAP | \-1,007,728 | "Phase Mapping" |
| RVT\_LINK\_REFERENCE\_TYPE | \-1,007,727 | "Reference Type" |
| RVT\_SOURCE\_LEVEL | \-1,007,723 | "Map Levels..." |
| SCALE\_FACTOR\_PARAM | \-1,001,010 | "Scale" |
| SCHEDULE\_BASE\_LEVEL\_OFFSET\_PARAM | \-1,002,065 | "Base Offset" |
| SCHEDULE\_BASE\_LEVEL\_PARAM | \-1,002,063 | "Base Level" |
| SCHEDULE\_CATEGORY | \-1,001,717 | "Category" |
| SCHEDULE\_EMBEDDED\_PARAM | \-1,007,806 | "Embedded Schedule" |
| SCHEDULE\_FIELDS\_PARAM | \-1,007,800 | "Fields" |
| SCHEDULE\_FILTER\_PARAM | \-1,007,801 | "Filter" |
| SCHEDULE\_FORMAT\_PARAM | \-1,007,804 | "Formatting" |
| SCHEDULE\_GROUP\_PARAM | \-1,007,803 | "Sorting/Grouping" |
| SCHEDULE\_LEVEL\_PARAM | \-1,002,062 | "Level" |
| SCHEDULE\_RESIZE\_ROWS | \-1,155,281 | "Resize Rows" |
| SCHEDULE\_ROTATION\_ON\_SHEET | \-1,155,280 | "Rotation on Sheet" |
| SCHEDULE\_ROW\_HEIGHT\_INPUT | \-1,155,282 | "Row Height" |
| SCHEDULE\_SHEET\_APPEARANCE\_PARAM | \-1,007,805 | "Appearance" |
| SCHEDULE\_TOP\_LEVEL\_OFFSET\_PARAM | \-1,002,066 | "Top Offset" |
| SCHEDULE\_TOP\_LEVEL\_PARAM | \-1,002,064 | "Top Level" |
| SCHEDULE\_TYPE\_FOR\_BROWSER | \-1,001,718 | "Schedule Type" |
| SECTION\_ATTR\_HEAD\_TAG | \-1,006,600 | "Section Head" |
| SECTION\_ATTR\_TAIL\_LENGTH | \-1,006,603 | "Tail length" |
| SECTION\_ATTR\_TAIL\_TAG | \-1,006,608 | "Section Tail" |
| SECTION\_ATTR\_TAIL\_WIDTH | \-1,006,604 | "Tail width" |
| SECTION\_BROKEN\_DISPLAY\_STYLE | \-1,006,615 | "Broken Section Display Style" |
| SECTION\_COARSER\_SCALE\_PULLDOWN\_IMPERIAL | \-1,006,614 | "Hide at scales coarser than" |
| SECTION\_COARSER\_SCALE\_PULLDOWN\_METRIC | \-1,006,613 | "Hide at scales coarser than" |
| SECTION\_PARENT\_VIEW\_NAME | \-1,006,612 | "Parent View" |
| SECTION\_SHOW\_IN\_ONE\_VIEW\_ONLY | \-1,006,609 | "Show in" |
| SECTION\_TAG | \-1,008,205 | "Section Tag" |
| SEEK\_ITEM\_ID | \-1,002,504 | "Seek Item ID" |
| SELECTION\_EDITABLE\_ONLY | \-1,002,072 | "Editable only" |
| SHEET\_APPROVED\_BY | \-1,007,408 | "Approved By" |
| SHEET\_ASSEMBLY\_ASSEMBLY\_CODE | \-1,150,456 | "Assembly: Assembly Code" |
| SHEET\_ASSEMBLY\_ASSEMBLY\_DESCRIPTION | \-1,150,459 | "Assembly: Assembly Description" |
| SHEET\_ASSEMBLY\_COST | \-1,150,458 | "Assembly: Cost" |
| SHEET\_ASSEMBLY\_DESCRIPTION | \-1,150,455 | "Assembly: Description" |
| SHEET\_ASSEMBLY\_KEYNOTE | \-1,150,460 | "Assembly: Keynote" |
| SHEET\_ASSEMBLY\_MANUFACTURER | \-1,150,452 | "Assembly: Manufacturer" |
| SHEET\_ASSEMBLY\_MODEL | \-1,150,451 | "Assembly: Model" |
| SHEET\_ASSEMBLY\_NAME | \-1,150,450 | "Assembly: Name" |
| SHEET\_ASSEMBLY\_TYPE\_COMMENTS | \-1,150,453 | "Assembly: Type Comments" |
| SHEET\_ASSEMBLY\_TYPE\_MARK | \-1,150,457 | "Assembly: Type Mark" |
| SHEET\_ASSEMBLY\_URL | \-1,150,454 | "Assembly: URL" |
| SHEET\_CHECKED\_BY | \-1,007,405 | "Checked By" |
| SHEET\_COLLECTION | \-1,007,421 | "Sheet Collection" |
| SHEET\_COLLECTION\_NAME | \-1,007,071 | "Name" |
| SHEET\_CURRENT\_REVISION | \-1,007,412 | "Current Revision" |
| SHEET\_CURRENT\_REVISION\_DATE | \-1,007,415 | "Current Revision Date" |
| SHEET\_CURRENT\_REVISION\_DESCRIPTION | \-1,007,414 | "Current Revision Description" |
| SHEET\_CURRENT\_REVISION\_ISSUED | \-1,007,418 | "Current Revision Issued" |
| SHEET\_CURRENT\_REVISION\_ISSUED\_BY | \-1,007,417 | "Current Revision Issued By" |
| SHEET\_CURRENT\_REVISION\_ISSUED\_TO | \-1,007,416 | "Current Revision Issued To" |
| SHEET\_DATE | \-1,007,403 | "Date/Time Stamp" |
| SHEET\_DESIGNED\_BY | \-1,007,407 | "Designed By" |
| SHEET\_DRAWN\_BY | \-1,007,404 | "Drawn By" |
| SHEET\_FILE\_PATH | \-1,007,409 | "File Path" |
| SHEET\_GUIDE\_GRID | \-1,007,419 | "Guide Grid" |
| SHEET\_HEIGHT | \-1,007,411 | "Sheet Height" |
| SHEET\_ISSUE\_DATE | \-1,006,322 | "Sheet Issue Date" |
| SHEET\_KEY\_NUMBER | \-1,140,420 | "Sheet Key Number" |
| SHEET\_NAME | \-1,007,400 | "Sheet Name" |
| SHEET\_NUMBER | \-1,007,401 | "Sheet Number" |
| SHEET\_PRIMARY\_TITLE\_BLOCK | \-1,007,422 | "Primary Title Block" |
| SHEET\_REVISIONS\_ON\_SHEET | \-1,007,413 | "Revisions on Sheet" |
| SHEET\_SCALE | \-1,007,402 | "Scale" |
| SHEET\_SCALE\_OVERRIDE | \-1,155,322 | "Scale Override (Multiple Values)" |
| SHEET\_SCHEDULED | \-1,007,406 | "Appears In Sheet List" |
| SHEET\_WIDTH | \-1,007,410 | "Sheet Width" |
| SHOW\_ARROWHEAD\_TO\_CUT\_MARK | \-1,006,630 | "Show Arrowhead to Cut Mark" |
| SHOW\_ICON\_PARAM | \-1,010,016 | "Flag to display icon in Ribbon Combo Item" |
| SHOW\_TITLE | \-1,006,333 | "Show Title" |
| SKETCH\_GRID\_SPACING\_PARAM | \-1,013,000 | "Work Plane Grid Spacing" |
| SKETCH\_PLANE\_PARAM | \-1,001,380 | "Work Plane" |
| SLAB\_EDGE\_MATERIAL\_PARAM | \-1,012,824 | "Material" |
| SLAB\_EDGE\_PROFILE\_PARAM | \-1,012,837 | "Profile" |
| SLANTED\_COLUMN\_BASE\_CUT\_STYLE | \-1,150,205 | "Base Cut Style" |
| SLANTED\_COLUMN\_BASE\_EXTENSION | \-1,150,207 | "Base Extension" |
| SLANTED\_COLUMN\_GEOMETRY\_TREATMENT\_BASE | \-1,150,190 | "Base Geometry Alignment" |
| SLANTED\_COLUMN\_GEOMETRY\_TREATMENT\_TOP | \-1,150,189 | "Top Geometry Alignment" |
| SLANTED\_COLUMN\_TOP\_CUT\_STYLE | \-1,150,204 | "Top Cut Style" |
| SLANTED\_COLUMN\_TOP\_EXTENSION | \-1,150,206 | "Top Extension" |
| SLANTED\_COLUMN\_TYPE\_PARAM | \-1,150,171 | "Column Style" |
| SLOPE\_ARROW\_LEVEL\_END | \-1,006,011 | "Level at Head" |
| SLOPE\_ARROW\_LEVEL\_START | \-1,006,010 | "Level at Tail" |
| SLOPE\_END\_HEIGHT | \-1,002,401 | "Height Offset at Head" |
| SLOPE\_START\_HEIGHT | \-1,002,400 | "Height Offset at Tail" |
| SPACE\_AIR\_CHANGES\_PER\_HOUR | \-1,114,811 | "Air Changes per Hour" |
| SPACE\_AIRFLOW\_PER\_AREA\_PARAM | \-1,114,802 | "Airflow per area" |
| SPACE\_AREA | \-1,114,820 | "Area" |
| SPACE\_AREA\_PER\_PERSON\_PARAM | \-1,114,803 | "Area per person" |
| SPACE\_ASSOC\_ROOM\_NAME | \-1,114,327 | "Room Name" |
| SPACE\_ASSOC\_ROOM\_NUMBER | \-1,114,328 | "Room Number" |
| SPACE\_CARPETING\_PARAM | \-1,114,347 | "Carpeting" |
| SPACE\_COMPOSEDNAME\_PARAM | \-1,114,848 | "Composed Name" |
| SPACE\_CONDITION\_TYPE | \-1,114,837 | "Condition Type" |
| SPACE\_COOLING\_SET\_POINT | \-1,114,709 | "Cooling Set Point" |
| SPACE\_DEHUMIDIFICATION\_SET\_POINT | \-1,114,711 | "Dehumidification Set Point" |
| SPACE\_ELEC\_EQUIPMENT\_RADIANT\_PERCENTAGE\_PARAM | \-1,114,353 | "Electrical Equipment Radiant" |
| SPACE\_HEATING\_SET\_POINT | \-1,114,708 | "Heating Set Point" |
| SPACE\_HUMIDIFICATION\_SET\_POINT | \-1,114,710 | "Humidification Set Point" |
| SPACE\_INFILTRATION\_AIRFLOW | \-1,114,816 | "Infiltration Airflow" |
| SPACE\_INFILTRATION\_AIRFLOW\_PER\_AREA | \-1,114,815 | "Infiltration Airflow per area" |
| SPACE\_INFILTRATION\_PARAM | \-1,114,348 | "Infiltration Airflow per area" |
| SPACE\_IS\_OCCUPIABLE | \-1,114,329 | "Occupiable" |
| SPACE\_IS\_PLENUM | \-1,114,330 | "Plenum" |
| SPACE\_LIGHTING\_LOAD\_PARAM | \-1,114,809 | "Lighting Load" |
| SPACE\_LIGHTING\_LOAD\_PER\_AREA\_PARAM | \-1,114,806 | "Lighting Load per area" |
| SPACE\_LIGHTING\_SCHEDULE\_PARAM | \-1,114,350 | "Lighting Schedule" |
| SPACE\_NAME\_PARAM | \-1,114,825 | "Name" |
| SPACE\_NUMBER\_OF\_PEOPLE | \-1,114,838 | "Number of People" |
| SPACE\_NUMBER\_PARAM | \-1,114,847 | "Number" |
| SPACE\_OCCUPANCY\_SCHEDULE\_PARAM | \-1,114,349 | "Occupancy Schedule" |
| SPACE\_OUTDOOR\_AIRFLOW | \-1,114,814 | "Outdoor Airflow" |
| SPACE\_OUTDOOR\_AIRFLOW\_PER\_AREA | \-1,114,812 | "Outdoor Airflow per area" |
| SPACE\_OUTDOOR\_AIRFLOW\_PER\_PERSON | \-1,114,813 | "Outdoor Airflow per person" |
| SPACE\_PEOPLE\_ACTIVITY\_LEVEL\_PARAM | \-1,114,354 | "People Activity Level" |
| SPACE\_PEOPLE\_LATENT\_HEAT\_GAIN\_PER\_PERSON\_PARAM | \-1,114,805 | "Latent Heat Gain per person" |
| SPACE\_PEOPLE\_LOAD\_PARAM | \-1,114,808 | "Occupancy Load" |
| SPACE\_PEOPLE\_SENSIBLE\_HEAT\_GAIN\_PER\_PERSON\_PARAM | \-1,114,804 | "Sensible Heat Gain per person" |
| SPACE\_POWER\_LOAD\_PARAM | \-1,114,810 | "Power Load" |
| SPACE\_POWER\_LOAD\_PER\_AREA\_PARAM | \-1,114,807 | "Power Load per area" |
| SPACE\_POWER\_SCHEDULE\_PARAM | \-1,114,351 | "Power Schedule" |
| SPACE\_REFERENCE\_LEVEL\_PARAM | \-1,114,817 | "Reference Level" |
| SPACE\_TYPE\_GBXML | \-1,114,836 | "Space Type (gbXML)" |
| SPACE\_VOLUME | \-1,114,821 | "Volume" |
| SPACE\_ZONE\_NAME | \-1,114,384 | "Zone" |
| SPACING\_APPEND | \-1,007,398 | "Append Position" |
| SPACING\_JUSTIFICATION | \-1,013,353 | "Justification" |
| SPACING\_JUSTIFICATION\_1 | \-1,013,334 | "Justification" |
| SPACING\_JUSTIFICATION\_2 | \-1,013,335 | "Justification" |
| SPACING\_JUSTIFICATION\_HORIZ | \-1,013,305 | "Justification" |
| SPACING\_JUSTIFICATION\_U | \-1,013,374 | "Justification" |
| SPACING\_JUSTIFICATION\_V | \-1,013,375 | "Justification" |
| SPACING\_JUSTIFICATION\_VERT | \-1,013,304 | "Justification" |
| SPACING\_LAYOUT | \-1,013,350 | "Layout" |
| SPACING\_LAYOUT\_1 | \-1,013,330 | "Layout" |
| SPACING\_LAYOUT\_2 | \-1,013,331 | "Layout" |
| SPACING\_LAYOUT\_HORIZ | \-1,013,301 | "Layout" |
| SPACING\_LAYOUT\_U | \-1,013,370 | "Layout" |
| SPACING\_LAYOUT\_V | \-1,013,371 | "Layout" |
| SPACING\_LAYOUT\_VERT | \-1,013,300 | "Layout" |
| SPACING\_LENGTH | \-1,013,351 | "Spacing" |
| SPACING\_LENGTH\_1 | \-1,013,332 | "Spacing" |
| SPACING\_LENGTH\_2 | \-1,013,333 | "Spacing" |
| SPACING\_LENGTH\_HORIZ | \-1,013,303 | "Spacing" |
| SPACING\_LENGTH\_U | \-1,013,372 | "Distance" |
| SPACING\_LENGTH\_V | \-1,013,373 | "Distance" |
| SPACING\_LENGTH\_VERT | \-1,013,302 | "Spacing" |
| SPACING\_NUM\_DIVISIONS | \-1,013,352 | "Number" |
| SPACING\_NUM\_DIVISIONS\_1 | \-1,013,336 | "Number" |
| SPACING\_NUM\_DIVISIONS\_2 | \-1,013,337 | "Number" |
| SPACING\_NUM\_DIVISIONS\_HORIZ | \-1,013,307 | "Number" |
| SPACING\_NUM\_DIVISIONS\_U | \-1,013,376 | "Number" |
| SPACING\_NUM\_DIVISIONS\_V | \-1,013,377 | "Number" |
| SPACING\_NUM\_DIVISIONS\_VERT | \-1,013,306 | "Number" |
| SPAN\_DIR\_INST\_PARAM\_ANGLE | \-1,014,000 | "Span Direction" |
| SPAN\_DIR\_SYM\_PARAM\_BOTTOM | \-1,014,002 | "Bottom" |
| SPAN\_DIR\_SYM\_PARAM\_LEFT | \-1,014,003 | "Left" |
| SPAN\_DIR\_SYM\_PARAM\_RIGHT | \-1,014,004 | "Right" |
| SPAN\_DIR\_SYM\_PARAM\_TOP | \-1,014,001 | "Top" |
| SPATIAL\_FIELD\_MGR\_CURRENT\_NAME | \-1,006,851 | "Analysis Configuration" |
| SPATIAL\_FIELD\_MGR\_DESCRIPTION | \-1,006,852 | "Description" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_HEIGHT | \-1,006,858 | "Legend Height" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_HOR\_ORIGIN\_GAP | \-1,006,861 | "Legend Horizontal Origin Gap" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_SHOW\_CONFIG\_NAME | \-1,006,853 | "Show Configuration Name" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_SHOW\_DESCRIPTION | \-1,006,854 | "Show Description" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_TEXT\_TYPE | \-1,006,856 | "Overall Legend Text" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_VERT\_ORIGIN\_GAP | \-1,006,860 | "Legend Vertical Origin Gap" |
| SPATIAL\_FIELD\_MGR\_LEGEND\_WIDTH | \-1,006,859 | "Legend Width" |
| SPATIAL\_FIELD\_MGR\_RANGE | \-1,006,850 | "Data Range" |
| SPATIAL\_FIELD\_MGR\_RESULTS\_VISIBILITY | \-1,006,855 | "Results Visibility" |
| SPECIFY\_SLOPE\_OR\_OFFSET | \-1,006,012 | "Specify " |
| SPLICE\_BY\_RULES\_MAX\_LENGTH | \-1,180,402 | "Maximum bar length" |
| SPLICE\_BY\_RULES\_MIN\_LENGTH | \-1,180,403 | "Minimum bar length" |
| SPLICE\_BY\_RULES\_RUNOUT | \-1,180,404 | "Runout" |
| SPLICE\_LAP\_LENGTH\_AT\_END | \-1,180,406 | "Lap Length at End" |
| SPLICE\_LAP\_LENGTH\_AT\_START | \-1,180,405 | "Lap Length at Start" |
| SPLICE\_TYPE\_AT\_END | \-1,180,408 | "Splice at End" |
| SPLICE\_TYPE\_AT\_START | \-1,180,407 | "Splice at Start" |
| SPOT\_COORDINATE\_BASE | \-1,006,461 | "Coordinate Base" |
| SPOT\_COORDINATE\_BOTTOM\_PREFIX | \-1,006,484 | "Bottom Coordinate Prefix" |
| SPOT\_COORDINATE\_BOTTOM\_SUFFIX | \-1,006,485 | "Bottom Coordinate Suffix" |
| SPOT\_COORDINATE\_ELEVATION\_PREFIX | \-1,006,486 | "Elevation Prefix" |
| SPOT\_COORDINATE\_ELEVATION\_SUFFIX | \-1,006,487 | "Elevation Suffix" |
| SPOT\_COORDINATE\_INCLUDE\_ELEVATION | \-1,006,488 | "Include Elevation" |
| SPOT\_COORDINATE\_TOP\_PREFIX | \-1,006,482 | "Top Coordinate Prefix" |
| SPOT\_COORDINATE\_TOP\_SUFFIX | \-1,006,483 | "Top Coordinate Suffix" |
| SPOT\_DIM\_LEADER | \-1,006,466 | "Leader" |
| SPOT\_DIM\_LEADER\_LINE | \-1,006,596 | "Leader Line" |
| SPOT\_DIM\_STYLE\_SLOPE\_UNITS | \-1,150,154 | "Units Format" |
| SPOT\_DIM\_STYLE\_SLOPE\_UNITS\_ALT | \-1,150,143 | "Alternate Units Format" |
| SPOT\_ELEV\_BASE | \-1,006,437 | "Elevation Base" |
| SPOT\_ELEV\_BEND\_LEADER | \-1,006,476 | "Leader Shoulder" |
| SPOT\_ELEV\_BOT\_VALUE | \-1,006,457 | "Bottom Coordinate" |
| SPOT\_ELEV\_DISPLAY\_ELEVATIONS | \-1,006,469 | "Display Elevations" |
| SPOT\_ELEV\_FLIP\_TEXT\_VERT | \-1,006,440 | "Auto Mirror" |
| SPOT\_ELEV\_IND\_BOTTOM | \-1,006,473 | "Bottom Indicator" |
| SPOT\_ELEV\_IND\_ELEVATION | \-1,006,452 | "Elevation Indicator" |
| SPOT\_ELEV\_IND\_EW | \-1,006,451 | "East / West Indicator" |
| SPOT\_ELEV\_IND\_NS | \-1,006,450 | "North / South Indicator" |
| SPOT\_ELEV\_IND\_TOP | \-1,006,472 | "Top Indicator" |
| SPOT\_ELEV\_IND\_TYPE | \-1,006,458 | "Indicator as Prefix / Suffix" |
| SPOT\_ELEV\_IND\_TYPE\_BOTTOM | \-1,006,475 | "Bottom Indicator as Prefix/Suffix" |
| SPOT\_ELEV\_IND\_TYPE\_ELEVATION | \-1,006,489 | "Elevation Indicator as Prefix/Suffix" |
| SPOT\_ELEV\_IND\_TYPE\_TOP | \-1,006,474 | "Top Indicator as Prefix/Suffix" |
| SPOT\_ELEV\_LEADER\_ARROWHEAD | \-1,006,442 | "Leader Arrowhead" |
| SPOT\_ELEV\_LINE\_PEN | \-1,006,444 | "Leader Line Weight" |
| SPOT\_ELEV\_LOWER\_PREFIX | \-1,006,480 | "Lower Value Prefix" |
| SPOT\_ELEV\_LOWER\_SUFFIX | \-1,006,481 | "Lower Value Suffix" |
| SPOT\_ELEV\_LOWER\_VALUE | \-1,006,491 | "Lower Value" |
| SPOT\_ELEV\_RELATIVE\_BASE | \-1,006,441 | "Relative Base" |
| SPOT\_ELEV\_ROTATE\_WITH\_COMPONENT | \-1,006,470 | "Rotate with Component" |
| SPOT\_ELEV\_SINGLE\_OR\_UPPER\_PREFIX | \-1,006,478 | "Single/Upper Value Prefix" |
| SPOT\_ELEV\_SINGLE\_OR\_UPPER\_SUFFIX | \-1,006,479 | "Single/Upper Value Suffix" |
| SPOT\_ELEV\_SINGLE\_OR\_UPPER\_VALUE | \-1,006,490 | "Single/Upper Value" |
| SPOT\_ELEV\_SYMBOL | \-1,006,436 | "Symbol" |
| SPOT\_ELEV\_TEXT\_HORIZ\_OFFSET | \-1,006,439 | "Text Offset from Symbol" |
| SPOT\_ELEV\_TEXT\_LOCATION | \-1,006,471 | "Text Location" |
| SPOT\_ELEV\_TEXT\_ORIENTATION | \-1,006,453 | "Text Orientation" |
| SPOT\_ELEV\_TICK\_MARK\_PEN | \-1,006,443 | "Leader Arrowhead Line Weight" |
| SPOT\_ELEV\_TOP\_VALUE | \-1,006,455 | "Top Coordinate" |
| SPOT\_SLOPE\_LEADER\_LENGTH | \-1,150,152 | "Leader Line Length" |
| SPOT\_SLOPE\_OFFSET\_FROM\_REFERENCE | \-1,006,494 | "Offset from Reference" |
| SPOT\_SLOPE\_PREFIX | \-1,150,150 | "Prefix" |
| SPOT\_SLOPE\_SLOPE\_DIRECTION | \-1,006,492 | "Slope Direction" |
| SPOT\_SLOPE\_SLOPE\_REPRESENTATION | \-1,006,493 | "Slope Representation" |
| SPOT\_SLOPE\_SUFFIX | \-1,150,151 | "Suffix" |
| SPOT\_TEXT\_FROM\_LEADER | \-1,006,462 | "Text Offset from Leader" |
| SSE\_POINT\_BASETYPE\_ENUM | \-1,155,270 | "Point Base Type" |
| SSE\_POINT\_ELEVATION | \-1,155,272 | "Elevation" |
| SSE\_POINT\_ELEVATION\_BASE\_TYPE | \-1,155,273 | "Elevation Base Type" |
| SSE\_POINT\_OFFSET\_FROM\_SNAPS | \-1,155,285 | "Offset from Snaps" |
| SSE\_POINT\_OFFSET\_FROM\_SURFACE | \-1,155,271 | "Offset from Surface" |
| STAIRS\_ACTUAL\_NUM\_RISERS | \-1,007,246 | "Actual Number of Risers" |
| STAIRS\_ACTUAL\_NUMBER\_OF\_RISERS | \-1,151,111 | "Actual Number of Risers": The total number of actually created risers in model |
| STAIRS\_ACTUAL\_RISER\_HEIGHT | \-1,007,206 | "Actual Riser Height" |
| STAIRS\_ACTUAL\_TREAD\_DEPTH | \-1,007,250 | "Actual Tread Depth" |
| STAIRS\_ATTR\_BODY\_MATERIAL | \-1,007,268 | "Monolithic Material" |
| STAIRS\_ATTR\_BREAK\_SYM\_IN\_CUTLINE | \-1,007,245 | "Break Symbol in Plan" |
| STAIRS\_ATTR\_CALC\_ENABLED | \-1,007,254 | "Calculation Rules" |
| STAIRS\_ATTR\_CALC\_MAX | \-1,007,253 | "Calculation Rules" |
| STAIRS\_ATTR\_CALC\_MIN | \-1,007,252 | "Calculation Rules" |
| STAIRS\_ATTR\_EQ\_RESULT | \-1,007,251 | "Calculation Rules" |
| STAIRS\_ATTR\_FIRST\_RISER | \-1,007,257 | "Begin with Riser" |
| STAIRS\_ATTR\_LANDING\_CARRIAGE | \-1,007,267 | "Landing Carriage Height" |
| STAIRS\_ATTR\_LANDINGS\_OVERLAPPING | \-1,007,266 | "Landing Overlap" |
| STAIRS\_ATTR\_LAST\_RISER | \-1,007,258 | "End with Riser" |
| STAIRS\_ATTR\_LEFT\_SIDE\_STRINGER | \-1,007,264 | "Left Stringer" |
| STAIRS\_ATTR\_MAX\_RISER\_HEIGHT | \-1,007,202 | "Maximum Riser Height" |
| STAIRS\_ATTR\_MINIMUM\_TREAD\_DEPTH | \-1,007,203 | "Minimum Tread Depth" |
| STAIRS\_ATTR\_MONOLITHIC\_STAIRS | \-1,007,255 | "Monolithic Stairs" |
| STAIRS\_ATTR\_NOSING\_LENGTH | \-1,007,241 | "Nosing Length" |
| STAIRS\_ATTR\_NOSING\_PLACEMENT | \-1,007,263 | "Apply Nosing Profile" |
| STAIRS\_ATTR\_NUM\_MID\_STRINGERS | \-1,007,260 | "Middle Stringers" |
| STAIRS\_ATTR\_RIGHT\_SIDE\_STRINGER | \-1,007,265 | "Right Stringer" |
| STAIRS\_ATTR\_RISER\_ANGLE | \-1,007,212 | "Riser Angle" |
| STAIRS\_ATTR\_RISER\_MATERIAL | \-1,007,244 | "Riser Material" |
| STAIRS\_ATTR\_RISER\_MULT | \-1,007,248 | "Riser Multiplier" |
| STAIRS\_ATTR\_RISER\_THICKNESS | \-1,007,261 | "Riser Thickness" |
| STAIRS\_ATTR\_RISER\_TREAD\_CONNECT | \-1,007,262 | "Riser to Tread Connection" |
| STAIRS\_ATTR\_RISER\_TYPE | \-1,007,243 | "Riser Type" |
| STAIRS\_ATTR\_RISERS\_PRESENT | \-1,007,208 | "Risers Present" |
| STAIRS\_ATTR\_SIDE\_STRINGER\_TYPE\_PARAM | \-1,007,236 | "Type of Side Stringers" |
| STAIRS\_ATTR\_STAIR\_CALCULATOR | \-1,007,247 | "Calculation Rules" |
| STAIRS\_ATTR\_STAIRS\_BOTTOM | \-1,007,256 | "Underside of Winder" |
| STAIRS\_ATTR\_STAIRS\_CUT\_OFFSET | \-1,007,259 | "Extend Below Base" |
| STAIRS\_ATTR\_STRINGER\_CARRIAGE | \-1,007,237 | "Stringer Carriage Height" |
| STAIRS\_ATTR\_STRINGER\_HEIGHT | \-1,007,209 | "Stringer Height" |
| STAIRS\_ATTR\_STRINGER\_MATERIAL | \-1,007,239 | "Stringer Material" |
| STAIRS\_ATTR\_STRINGER\_OFFSET | \-1,007,238 | "Open Stringer Offset" |
| STAIRS\_ATTR\_STRINGER\_THICKNESS | \-1,007,210 | "Stringer Thickness" |
| STAIRS\_ATTR\_TEXT\_FONT | \-1,007,269 | "Text Font" |
| STAIRS\_ATTR\_TEXT\_SIZE | \-1,007,270 | "Text Size" |
| STAIRS\_ATTR\_TREAD\_FRONT\_PROFILE | \-1,007,240 | "Nosing Profile" |
| STAIRS\_ATTR\_TREAD\_MATERIAL | \-1,007,242 | "Tread Material" |
| STAIRS\_ATTR\_TREAD\_MULT | \-1,007,249 | "Tread Multiplier" |
| STAIRS\_ATTR\_TREAD\_THICKNESS | \-1,007,211 | "Tread Thickness" |
| STAIRS\_ATTR\_TREAD\_WIDTH | \-1,007,204 | "Width" |
| STAIRS\_ATTR\_TRIM\_TOP | \-1,007,277 | "Trim Stringers at Top" |
| STAIRS\_BASE\_LEVEL | \-1,151,101 | "Base Level": The base level of stairs |
| STAIRS\_BASE\_LEVEL\_PARAM | \-1,007,200 | "Base Level" |
| STAIRS\_BASE\_OFFSET | \-1,007,218 | "Base Offset" |
| STAIRS\_CURVE\_TYPE | \-1,006,100 | "Stairs Line Type" |
| STAIRS\_DBG\_SHOW\_ANNOTATION\_CUT\_MARK | \-1,151,153 | "Cut by Cut Plane" |
| STAIRS\_DBG\_SHOW\_BOUNDARY\_2D | \-1,151,144 | "Show Stairs' Boundary 2D" |
| STAIRS\_DBG\_SHOW\_BOUNDARY\_3D | \-1,151,145 | "Show Stairs' Boundary 3D" |
| STAIRS\_DBG\_SHOW\_LANDING\_BOUNDARY | \-1,151,142 | "Show Landing Boundary" |
| STAIRS\_DBG\_SHOW\_LANDING\_FACES | \-1,151,132 | "Show Landing Faces" |
| STAIRS\_DBG\_SHOW\_LANDING\_PATH | \-1,151,143 | "Show Landing Path" |
| STAIRS\_DBG\_SHOW\_LEFT\_RUN\_BOUNDARY\_2D | \-1,151,133 | "Show Run's Left Boundary 2D" |
| STAIRS\_DBG\_SHOW\_LEFT\_RUN\_BOUNDARY\_3D | \-1,151,135 | "Show Run's Left Boundary 3D" |
| STAIRS\_DBG\_SHOW\_MONOLITHIC\_SUPPORT\_CORSE\_GEOM | \-1,151,152 | "Show Monolithic Support Corse Geometry" |
| STAIRS\_DBG\_SHOW\_MONOLITHIC\_SUPPORT\_GEOM | \-1,151,149 | "Show Monolithic Support Geometry" |
| STAIRS\_DBG\_SHOW\_RIGHT\_RUN\_BOUNDARY\_2D | \-1,151,134 | "Show Run's Right Boundary 2D" |
| STAIRS\_DBG\_SHOW\_RIGHT\_RUN\_BOUNDARY\_3D | \-1,151,136 | "Show Run's Right Boundary 3D" |
| STAIRS\_DBG\_SHOW\_RUN\_CORSE\_GEOM | \-1,151,150 | "Show Run Corse Geometry" |
| STAIRS\_DBG\_SHOW\_RUN\_GEOM | \-1,151,147 | "Show Run Geometry" |
| STAIRS\_DBG\_SHOW\_RUN\_NOSING | \-1,151,140 | "Show Run's Nosings" |
| STAIRS\_DBG\_SHOW\_RUN\_OUTLINE\_FOR\_PLAN | \-1,151,141 | "Show Run Outline For Plan" |
| STAIRS\_DBG\_SHOW\_RUN\_PATH\_2D | \-1,151,137 | "Show Run's Path 2D" |
| STAIRS\_DBG\_SHOW\_RUN\_PATH\_3D | \-1,151,138 | "Show Run's Path 3D" |
| STAIRS\_DBG\_SHOW\_RUN\_RISER | \-1,151,139 | "Show Run's Risers" |
| STAIRS\_DBG\_SHOW\_SUPPORT\_PATH | \-1,151,146 | "Show Support Path" |
| STAIRS\_DBG\_SHOW\_TREAD\_FACES | \-1,151,131 | "Show Run's Tread Faces" |
| STAIRS\_DBG\_SHOW\_TRISER\_CORSE\_GEOM | \-1,151,151 | "Show Triser Corse Geometry" |
| STAIRS\_DBG\_SHOW\_TRISER\_GEOM | \-1,151,148 | "Show Triser Geometry" |
| STAIRS\_DESIRED\_NUM\_RISERS | \-1,007,205 | "Desired Number of Risers" |
| STAIRS\_DESIRED\_NUMBER\_OF\_RISERS | \-1,151,110 | "Desired Number of Risers": The number of risers is calculated based on stairs height |
| STAIRS\_DOWN\_TEXT | \-1,006,634 | "Down Text" |
| STAIRS\_ENABLE\_CALCULATION\_RULE\_CHECKING | \-1,151,118 | "Enable Calculator Rules Check": Enable calculation rule checking |
| STAIRS\_INST\_ALWAYS\_UP | \-1,007,278 | "Show Up arrow in all views" |
| STAIRS\_INST\_DOWN\_ARROW\_ON | \-1,007,276 | "Down arrow" |
| STAIRS\_INST\_DOWN\_LABEL\_ON | \-1,007,274 | "Down label" |
| STAIRS\_INST\_DOWN\_LABEL\_TEXT | \-1,007,275 | "Down text" |
| STAIRS\_INST\_UP\_ARROW\_ON | \-1,007,273 | "Up arrow" |
| STAIRS\_INST\_UP\_LABEL\_ON | \-1,007,271 | "Up label" |
| STAIRS\_INST\_UP\_LABEL\_TEXT | \-1,007,272 | "Up text" |
| STAIRS\_LANDING\_BASE\_ELEVATION | \-1,151,501 | "Relative Height": Height |
| STAIRS\_LANDING\_OVERRIDDEN | \-1,151,508 | "Overridden": Overridden |
| STAIRS\_LANDING\_STRUCTURAL | \-1,151,502 | "Structural": Structural |
| STAIRS\_LANDING\_THICKNESS | \-1,151,507 | "Total Thickness": Thickness |
| STAIRS\_LANDINGTYPE\_HAS\_MONOLITHIC\_SUPPORT | \-1,151,601 | "Monolithic Support": Monolithic Support |
| STAIRS\_LANDINGTYPE\_LANDING\_MATERIAL | \-1,151,606 | "Monolithic Material": Landing Material |
| STAIRS\_LANDINGTYPE\_STRUCTURE | \-1,151,602 | "Structure": Structure |
| STAIRS\_LANDINGTYPE\_THICKNESS | \-1,151,603 | "Monolithic Thickness": Default thickness |
| STAIRS\_LANDINGTYPE\_TREADRISER\_TYPE | \-1,151,605 | "Type": Tread/Riser Type |
| STAIRS\_LANDINGTYPE\_USE\_SAME\_TRISER\_AS\_RUN | \-1,151,604 | "Same as Run": Same as Run |
| STAIRS\_MIN\_AUTOMATIC\_LANDING\_DEPTH | \-1,151,117 | "Minimum Automatic Landing Depth": The minimum depth of automatic landing |
| STAIRS\_MULTISTORY\_TOP\_LEVEL\_PARAM | \-1,007,235 | "Multistory Top Level" |
| STAIRS\_MULTISTORY\_UP\_TO\_LEVEL | \-1,151,106 | "Multistory Top Level": The top level of multi\-story stairs |
| STAIRS\_PATH\_FULL\_STEP\_ARROW | \-1,006,661 | "Full Step Arrow" |
| STAIRS\_PATH\_START\_EXTENSION | \-1,006,660 | "Start Extension" |
| STAIRS\_PATH\_START\_FROM\_RISER | \-1,006,626 | "Start from Riser" |
| STAIRS\_RAILING\_ANGLED\_CONNECTION | \-1,008,631 | "Angled Joins" |
| STAIRS\_RAILING\_BALUSTER\_BOTTOM\_ANGLE | \-1,008,624 | "Bottom Cut Angle" |
| STAIRS\_RAILING\_BALUSTER\_FAMILY | \-1,008,618 | "Baluster Family" |
| STAIRS\_RAILING\_BALUSTER\_HEIGHT | \-1,008,622 | "Baluster Height" |
| STAIRS\_RAILING\_BALUSTER\_IS\_POST | \-1,008,633 | "Post" |
| STAIRS\_RAILING\_BALUSTER\_LENGTH | \-1,008,612 | "Baluster Length" |
| STAIRS\_RAILING\_BALUSTER\_OFFSET | \-1,008,619 | "Baluster Offset" |
| STAIRS\_RAILING\_BALUSTER\_PLACEMENT | \-1,008,626 | "Baluster Placement" |
| STAIRS\_RAILING\_BALUSTER\_SHAPE | \-1,008,605 | "Baluster Shape" |
| STAIRS\_RAILING\_BALUSTER\_SLOPE\_ANGLE | \-1,008,625 | "Slope Angle" |
| STAIRS\_RAILING\_BALUSTER\_SPACING | \-1,008,609 | "Baluster Separation" |
| STAIRS\_RAILING\_BALUSTER\_SPACING\_TYPE | \-1,008,608 | "Baluster Spacing Type (Stair Railing Only)" |
| STAIRS\_RAILING\_BALUSTER\_TOP\_ANGLE | \-1,008,623 | "Top Cut Angle" |
| STAIRS\_RAILING\_BALUSTER\_WIDTH | \-1,008,611 | "Baluster Width" |
| STAIRS\_RAILING\_BALUSTERS\_PER\_TREAD | \-1,008,610 | "Balusters Per Tread (Stair Railing Only)" |
| STAIRS\_RAILING\_BASE\_LEVEL\_PARAM | \-1,008,620 | "Base Level" |
| STAIRS\_RAILING\_CONNECTION | \-1,008,632 | "Rail Connections" |
| STAIRS\_RAILING\_HEIGHT | \-1,008,602 | "Railing Height" |
| STAIRS\_RAILING\_HEIGHT\_OFFSET | \-1,008,621 | "Base Offset" |
| STAIRS\_RAILING\_HEIGHT\_SHIFT\_TYPE | \-1,008,628 | "Use Landing Height Adjustment" |
| STAIRS\_RAILING\_HEIGHT\_SHIFT\_VAL | \-1,008,629 | "Landing Height Adjustment" |
| STAIRS\_RAILING\_PLACEMENT\_OFFSET | \-1,152,300 | "Offset from Path" |
| STAIRS\_RAILING\_RAIL\_HEIGHT | \-1,008,616 | "Rail Height" |
| STAIRS\_RAILING\_RAIL\_NAME | \-1,008,627 | "Name" |
| STAIRS\_RAILING\_RAIL\_OFFSET | \-1,008,617 | "Rail Offset" |
| STAIRS\_RAILING\_RAIL\_STRUCTURE | \-1,008,615 | "Rail Structure (Non\-Continuous)" |
| STAIRS\_RAILING\_SHAPE | \-1,008,614 | "Rail Shape" |
| STAIRS\_RAILING\_TANGENT\_CONNECTION | \-1,008,630 | "Tangent Joins" |
| STAIRS\_RAILING\_THICKNESS | \-1,008,604 | "Railing Thickness" |
| STAIRS\_RAILING\_WIDTH | \-1,008,603 | "Railing Width" |
| STAIRS\_RUN\_ACTUAL\_NUMBER\_OF\_RISERS | \-1,151,305 | "Actual Number of Risers": Actual Number of Risers |
| STAIRS\_RUN\_ACTUAL\_NUMBER\_OF\_TREADS | \-1,151,306 | "Actual Number of Treads": Actual Number of Treads |
| STAIRS\_RUN\_ACTUAL\_RISER\_HEIGHT | \-1,151,307 | "Actual Riser Height": Actual Riser Height |
| STAIRS\_RUN\_ACTUAL\_RUN\_WIDTH | \-1,151,309 | "Actual Run Width": Actual Run Width |
| STAIRS\_RUN\_ACTUAL\_TREAD\_DEPTH | \-1,151,308 | "Actual Tread Depth": Actual Tread Depth |
| STAIRS\_RUN\_BEGIN\_WITH\_RISER | \-1,151,316 | "Begin with Riser": Begin with Riser |
| STAIRS\_RUN\_BOTTOM\_ELEVATION | \-1,151,301 | "Relative Base Height": Relative height to stairs bottom elevation |
| STAIRS\_RUN\_CCW | \-1,151,322 | "CCW": Revert the run preview |
| STAIRS\_RUN\_CENTER\_MARK\_VISIBLE | \-1,151,313 | "Center Mark Visible": Center Mark Visible |
| STAIRS\_RUN\_CREATE\_AUTO\_LANDING | \-1,151,321 | "With Automatic Landing": Create automatic landing |
| STAIRS\_RUN\_END\_WITH\_RISER | \-1,151,317 | "End with Riser": End with Riser |
| STAIRS\_RUN\_EXTEND\_BELOW\_RISER\_BASE | \-1,151,304 | "Extend Below Riser Base": Extend Below Base |
| STAIRS\_RUN\_EXTEND\_BELOW\_TREAD\_BASE | \-1,151,323 | "Extend Below Tread Base": Extend Below Tread Base |
| STAIRS\_RUN\_HEIGHT | \-1,151,303 | "Run Height": Run Height |
| STAIRS\_RUN\_LOCATIONPATH\_JUSTFICATION | \-1,151,318 | "Location Line": Location Line |
| STAIRS\_RUN\_OVERRIDDEN | \-1,151,315 | "Overridden": Overridden |
| STAIRS\_RUN\_STRUCTURAL | \-1,151,314 | "Structural": Structural |
| STAIRS\_RUN\_TOP\_ELEVATION | \-1,151,302 | "Relative Top Height": Top height of run |
| STAIRS\_RUN\_WIDTH\_MEASUREMENT | \-1,151,116 | "Run Width Measurement": Run Width Measurement |
| STAIRS\_RUN\_WINDER\_BEGIN\_WITH\_STRAIGHT | \-1,151,319 | "Begin with Straight Run": Winder begin with straight run |
| STAIRS\_RUN\_WINDER\_END\_WITH\_STRAIGHT | \-1,151,320 | "End with Straight Run": Winder end with straight run |
| STAIRS\_RUNTYPE\_HAS\_MONOLITHIC\_SUPPORT | \-1,151,401 | "Monolithic Support": Monolithic Support |
| STAIRS\_RUNTYPE\_RUN\_MATERIAL | \-1,151,406 | "Monolithic Material": Material |
| STAIRS\_RUNTYPE\_STRUCTURAL\_DEPTH | \-1,151,404 | "Structural Depth": Structural Depth |
| STAIRS\_RUNTYPE\_STRUCTURE | \-1,151,403 | "Structure": Structure |
| STAIRS\_RUNTYPE\_TOTAL\_DEPTH | \-1,151,405 | "Total Depth": Total Depth |
| STAIRS\_RUNTYPE\_UNDERSIDE\_SURFACE\_TYPE | \-1,151,402 | "Underside Surface": Underside Surface |
| STAIRS\_SHOW\_DOWN\_TEXT | \-1,006,633 | "Show Down Text" |
| STAIRS\_SHOW\_UP\_TEXT | \-1,006,631 | "Show Up Text" |
| STAIRS\_STAIRS\_HEIGHT | \-1,151,105 | "Desired Stair Height": Stairs unconnected height |
| STAIRS\_STRINGERS\_PRESENT | \-1,007,234 | "Stringer Position" |
| STAIRS\_SUPPORT\_HORIZONTAL\_OFFSET | \-1,151,701 | "Lateral Offset": Distance from center or edge of boundary |
| STAIRS\_SUPPORT\_LANDINGSUPPORT\_TYPE | \-1,151,710 | "Landing Support Type": Landing Support Type |
| STAIRS\_SUPPORT\_LOWER\_END\_CUT | \-1,151,705 | "Lower End Cut": Lower End Cut |
| STAIRS\_SUPPORT\_OVERRIDDEN | \-1,151,709 | "Overridden": Overridden |
| STAIRS\_SUPPORT\_TRIM\_SUPPORT\_UPPER | \-1,151,708 | "Trim Support at Upper": Trim Support at Upper |
| STAIRS\_SUPPORT\_UPPER\_END\_CUT | \-1,151,706 | "Upper End Cut": Upper End Cut |
| STAIRS\_SUPPORT\_VERTICAL\_OFFSET | \-1,151,702 | "Vertical Offset": Distance of top plane of edge stringer relative to the plane connecting tread nosing |
| STAIRS\_SUPPORTTYPE\_FLIP\_SECTION\_PROFILE | \-1,151,811 | "Flip Section Profile": Flip Section Profile |
| STAIRS\_SUPPORTTYPE\_MATERIAL | \-1,151,808 | "Material": Material |
| STAIRS\_SUPPORTTYPE\_SECTION\_PROFILE | \-1,151,801 | "Section Profile": Section Profile |
| STAIRS\_SUPPORTTYPE\_STRUCTURAL\_DEPTH | \-1,151,805 | "Structural Depth": Structural Depth |
| STAIRS\_SUPPORTTYPE\_STRUCTURAL\_DEPTH\_ON\_LANDING | \-1,151,810 | "Structural Depth On Landing": Structural Depth |
| STAIRS\_SUPPORTTYPE\_STRUCTURAL\_DEPTH\_ON\_RUN | \-1,151,809 | "Structural Depth On Run": Structural Depth |
| STAIRS\_SUPPORTTYPE\_TOPSIDE\_SURFACE | \-1,151,803 | "Topside Surface": Topside Surface |
| STAIRS\_SUPPORTTYPE\_TOTAL\_DEPTH | \-1,151,806 | "Total Depth": Total Depth |
| STAIRS\_SUPPORTTYPE\_UNDERSIDE\_SURFACE | \-1,151,804 | "Underside Surface": Underside Surface |
| STAIRS\_SUPPORTTYPE\_WIDTH | \-1,151,807 | "Width": Width |
| STAIRS\_TEXT\_ORIENTATION | \-1,006,636 | "Orientation" |
| STAIRS\_TEXT\_TYPE | \-1,006,635 | "Text Type" |
| STAIRS\_TOP\_LEVEL | \-1,151,103 | "Top Level": The top level of stairs |
| STAIRS\_TOP\_LEVEL\_PARAM | \-1,007,201 | "Top Level" |
| STAIRS\_TOP\_OFFSET | \-1,007,219 | "Top Offset" |
| STAIRS\_TOTAL\_NUMBER\_OF\_RISERS | \-1,151,112 | "Total Number of Risers": Total number of risers |
| STAIRS\_TOTAL\_NUMBER\_OF\_TREADS | \-1,151,113 | "Total Number of Treads": Total number of treads |
| STAIRS\_TRISER\_IS\_TYPE\_OVERRIDDEN | \-1,152,101 | "Overridden": (OBSOLETE) Indicate whether selected individual step is governed by default type setting. |
| STAIRS\_TRISER\_NUMBER\_BASE\_INDEX | \-1,151,154 | "Tread/Riser Start Number": |
| STAIRS\_TRISER\_RISER\_MARK | \-1,152,105 | "Riser Mark": (OBSOLETE) |
| STAIRS\_TRISER\_RISER\_NUMBER | \-1,152,103 | "Riser Number": Count the sequential number of riser in the stair. |
| STAIRS\_TRISER\_TREAD\_MARK | \-1,152,104 | "Tread Mark": (OBSOLETE) |
| STAIRS\_TRISER\_TREAD\_NUMBER | \-1,152,102 | "Tread Number": Count the sequential number of tread in the stair. |
| STAIRS\_TRISERTYPE\_BACK\_NOSING | \-1,152,158 | "Back Nosing": (OBSOLETE) |
| STAIRS\_TRISERTYPE\_FRONT\_NOSING | \-1,152,155 | "Front Nosing": (OBSOLETE) |
| STAIRS\_TRISERTYPE\_LEFT\_NOSING | \-1,152,157 | "Left Nosing": (OBSOLETE) |
| STAIRS\_TRISERTYPE\_NOSING\_LENGTH | \-1,152,154 | "Nosing Length" |
| STAIRS\_TRISERTYPE\_NOSING\_PLACEMENT | \-1,152,175 | "Apply Nosing Profile" |
| STAIRS\_TRISERTYPE\_NOSING\_PROFILE | \-1,152,153 | "Nosing Profile" |
| STAIRS\_TRISERTYPE\_RIGHT\_NOSING | \-1,152,156 | "Right Nosing": (OBSOLETE) |
| STAIRS\_TRISERTYPE\_RISER | \-1,152,176 | "Riser" |
| STAIRS\_TRISERTYPE\_RISER\_IS\_SLANTED | \-1,152,177 | "Slanted" |
| STAIRS\_TRISERTYPE\_RISER\_MATERIAL | \-1,152,163 | "Riser Material" |
| STAIRS\_TRISERTYPE\_RISER\_PROFILE | \-1,152,174 | "Riser Profile" |
| STAIRS\_TRISERTYPE\_RISER\_STYLE | \-1,152,159 | "Riser Type": (OBSOLETE) |
| STAIRS\_TRISERTYPE\_RISER\_THICKNESS | \-1,152,160 | "Riser Thickness" |
| STAIRS\_TRISERTYPE\_RISER\_TREAD\_CONNECTION | \-1,152,161 | "Riser To Tread Connection" |
| STAIRS\_TRISERTYPE\_TREAD | \-1,152,151 | "Tread" |
| STAIRS\_TRISERTYPE\_TREAD\_MATERIAL | \-1,152,162 | "Tread Material" |
| STAIRS\_TRISERTYPE\_TREAD\_PROFILE | \-1,152,164 | "Tread Profile" |
| STAIRS\_TRISERTYPE\_TREAD\_THICKNESS | \-1,152,152 | "Tread Thickness" |
| STAIRS\_UP\_TEXT | \-1,006,632 | "Up Text" |
| STAIRS\_WINDERPATTERN\_FILLET\_INSIDE\_CORNER | \-1,151,905 | "Fillet on Corner": Fillet on inside corner |
| STAIRS\_WINDERPATTERN\_MINIMUM\_WIDTH\_CORNER | \-1,151,902 | "Minimum Width on Inside Boundary": Minimum Width on Inside Boundary |
| STAIRS\_WINDERPATTERN\_MINIMUM\_WIDTH\_INSIDE\_WALKLINE | \-1,151,903 | "Minimum Width on Inside Walk Line": Minimum width on inside walkline |
| STAIRS\_WINDERPATTERN\_NUMBER\_OF\_STRAIGHT\_STEPS\_AT\_BEGIN | \-1,151,907 | "Parallel Treads at Start": Number of straight steps at the begin of winder |
| STAIRS\_WINDERPATTERN\_NUMBER\_OF\_STRAIGHT\_STEPS\_AT\_END | \-1,151,908 | "Parallel Treads at End": Number of straight steps at the begin of winder |
| STAIRS\_WINDERPATTERN\_RADIUS\_INTERIOR | \-1,151,906 | "Fillet Radius": The fillet corner radius on the interior boundary |
| STAIRS\_WINDERPATTERN\_STAIR\_PATH\_OFFSET | \-1,151,904 | "Inside Walk Line Offset": The offset from inside walk line to interior boundary |
| STAIRS\_WINDERPATTERN\_WINDER\_STYLE | \-1,151,901 | "Winder Style": Winder Style |
| STAIRSTYPE\_CALC\_RULE\_MAX\_RESULT | \-1,151,221 | "Max. Result": Calculation Rule Max Result |
| STAIRSTYPE\_CALC\_RULE\_MIN\_RESULT | \-1,151,222 | "Min. Result": Calculation Rule Min Result |
| STAIRSTYPE\_CALC\_RULE\_RISER\_MULTIPLIER | \-1,151,219 | "Riser Multiplier": Calculation Rule Riser Multiplier |
| STAIRSTYPE\_CALC\_RULE\_TARGET\_RESULT | \-1,151,223 | "Target Result": Calculation Rule Target Result |
| STAIRSTYPE\_CALC\_RULE\_TREAD\_MULTIPLIER | \-1,151,220 | "Tread Multiplier": Calculation Rule Tread Multiplier |
| STAIRSTYPE\_CALCULATION\_RULES | \-1,151,206 | "Calculation Rules": Calculation Rules |
| STAIRSTYPE\_CONSTRUCTION\_METHOD | \-1,151,233 | "Construction Method": |
| STAIRSTYPE\_CUTMARK\_TYPE | \-1,151,234 | "Cut Mark Type": Cut Mark Type |
| STAIRSTYPE\_GEOMUNJOINED\_END\_CUT\_STYLE | \-1,151,224 | "Connection Method": Cut Style for Geometrically Unjoined End |
| STAIRSTYPE\_HAS\_INTERMEDIATE\_SUPPORT | \-1,151,237 | "Middle Support": Whether stairs is assembled |
| STAIRSTYPE\_HAS\_LEFT\_SUPPORT | \-1,151,231 | "Left Support": |
| STAIRSTYPE\_HAS\_RIGHT\_SUPPORT | \-1,151,232 | "Right Support": |
| STAIRSTYPE\_INTERMEDIATE\_SUPPORT\_TYPE | \-1,151,211 | "Middle Support Type": Intermediate Support Type |
| STAIRSTYPE\_IS\_ASSEMBLED\_STAIRS | \-1,151,218 | "Assembled Stair": Whether stairs is assembled |
| STAIRSTYPE\_LANDING\_TYPE | \-1,151,208 | "Landing Type": Landing Type |
| STAIRSTYPE\_LEFT\_SIDE\_SUPPORT\_TYPE | \-1,151,210 | "Left Support Type": Left Side Support Type |
| STAIRSTYPE\_LEFT\_SUPPORT\_LATERAL\_OFFSET | \-1,151,236 | "Left Lateral Offset": |
| STAIRSTYPE\_MAXIMUM\_RISER\_HEIGHT | \-1,151,203 | "Max. Riser Height": Maximum Riser Height |
| STAIRSTYPE\_MINIMUM\_RUN\_WIDTH | \-1,151,216 | "Minimum Run Width": Minimum Run Width |
| STAIRSTYPE\_MINIMUM\_TREAD\_DEPTH | \-1,151,204 | "Min. Tread Depth": Minimum Tread Depth |
| STAIRSTYPE\_MINIMUM\_TREAD\_WIDTH\_INSIDE\_BOUNDARY | \-1,151,205 | "Min. Tread Depth on Winder Inner Boundary": Minimum Tread Width on Inside Boundary |
| STAIRSTYPE\_NOTCH\_CUSTOM\_WIDTH | \-1,151,227 | "Custom": |
| STAIRSTYPE\_NOTCH\_EXTENSION | \-1,151,225 | "Notch Extension": |
| STAIRSTYPE\_NOTCH\_HORIZONTAL\_GAP | \-1,151,228 | "Horizontal Gap Distance": |
| STAIRSTYPE\_NOTCH\_THICKNESS | \-1,151,226 | "Notch Thickness": |
| STAIRSTYPE\_NOTCH\_VERTICAL\_GAP | \-1,151,229 | "Vertical Gap Distance": |
| STAIRSTYPE\_NOTCH\_WIDTH | \-1,151,230 | "Notch Width": |
| STAIRSTYPE\_NUMBER\_OF\_INTERMEDIATE\_SUPPORTS | \-1,151,217 | "Middle Support Number": Number of intermediate supports |
| STAIRSTYPE\_RIGHT\_SIDE\_SUPPORT\_TYPE | \-1,151,209 | "Right Support Type": Right Side Support Type |
| STAIRSTYPE\_RIGHT\_SUPPORT\_LATERAL\_OFFSET | \-1,151,235 | "Right Lateral Offset": |
| STAIRSTYPE\_RUN\_TYPE | \-1,151,207 | "Run Type": Run Type |
| STAIRSTYPE\_SHOW\_CUTLINE | \-1,151,212 | "Show Cut Line in Plan": Show Cut Line in Plan |
| STAIRSTYPE\_SHOW\_STAIR\_PATH | \-1,151,213 | "Show Stair Path in Plan": Show Stair Path in Plan |
| STAIRSTYPE\_SHOW\_UPDOWN | \-1,151,214 | "Show Up/Down in Plan": Show Up/Down in Plan |
| STAIRSTYPE\_WINDER\_STEP\_FRONT\_MEASUREMENT | \-1,151,215 | "Winder Algorithm": Winder Algorithm |
| START\_EXTENSION | \-1,152,357 | "Start Extension" |
| START\_JOIN\_CUTBACK | \-1,152,359 | "Start Join Cutback" |
| START\_SYMBOL\_TYPE | \-1,006,622 | "Start Symbol Type" |
| START\_Y\_JUSTIFICATION | \-1,152,366 | "Start y Justification" |
| START\_Y\_OFFSET\_VALUE | \-1,152,367 | "Start y Offset Value" |
| START\_Z\_JUSTIFICATION | \-1,152,368 | "Start z Justification" |
| START\_Z\_OFFSET\_VALUE | \-1,152,369 | "Start z Offset Value" |
| STEEL\_ELEM\_ANCHOR\_ASSEMBLY | \-1,155,012 | "Assembly" |
| STEEL\_ELEM\_ANCHOR\_DIAMETER | \-1,155,013 | "Diameter" |
| STEEL\_ELEM\_ANCHOR\_GRADE | \-1,155,011 | "Grade" |
| STEEL\_ELEM\_ANCHOR\_LENGTH | \-1,155,017 | "Length" |
| STEEL\_ELEM\_ANCHOR\_ORIENTATION | \-1,155,130 | "Anchor Orientation" |
| STEEL\_ELEM\_ANCHOR\_STANDARD | \-1,155,010 | "Standard" |
| STEEL\_ELEM\_ANCHOR\_TOTAL\_WEIGHT | \-1,155,132 | "Total Weight" |
| STEEL\_ELEM\_BOLT\_ASSEMBLY | \-1,155,007 | "Assembly" |
| STEEL\_ELEM\_BOLT\_COATING | \-1,155,018 | "Coating" |
| STEEL\_ELEM\_BOLT\_DIAMETER | \-1,155,008 | "Diameter" |
| STEEL\_ELEM\_BOLT\_FINISH\_CALCULATION\_AT\_GAP | \-1,155,121 | "Finish Calculation At Gap" |
| STEEL\_ELEM\_BOLT\_GRADE | \-1,155,006 | "Grade" |
| STEEL\_ELEM\_BOLT\_GRIP\_LENGTH | \-1,155,118 | "Grip Length" |
| STEEL\_ELEM\_BOLT\_GRIP\_LENGTH\_INCREASE | \-1,155,119 | "Grip Length Increase" |
| STEEL\_ELEM\_BOLT\_INVERTED | \-1,155,120 | "Inverted" |
| STEEL\_ELEM\_BOLT\_LENGTH | \-1,155,117 | "Bolt Length" |
| STEEL\_ELEM\_BOLT\_LOCATION | \-1,155,122 | "Location" |
| STEEL\_ELEM\_BOLT\_STANDARD | \-1,155,005 | "Standard" |
| STEEL\_ELEM\_BOLT\_TOTAL\_WEIGHT | \-1,155,135 | "Total Weight" |
| STEEL\_ELEM\_COATING | \-1,155,009 | "Coating" |
| STEEL\_ELEM\_CONTOUR\_GAP\_WIDTH | \-1,155,023 | "Gap Width" |
| STEEL\_ELEM\_CONTOUR\_SIDE1DIST | \-1,155,026 | "Boundary distance 1" |
| STEEL\_ELEM\_CONTOUR\_SIDE2DIST | \-1,155,027 | "Boundary distance 2" |
| STEEL\_ELEM\_COPE\_AROUND\_AXIS | \-1,155,086 | "Around beam axis" |
| STEEL\_ELEM\_COPE\_AXIS\_ANGLE | \-1,155,085 | "Tilt angle" |
| STEEL\_ELEM\_COPE\_DISTANCE\_AXIS | \-1,155,082 | "Distance from axis" |
| STEEL\_ELEM\_COPE\_WIDTHX | \-1,155,081 | "Cutback" |
| STEEL\_ELEM\_COPE\_X\_ANGLE | \-1,155,083 | "Cross\-section rotation" |
| STEEL\_ELEM\_COPE\_Z\_ANGLE | \-1,155,084 | "Plan rotation" |
| STEEL\_ELEM\_CUT\_LENGTH | \-1,155,128 | "Cut Length" |
| STEEL\_ELEM\_CUT\_TYPE | \-1,155,078 | "Type" |
| STEEL\_ELEM\_EXACT\_WEIGHT | \-1,155,127 | "Exact Weight" |
| STEEL\_ELEM\_HOLE\_ALPHA | \-1,155,066 | "Taper Angle" |
| STEEL\_ELEM\_HOLE\_ANGLE | \-1,155,067 | "Chamfer angle" |
| STEEL\_ELEM\_HOLE\_BACK\_TAPER\_THREAD | \-1,155,070 | "Back taper thread" |
| STEEL\_ELEM\_HOLE\_DEFINITION | \-1,155,101 | "Hole Definition" |
| STEEL\_ELEM\_HOLE\_DEPTH | \-1,155,065 | "Hole Depth" |
| STEEL\_ELEM\_HOLE\_DEPTH\_OF\_BOLT\_HEAD | \-1,155,072 | "Depth of bolt head" |
| STEEL\_ELEM\_HOLE\_DIAMETER | \-1,155,061 | "Diameter" |
| STEEL\_ELEM\_HOLE\_HEAD\_DIAMETER | \-1,155,068 | "Head diameter" |
| STEEL\_ELEM\_HOLE\_SLOT\_DIRECTION | \-1,155,064 | "Along side 1" |
| STEEL\_ELEM\_HOLE\_SLOT\_LENGTH | \-1,155,063 | "Length of the slot" |
| STEEL\_ELEM\_HOLE\_TAPPING | \-1,155,071 | "Right\-handed thread" |
| STEEL\_ELEM\_HOLE\_TAPPING\_HOLE | \-1,155,069 | "Tapping hole" |
| STEEL\_ELEM\_HOLE\_TYPE | \-1,155,062 | "Type" |
| STEEL\_ELEM\_MARK | \-1,180,318 | "Assembly Mark" |
| STEEL\_ELEM\_PAINT\_AREA | \-1,155,125 | "Paint Area" |
| STEEL\_ELEM\_PARAM\_BORINGOUT | \-1,155,029 | "Boring out" |
| STEEL\_ELEM\_PARAM\_RADIUS | \-1,155,028 | "Radius" |
| STEEL\_ELEM\_PATTERN\_EDGE\_DISTANCE\_X | \-1,155,057 | "Edge distance on side 1" |
| STEEL\_ELEM\_PATTERN\_EDGE\_DISTANCE\_Y | \-1,155,058 | "Edge distance on side 2" |
| STEEL\_ELEM\_PATTERN\_INTERMEDIATE\_DISTANCE\_X | \-1,155,055 | "Intermediate distance on side 1" |
| STEEL\_ELEM\_PATTERN\_INTERMEDIATE\_DISTANCE\_Y | \-1,155,056 | "Intermediate distance on side 2" |
| STEEL\_ELEM\_PATTERN\_NUMBER | \-1,155,060 | "Number" |
| STEEL\_ELEM\_PATTERN\_NUMBER\_X | \-1,155,051 | "Number on side 1" |
| STEEL\_ELEM\_PATTERN\_NUMBER\_Y | \-1,155,052 | "Number on side 2" |
| STEEL\_ELEM\_PATTERN\_RADIUS | \-1,155,059 | "Radius" |
| STEEL\_ELEM\_PATTERN\_TOTAL\_LENGTH | \-1,155,053 | "Length on side 1" |
| STEEL\_ELEM\_PATTERN\_TOTAL\_WIDTH | \-1,155,054 | "Length on side 2" |
| STEEL\_ELEM\_PLATE\_AREA | \-1,155,139 | "Area" |
| STEEL\_ELEM\_PLATE\_EXACT\_WEIGHT | \-1,155,142 | "Exact Weight" |
| STEEL\_ELEM\_PLATE\_JUSTIFICATION | \-1,155,144 | "Justification" |
| STEEL\_ELEM\_PLATE\_LENGTH | \-1,155,137 | "Length" |
| STEEL\_ELEM\_PLATE\_PAINT\_AREA | \-1,155,143 | "Paint Area" |
| STEEL\_ELEM\_PLATE\_SHORTEN\_ANGLE | \-1,155,075 | "Angle" |
| STEEL\_ELEM\_PLATE\_SHORTEN\_CUTSTRAIGHT | \-1,155,077 | "Cut straight" |
| STEEL\_ELEM\_PLATE\_SHORTEN\_SUCTION | \-1,155,076 | "Suction" |
| STEEL\_ELEM\_PLATE\_THICKNESS | \-1,155,003 | "Thickness" |
| STEEL\_ELEM\_PLATE\_TYPE | \-1,155,136 | "Type" |
| STEEL\_ELEM\_PLATE\_VOLUME | \-1,155,140 | "Volume" |
| STEEL\_ELEM\_PLATE\_WEIGHT | \-1,155,141 | "Weight" |
| STEEL\_ELEM\_PLATE\_WIDTH | \-1,155,138 | "Width" |
| STEEL\_ELEM\_PROFILE\_LENGTH | \-1,155,147 | "System Length" |
| STEEL\_ELEM\_PROFILE\_TYPE | \-1,155,146 | "Profile Type" |
| STEEL\_ELEM\_PROFILE\_VOLUME | \-1,155,148 | "Volume" |
| STEEL\_ELEM\_SHEARSTUD\_DIAMETER | \-1,155,016 | "Diameter" |
| STEEL\_ELEM\_SHEARSTUD\_GRADE | \-1,155,015 | "Grade" |
| STEEL\_ELEM\_SHEARSTUD\_LENGTH | \-1,155,019 | "Length" |
| STEEL\_ELEM\_SHEARSTUD\_STANDARD | \-1,155,014 | "Standard" |
| STEEL\_ELEM\_SHEARSTUD\_TOTAL\_WEIGHT | \-1,155,134 | "Total Weight" |
| STEEL\_ELEM\_SHORTEN\_ANGLEY | \-1,155,021 | "Angle along height" |
| STEEL\_ELEM\_SHORTEN\_ANGLEZ | \-1,155,022 | "Angle along width" |
| STEEL\_ELEM\_SHORTEN\_REFLENGTH | \-1,155,020 | "Length" |
| STEEL\_ELEM\_SINGLE\_PART\_MARK | \-1,180,319 | "Single Part Mark" |
| STEEL\_ELEM\_WEIGHT | \-1,155,124 | "Weight" |
| STEEL\_ELEM\_WELD\_CONTINUOUS | \-1,155,035 | "Continuous" |
| STEEL\_ELEM\_WELD\_DOUBLE\_EFFECTIVETHROAT | \-1,155,049 | "Double Effective Throat" |
| STEEL\_ELEM\_WELD\_DOUBLE\_PREPDEPTH | \-1,155,050 | "Double Preparation Depth" |
| STEEL\_ELEM\_WELD\_DOUBLE\_ROOTOPENING | \-1,155,048 | "Double Root Opening" |
| STEEL\_ELEM\_WELD\_DOUBLE\_SURFACESHAPE | \-1,155,046 | "Double Surface Shape" |
| STEEL\_ELEM\_WELD\_DOUBLE\_TEXT | \-1,155,045 | "Double Text" |
| STEEL\_ELEM\_WELD\_DOUBLE\_THICKNESS | \-1,155,044 | "Double Thickness" |
| STEEL\_ELEM\_WELD\_DOUBLE\_TYPE | \-1,155,043 | "Double Type" |
| STEEL\_ELEM\_WELD\_DOUBLE\_WELDPREP | \-1,155,047 | "Double Weld preparation" |
| STEEL\_ELEM\_WELD\_LENGTH | \-1,155,033 | "Length" |
| STEEL\_ELEM\_WELD\_LOCATION | \-1,155,034 | "Location" |
| STEEL\_ELEM\_WELD\_MAIN\_EFFECTIVETHROAT | \-1,155,041 | "Main Effective Throat" |
| STEEL\_ELEM\_WELD\_MAIN\_PREPDEPTH | \-1,155,042 | "Main Preparation Depth" |
| STEEL\_ELEM\_WELD\_MAIN\_ROOTOPENING | \-1,155,040 | "Main Root Opening" |
| STEEL\_ELEM\_WELD\_MAIN\_SURFACESHAPE | \-1,155,038 | "Surface Shape" |
| STEEL\_ELEM\_WELD\_MAIN\_TEXT | \-1,155,037 | "Main Text" |
| STEEL\_ELEM\_WELD\_MAIN\_THICKNESS | \-1,155,032 | "Main Thickness" |
| STEEL\_ELEM\_WELD\_MAIN\_TYPE | \-1,155,031 | "Main Type" |
| STEEL\_ELEM\_WELD\_MAIN\_WELDPREP | \-1,155,039 | "Main Weld preparation" |
| STEEL\_ELEM\_WELD\_PITCH | \-1,155,036 | "Pitch" |
| STEEL\_ELEM\_WELD\_PREFIX | \-1,155,074 | "Prefix" |
| STEEL\_ELEM\_WELD\_TEXT\_MODULE | \-1,155,073 | "Text module" |
| STEEL\_ELEM\_X\_DISTANCE | \-1,155,079 | "Side 1" |
| STEEL\_ELEM\_Y\_DISTANCE | \-1,155,080 | "Side 2" |
| STEEL\_ELEM\_ZCLIP\_TYPE | \-1,155,087 | "Boundary" |
| STIFFENER\_CLASSIFICATION | \-1,155,245 | "Classification" |
| STRUCT\_CONNECTION\_APPLY\_TO | \-1,018,800 | "Apply to" |
| STRUCT\_CONNECTION\_BEAM\_END | \-1,018,802 | "End Connection" |
| STRUCT\_CONNECTION\_BEAM\_START | \-1,018,801 | "Start Connection" |
| STRUCT\_CONNECTION\_COLUMN\_BASE | \-1,018,804 | "Base Connection" |
| STRUCT\_CONNECTION\_COLUMN\_TOP | \-1,018,803 | "Top Connection" |
| STRUCT\_CONNECTION\_CUTBACK | \-1,018,805 | "Automatic Cutback for Beams and Braces" |
| STRUCT\_CONNECTION\_TYPE\_NAME | \-1,018,850 | "Name" |
| STRUCT\_FRAM\_JOIN\_STATUS | \-1,152,383 | "Join Status" |
| STRUCTURAL\_ANALYTICAL\_BEAM\_HORIZONTAL\_PROJECTION\_PLANE | \-1,001,593 | "Horizontal Projection" |
| STRUCTURAL\_ANALYTICAL\_BEAM\_RIGID\_LINK | \-1,001,595 | "Analytical Links" |
| STRUCTURAL\_ANALYTICAL\_COLUMN\_HORIZONTAL\_PROJECTION\_PLANE | \-1,001,594 | "Horizontal Projection" |
| STRUCTURAL\_ANALYTICAL\_COLUMN\_RIGID\_LINK | \-1,001,551 | "Analytical Links" |
| STRUCTURAL\_ANALYTICAL\_HARD\_POINTS | \-1,001,587 | "Use hard\-points" |
| STRUCTURAL\_ANALYTICAL\_MODEL | \-1,001,552 | "Enable Analytical Model" |
| STRUCTURAL\_ANALYTICAL\_PROJECT\_FLOOR\_PLANE | \-1,001,510 | "Vertical Projection" |
| STRUCTURAL\_ANALYTICAL\_PROJECT\_MEMBER\_PLANE | \-1,001,508 | "Vertical Projection" |
| STRUCTURAL\_ANALYTICAL\_PROJECT\_MEMBER\_PLANE\_COLUMN\_BOTTOM | \-1,001,535 | "Bottom Vertical Projection" |
| STRUCTURAL\_ANALYTICAL\_PROJECT\_MEMBER\_PLANE\_COLUMN\_TOP | \-1,001,534 | "Top Vertical Projection" |
| STRUCTURAL\_ANALYTICAL\_TESS\_DEVIATION | \-1,001,588 | "Maximum discretized offset" |
| STRUCTURAL\_ANALYTICAL\_TESSELLATE | \-1,001,589 | "Approximate curve" |
| STRUCTURAL\_ANALYZES\_AS | \-1,001,576 | "Analyze As" |
| STRUCTURAL\_ASSET\_PARAM | \-1,013,450 | "Physical Material Asset" |
| STRUCTURAL\_ATTACHMENT\_BASE\_DISTANCE | \-1,150,177 | "Base Attachment Distance" |
| STRUCTURAL\_ATTACHMENT\_BASE\_RATIO | \-1,150,178 | "Base Attachment Ratio" |
| STRUCTURAL\_ATTACHMENT\_BASE\_REFERENCEDEND | \-1,150,179 | "Base Attachment Referenced End" |
| STRUCTURAL\_ATTACHMENT\_BASE\_TYPE | \-1,150,176 | "Base Attachment Type" |
| STRUCTURAL\_ATTACHMENT\_END\_LEVEL\_REFERENCE | \-1,001,396 | "End Attachment Level Reference" |
| STRUCTURAL\_ATTACHMENT\_END\_REFELEMENT\_END | \-1,001,391 | "End of Attachment to Reference Element" |
| STRUCTURAL\_ATTACHMENT\_END\_TYPE | \-1,001,386 | "End Attachment Type" |
| STRUCTURAL\_ATTACHMENT\_END\_VALUE\_DISTANCE | \-1,001,388 | "End Attachment Distance" |
| STRUCTURAL\_ATTACHMENT\_END\_VALUE\_ELEVATION | \-1,001,398 | "End Attachment Elevation" |
| STRUCTURAL\_ATTACHMENT\_END\_VALUE\_RATIO | \-1,001,393 | "End attachment ratio" |
| STRUCTURAL\_ATTACHMENT\_START\_LEVEL\_REFERENCE | \-1,001,395 | "Start Attachment Level Reference" |
| STRUCTURAL\_ATTACHMENT\_START\_REFELEMENT\_END | \-1,001,389 | "Start of Attachment to Reference Element" |
| STRUCTURAL\_ATTACHMENT\_START\_TYPE | \-1,001,385 | "Start Attachment Type" |
| STRUCTURAL\_ATTACHMENT\_START\_VALUE\_DISTANCE | \-1,001,387 | "Start Attachment Distance" |
| STRUCTURAL\_ATTACHMENT\_START\_VALUE\_ELEVATION | \-1,001,397 | "Start Attachment Elevation" |
| STRUCTURAL\_ATTACHMENT\_START\_VALUE\_RATIO | \-1,001,392 | "Start Attachment Ratio" |
| STRUCTURAL\_ATTACHMENT\_TOP\_DISTANCE | \-1,150,181 | "Top Attachment Distance" |
| STRUCTURAL\_ATTACHMENT\_TOP\_RATIO | \-1,150,182 | "Top Attachment Ratio" |
| STRUCTURAL\_ATTACHMENT\_TOP\_REFERENCEDEND | \-1,150,183 | "Top Attachment Referenced End" |
| STRUCTURAL\_ATTACHMENT\_TOP\_TYPE | \-1,150,180 | "Top Attachment Type" |
| STRUCTURAL\_BEAM\_CUTBACK\_FOR\_COLUMN | \-1,001,575 | "Beam cutback in plan" |
| STRUCTURAL\_BEAM\_END\_ATTACHMENT\_DISTANCE | \-1,150,217 | "End Attachment Distance" |
| STRUCTURAL\_BEAM\_END\_ATTACHMENT\_REFCOLUMN\_END | \-1,150,219 | "End of Attachment to Reference Column" |
| STRUCTURAL\_BEAM\_END\_ATTACHMENT\_TYPE | \-1,150,215 | "End Attachment Type" |
| STRUCTURAL\_BEAM\_END\_SUPPORT | \-1,001,502 | "Beam End Pocket Seat" |
| STRUCTURAL\_BEAM\_END0\_ELEVATION | \-1,001,571 | "Start Level Offset" |
| STRUCTURAL\_BEAM\_END1\_ELEVATION | \-1,001,572 | "End Level Offset" |
| STRUCTURAL\_BEAM\_ORIENTATION | \-1,001,573 | "Orientation" |
| STRUCTURAL\_BEAM\_START\_ATTACHMENT\_DISTANCE | \-1,150,216 | "Start Attachment Distance" |
| STRUCTURAL\_BEAM\_START\_ATTACHMENT\_REFCOLUMN\_END | \-1,150,218 | "Start of Attachment to Reference Column" |
| STRUCTURAL\_BEAM\_START\_ATTACHMENT\_TYPE | \-1,150,214 | "Start Attachment Type" |
| STRUCTURAL\_BEAM\_START\_SUPPORT | \-1,001,501 | "Beam Start Pocket Seat" |
| STRUCTURAL\_BEND\_DIR\_ANGLE | \-1,001,586 | "Cross\-Section Rotation" |
| STRUCTURAL\_BOTTOM\_RELEASE\_FX | \-1,001,544 | "Base Fx" |
| STRUCTURAL\_BOTTOM\_RELEASE\_FY | \-1,001,545 | "Base Fy" |
| STRUCTURAL\_BOTTOM\_RELEASE\_FZ | \-1,001,546 | "Base Fz" |
| STRUCTURAL\_BOTTOM\_RELEASE\_MX | \-1,001,547 | "Base Mx" |
| STRUCTURAL\_BOTTOM\_RELEASE\_MY | \-1,001,548 | "Base My" |
| STRUCTURAL\_BOTTOM\_RELEASE\_MZ | \-1,001,549 | "Base Mz" |
| STRUCTURAL\_BOTTOM\_RELEASE\_TYPE | \-1,001,537 | "Base Release" |
| STRUCTURAL\_BRACE\_REPRESENTATION | \-1,001,507 | "Representation Type" |
| STRUCTURAL\_CAMBER | \-1,001,530 | "Camber Size" |
| STRUCTURAL\_CONNECTION\_APPROVAL\_STATUS | \-1,153,001 | "Approval Status" |
| STRUCTURAL\_CONNECTION\_CODE\_CHECKING\_STATUS | \-1,153,002 | "Code Checking Status" |
| STRUCTURAL\_CONNECTION\_EDIT\_RANGES\_OF\_APPLICABILITY | \-1,115,520 | "Modify Ranges of applicability" |
| STRUCTURAL\_CONNECTION\_EDIT\_TYPE | \-1,155,091 | "Modify Parameters" |
| STRUCTURAL\_CONNECTION\_INPUT\_ELEMENTS | \-1,153,004 | "Input Elements" |
| STRUCTURAL\_CONNECTION\_MODIFY\_CONNECTION\_PARAMETERS | \-1,153,000 | "Detailed Parameters" |
| STRUCTURAL\_CONNECTION\_NOBLE\_STATUS | \-1,153,003 | "Noble Status" |
| STRUCTURAL\_CONNECTION\_OVERRIDE\_TYPE | \-1,155,092 | "Override by Instance" |
| STRUCTURAL\_CONNECTION\_SYMBOL | \-1,152,999 | "Connection Symbol" |
| STRUCTURAL\_COPING\_DISTANCE | \-1,001,559 | "Coping Distance" |
| STRUCTURAL\_DISPLAY\_IN\_HIDDEN\_VIEWS | \-1,001,956 | "Display in Hidden Views" |
| STRUCTURAL\_DISPLAY\_IN\_HIDDEN\_VIEWS\_COLUMN | \-1,001,585 | "Display in Hidden Views" |
| STRUCTURAL\_DISPLAY\_IN\_HIDDEN\_VIEWS\_FRAMING | \-1,001,584 | "Display in Hidden Views" |
| STRUCTURAL\_ELEVATION\_AT\_BOTTOM | \-1,001,561 | "Elevation at Bottom" |
| STRUCTURAL\_ELEVATION\_AT\_BOTTOM\_CORE | \-1,001,655 | "Elevation at Bottom Core" |
| STRUCTURAL\_ELEVATION\_AT\_BOTTOM\_SURVEY | \-1,001,658 | "Elevation at Bottom Survey" |
| STRUCTURAL\_ELEVATION\_AT\_TOP | \-1,001,598 | "Elevation at Top" |
| STRUCTURAL\_ELEVATION\_AT\_TOP\_CORE | \-1,001,654 | "Elevation at Top Core" |
| STRUCTURAL\_ELEVATION\_AT\_TOP\_SURVEY | \-1,001,657 | "Elevation at Top Survey" |
| STRUCTURAL\_END\_RELEASE\_FX | \-1,001,523 | "End Fx" |
| STRUCTURAL\_END\_RELEASE\_FY | \-1,001,524 | "End Fy" |
| STRUCTURAL\_END\_RELEASE\_FZ | \-1,001,525 | "End Fz" |
| STRUCTURAL\_END\_RELEASE\_MX | \-1,001,526 | "End Mx" |
| STRUCTURAL\_END\_RELEASE\_MY | \-1,001,527 | "End My" |
| STRUCTURAL\_END\_RELEASE\_MZ | \-1,001,528 | "End Mz" |
| STRUCTURAL\_END\_RELEASE\_TYPE | \-1,001,516 | "End Release" |
| STRUCTURAL\_FAMILY\_CODE\_NAME | \-1,005,556 | "Code Name" |
| STRUCTURAL\_FAMILY\_NAME\_KEY | \-1,005,555 | "Family Name Key" |
| STRUCTURAL\_FLOOR\_ANALYZES\_AS | \-1,001,577 | "Analyze As" |
| STRUCTURAL\_FLOOR\_CORE\_THICKNESS | \-1,001,656 | "Core Thickness" |
| STRUCTURAL\_FOUNDATION\_LENGTH | \-1,001,569 | "Length" |
| STRUCTURAL\_FOUNDATION\_THICKNESS | \-1,001,557 | "Foundation Thickness" |
| STRUCTURAL\_FOUNDATION\_WIDTH | \-1,001,568 | "Width" |
| STRUCTURAL\_FRAME\_CUT\_LENGTH | \-1,001,384 | "Cut Length" |
| STRUCTURAL\_MATERIAL\_PARAM | \-1,005,500 | "Structural Material" |
| STRUCTURAL\_MATERIAL\_TYPE | \-1,001,531 | "Structural Material Type" |
| STRUCTURAL\_MEMBER\_FORCES | \-1,060,012 | "Member Forces" |
| STRUCTURAL\_NUMBER\_OF\_STUDS | \-1,001,529 | "Number of studs" |
| STRUCTURAL\_REFERENCE\_LEVEL\_ELEVATION | \-1,001,653 | "Reference Level Elevation" |
| STRUCTURAL\_SECTION\_AREA | \-1,005,507 | "Section Area" |
| STRUCTURAL\_SECTION\_BOTTOM\_CUT\_HEIGHT | \-1,005,560 | "Bottom Cut Height" |
| STRUCTURAL\_SECTION\_BOTTOM\_CUT\_WIDTH | \-1,005,559 | "Bottom Cut Width" |
| STRUCTURAL\_SECTION\_CANTILEVER\_HEIGHT | \-1,005,562 | "Cantilever Height" |
| STRUCTURAL\_SECTION\_CANTILEVER\_LENGTH | \-1,005,561 | "Cantilever Length" |
| STRUCTURAL\_SECTION\_COMMON\_ALPHA | \-1,005,510 | "Principal Axes Angle" |
| STRUCTURAL\_SECTION\_COMMON\_CENTROID\_HORIZ | \-1,005,508 | "Centroid Horizontal" |
| STRUCTURAL\_SECTION\_COMMON\_CENTROID\_VERTICAL | \-1,005,509 | "Centroid Vertical" |
| STRUCTURAL\_SECTION\_COMMON\_DIAMETER | \-1,005,504 | "Diameter" |
| STRUCTURAL\_SECTION\_COMMON\_ELASTIC\_MODULUS\_STRONG\_AXIS | \-1,005,515 | "Elastic Modulus strong axis" |
| STRUCTURAL\_SECTION\_COMMON\_ELASTIC\_MODULUS\_WEAK\_AXIS | \-1,005,516 | "Elastic Modulus weak axis" |
| STRUCTURAL\_SECTION\_COMMON\_HEIGHT | \-1,005,503 | "Height" |
| STRUCTURAL\_SECTION\_COMMON\_MOMENT\_OF\_INERTIA\_STRONG\_AXIS | \-1,005,513 | "Moment of Inertia strong axis" |
| STRUCTURAL\_SECTION\_COMMON\_MOMENT\_OF\_INERTIA\_WEAK\_AXIS | \-1,005,514 | "Moment of Inertia weak axis" |
| STRUCTURAL\_SECTION\_COMMON\_NOMINAL\_WEIGHT | \-1,005,512 | "Nominal Weight" |
| STRUCTURAL\_SECTION\_COMMON\_PERIMETER | \-1,005,511 | "Perimeter" |
| STRUCTURAL\_SECTION\_COMMON\_PLASTIC\_MODULUS\_STRONG\_AXIS | \-1,005,517 | "Plastic Modulus strong axis" |
| STRUCTURAL\_SECTION\_COMMON\_PLASTIC\_MODULUS\_WEAK\_AXIS | \-1,005,518 | "Plastic Modulus weak axis" |
| STRUCTURAL\_SECTION\_COMMON\_SHEAR\_AREA\_STRONG\_AXIS | \-1,005,522 | "Shear Area strong axis" |
| STRUCTURAL\_SECTION\_COMMON\_SHEAR\_AREA\_WEAK\_AXIS | \-1,005,523 | "Shear Area weak axis" |
| STRUCTURAL\_SECTION\_COMMON\_TORSIONAL\_MODULUS | \-1,005,520 | "Torsional Modulus" |
| STRUCTURAL\_SECTION\_COMMON\_TORSIONAL\_MOMENT\_OF\_INERTIA | \-1,005,519 | "Torsional Moment of Inertia" |
| STRUCTURAL\_SECTION\_COMMON\_WARPING\_CONSTANT | \-1,005,521 | "Warping Constant" |
| STRUCTURAL\_SECTION\_COMMON\_WIDTH | \-1,005,502 | "Width" |
| STRUCTURAL\_SECTION\_CPROFILE\_FOLD\_LENGTH | \-1,005,549 | "Fold Length" |
| STRUCTURAL\_SECTION\_HSS\_INNERFILLET | \-1,005,529 | "Inner Fillet" |
| STRUCTURAL\_SECTION\_HSS\_OUTERFILLET | \-1,005,530 | "Outer Fillet" |
| STRUCTURAL\_SECTION\_ISHAPE\_BOLT\_DIAMETER | \-1,005,539 | "Bolt Diameter" |
| STRUCTURAL\_SECTION\_ISHAPE\_BOLT\_SPACING | \-1,005,538 | "Bolt Spacing" |
| STRUCTURAL\_SECTION\_ISHAPE\_BOLT\_SPACING\_BETWEEN\_ROWS | \-1,005,541 | "Bolt Spacing between Rows" |
| STRUCTURAL\_SECTION\_ISHAPE\_BOLT\_SPACING\_TWO\_ROWS | \-1,005,540 | "Bolt Spacing Two Rows" |
| STRUCTURAL\_SECTION\_ISHAPE\_BOLT\_SPACING\_WEB | \-1,005,542 | "Bolt Spacing web" |
| STRUCTURAL\_SECTION\_ISHAPE\_CLEAR\_WEB\_HEIGHT | \-1,005,535 | "Clear Web Height" |
| STRUCTURAL\_SECTION\_ISHAPE\_FLANGE\_TOE\_OF\_FILLET | \-1,005,536 | "Flange Toe of Fillet" |
| STRUCTURAL\_SECTION\_ISHAPE\_FLANGEFILLET | \-1,005,527 | "Flange Fillet" |
| STRUCTURAL\_SECTION\_ISHAPE\_FLANGETHICKNESS | \-1,005,524 | "Flange Thickness" |
| STRUCTURAL\_SECTION\_ISHAPE\_FLANGETHICKNESS\_LOCATION | \-1,005,566 | "Flange Thickness Location" |
| STRUCTURAL\_SECTION\_ISHAPE\_WEB\_TOE\_OF\_FILLET | \-1,005,537 | "Web Toe of Fillet" |
| STRUCTURAL\_SECTION\_ISHAPE\_WEBFILLET | \-1,005,528 | "Web Fillet" |
| STRUCTURAL\_SECTION\_ISHAPE\_WEBHEIGHT | \-1,005,526 | "Web Height" |
| STRUCTURAL\_SECTION\_ISHAPE\_WEBTHICKNESS | \-1,005,525 | "Web Thickness" |
| STRUCTURAL\_SECTION\_ISHAPE\_WEBTHICKNESS\_LOCATION | \-1,005,567 | "Web Thickness Location" |
| STRUCTURAL\_SECTION\_IWELDED\_BOTTOMFLANGETHICKNESS | \-1,005,533 | "Bottom Flange Thickness" |
| STRUCTURAL\_SECTION\_IWELDED\_BOTTOMFLANGEWIDTH | \-1,005,534 | "Bottom Flange Width" |
| STRUCTURAL\_SECTION\_IWELDED\_TOPFLANGETHICKNESS | \-1,005,531 | "Top Flange Thickness" |
| STRUCTURAL\_SECTION\_IWELDED\_TOPFLANGEWIDTH | \-1,005,532 | "Top Flange Width" |
| STRUCTURAL\_SECTION\_LANGLE\_BOLT\_DIAMETER\_LONGER\_FLANGE | \-1,005,546 | "Bolt Diameter Longer Flange" |
| STRUCTURAL\_SECTION\_LANGLE\_BOLT\_DIAMETER\_SHORTER\_FLANGE | \-1,005,547 | "Bolt Diameter Shorter Flange" |
| STRUCTURAL\_SECTION\_LANGLE\_BOLT\_SPACING\_1\_LONGER\_FLANGE | \-1,005,543 | "Bolt Spacing 1 Longer Flange" |
| STRUCTURAL\_SECTION\_LANGLE\_BOLT\_SPACING\_2\_LONGER\_FLANGE | \-1,005,544 | "Bolt Spacing 2 Longer Flange" |
| STRUCTURAL\_SECTION\_LANGLE\_BOLT\_SPACING\_SHORTER\_FLANGE | \-1,005,545 | "Bolt Spacing Shorter Flange" |
| STRUCTURAL\_SECTION\_LPROFILE\_LIP\_LENGTH | \-1,005,548 | "Lip Length" |
| STRUCTURAL\_SECTION\_NAME\_KEY | \-1,005,554 | "Section Name Key" |
| STRUCTURAL\_SECTION\_PIPESTANDARD\_WALLDESIGNTHICKNESS | \-1,005,506 | "Wall Design Thickness" |
| STRUCTURAL\_SECTION\_PIPESTANDARD\_WALLNOMINALTHICKNESS | \-1,005,505 | "Wall Nominal Thickness" |
| STRUCTURAL\_SECTION\_SHAPE | \-1,005,501 | "Section Shape" |
| STRUCTURAL\_SECTION\_SIGMA\_PROFILE\_BEND\_WIDTH | \-1,005,551 | "Bend Width" |
| STRUCTURAL\_SECTION\_SIGMA\_PROFILE\_MIDDLE\_BEND\_WIDTH | \-1,005,552 | "Middle Bend Length" |
| STRUCTURAL\_SECTION\_SIGMA\_PROFILE\_TOP\_BEND\_WIDTH | \-1,005,553 | "Top Bend Length" |
| STRUCTURAL\_SECTION\_SLOPED\_FLANGE\_ANGLE | \-1,005,563 | "Sloped Flange Angle" |
| STRUCTURAL\_SECTION\_SLOPED\_WEB\_ANGLE | \-1,005,564 | "Sloped Web Angle" |
| STRUCTURAL\_SECTION\_TOP\_CUT\_HEIGHT | \-1,005,558 | "Top Cut Height" |
| STRUCTURAL\_SECTION\_TOP\_CUT\_WIDTH | \-1,005,557 | "Top Cut Width" |
| STRUCTURAL\_SECTION\_TOP\_WEB\_FILLET | \-1,005,565 | "Top Web Fillet" |
| STRUCTURAL\_SECTION\_ZPROFILE\_BOTTOM\_FLANGE\_LENGTH | \-1,005,550 | "Bottom Flange Length" |
| STRUCTURAL\_START\_RELEASE\_FX | \-1,001,517 | "Start Fx" |
| STRUCTURAL\_START\_RELEASE\_FY | \-1,001,518 | "Start Fy" |
| STRUCTURAL\_START\_RELEASE\_FZ | \-1,001,519 | "Start Fz" |
| STRUCTURAL\_START\_RELEASE\_MX | \-1,001,520 | "Start Mx" |
| STRUCTURAL\_START\_RELEASE\_MY | \-1,001,521 | "Start My" |
| STRUCTURAL\_START\_RELEASE\_MZ | \-1,001,522 | "Start Mz" |
| STRUCTURAL\_START\_RELEASE\_TYPE | \-1,001,515 | "Start Release" |
| STRUCTURAL\_STICK\_SYMBOL\_LOCATION | \-1,001,503 | "Stick Symbol Location" |
| STRUCTURAL\_TOP\_RELEASE\_FX | \-1,001,538 | "Top Fx" |
| STRUCTURAL\_TOP\_RELEASE\_FY | \-1,001,539 | "Top Fy" |
| STRUCTURAL\_TOP\_RELEASE\_FZ | \-1,001,540 | "Top Fz" |
| STRUCTURAL\_TOP\_RELEASE\_MX | \-1,001,541 | "Top Mx" |
| STRUCTURAL\_TOP\_RELEASE\_MY | \-1,001,542 | "Top My" |
| STRUCTURAL\_TOP\_RELEASE\_MZ | \-1,001,543 | "Top Mz" |
| STRUCTURAL\_TOP\_RELEASE\_TYPE | \-1,001,536 | "Top Release" |
| STRUCTURAL\_WALL\_BOTTOM\_PROJECTION\_PLANE | \-1,001,514 | "Bottom Vertical Projection" |
| STRUCTURAL\_WALL\_PROJECTION\_SURFACE | \-1,001,512 | "Horizontal Projection" |
| STRUCTURAL\_WALL\_TOP\_PROJECTION\_PLANE | \-1,001,513 | "Top Vertical Projection" |
| SUPPORT\_HAND\_CLEARANCE | \-1,152,165 | "Hand Clearance" |
| SUPPORT\_HEIGHT | \-1,152,166 | "Height" |
| SURFACE\_AREA | \-1,012,601 | "Surface Area" |
| SURFACE\_NAME | \-1,114,834 | "Name" |
| SURFACE\_PATTERN\_ID\_PARAM | \-1,002,102 | "Surface fill pattern" |
| SURFACE\_PERIMETER | \-1,012,602 | "Perimeter" |
| SWEEP\_BASE\_FLOOR\_SUBCATEGORY\_ID | \-1,012,821 | "Subcategory of Floors" |
| SWEEP\_BASE\_OFFSET | \-1,012,825 | "Horizontal Profile Offset" |
| SWEEP\_BASE\_ROOF\_SUBCATEGORY\_ID | \-1,012,820 | "Subcategory of Roofs" |
| SWEEP\_BASE\_VERT\_OFFSET | \-1,012,827 | "Vertical Profile Offset" |
| SWEEP\_MAX\_SEG\_ANGLE | \-1,001,819 | "Maximum Segment Angle" |
| SWEEP\_TRAJ\_SEGMENTED | \-1,001,820 | "Trajectory Segmentation" |
| SYMBOL\_FAMILY\_AND\_TYPE\_NAMES\_PARAM | \-1,002,003 | "Family and Type" |
| SYMBOL\_FAMILY\_NAME\_PARAM | \-1,002,002 | "Family Name" |
| SYMBOL\_ID\_PARAM | \-1,002,000 | "Type Id" |
| SYMBOL\_NAME\_PARAM | \-1,002,001 | "Type Name" |
| SYSTEM\_EQUIPMENT\_SETS | \-1,153,115 | "Equipment Sets" |
| SYSTEM\_ZONE\_AREA | \-1,114,712 | "System\-Zone Area" |
| SYSTEM\_ZONE\_LEVEL\_ID | \-1,114,705 | "Level" |
| SYSTEM\_ZONE\_VOLUME | \-1,114,714 | "System\-Zone Volume" |
| SYSTEMS\_ANALYSIS\_REPORT\_FOLDER | \-1,114,824 | "Reports Folder Path" |
| SYSTEMS\_ANALYSIS\_REPORT\_STYLE | \-1,114,823 | "Report Style" |
| TAG\_ANGLE\_PARAM | \-1,007,007 | "Angle" |
| TAG\_ELEMENT\_COUNT | \-1,007,008 | "Host Count" |
| TAG\_ELEVATION\_BASE | \-1,007,010 | "Elevation Base" |
| TAG\_HEAD\_ALIGNMENT | \-1,180,310 | "Tag Alignment" |
| TAG\_HEAD\_POSITION | \-1,180,302 | "Tag Position" |
| TAG\_LEADER\_TYPE | \-1,007,006 | "Leader Type" |
| TAG\_NO\_BREAK\_PARAM\_STRINGS | \-1,007,005 | "Wrap between parameters only" |
| TAG\_ON\_PLACEMENT\_UI | \-1,155,096 | "Tag on Placement" |
| TAG\_ORIENTATION\_BEHAVIOR | \-1,155,321 | "Tag Orientation" |
| TAG\_ORIENTATION\_PARAM | \-1,007,003 | "Orientation" |
| TAG\_SAMPLE\_TEXT | \-1,007,001 | "Sample Text" |
| TAG\_TAG | \-1,007,000 | "Label" |
| TEMPLATE\_NAME | \-1,140,167 | "Template" |
| TERMINATION\_EXTENSION\_LENGTH | \-1,152,167 | "Extension Length" |
| TEXT\_ALIGN\_HORZ | \-1,006,308 | "Horizontal Align" |
| TEXT\_ALIGN\_VERT | \-1,006,309 | "Vertical Align" |
| TEXT\_ALIGNMENT | \-1,006,400 | "Text Alignment" |
| TEXT\_BACKGROUND | \-1,006,314 | "Background" |
| TEXT\_BOX\_VISIBILITY | \-1,150,213 | "Show Border" |
| TEXT\_COLOR | \-1,006,302 | "Color" |
| TEXT\_DIST\_TO\_LINE | \-1,006,401 | "Text Offset" |
| TEXT\_FONT | \-1,006,300 | "Text Font" |
| TEXT\_POSITION | \-1,006,411 | "Text Position" |
| TEXT\_SIZE | \-1,006,301 | "Text Size" |
| TEXT\_STYLE\_BOLD | \-1,006,311 | "Bold" |
| TEXT\_STYLE\_FONT | \-1,006,334 | "Font" |
| TEXT\_STYLE\_ITALIC | \-1,006,312 | "Italic" |
| TEXT\_STYLE\_SIZE | \-1,006,335 | "Size" |
| TEXT\_STYLE\_UNDERLINE | \-1,006,313 | "Underline" |
| TEXT\_TAB\_SIZE | \-1,006,326 | "Tab Size" |
| TEXT\_TEXT | \-1,006,307 | "Text" |
| TEXT\_WIDTH\_SCALE | \-1,006,327 | "Width Factor" |
| THERMAL\_MATERIAL\_CONDUCTIVITY | \-1,114,852 | "Thermal Conductivity" |
| THERMAL\_MATERIAL\_DENSITY | \-1,114,853 | "Density" |
| THERMAL\_MATERIAL\_DESCRIPTION | \-1,114,850 | "Description" |
| THERMAL\_MATERIAL\_NAME | \-1,114,849 | "Name" |
| THERMAL\_MATERIAL\_PARAM\_COMPRESSIBILITY | \-1,152,322 | "Compressibility" |
| THERMAL\_MATERIAL\_PARAM\_ELECTRICAL\_RESISTIVITY | \-1,152,330 | "Electrical Resistivity" |
| THERMAL\_MATERIAL\_PARAM\_EMISSIVITY | \-1,152,320 | "Emissivity" |
| THERMAL\_MATERIAL\_PARAM\_GAS\_VISCOSITY | \-1,152,321 | "Gas Viscosity" |
| THERMAL\_MATERIAL\_PARAM\_LIQUID\_VISCOSITY | \-1,152,323 | "Liquid Viscosity" |
| THERMAL\_MATERIAL\_PARAM\_PERMEABILITY | \-1,152,327 | "Permeability" |
| THERMAL\_MATERIAL\_PARAM\_POROSITY | \-1,152,328 | "Porosity" |
| THERMAL\_MATERIAL\_PARAM\_REFLECTIVITY | \-1,152,329 | "Reflectivity" |
| THERMAL\_MATERIAL\_PARAM\_SPECIFIC\_HEAT\_OF\_VAPORIZATION | \-1,152,324 | "Specific Heat of Vaporization" |
| THERMAL\_MATERIAL\_PARAM\_TRANSMITS\_LIGHT | \-1,152,326 | "Transmits Light" |
| THERMAL\_MATERIAL\_PARAM\_VAPOR\_PRESSURE | \-1,152,325 | "Vapor Pressure" |
| THERMAL\_MATERIAL\_SPECIFIC\_HEAT\_CAPACITY | \-1,114,854 | "Specific Heat Capacity" |
| THERMAL\_MATERIAL\_THICKNESS | \-1,114,851 | "Thickness" |
| TICK\_MARK\_PEN | \-1,006,412 | "Tick Mark Line Weight" |
| TILE\_PATTERN\_FAMREF\_COMPONENT\_EXTENTS | \-1,150,202 | "Component Extents" |
| TILE\_PATTERN\_GRID\_CELLS\_X | \-1,150,200 | "Number of horizontal cells" |
| TILE\_PATTERN\_GRID\_CELLS\_Y | \-1,150,201 | "Number of vertical cells" |
| TILE\_PATTERN\_GRID\_UNIT\_X | \-1,150,198 | "Horizontal spacing" |
| TILE\_PATTERN\_GRID\_UNIT\_Y | \-1,150,199 | "Vertical spacing" |
| TILT | \-1,114,829 | "Tilt" |
| TITLE\_FONT | \-1,006,328 | "Font" |
| TITLE\_SIZE | \-1,006,329 | "Size" |
| TITLE\_STYLE\_BOLD | \-1,006,330 | "Bold" |
| TITLE\_STYLE\_ITALIC | \-1,006,331 | "Italic" |
| TITLE\_STYLE\_UNDERLINE | \-1,006,332 | "Underline" |
| TOPOGRAPHY\_LINK\_NAME | \-1,012,408 | "Link Name" |
| TOPOGRAPHY\_LINK\_PATH | \-1,012,409 | "Saved Path" |
| TOPOSOLID\_ATTR\_THICKNESS\_PARAM | \-1,155,254 | "Thickness" |
| TOPOSOLID\_CONTOUR\_DISPLAY\_SETTINGS\_ID\_PARAM | \-1,155,268 | "Contour Display" |
| TOPOSOLID\_CONTOUR\_SUBCATEGORY\_ID | \-1,155,269 | "Subcategory" |
| TOPOSOLID\_ELEVATION\_AT\_BOTTOM | \-1,155,260 | "Elevation at Bottom" |
| TOPOSOLID\_ELEVATION\_AT\_TOP | \-1,155,261 | "Elevation at Top" |
| TOPOSOLID\_FACES\_LOCATION | \-1,180,201 | "Picked Faces Location" |
| TOPOSOLID\_FUNCTION\_PARAM | \-1,155,264 | "Function" |
| TOPOSOLID\_HEIGHTABOVELEVEL\_PARAM | \-1,155,255 | "Height Offset From Level" |
| TOPOSOLID\_INHERIT\_CONTOURS | \-1,155,265 | "Inherit Contours" |
| TOPOSOLID\_STRUCTURE\_ID\_PARAM | \-1,155,259 | "Structure" |
| TOPOSOLID\_SUBDIVIDE\_HEIGHT | \-1,155,266 | "Sub\-divide Offset" |
| TOPOSOLID\_SUBDIVIDE\_MATERIAL | \-1,155,267 | "Material" |
| TOPOSOLID\_TYPE\_DEFAULT\_THICKNESS\_PARAM | \-1,155,253 | "Default Thickness" |
| TOPOSURFACE\_CONTOUR\_SUBCATEGORY\_ID | \-1,012,405 | "Subcategory" |
| TOTAL\_EXCAVATION\_VOLUME | \-1,180,307 | "Total Excavation Volume" |
| TRAP\_MULL\_WIDTH | \-1,007,359 | "Center Width" |
| TRUSS\_BEARING\_CHORD\_TOP\_BOTTOM\_PARAM | \-1,140,716 | "Bearing Chord" |
| TRUSS\_ELEMENT\_ANGLE\_PARAM | \-1,140,703 | "Rotation Angle" |
| TRUSS\_ELEMENT\_BEARING\_JUST\_PARAM | \-1,140,706 | "Bearing Vertical Justification" |
| TRUSS\_ELEMENT\_CLASS\_PARAM | \-1,140,702 | "Engineering Type" |
| TRUSS\_ELEMENT\_CREATE\_BOTTOM\_PARAM | \-1,140,705 | "Create Bottom Chord" |
| TRUSS\_ELEMENT\_CREATE\_TOP\_PARAM | \-1,140,704 | "Create Top Chord" |
| TRUSS\_ELEMENT\_END0\_ELEVATION | \-1,140,707 | "Start Level Offset" |
| TRUSS\_ELEMENT\_END1\_ELEVATION | \-1,140,708 | "End Level Offset" |
| TRUSS\_ELEMENT\_REFERENCE\_LEVEL\_PARAM | \-1,140,709 | "Reference Level" |
| TRUSS\_ELEMENT\_ROTATE\_CHORDS\_WITH\_TRUSS | \-1,140,710 | "Rotate Chords With Truss" |
| TRUSS\_ELEMENT\_SPAN\_PARAM | \-1,140,715 | "Span" |
| TRUSS\_ELEMENT\_STICK\_JUST\_PARAM | \-1,140,714 | "Stick Symbol Location" |
| TRUSS\_ELEMENT\_TAG\_NEW\_MEMBERS\_VIEW | \-1,140,718 | "Tag new members in view" |
| TRUSS\_FAMILY\_BOTTOM\_CHORD\_ANGLE\_PARAM | \-1,140,764 | "Angle" |
| TRUSS\_FAMILY\_BOTTOM\_CHORD\_END\_RELEASE\_TYPE | \-1,140,761 | "End Release" |
| TRUSS\_FAMILY\_BOTTOM\_CHORD\_START\_RELEASE\_TYPE | \-1,140,762 | "Start Release" |
| TRUSS\_FAMILY\_BOTTOM\_CHORD\_STRUCTURAL\_TYPES\_PARAM | \-1,140,766 | "Structural Framing Type" |
| TRUSS\_FAMILY\_BOTTOM\_CHORD\_VERTICAL\_PROJECTION\_PARAM | \-1,140,763 | "Analytical Vertical Projection" |
| TRUSS\_FAMILY\_DIAG\_WEB\_ANGLE\_PARAM | \-1,140,734 | "Angle" |
| TRUSS\_FAMILY\_DIAG\_WEB\_END\_RELEASE\_TYPE | \-1,140,731 | "End Release" |
| TRUSS\_FAMILY\_DIAG\_WEB\_START\_RELEASE\_TYPE | \-1,140,732 | "Start Release" |
| TRUSS\_FAMILY\_DIAG\_WEB\_STRUCTURAL\_TYPES\_PARAM | \-1,140,736 | "Structural Framing Type" |
| TRUSS\_FAMILY\_TOP\_CHORD\_ANGLE\_PARAM | \-1,140,744 | "Angle" |
| TRUSS\_FAMILY\_TOP\_CHORD\_END\_RELEASE\_TYPE | \-1,140,741 | "End Release" |
| TRUSS\_FAMILY\_TOP\_CHORD\_START\_RELEASE\_TYPE | \-1,140,742 | "Start Release" |
| TRUSS\_FAMILY\_TOP\_CHORD\_STRUCTURAL\_TYPES\_PARAM | \-1,140,746 | "Structural Framing Type" |
| TRUSS\_FAMILY\_TOP\_CHORD\_VERTICAL\_PROJECTION\_PARAM | \-1,140,743 | "Analytical Vertical Projection" |
| TRUSS\_FAMILY\_TRANSFORMATION\_PARAM | \-1,140,711 | "Web Orientation" |
| TRUSS\_FAMILY\_VERT\_WEB\_ANGLE\_PARAM | \-1,140,724 | "Angle" |
| TRUSS\_FAMILY\_VERT\_WEB\_END\_RELEASE\_TYPE | \-1,140,721 | "End Release" |
| TRUSS\_FAMILY\_VERT\_WEB\_START\_RELEASE\_TYPE | \-1,140,722 | "Start Release" |
| TRUSS\_FAMILY\_VERT\_WEB\_STRUCTURAL\_TYPES\_PARAM | \-1,140,726 | "Structural Framing Type" |
| TRUSS\_FAMILY\_WEBS\_HAVE\_SYMBOLIC\_CUTBACK\_PARAM | \-1,140,713 | "Webs have symbolic cutback" |
| TRUSS\_HEIGHT | \-1,140,712 | "Truss Height" |
| TRUSS\_LENGTH | \-1,140,700 | "Truss Length" |
| TRUSS\_NON\_BEARING\_OFFSET\_PARAM | \-1,140,717 | "Non Bearing Offset" |
| TYPE\_WALL\_CLOSURE | \-1,001,390 | "Wall Closure" |
| USE\_3D\_SNAPPING | \-1,123,513 | "3D Snapping" |
| USING\_MULTIPLE | \-1,180,000 | "Multiple Join" |
| VIEW\_ANALYSIS\_DISPLAY\_STYLE | \-1,005,332 | "Default Analysis Display Style" |
| VIEW\_ANALYSIS\_RESULTS\_VISIBILITY | \-1,006,857 | "Analysis Display Settings" |
| VIEW\_ANCHOR | \-1,013,203 | "View Anchor" |
| VIEW\_ASSOCIATED\_ASSEMBLY\_INSTANCE\_ID | \-1,005,179 | "Associated Assembly Instance" |
| VIEW\_BACK\_CLIPPING | \-1,005,181 | "Depth Clipping" |
| VIEW\_CAMERA\_ORIENTATION | \-1,005,184 | "Locked Orientation" |
| VIEW\_CAMERA\_POSITION | \-1,005,169 | "Camera Position" |
| VIEW\_CLEAN\_JOINS | \-1,005,158 | "Wall Join Display" |
| VIEW\_DEPENDENCY | \-1,005,182 | "Dependency" |
| VIEW\_DEPTH | \-1,005,154 | "View Depth" |
| VIEW\_DESCRIPTION | \-1,005,114 | "Title on Sheet" |
| VIEW\_DETAIL\_LEVEL | \-1,011,002 | "Detail Level" |
| VIEW\_DISCIPLINE | \-1,005,163 | "Discipline" |
| VIEW\_FAMILY | \-1,012,109 | "Family" |
| VIEW\_FAMILY\_AND\_TYPE\_SCHEDULES | \-1,139,998 | "Family and Type" |
| VIEW\_FAMILY\_SCHEDULES | \-1,139,999 | "Family" |
| VIEW\_FIXED\_SKETCH\_PLANE | \-1,005,147 | "None" |
| VIEW\_GRAPH\_SCHED\_BOTTOM\_LEVEL | \-1,005,314 | "Bottom Level" |
| VIEW\_GRAPH\_SCHED\_GRID\_APPEARANCE | \-1,005,327 | "Grid Appearance" |
| VIEW\_GRAPH\_SCHED\_GROUP\_SIMILAR | \-1,005,318 | "Group Similar Locations" |
| VIEW\_GRAPH\_SCHED\_HIDDEN\_LEVELS | \-1,005,330 | "Hidden Levels" |
| VIEW\_GRAPH\_SCHED\_LEVEL\_RELATIVE\_BASE\_TYPE | \-1,005,331 | "Elevation Base for Levels" |
| VIEW\_GRAPH\_SCHED\_LOCATIONS\_HIGH | \-1,005,316 | "Column Locations End" |
| VIEW\_GRAPH\_SCHED\_LOCATIONS\_LOW | \-1,005,315 | "Column Locations Start" |
| VIEW\_GRAPH\_SCHED\_MATERIAL\_TYPES | \-1,005,317 | "Material Types" |
| VIEW\_GRAPH\_SCHED\_NUMBER\_COLUMNS | \-1,005,175 | "Column Locations per Segment" |
| VIEW\_GRAPH\_SCHED\_OFF\_GRID | \-1,005,209 | "Include Off\-Grid Columns" |
| VIEW\_GRAPH\_SCHED\_ROWS\_COUNT | \-1,005,328 | "Segments in Viewport" |
| VIEW\_GRAPH\_SCHED\_ROWS\_FROM | \-1,005,319 | "Segment Start in Viewport" |
| VIEW\_GRAPH\_SCHED\_TEXT\_APPEARANCE | \-1,005,326 | "Text Appearance" |
| VIEW\_GRAPH\_SCHED\_TITLE | \-1,005,325 | "Title" |
| VIEW\_GRAPH\_SCHED\_TOP\_LEVEL | \-1,005,313 | "Top Level" |
| VIEW\_GRAPH\_SCHED\_TOTAL\_COLUMNS | \-1,005,178 | "Total Column Locations" |
| VIEW\_GRAPH\_SCHED\_TOTAL\_ROWS | \-1,005,329 | "Total Segments" |
| VIEW\_GRAPH\_SCHED\_UNITS\_FORMAT | \-1,005,208 | "Off\-Grid Units Format" |
| VIEW\_GRAPH\_SUN\_PATH | \-1,005,333 | "Sun Path" |
| VIEW\_GRAPH\_SUN\_PATH\_SIZE | \-1,005,334 | "Sun path size (%)" |
| VIEW\_MODEL\_DISPLAY\_MODE | \-1,005,161 | "Display Model" |
| VIEW\_NAME | \-1,005,112 | "View Name" |
| VIEW\_PARTS\_VISIBILITY | \-1,011,003 | "Parts Visibility" |
| VIEW\_PHASE | \-1,012,102 | "Phase" |
| VIEW\_PHASE\_FILTER | \-1,012,103 | "Phase Filter" |
| VIEW\_POSITION | \-1,013,202 | "Saved Position" |
| VIEW\_POSITION\_NAME | \-1,013,206 | "Name" |
| VIEW\_POSITION\_X | \-1,013,204 | "View Position X" |
| VIEW\_POSITION\_Y | \-1,013,205 | "View Position Y" |
| VIEW\_REFERENCING\_DETAIL | \-1,005,171 | "Referencing Detail" |
| VIEW\_REFERENCING\_SHEET | \-1,005,170 | "Referencing Sheet" |
| VIEW\_REFERENCING\_SHEET\_COLLECTION | \-1,005,222 | "Referencing Sheet Collection" |
| VIEW\_SCALE | \-1,005,150 | "Scale Value 1:" |
| VIEW\_SCALE\_CUSTOMNAME | \-1,005,230 | "Display Name" |
| VIEW\_SCALE\_HAVENAME | \-1,005,231 | "Display Name" |
| VIEW\_SCALE\_PULLDOWN\_IMPERIAL | \-1,005,152 | "View Scale" |
| VIEW\_SCALE\_PULLDOWN\_METRIC | \-1,005,151 | "View Scale" |
| VIEW\_SCHEMA\_SETTING\_FOR\_BUILDING | \-1,005,148 | "Color Scheme" |
| VIEW\_SCHEMA\_SETTING\_FOR\_SYSTEM | \-1,005,149 | "System Color Schemes" |
| VIEW\_SCHEMA\_SETTING\_FOR\_SYSTEM\_TEMPLATE | \-1,133,900 | "System Color Schemes" |
| VIEW\_SHEET\_VIEWPORT\_INFO | \-1,005,157 | "Viewport" |
| VIEW\_SHOW\_GRIDS | \-1,155,222 | "Show Grids" |
| VIEW\_SHOW\_HIDDEN\_LINES | \-1,154,613 | "Show Hidden Lines" |
| VIEW\_SHOW\_MASSING | \-1,005,160 | "Show Mass" |
| VIEW\_SLANTED\_COLUMN\_SYMBOL\_OFFSET | \-1,150,170 | "Column Symbolic Offset" |
| VIEW\_SOLARSTUDY\_ANIMATION\_SPEED\_TEXT | \-1,005,356 | "Loop animation speed" |
| VIEW\_SOLARSTUDY\_ANIMATION\_SPEED\_VALUE | \-1,005,355 | "Loop animation speed" |
| VIEW\_SOLARSTUDY\_CURRENT\_STUDY\_TYPE\_INDEX | \-1,005,350 | "Study type" |
| VIEW\_SOLARSTUDY\_IS\_LIGHTING\_STUDY\_TYPE | \-1,005,354 | "Lighting study" |
| VIEW\_SOLARSTUDY\_IS\_MULTIDAY\_STUDY\_TYPE | \-1,005,353 | "Multi\-day study" |
| VIEW\_SOLARSTUDY\_IS\_SINGLEDAY\_STUDY\_TYPE | \-1,005,352 | "Single day study" |
| VIEW\_SOLARSTUDY\_IS\_STILLIMAGE\_STUDY\_TYPE | \-1,005,351 | "Still image study" |
| VIEW\_SOLARSTUDY\_LIGHTING\_ALTITUDE\_TEXT | \-1,005,378 | "Lighting altitude text" |
| VIEW\_SOLARSTUDY\_LIGHTING\_ALTITUDE\_VALUE | \-1,005,377 | "Lighting altitude" |
| VIEW\_SOLARSTUDY\_LIGHTING\_AZIMUTH\_TEXT | \-1,005,376 | "Lighting azimuth text" |
| VIEW\_SOLARSTUDY\_LIGHTING\_AZIMUTH\_VALUE | \-1,005,375 | "Lighting azimuth" |
| VIEW\_SOLARSTUDY\_LIGHTING\_PRESET\_INDEX | \-1,005,364 | "Lighting presets combo" |
| VIEW\_SOLARSTUDY\_MULTIDAY\_DATETIME\_TEXT | \-1,005,374 | "Multi\-day date and time text" |
| VIEW\_SOLARSTUDY\_MULTIDAY\_FRAME\_TEXT | \-1,005,373 | "Multi\-day frame text" |
| VIEW\_SOLARSTUDY\_MULTIDAY\_FRAME\_VALUE | \-1,005,372 | "Multi\-day frame" |
| VIEW\_SOLARSTUDY\_MULTIDAY\_PRESET\_INDEX | \-1,005,363 | "Multi\-day presets combo" |
| VIEW\_SOLARSTUDY\_SHADOWS\_INTENSITY\_TEXT | \-1,005,360 | "Shadows intensity text" |
| VIEW\_SOLARSTUDY\_SHADOWS\_INTENSITY\_VALUE | \-1,005,359 | "Shadows intensity" |
| VIEW\_SOLARSTUDY\_SINGLEDAY\_DATETIME\_TEXT | \-1,005,371 | "Single day date and time text" |
| VIEW\_SOLARSTUDY\_SINGLEDAY\_FRAME\_TEXT | \-1,005,370 | "Single day frame text" |
| VIEW\_SOLARSTUDY\_SINGLEDAY\_FRAME\_VALUE | \-1,005,369 | "Single day frame" |
| VIEW\_SOLARSTUDY\_SINGLEDAY\_PRESET\_INDEX | \-1,005,362 | "Single day presets combo" |
| VIEW\_SOLARSTUDY\_STILL\_DATE\_TEXT | \-1,005,366 | "Still date text" |
| VIEW\_SOLARSTUDY\_STILL\_DATE\_VALUE | \-1,005,365 | "Still date" |
| VIEW\_SOLARSTUDY\_STILL\_PRESET\_INDEX | \-1,005,361 | "Still presets combo" |
| VIEW\_SOLARSTUDY\_STILL\_TIME\_TEXT | \-1,005,368 | "Still time text" |
| VIEW\_SOLARSTUDY\_STILL\_TIME\_VALUE | \-1,005,367 | "Still time" |
| VIEW\_SOLARSTUDY\_SUN\_INTENSITY\_TEXT | \-1,005,358 | "Sun intensity text" |
| VIEW\_SOLARSTUDY\_SUN\_INTENSITY\_VALUE | \-1,005,357 | "Sun intensity" |
| VIEW\_TEMPLATE | \-1,005,176 | "View Template" |
| VIEW\_TEMPLATE\_FOR\_SCHEDULE | \-1,005,199 | "View Template" |
| VIEW\_TYPE | \-1,012,106 | "Family and Type" |
| VIEW\_TYPE\_SCHEDULES | \-1,139,997 | "Type" |
| VIEW\_UNDERLAY\_BOTTOM\_ID | \-1,005,153 | "Range: Base Level" |
| VIEW\_UNDERLAY\_ORIENTATION | \-1,005,177 | "Underlay Orientation" |
| VIEW\_UNDERLAY\_TOP\_ID | \-1,005,335 | "Range: Top Level" |
| VIEW\_VISIBLE\_CATEGORIES | \-1,005,164 | "Visibility/Graphics Overrides" |
| VIEWER\_ANNOTATION\_CROP\_ACTIVE | \-1,005,094 | "Annotation Crop" |
| VIEWER\_BOUND\_ACTIVE\_BOTTOM | \-1,005,109 | "Bottom Clip Active" |
| VIEWER\_BOUND\_ACTIVE\_FAR | \-1,005,110 | "Far Clip Active" |
| VIEWER\_BOUND\_ACTIVE\_LEFT | \-1,005,107 | "Left Clip Active" |
| VIEWER\_BOUND\_ACTIVE\_NEAR | \-1,005,111 | "Near Clip Active" |
| VIEWER\_BOUND\_ACTIVE\_RIGHT | \-1,005,106 | "Right Clip Active" |
| VIEWER\_BOUND\_ACTIVE\_TOP | \-1,005,108 | "Top Clip Active" |
| VIEWER\_BOUND\_FAR\_CLIPPING | \-1,005,123 | "Far Clipping" |
| VIEWER\_BOUND\_OFFSET\_BOTTOM | \-1,005,103 | "Bottom Clip Offset" |
| VIEWER\_BOUND\_OFFSET\_FAR | \-1,005,104 | "Far Clip Offset" |
| VIEWER\_BOUND\_OFFSET\_LEFT | \-1,005,101 | "Left Clip Offset" |
| VIEWER\_BOUND\_OFFSET\_NEAR | \-1,005,105 | "Near Clip Offset" |
| VIEWER\_BOUND\_OFFSET\_RIGHT | \-1,005,100 | "Right Clip Offset" |
| VIEWER\_BOUND\_OFFSET\_TOP | \-1,005,102 | "Top Clip Offset" |
| VIEWER\_CROP\_REGION | \-1,005,090 | "Crop View" |
| VIEWER\_CROP\_REGION\_DISABLED | \-1,005,092 | "Crop View" |
| VIEWER\_CROP\_REGION\_VISIBLE | \-1,005,091 | "Crop Region Visible" |
| VIEWER\_DETAIL\_NUMBER | \-1,006,602 | "Detail Number" |
| VIEWER\_EYE\_ELEVATION | \-1,005,000 | "Eye Elevation" |
| VIEWER\_IS\_REFERENCE | \-1,005,121 | "Is a Reference" |
| VIEWER\_MODEL\_CLIP\_BOX\_ACTIVE | \-1,005,113 | "Section Box" |
| VIEWER\_OPTION\_VISIBILITY | \-1,005,001 | "Visible In Option" |
| VIEWER\_PERSPECTIVE | \-1,005,050 | "Projection Mode" |
| VIEWER\_REFERENCE\_LABEL | \-1,005,120 | "Reference Label" |
| VIEWER\_REFERENCE\_LABEL\_TEXT | \-1,005,122 | "Default Reference Label" |
| VIEWER\_SHEET\_COLLECTION | \-1,005,224 | "Sheet Collection" |
| VIEWER\_SHEET\_NAME | \-1,005,223 | "Sheet Name" |
| VIEWER\_SHEET\_NUMBER | \-1,006,601 | "Sheet Number" |
| VIEWER\_SHOW\_UNCROPPED | \-1,005,093 | "Show uncropped" |
| VIEWER\_TARGET\_ELEVATION | \-1,005,002 | "Target Elevation" |
| VIEWER\_VOLUME\_OF\_INTEREST\_CROP | \-1,012,202 | "Scope Box" |
| VIEWER3D\_RENDER\_SETTINGS | \-1,005,124 | "Rendering Settings" |
| VIEWPORT\_ATTR\_LABEL\_TAG | \-1,005,250 | "Title" |
| VIEWPORT\_ATTR\_ORIENTATION\_ON\_SHEET | \-1,005,254 | "Rotation on Sheet" |
| VIEWPORT\_ATTR\_PRESERVE\_TITLE\_POSITION | \-1,005,211 | "Preserve Title Position" |
| VIEWPORT\_ATTR\_SHOW\_BOX | \-1,005,253 | "Show Box" |
| VIEWPORT\_ATTR\_SHOW\_EXTENSION\_LINE | \-1,005,252 | "Show Extension Line" |
| VIEWPORT\_ATTR\_SHOW\_LABEL | \-1,005,251 | "Show Title" |
| VIEWPORT\_DETAIL\_NUMBER | \-1,005,201 | "Detail Number" |
| VIEWPORT\_POSITIONING | \-1,005,210 | "Viewport Positioning" |
| VIEWPORT\_SCALE | \-1,005,204 | "View Scale" |
| VIEWPORT\_SHEET\_COLLECTION | \-1,005,221 | "Sheet Collection" |
| VIEWPORT\_SHEET\_NAME | \-1,005,207 | "Sheet Name" |
| VIEWPORT\_SHEET\_NUMBER | \-1,005,206 | "Sheet Number" |
| VIEWPORT\_VIEW | \-1,005,202 | "View" |
| VIEWPORT\_VIEW\_NAME | \-1,005,203 | "View Name" |
| VIS\_GRAPHICS\_ANALYTICAL\_MODEL | \-1,006,967 | "V/G Overrides Analytical Model" |
| VIS\_GRAPHICS\_ANNOTATION | \-1,006,962 | "V/G Overrides Annotation" |
| VIS\_GRAPHICS\_COORDINATION\_MODEL | \-1,006,970 | "V/G Overrides Coordination Model" |
| VIS\_GRAPHICS\_DESIGNOPTIONS | \-1,006,966 | "V/G Overrides Design Options" |
| VIS\_GRAPHICS\_FILTERS | \-1,006,964 | "V/G Overrides Filters" |
| VIS\_GRAPHICS\_IMPORT | \-1,006,963 | "V/G Overrides Import" |
| VIS\_GRAPHICS\_MODEL | \-1,006,961 | "V/G Overrides Model" |
| VIS\_GRAPHICS\_POINT\_CLOUDS | \-1,006,969 | "V/G Overrides Point Clouds" |
| VIS\_GRAPHICS\_RVT\_LINKS | \-1,006,965 | "V/G Overrides RVT Links" |
| VIS\_GRAPHICS\_WORKSETS | \-1,006,968 | "V/G Overrides Worksets" |
| VOID\_CUTS\_GEOMETRY | \-1,155,218 | "Cuts Geometry" |
| VOLUME\_CUT | \-1,012,603 | "Cut" |
| VOLUME\_FILL | \-1,012,604 | "Fill" |
| VOLUME\_NET | \-1,012,611 | "Net cut/fill" |
| VOLUME\_OF\_INTEREST\_HEIGHT | \-1,012,114 | "Height" |
| VOLUME\_OF\_INTEREST\_NAME | \-1,012,205 | "Name" |
| VOLUME\_OF\_INTEREST\_VIEWS\_VISIBLE | \-1,012,203 | "Views Visible" |
| WALKTHROUGH\_FRAMES\_COUNT | \-1,005,167 | "Walkthrough Frames" |
| WALL\_ALIGN\_KEY\_REF\_PARAM | \-1,016,021 | "Location line to align" |
| WALL\_ATTR\_DEFHEIGHT\_PARAM | \-1,001,002 | "Default height" |
| WALL\_ATTR\_HEIGHT\_PARAM | \-1,001,001 | "Height" |
| WALL\_ATTR\_ROOM\_BOUNDING | \-1,001,007 | "Room Bounding" |
| WALL\_ATTR\_WIDTH\_PARAM | \-1,001,000 | "Width" |
| WALL\_BASE\_CONSTRAINT | \-1,001,107 | "Base Constraint" |
| WALL\_BASE\_HEIGHT\_PARAM | \-1,001,102 | "Base height" |
| WALL\_BASE\_OFFSET | \-1,001,108 | "Base Offset" |
| WALL\_BOTTOM\_EXTENSION\_DIST\_PARAM | \-1,012,829 | "Base Extension Distance" |
| WALL\_BOTTOM\_IS\_ATTACHED | \-1,001,118 | "Base is Attached" |
| WALL\_CROSS\_SECTION | \-1,019,100 | "Cross\-Section" |
| WALL\_HEIGHT\_TYPE | \-1,001,103 | "Top Constraint" |
| WALL\_JOIN\_VIS | \-1,001,011 | "Display" |
| WALL\_KEY\_REF\_PARAM | \-1,001,122 | "Location Line" |
| WALL\_LOCATION\_LINE\_OFFSET\_PARAM | \-1,001,123 | "Location Line Offset" |
| WALL\_SINGLE\_SLANT\_ANGLE\_FROM\_VERTICAL | \-1,019,101 | "Angle From Vertical" |
| WALL\_STRUCTURAL\_SIGNIFICANT | \-1,001,596 | "Structural" |
| WALL\_STRUCTURAL\_USAGE\_PARAM | \-1,001,119 | "Structural Usage" |
| WALL\_STRUCTURE\_ID\_PARAM | \-1,002,103 | "Structure" |
| WALL\_SWEEP\_CUT\_BY\_INSERTS\_PARAM | \-1,012,838 | "Cut by Inserts" |
| WALL\_SWEEP\_CUTS\_WALL\_PARAM | \-1,012,839 | "Cuts Wall" |
| WALL\_SWEEP\_DEFAULT\_SETBACK\_PARAM | \-1,012,840 | "Default Setback" |
| WALL\_SWEEP\_LEVEL\_PARAM | \-1,012,801 | "Level" |
| WALL\_SWEEP\_OFFSET\_PARAM | \-1,012,802 | "Offset From Level" |
| WALL\_SWEEP\_ORIENTATION | \-1,001,399 | "Orientation" |
| WALL\_SWEEP\_PLACEMENT\_HORIZONTAL | \-1,027,602 | "Horizontal" |
| WALL\_SWEEP\_PLACEMENT\_VERTICAL | \-1,027,603 | "Vertical" |
| WALL\_SWEEP\_PROFILE\_PARAM | \-1,012,800 | "Profile" |
| WALL\_SWEEP\_RETURN\_ANGLE | \-1,027,601 | "Return Angle" |
| WALL\_SWEEP\_WALL\_OFFSET\_PARAM | \-1,012,804 | "Offset From Wall" |
| WALL\_SWEEP\_WALL\_SUBCATEGORY\_ID | \-1,012,809 | "Subcategory of Walls" |
| WALL\_TAPERED\_EXTERIOR\_INWARD\_ANGLE | \-1,019,102 | "Exterior Angle" |
| WALL\_TAPERED\_INTERIOR\_INWARD\_ANGLE | \-1,019,103 | "Interior Angle" |
| WALL\_TAPERED\_USE\_INSTANCE\_ANGLES | \-1,019,110 | "Enable Angle Overrides" |
| WALL\_TAPERED\_WIDTH\_AT\_BOTTOM | \-1,019,121 | "Bottom Width" |
| WALL\_TAPERED\_WIDTH\_AT\_TOP | \-1,019,120 | "Top Width" |
| WALL\_TOP\_EXTENSION\_DIST\_PARAM | \-1,012,828 | "Top Extension Distance" |
| WALL\_TOP\_IS\_ATTACHED | \-1,001,117 | "Top is Attached" |
| WALL\_TOP\_OFFSET | \-1,001,109 | "Top Offset" |
| WALL\_TYPE\_DEFAULT\_TAPERED\_EXTERIOR\_INWARD\_ANGLE | \-1,019,105 | "Default Exterior Angle" |
| WALL\_TYPE\_DEFAULT\_TAPERED\_INTERIOR\_INWARD\_ANGLE | \-1,019,106 | "Default Interior Angle" |
| WALL\_TYPE\_WIDTH\_MEASURED\_AT | \-1,019,107 | "Width Measured At" |
| WALL\_USER\_HEIGHT\_PARAM | \-1,001,105 | "Unconnected Height" |
| WINDOW\_CONSTRUCTION\_TYPE | \-1,001,207 | "Construction Type" |
| WINDOW\_HEIGHT | \-1,001,300 | "Height" |
| WINDOW\_INSET | \-1,001,303 | "Inset" |
| WINDOW\_OPERATION\_TYPE | \-1,001,211 | "Operation" |
| WINDOW\_THICKNESS | \-1,001,302 | "Thickness" |
| WINDOW\_TYPE\_ID | \-1,001,405 | "Type Mark" |
| WINDOW\_TYPE\_NAME | \-1,114,832 | "Name" |
| WINDOW\_WIDTH | \-1,001,301 | "Width" |
| WINDOWTYPE\_IS\_SCHEMATIC | \-1,114,855 | "Schematic" |
| WITNS\_LINE\_EXTENSION | \-1,006,404 | "Witness Line Extension" |
| WITNS\_LINE\_GAP\_TO\_ELT | \-1,006,405 | "Witness Line Gap to Element" |
| WITNS\_LINE\_TICK\_MARK | \-1,006,522 | "Witness Line Tick Mark" |
| WORK\_PLANE\_PARAM | \-1,123,517 | "Work Plane" |
| WRAPPING\_AT\_ENDS\_PARAM | \-1,002,111 | "Wrapping at Ends" |
| WRAPPING\_AT\_INSERTS\_PARAM | \-1,002,112 | "Wrapping at Inserts" |
| Y\_JUSTIFICATION | \-1,152,362 | "y Justification" |
| Y\_OFFSET\_VALUE | \-1,152,363 | "y Offset Value" |
| YZ\_JUSTIFICATION | \-1,152,361 | "yz Justification" |
| Z\_JUSTIFICATION | \-1,152,364 | "z Justification" |
| Z\_OFFSET\_VALUE | \-1,152,365 | "z Offset Value" |
| ZONE\_AIR\_CHANGES\_PER\_HOUR | \-1,114,840 | "Air Changes per Hour" |
| ZONE\_AIR\_VOLUME\_CALCULATION\_TYPE\_PARAM | \-1,114,345 | "Air Volume Calculation Type" |
| ZONE\_AREA | \-1,114,301 | "Occupied Area" |
| ZONE\_AREA\_GROSS | \-1,114,332 | "Gross Area" |
| ZONE\_CALCULATED\_AREA\_PER\_COOLING\_LOAD\_PARAM | \-1,114,343 | "Calculated Area per Cooling Load" |
| ZONE\_CALCULATED\_AREA\_PER\_HEATING\_LOAD\_PARAM | \-1,114,342 | "Calculated Area per Heating Load" |
| ZONE\_CALCULATED\_COOLING\_LOAD\_PARAM | \-1,114,306 | "Calculated Cooling Load" |
| ZONE\_CALCULATED\_COOLING\_LOAD\_PER\_AREA\_PARAM | \-1,114,319 | "Calculated Cooling Load per area" |
| ZONE\_CALCULATED\_HEATING\_LOAD\_PARAM | \-1,114,305 | "Calculated Heating Load" |
| ZONE\_CALCULATED\_HEATING\_LOAD\_PER\_AREA\_PARAM | \-1,114,318 | "Calculated Heating Load per area" |
| ZONE\_CALCULATED\_HYDRONIC\_COOLINGFLOW\_PARAM | \-1,114,702 | "Calculated Hydronic Cooling Flow" |
| ZONE\_CALCULATED\_HYDRONIC\_HEATINGFLOW\_PARAM | \-1,114,701 | "Calculated Hydronic Heating Flow" |
| ZONE\_CALCULATED\_SUPPLY\_AIRFLOW\_PARAM | \-1,114,307 | "Calculated Supply Airflow" |
| ZONE\_CALCULATED\_SUPPLY\_AIRFLOW\_PER\_AREA\_PARAM | \-1,114,320 | "Calculated Supply Airflow per area" |
| ZONE\_COIL\_BYPASS\_PERCENTAGE\_PARAM | \-1,114,344 | "Coil Bypass" |
| ZONE\_COOLING\_AIR\_TEMPERATURE\_PARAM | \-1,114,311 | "Cooling Air Temperature" |
| ZONE\_COOLING\_INFORMATION\_PARAM | \-1,114,335 | "Cooling Information" |
| ZONE\_COOLING\_SET\_POINT\_PARAM | \-1,114,309 | "Cooling Set Point" |
| ZONE\_DEHUMIDIFICATION\_SET\_POINT\_PARAM | \-1,114,313 | "Dehumidification Set Point" |
| ZONE\_DESIGN\_COOL\_TEMPERATURE | \-1,114,844 | "Design Temperature for Cooling" |
| ZONE\_DESIGN\_HEAT\_TEMPERATURE | \-1,114,843 | "Design Temperature for Heating" |
| ZONE\_HEATING\_AIR\_TEMPERATURE\_PARAM | \-1,114,310 | "Heating Air Temperature" |
| ZONE\_HEATING\_INFORMATION\_PARAM | \-1,114,334 | "Heating Information" |
| ZONE\_HEATING\_SET\_POINT\_PARAM | \-1,114,308 | "Heating Set Point" |
| ZONE\_HUMIDIFICATION\_SET\_POINT\_PARAM | \-1,114,312 | "Humidification Set Point" |
| ZONE\_LEVEL\_ID | \-1,114,317 | "Level" |
| ZONE\_LEVEL\_OFFSET | \-1,114,706 | "Level Offset" |
| ZONE\_LEVEL\_OFFSET\_TOP | \-1,114,707 | "Top Offset" |
| ZONE\_NAME | \-1,114,300 | "Name" |
| ZONE\_OA\_RATE\_PER\_ACH\_PARAM | \-1,114,316 | "Outdoor Air Rate / Air Changes per Hour" |
| ZONE\_OUTDOOR\_AIR\_INFORMATION\_PARAM | \-1,114,336 | "Outdoor Air Information" |
| ZONE\_OUTSIDE\_AIR\_FLOW\_PER\_AREA | \-1,114,841 | "Outside Air Flow per Area" |
| ZONE\_OUTSIDE\_AIR\_FLOW\_PER\_PERSON | \-1,114,842 | "Outside Air Flow per Person" |
| ZONE\_OUTSIDE\_AIR\_PER\_AREA\_PARAM | \-1,114,315 | "Outdoor Air per Area" |
| ZONE\_OUTSIDE\_AIR\_PER\_PERSON\_PARAM | \-1,114,314 | "Outdoor Air per Person" |
| ZONE\_PERIMETER | \-1,114,302 | "Perimeter" |
| ZONE\_PHASE | \-1,114,326 | "Phase" |
| ZONE\_PHASE\_ID | \-1,114,325 | "Phase Id" |
| ZONE\_SERVICE\_TYPE\_PARAM | \-1,114,304 | "Service Type" |
| ZONE\_SPACE\_OUTDOOR\_AIR\_OPTION\_PARAM | \-1,114,700 | "Space Outdoor Air Option" |
| ZONE\_USE\_AIR\_CHANGES\_PER\_HOUR\_PARAM | \-1,114,341 | "Use Air Changes Per Hour" |
| ZONE\_USE\_DEHUMIDIFICATION\_SETPOINT\_PARAM | \-1,114,338 | "Use Dehumidification Set Point" |
| ZONE\_USE\_HUMIDIFICATION\_SETPOINT\_PARAM | \-1,114,337 | "Use Humidification Set Point" |
| ZONE\_USE\_OUTSIDE\_AIR\_PER\_AREA\_PARAM | \-1,114,340 | "Use Outside Air Per Area" |
| ZONE\_USE\_OUTSIDE\_AIR\_PER\_PERSON\_PARAM | \-1,114,339 | "Use Outside Air Per Person" |
| ZONE\_VOLUME | \-1,114,303 | "Occupied Volume" |
| ZONE\_VOLUME\_GROSS | \-1,114,331 | "Gross Volume" |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The ID of the parameter can be used to retrieve property values from an Element
by using the Element.Parameter property.
The documentation for each ID includes the parameter name, as found in the
Element Properties dialog in the English version of Autodesk Revit. Note that
multiple distinct parameter ids may map to the same English name; in those case you must 
examine the parameters associated with a specific element to determine
which parameter id to use. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
